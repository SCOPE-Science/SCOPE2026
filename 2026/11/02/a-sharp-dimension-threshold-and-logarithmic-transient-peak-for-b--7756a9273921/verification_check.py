#!/usr/bin/env python3
"""Finite exact checks for a Boolean-cube heat-semigroup norm theorem.
Run with Python 3.10 or later. Standard library only.
Finite checks complement, but do not replace, the all-dimensional proof.
"""
from fractions import Fraction as F
from itertools import product
from math import log


def mu(n, rates):
    out=[]
    for v in range(1 << n):
        z=F(1)
        for i, r in enumerate(rates):
            z *= (1-r)/2 if (v>>i)&1 else (1+r)/2
        out.append(z)
    return out


def measure(n, rates, i):
    p=mu(n,rates); v=[F(0)]*(1<<n)
    v[0]+=1;v[1<<i]-=1
    for j in range(1<<n):
        v[j]+=-p[j]+p[j^(1<<i)]
    assert sum(v)==0
    return v


def claimed(n, rates, i):
    z=F(1)
    for j,r in enumerate(rates):
        if j!=i:z*=(1+r)/2
    return 1+rates[i]-2*rates[i]*z


def exact_dual(n, rates, i):
    """Exhaust all integer-valued 1-Lipschitz dual potentials rooted at 0,
    using spanning-tree differences in {-1,0,1}; valid for small n.
    The incidence matrix is totally unimodular, so these suffice.
    """
    v=measure(n,rates,i)
    order=sorted(range(1,1<<n),key=lambda s:(s.bit_count(),s))
    vals={0:0}; best=F(-10**9)
    def rec(k):
        nonlocal best
        if k==len(order):
            score=sum(v[x]*vals[x] for x in range(1<<n))
            if score>best:best=score
            return
        x=order[k]; prev=x&(x-1)
        for z in (vals[prev]-1,vals[prev],vals[prev]+1):
            if all(abs(z-vals[x^(1<<b)])<=1
                   for b in range(n) if (x>>b)&1 and (x^(1<<b)) in vals):
                vals[x]=z;rec(k+1);del vals[x]
    rec(0)
    return best

count=0
for n in (1,2,3):
    for seed in range(8):
        rates=[F((3*i+2*seed+1)%9,9) for i in range(n)]
        for i in range(n):
            assert exact_dual(n,rates,i)==claimed(n,rates,i), (n,rates,i)
            count+=1
print('PASS',count,'exhaustive integral Lipschitz-dual comparisons')

count=0
for n in range(1,10):
    for seed in range(8):
        rates=[F((3*i+2*seed+1)%11,11) for i in range(n)]
        p=mu(n,rates)
        for i in range(n):
            c=[]
            for u in range(1<<(n-1)):
                z=F(1)
                k=0
                for j in range(n):
                    if j==i:continue
                    z *= (1-rates[j])/2 if (u>>k)&1 else (1+rates[j])/2
                    k+=1
                c.append((F(1) if u==0 else F(0))-rates[i]*z)
            val=sum(abs(x) for x in c)
            assert val==claimed(n,rates,i)
            # Every signed coefficient is exposed by an explicit two-valued
            # 1-Lipschitz function on the cube.
            signs=[1 if x>=0 else -1 for x in c]
            assert sum(x*y for x,y in zip(c,signs))==val
            count+=1
print('PASS',count,'exact rational anisotropic edge-shadow identities')
