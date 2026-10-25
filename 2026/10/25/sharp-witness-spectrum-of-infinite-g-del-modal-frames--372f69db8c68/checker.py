#!/usr/bin/env python3
"""Exact rational finite-prefix checks for modal witness-spectrum examples.

These checks corroborate explicit finite-prefix identities. The infinite
nonattainment statements are established in RESULT.md by proof, not by code.
"""
from fractions import Fraction as Q
from itertools import product


def impl(a,b):
    return Q(1) if a <= b else b


def box(r,f):
    return min(impl(a,b) for a,b in zip(r,f))


def diamond(r,f):
    return max(min(a,b) for a,b in zip(r,f))


def check_finite():
    palette = [Q(0),Q(1,3),Q(2,3),Q(1)]
    for n in range(1,4):
        for r in product(palette, repeat=n):
            for f in product(palette, repeat=n):
                assert box(r,f) in [impl(a,b) for a,b in zip(r,f)]
                assert diamond(r,f) in [min(a,b) for a,b in zip(r,f)]


def check_truncations():
    for n in (4,8,16,32):
        r = [Q(1,k+1) for k in range(1,n+1)]
        f = [r[k-1]/Q(k+1) for k in range(1,n+1)]
        assert box(r,f)==Q(1,(n+1)*(n+1))
        assert diamond(r,[Q(1)]*n)==Q(1,2)
        # Box minima decrease strictly to zero although every finite prefix attains.
        assert box(r,f)>0
        up=[Q(1)-Q(1,k+1) for k in range(1,n+1)]
        assert diamond(up,[Q(1)]*n)==Q(n,n+1)
        # Open threshold at c=1/2. Values are strictly above c and tend to c.
        c=Q(1,2)
        r2=[c+(1-c)/Q(k+1) for k in range(1,n+1)]
        f2=[c+(r2[k-1]-c)/Q(2) for k in range(1,n+1)]
        assert box(r2,f2)==c+Q(1,4*(n+1))
        assert box(r2,f2)>c
    print('EXACT_PREFIX_CHECKS_OK: enumerations n<=3; illustrative prefixes 4,8,16,32')

if __name__=='__main__':
    check_finite()
    check_truncations()
