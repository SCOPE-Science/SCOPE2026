#!/usr/bin/env python3
"""Exact rational checks for a polygonal section of an affine absolute-value map.
Only the scientific identities are verified; no external resources are accessed.
"""
from fractions import Fraction as Q
from itertools import product

def F(z, a, b):
    x, y = z
    return abs(x)-y+a, x-abs(y)+b

def F3(z, a, b):
    for _ in range(3):
        z = F(z, a, b)
    return z

def X(r, a, b):
    d = b-2*a
    if r <= d:
        return d-r, a+r
    return r-d, b-a+r-d

def S(r, a, b):
    d = b-2*a
    if r <= d/2:
        return Q(0)
    if r <= d:
        return 4*r-2*d
    return 2*d

def run():
    tested = 0
    for a,bmult in product((Q(1,8),Q(1,3),Q(1),Q(5,4),Q(3),Q(7)),
                            (Q(201,100),Q(5,2),Q(3),Q(7),Q(10),Q(101,3))):
        b = a*bmult
        d = b-2*a
        assert d > 0
        p0 = (d,a)
        r1 = (d,2*b-3*a)
        p2 = (2*a-b,a)
        assert F(p0,a,b)==r1
        assert F(r1,a,b)==p2
        assert F(p2,a,b)==p0
        assert F3(p0,a,b)==p0 and F3(r1,a,b)==r1
        assert X(Q(0),a,b)==p0
        assert X(d,a,b)==(Q(0),b-a)
        assert X(2*d,a,b)==r1
        assert X(2*b,a,b)==(b+2*a,2*b+a)
        boundaries = (Q(0),d/2,3*d/4,d,2*d,2*b)
        for r in boundaries:
            assert F3(X(r,a,b),a,b)==X(S(r,a,b),a,b)
            tested += 1
        for l,h in zip(boundaries,boundaries[1:]):
            if l == h:continue
            for k in range(1,20):
                t=l+(h-l)*Q(k,20)
                assert F3(X(t,a,b),a,b)==X(S(t,a,b),a,b)
                tested += 1
        w=d/(4*b)
        assert 0 < w < Q(1,4)
        for m in range(1,15):
            r=w*Q(1,4)**(m-1)
            pm=4*w/3-r/3
            qm=1-4*w/3-2*r/3
            assert pm+qm+r==1
            assert (pm if m==1 else pm-(4*w/3-w*Q(1,4)**(m-2)/3)) == (w if m==1 else w*Q(1,4)**(m-2)/4)
            assert r==w*Q(1,4)**(m-1)
            assert pm>=0 and qm>=0
        assert 4*w/3==d/(3*b)
        assert (1-4*w/3)==(2*b+2*a)/(3*b)
        assert 1+4*w/3==(4*b-2*a)/(3*b)
    print(f'EXACT_POLYGONAL_PHASE_LAW_OK: {tested} rational branch tests, 36 parameter pairs, 14 distribution levels')

if __name__=='__main__':run()
