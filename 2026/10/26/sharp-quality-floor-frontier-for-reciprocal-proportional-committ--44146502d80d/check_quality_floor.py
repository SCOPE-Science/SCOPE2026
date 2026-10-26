#!/usr/bin/env python3
"""Exact checks for the sharp quality-floor envelope in reciprocal representation."""
from fractions import Fraction as F
from itertools import product
from math import gcd

def analytic(q):
    r=max(q,F(1,2))
    return 1-r+r*r

def g(q,x):
    return 1-x+max(q*x,x*x)

def witness(r,k):
    assert F(1,2)<=r<1 and k*r == int(k*r)
    n=int(k*r)
    t=n-1
    assert n>=2 and t<k
    # Each low-voter has reciprocal funding capacity exactly 1/r.
    assert F(k,n)==1/r
    # A singleton low-only group can afford its private candidate.
    assert 1>=F(n,k)/r
    # High party can afford up to floor(1/r) quality-one seats.
    assert k-t>=int(1/r)
    # All low candidates forced, and all k optimal candidates have quality 1.
    ratio=(t*r+(k-t))/k
    assert ratio==1-(1-r)*(r-F(1,k))
    return ratio

checks=0
for den in range(1,49):
    for num in range(1,den+1):
        q=F(num,den)
        target=analytic(q)
        # The continuous piecewise function's possible interior minima occur
        # at 1/2 or q; boundary points are 0 and 1.
        for x in (F(0),F(1),q,F(1,2)):
            assert g(q,x)>=target, (q,x,target)
            checks+=1
        r=max(q,F(1,2))
        assert g(q,r)==target
        checks+=1
        if r<1:
            k=2*r.denominator*max(1, r.denominator)
            if k*r<2:k*=2
            rat=witness(r,k)
            assert rat>=target
            assert rat-target==(1-r)/k
            checks+=2
# Cross-check tight rational families at increasingly large horizons.
for r in (F(1,2),F(3,5),F(2,3),F(3,4),F(9,10),F(99,100)):
    old=None
    for j in (2,4,8,16):
        k=j*r.denominator
        ratio=witness(r,k)
        assert ratio>analytic(r)
        if old is not None:assert ratio<old
        old=ratio
        checks+=2
# The minimum over x in [0,1] has a kink at x=q, and a derivative
# sign change at x=1/2; validate this structure on a rational mesh.
for q in (F(1,10),F(1,3),F(1,2),F(3,5),F(3,4),F(9,10),F(1)):
    for i in range(1001):
        x=F(i,1000)
        assert g(q,x)>=analytic(q)
        checks+=1
print(f'ALL EXACT CHECKS PASSED ({checks} rational tests)')
