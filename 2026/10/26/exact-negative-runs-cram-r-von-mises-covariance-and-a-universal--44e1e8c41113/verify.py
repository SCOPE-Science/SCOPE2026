#!/usr/bin/env python3
"""Exact, standalone finite checks for a two-sample runs/empirical-CvM covariance."""
from fractions import Fraction as F
from itertools import combinations
from math import comb

checks = 0

def one_word(n, chosen):
    global checks
    is_one = [False]*n
    for i in chosen: is_one[i] = True
    a = len(chosen)
    d = 0
    q = 0
    for t in range(1, n):
        d += n*int(is_one[t-1])-a
        q += d*d
    runs = 1 + sum(is_one[j] != is_one[j+1] for j in range(n-1))
    return runs, q

def via_enumeration(n,a):
    global checks
    vals=[one_word(n,z) for z in combinations(range(n),a)]
    size=len(vals)
    er=F(sum(r for r,q in vals),size)
    eq=F(sum(q for r,q in vals),size)
    cov=F(sum(r*q for r,q in vals),size)-er*eq
    assert er == 1 + F(2*a*(n-a),n)
    assert eq == F(a*(n-a)*n*(n+1),6)
    assert cov == F(a*(n-a)*(n-2*a*(n-a)),3)
    checks += 3
    return vals

def conditional_delta(n,a,j):
    global checks
    b=n-a
    assert n>=4 and 1<=j<n
    p=F(a-1,n-2)
    delta=F(0)
    for t in range(1,n):
        if t<j: h,extra,varb=t,F(0),F(0)
        elif t==j: h,extra,varb=j-1,F(1,2),F(1,4)
        else: h,extra,varb=t-2,F(1),F(0)
        varh=F(h*(n-2-h)*(a-1)*(b-1),(n-2)**2*(n-3))
        edsq=n*n*(varh+varb)+(n*(h*p+extra)-a*t)**2
        edsq_un=F(a*b*t*(n-t),n-1)
        delta+=edsq-edsq_un
    h=j*(n-j)
    predicted=F(n,6*(n-2)*(n-3))*((36*a*b-6*n*(n+1))*h + n**4+3*n**3-4*n*n+6*n-a*b*(8*n*n-4*n+12))
    assert delta==predicted, (n,a,j,delta,predicted)
    checks += 1
    return delta

def conditional_aggregate(n,a):
    global checks
    ds=[conditional_delta(n,a,j) for j in range(1,n)]
    assert sum(ds)==F(n*(n-1)*(n-2*a*(n-a)),6)
    p=F(2*a*(n-a),n*(n-1))
    assert p*sum(ds)==F(a*(n-a)*(n-2*a*(n-a)),3)
    checks += 2

for n in range(2,13):
    for a in range(1,n):
        via_enumeration(n,a)
        if n>=4:
            conditional_aggregate(n,a)

# All parameter pairs through 55: independent conditional-moment route and
# the exact formula, without relying on exhaustive permutation enumeration.
for n in range(13,56):
    for a in range(1,n):
        conditional_aggregate(n,a)

# Symbolic Pearson scaling checks at large balanced / imbalanced composition.
from math import sqrt
for p in (0.1,0.25,0.5,0.77,0.9):
    for n in (500,2000,10000):
        a=max(1,min(n-1,int(p*n)))
        b=n-a
        cov=float(F(n-2*a*b,3*n*n))
        var_r=float(F(2*a*b*(2*a*b-n),n*n*(n-1)))
        # Limit Var(T)=1/45; using this denominator tests the claimed constant
        corr_proxy=sqrt(n)*cov/sqrt(var_r/45)
        assert abs(corr_proxy+sqrt(5))<0.06, (n,a,corr_proxy)
        checks+=1

print('PASS:',checks,'exact finite checks and asymptotic consistency cases')
