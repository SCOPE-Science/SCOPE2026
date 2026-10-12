#!/usr/bin/env python3
"""Finite arithmetic cross-checks for fixed-support recursive-divisor extremals.

Uses the original recursion on exponent-lattice divisors and separately a
finite-difference evaluation of the positive convolution expansion.
"""
from functools import lru_cache
from itertools import product
from math import comb

@lru_cache(None)
def kappa(exponents):
    if not any(exponents):
        return 1
    s = 1
    for t in product(*(range(a + 1) for a in exponents)):
        if t != exponents:
            s += kappa(t)
    return s

def finite_difference_kappa(exponents):
    m = sum(exponents)
    if m == 0:
        return 1
    vals = [0] + [prod(comb(a+k-1, a) for a in exponents) for k in range(1,m+1)]
    total = 0
    for j in range(1,m+1):
        vals = [vals[i+1]-vals[i] for i in range(len(vals)-1)]
        total += vals[0]
    return 2*total

def prod(xs):
    z = 1
    for x in xs: z *= x
    return z

def partitions(m, limit=None):
    if m == 0:
        yield ()
    else:
        for a in range(min(limit or m,m), 0, -1):
            for q in partitions(m-a, a):
                yield (a,)+q

PASSES=0
transfers=0
splits=0
comparisons=0
for m in range(1,12):
    parts=list(partitions(m))
    for a in parts:
        x=kappa(a)
        assert x == finite_difference_kappa(a), (a, x, finite_difference_kappa(a))
        r=len(a)
        q,t=divmod(m,r)
        lo=(m-r+1,)+(1,)*(r-1)
        hi=tuple(sorted((q+1,)*t+(q,)*(r-t), reverse=True))
        assert kappa(lo)<=x<=kappa(hi), (a,lo,hi)
        assert (x==kappa(lo))==(a==lo), (m,r,a,lo)
        assert (x==kappa(hi))==(a==hi), (m,r,a,hi)
        comparisons += 1
        for i in range(r):
            for j in range(r):
                if a[i]>=a[j]+2:
                    b=list(a); b[i]-=1;b[j]+=1;b=tuple(sorted(b,reverse=True))
                    assert kappa(b)>x, (a,b)
                    transfers+=1
        for i in range(r):
            if a[i]>=2:
                for first in range(1,a[i]):
                    b=tuple(sorted(a[:i]+(first,a[i]-first)+a[i+1:],reverse=True))
                    assert kappa(b)>x, (a,b)
                    splits+=1
    assert kappa((m,)) == 2**m
    # Number of ordered set partitions (Fubini) from Stirling counts.
    stir=[0]*(m+1);stir[0]=1
    for step in range(1,m+1):
        nxt=[0]*(m+1)
        for j in range(1,step+1):
            nxt[j]=j*stir[j]+stir[j-1]
        stir=nxt
    import math
    fubini=sum(math.factorial(j)*stir[j] for j in range(1,m+1))
    assert kappa((1,)*m)==2*fubini
    PASSES+=1
print('VERIFY_OK')
print(f'multiplicities=1..{PASSES} support_and_shape_checks={comparisons}')
print(f'strict_balancing_transfers={transfers} strict_splitting_checks={splits}')
print('independent_recursion_vs_finite_differences=PASS')
print('prime_power_and_squarefree_endpoints=PASS')
for m,r in [(6,2),(7,3),(8,3),(10,4)]:
    q,t=divmod(m,r)
    lo=(m-r+1,)+(1,)*(r-1)
    hi=tuple(sorted((q+1,)*t+(q,)*(r-t),reverse=True))
    print(f'example m={m} r={r}: lower={lo} count={kappa(lo)} upper={hi} count={kappa(hi)}')
