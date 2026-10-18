#!/usr/bin/env python3
"""Standalone exact and numerical checks for a theorem on cycle/indegree covariance.
No third-party libraries or external data required. The code is not a proof of all n.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial, exp

checks = 0

def check(cond, description):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(description)


def bin_pmf(n, m, r):
    if 0 <= r <= m:
        return Fraction(comb(m, r) * (n-1)**(m-r), n**m)
    return Fraction(0)


def e_cycle(n, k):
    return Fraction(factorial(n), factorial(n-k) * k * n**k)


def bracket(n, k, r):
    m = n-k
    return k * bin_pmf(n, m, r-1) + m * bin_pmf(n, m, r) - n * bin_pmf(n, n, r)


def s_poly(n, k):
    m=n-k
    return Fraction(m*(m*(m-1) + 2*k*(n-1)), 1) - Fraction(n*n*(n-1)*(n-1)**k, n**k)


def cycle_counts(f):
    n=len(f)
    globally=set()
    counts=[0]*(n+1)
    for start in range(n):
        if start in globally: continue
        seen={}
        curr=start
        while curr not in globally and curr not in seen:
            seen[curr] = len(seen)
            curr = f[curr]
        if curr in seen:
            counts[len(seen)-seen[curr]] += 1
        globally.update(seen)
    return counts


def exact_exhaustion(n):
    sh=[0]*(n+1)
    sc=[0]*(n+1)
    sx=[[0]*(n+1) for _ in range(n+1)]
    scoal=[0]*(n+1)
    for f in product(range(n), repeat=n):
        deg=[0]*n
        for image in f: deg[image]+=1
        hist=[0]*(n+1)
        for d in deg: hist[d]+=1
        cyc=cycle_counts(f)
        collision=sum(d*(d-1)//2 for d in deg)
        for r in range(n+1): sh[r]+=hist[r]
        for k in range(1,n+1):
            sc[k]+=cyc[k]
            scoal[k]+=cyc[k]*collision
            if cyc[k]:
                for r in range(n+1): sx[k][r]+=cyc[k]*hist[r]
    total=n**n
    mean_col=Fraction(n-1,2)  # E sum_v C(D_v,2) = C(n,2)/n
    for k in range(1,n+1):
        ec=e_cycle(n,k)
        check(Fraction(sc[k],total)==ec, f'cycle mean n={n} k={k}')
        actual_col=Fraction(scoal[k],total)-ec*mean_col
        expected_col=-ec*Fraction(k*(k-1),2*n)
        check(actual_col==expected_col, f'collision covariance n={n} k={k}')
        for r in range(n+1):
            check(Fraction(sh[r],total)==n*bin_pmf(n,n,r), f'hist mean n={n} r={r}')
            actual=Fraction(sx[k][r],total)-ec*Fraction(sh[r],total)
            expected=ec*bracket(n,k,r)
            check(actual==expected, f'exhaustive cov n={n} k={k} r={r}')


for n in range(2,7):
    exact_exhaustion(n)

for n in range(2,45):
    p=Fraction(1,n)
    q=1-p
    for k in range(1,n+1):
        diff_pmf=[Fraction(k,n)*bin_pmf(n,n-k,r-1)+Fraction(n-k,n)*bin_pmf(n,n-k,r)-bin_pmf(n,n,r)
                  for r in range(n+1)]
        check(sum(diff_pmf)==0, f'probability mass n={n},k={k}')
        check(sum(r*diff_pmf[r] for r in range(n+1))==0, f'equal means n={n},k={k}')
        for r in range(n+1):
            d=bracket(n,k,r)
            check(d==n*diff_pmf[r], f'law n={n},k={k},r={r}')
            curvature=sum(j*(bin_pmf(n,n-j-1,r)-2*bin_pmf(n,n-j-1,r-1)+bin_pmf(n,n-j-1,r-2))
                          for j in range(1,k))
            check(d==-curvature/n, f'curvature n={n},k={k},r={r}')
            if k==1: check(d==0, f'loops n={n},r={r}')
            elif r==0: check(d<0, f'indegree zero n={n},k={k}')
            elif r==1: check(d>0, f'indegree one n={n},k={k}')
            elif r>=3: check(d<0, f'high indegree n={n},k={k},r={r}')
        check(bracket(n,k,2)>0 if s_poly(n,k)>0 else bracket(n,k,2)==0 if s_poly(n,k)==0 else bracket(n,k,2)<0,
              f'degree two sign n={n} k={k}')

for n in range(4,100):
    signs=[(s_poly(n,k)>0)-(s_poly(n,k)<0) for k in range(2,n+1)]
    check(signs[0]==1 and signs[-1]==-1, f'endpoint signs {n}')
    check(all(signs[j]>=signs[j+1] for j in range(len(signs)-1)), f'one switch {n}')

# Universal nonpositive covariance for discretely convex score phi(d)=d^3,
# plus exact identity for phi(d)=C(d,2).
for n in range(2,27):
    for k in range(1,n+1):
        for phi in (lambda d:d*(d-1)//2, lambda d:d**3):
            actual=sum(Fraction(phi(r))*bracket(n,k,r) for r in range(n+1))
            check(actual<=0 and (actual==0)==(k==1), f'convex score n={n} k={k}')
            if phi(5)==10:
                check(actual==-Fraction(k*(k-1),2*n),f'collision score n={n} k={k}')

# Root of h(t)=exp(t)(1-t)(1+t^2)=1 on (sqrt(2)-1,1).
a,b=.45,.85
for _ in range(75):
    mid=(a+b)/2
    val=exp(mid)*(1-mid)*(1+mid*mid)-1
    if val>0: a=mid
    else: b=mid
root=(a+b)/2
check(abs(root-0.584724386479944)<1e-12, 'nonzero crossover root')
for n in (200,500,1000,2000):
    def f(k):
        m=n-k
        return (m*(m*(m-1)+2*k*(n-1)))/(n**3) -(n-1)/n*((n-1)/n)**k
    kcrit=next(k for k in range(2,n+1) if f(k)<=0)
    check(abs(kcrit/n-root)<.02, f'crossover scale n={n},k={kcrit}')
print(f'PASS: {checks} checks; exhaustive n=2..6; crossover={root:.15f}')
