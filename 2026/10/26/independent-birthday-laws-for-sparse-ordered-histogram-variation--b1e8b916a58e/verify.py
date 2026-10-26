#!/usr/bin/env python3
"""Finite corroboration for the sparse uniform ordered-histogram theorem.

Run: python3 verify.py. Standard library only. Finite checks do not establish the asymptotic theorem.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, exp, factorial, sqrt
from random import Random

checks = 0


def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)


def theoretical(m, n):
    q = Fraction(2 * (m - 1), m * m)
    s = Fraction(4 * m - 6, m**3)
    mean = comb(n, 2) * q
    b1 = comb(n, 2) * (2*n-3) * q*q
    b2 = comb(n, 2) * 2*(n-2) * s
    triple = 2 * (m-1) * (n*(n-1)*(n-2)) / m**3
    bound = min(1.0, 2*n/m + triple + 2*min(1.0,1/float(mean)) * float(b1+b2))
    # Joint same-bin / adjacent-bin mark process (Arratia-Goldstein-Gordon).
    qtot=Fraction(3*m-2,m*m)
    stot=Fraction(9*m-10,m**3)
    b1_joint=comb(n,2)*(2*n-3)*qtot*qtot
    b2_joint=comb(n,2)*2*(n-2)*stot
    joint_bound=min(1.0, 2*n/m+triple+2*float(b1_joint+b2_joint))
    return q,s,mean,b1,b2,triple,bound,b1_joint,b2_joint,joint_bound


def stats(u,m):
    counts = [0]*m
    for j in u:
        counts[j] += 1
    n = len(u)
    t = sum(abs(a-b) for a,b in zip(counts,counts[1:]))
    z = sum(min(a,b) for a,b in zip(counts,counts[1:]))
    w = sum(a*b for a,b in zip(counts,counts[1:]))
    direct = sum(abs(u[i]-u[j]) == 1 for i in range(n) for j in range(i+1,n))
    return counts, t, z, w, direct

for m in range(2,7):
    q,s, *_ = theoretical(m,3)
    q_counts=sum(abs(a-b)==1 for a in range(m) for b in range(m))
    s_counts=sum(abs(a-b)==1 and abs(a-c)==1 for a in range(m) for b in range(m) for c in range(m))
    check(q==Fraction(q_counts,m*m),f'pair kernel {m}')
    check(s==Fraction(s_counts,m**3),f'triple kernel {m}')
    tot=sum(abs(a-b)<=1 for a in range(m) for b in range(m))
    st=sum(abs(a-b)<=1 and abs(a-c)<=1 for a in range(m) for b in range(m) for c in range(m))
    check(Fraction(tot,m*m)==Fraction(3*m-2,m*m),'two-color kernel')
    check(Fraction(st,m**3)==Fraction(9*m-10,m**3),'two-color shared-index kernel')

for m in range(2,7):
    for n in range(2,6):
        q,s,mean,b1,b2,triple,bound,b1j,b2j,joint_bound=theoretical(m,n)
        nobs=m**n
        dlaw=Counter()
        jointlaw=Counter()
        tot_w=tot_wz=0
        for u in product(range(m), repeat=n):
            cnt,t,z,w,direct=stats(u,m)
            check(2*n-t==cnt[0]+cnt[-1]+2*z,'cut identity')
            check(w==direct,'ordered-neighbor pair interpretation')
            check(w>=z,'adjacency count majorizes overlap')
            check(w-z<=sum(a*(a-1)*b+a*b*(b-1) for a,b in zip(cnt,cnt[1:])), 'triple bound pathwise')
            dlaw[2*n-t]+=1
            collision=sum(a*(a-1)//2 for a in cnt)
            check(collision==sum(u[i]==u[j] for i in range(n) for j in range(i+1,n)), 'collision statistic')
            jointlaw[(collision,2*n-t)]+=1
            tot_w+=w
            tot_wz+=w-z
        check(Fraction(tot_w,nobs)==mean,f'pair expectation {m} {n}')
        check(float(Fraction(tot_wz,nobs))<=triple+1e-12, f'triple error {m} {n}')
        # Exact mass of the largest possible variation: support is an
        # independent set of interior path vertices; occupied labels are onto.
        stirling=[[0]*(n+1) for _ in range(n+1)]
        stirling[0][0]=1
        for a in range(1,n+1):
            for b in range(1,a+1):
                stirling[a][b]=b*stirling[a-1][b]+stirling[a-1][b-1]
        max_count=sum(comb(m-k-1,k)*factorial(k)*stirling[n][k] for k in range(1, min(n,(m-1)//2)+1))
        check(dlaw[0]==max_count, f'closed maximum mass {m} {n}')
        jointmax=factorial(n)*comb(m-n-1,n) if m>=2*n+1 else 0
        check(jointlaw[(0,0)]==jointmax, f'collision-free maximum mass {m} {n}')
        # Compare law of integer-valued D with twice a Poisson variable, including all tails.
        lam=float(mean)
        upper=max(max(dlaw), 2*max(25,n*n))
        poi=[exp(-lam)*lam**k/factorial(k) for k in range(upper//2+1)]
        ztail=max(0.0,1.0-sum(poi))
        support=set(dlaw)|set(2*k for k in range(len(poi)))
        d_tv=(sum(abs(dlaw.get(j,0)/nobs-(poi[j//2] if j>=0 and j%2==0 and j//2<len(poi) else 0)) for j in support)+ztail)/2
        check(d_tv<=bound+1e-11,f'finite total variation bound {m} {n}: {d_tv} > {bound}')
        # Independently compare the joint collision / variation-defect law with
        # two independent Poisson laws, with the second coordinate doubled.
        l0=comb(n,2)/m
        l1=lam
        kmax=45+comb(n,2)
        def probs(l):
            p=[exp(-l)]
            for j in range(1,kmax+1):p.append(p[-1]*l/j)
            return p
        p0,p1=probs(l0),probs(l1)
        tail=max(0,1-sum(p0)*sum(p1))
        j_tv=tail
        for c in range(kmax+1):
            for w in range(kmax+1):
                j_tv+=abs(jointlaw.get((c,2*w),0)/nobs-p0[c]*p1[w])
        j_tv+=sum(count/nobs for (c,d),count in jointlaw.items() if d%2)
        j_tv/=2
        check(j_tv<=joint_bound+1e-11, f'joint bound {m} {n}: {j_tv} > {joint_bound}')

rng=Random(93671)
for m,n in ((1000,32),(2000,44),(5000,70)):
    trials=20000
    hit0=0
    hit2=0
    lam=float(theoretical(m,n)[2])
    for _ in range(trials):
        u=[rng.randrange(m) for _ in range(n)]
        counts=Counter(u)
        t=sum(abs(counts.get(j+1,0)-counts.get(j,0)) for j in range(m-1))
        delta=2*n-t
        hit0+=delta==0
        hit2+=delta==2
    # A diagnostic only; no statistical validation claim.
    print(f'm={m} N={n} lambda={lam:.6f} P(defect=0) observed={hit0/trials:.4f} predicted={exp(-lam):.4f}; P(defect=2) observed={hit2/trials:.4f} predicted={lam*exp(-lam):.4f}')
print(f'PASS {checks} finite exact/enumerative assertions; 60000 seeded simulations (diagnostic)')
