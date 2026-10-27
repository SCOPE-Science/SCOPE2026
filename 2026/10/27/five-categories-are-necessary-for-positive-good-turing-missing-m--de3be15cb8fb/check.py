#!/usr/bin/env python3
"""Exact independent enumeration for two-draw missing-mass covariance theorem.

Run: python3 check.py; uses Python standard library only.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def direct(p):
    em = eg = emg = F(0)
    for i, j in product(range(len(p)), repeat=2):
        w = p[i] * p[j]
        missing = sum(p[k] for k in range(len(p)) if k != i and k != j)
        singleton = F(1) if i != j else F(0)
        em += w * missing
        eg += w * singleton
        emg += w * missing * singleton
    return emg - em * eg


def moment(p):
    s2 = sum((x*x for x in p), F(0))
    s3 = sum((x*x*x for x in p), F(0))
    return s3*(1+s2)-2*s2*s2


checks=0
for m in range(2, 6):
    for den in range(m, 14):
        # Enumerate positive integer count compositions to avoid duplicate support.
        def comps(n, k):
            if k == 1:
                if n >= 1:
                    yield (n,)
                return
            for x in range(1, n-k+2):
                for rest in comps(n-x, k-1):
                    yield (x,)+rest
        for tup in comps(den, m):
            p=tuple(F(v,den) for v in tup)
            v=direct(p)
            assert v == moment(p), (p, v, moment(p))
            if m<=4:
                assert v < 0, (p, v)
            checks+=1

p=(F(4,5),)+4*(F(1,20),)
assert direct(p)==moment(p)==F(1,1600)
checks+=1
for m in range(2, 18):
    p=m*(F(1,m),)
    assert direct(p)==-F(m-1,m**3)
    checks+=1
for a_num in range(1,81):
    a=F(a_num,80)
    if a<F(1,4):
        continue
    b=(1-a)/3
    p=(a,b,b,b)
    expected=F(2,27)*(a-1)**3*(16*a*a-2*a+1)
    assert direct(p)==expected
    checks+=1
print('PASS:',checks,'independent exact rational comparisons; four-category negativity; five-category positive witness; sharp uniform values.')
