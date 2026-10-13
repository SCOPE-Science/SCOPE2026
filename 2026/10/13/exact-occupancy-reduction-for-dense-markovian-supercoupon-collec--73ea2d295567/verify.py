#!/usr/bin/env python3
"""Exact finite-path checks for the dense Markovian supercoupon identity.

Requires Python 3 standard library only.  This verifier checks finite cases;
the proof for all dimensions is analytic and included in RESULT.md.
"""
from fractions import Fraction
from math import comb, factorial
from collections import Counter
from itertools import product

def stirling2(m,j):
    if m==0: return int(j==0)
    row=[1]+[0]*j
    for _ in range(m):
        row=[0]+[row[q]*q+(row[q-1] if q>0 else 0) for q in range(1,j+1)]
    return row[j]

def falling(n,k):
    v=1
    for i in range(k):v*=n-i
    return v

def closed_k(n,t,k):
    return Fraction(falling(n-1,k-1)*stirling2(t-1,k-1),(n-1)**(t-1))

def geom_pgf_coefficients(n,s,m):
    # Coefficients P(T=t), t=0,...,m, by successive convolutions.
    d={1:Fraction(1)}
    for k in range(1,s+1):
        p=Fraction(n-k,n-1)
        nd={}
        for off,weight in d.items():
            for z in range(1,m-off+1):
                idx=off+z
                nd[idx]=nd.get(idx,Fraction())+weight*p*(1-p)**(z-1)
        d=nd
    return d

checks=0
for n in range(2,7):
    for t in range(1,7):
        cnt=Counter()
        for tail in product(range(n-1),repeat=t-1):
            path=[0]
            for a in tail:
                opts=[x for x in range(n) if x!=path[-1]]
                path.append(opts[a])
            cnt[len(set(path))]+=1
        total=(n-1)**(t-1)
        assert sum(cnt.values())==total
        for k in range(1,n+1):
            assert Fraction(cnt[k],total)==closed_k(n,t,k), (n,t,k)
            checks+=1
        for s in range(1,n):
            possible_U=Counter()
            for k,num in cnt.items():
                U=comb(n-k,s-k) if k<=s else 0
                possible_U[U]+=num
            assert sum(possible_U.values())==total
            law={comb(n-k,s-k):closed_k(n,t,k) for k in range(1,s+1)}
            law[0]=sum(closed_k(n,t,k) for k in range(s+1,n+1))
            for U,p in law.items():
                assert Fraction(possible_U[U],total)==p,(n,t,s,U)
                checks+=1
            stop_cdf=sum(closed_k(n,t,k) for k in range(s+1,n+1))
            pgf=geom_pgf_coefficients(n,s,t)
            assert stop_cdf==sum(pgf.values()),(n,t,s,stop_cdf,sum(pgf.values()))
            checks+=1
print(f'EXACT_PATH_CHECKS_PASS comparisons={checks} n=2..6 t=1..6 s=1..n-1')
for n,s in [(2,1),(3,1),(4,2),(7,3),(10,9)]:
    mean=1+sum(Fraction(n-1,n-k) for k in range(1,s+1))
    var=sum(Fraction((n-1)*(k-1),(n-k)**2) for k in range(1,s+1))
    print(f'n={n} s={s} mean={mean} variance={var}')
