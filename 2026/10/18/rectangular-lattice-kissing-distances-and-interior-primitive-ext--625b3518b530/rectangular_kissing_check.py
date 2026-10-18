#!/usr/bin/env python3
"""Exact finite checks for the rectangular lattice-polytope distance theorem.

Run with Python 3, without third-party modules. All arithmetic is integer or
Fraction arithmetic; the universal proof is in RESULT.md, not this sample check.
"""
from fractions import Fraction
from itertools import product, combinations
from math import gcd


def primitive_max(a, b):
    assert isinstance(a, int) and isinstance(b, int) and a >= 1 and b >= 1
    return max((p*p + q*q, p, q)
               for p in range(a + 1) for q in range(b + 1)
               if gcd(p, q) == 1)


def point_segment_squared(x, u, v):
    dx, dy = v[0] - u[0], v[1] - u[1]
    d2 = dx*dx + dy*dy
    assert d2
    ex, ey = x[0] - u[0], x[1] - u[1]
    lam_num = ex*dx + ey*dy
    if lam_num < 0:
        return Fraction(ex*ex + ey*ey)
    if lam_num > d2:
        return Fraction((x[0]-v[0])**2 + (x[1]-v[1])**2)
    determinant = ex*dy - ey*dx
    return Fraction(determinant*determinant, d2)


def exhaustive_point_segment_distance(a, b):
    pts = list(product(range(a + 1), range(b + 1)))
    candidate = None
    for u, v in combinations(pts, 2):
        for x in pts:
            dd = point_segment_squared(x, u, v)
            if dd <= 0:
                continue  # intersecting point and segment
            if candidate is None or dd < candidate:
                candidate = dd
    return candidate


def bezout_in_segment_box(p, q):
    """Find an integer witness (x,y) with p*y-q*x=1, in the box."""
    assert p >= 1 and q >= 1 and gcd(p, q) == 1
    for x in range(p + 1):
        numerator = 1 + q*x
        if numerator % p:
            continue
        y = numerator // p
        if 0 <= y <= q:
            return (x, y)
    raise AssertionError('Bezout witness absent')


def main():
    cases = 0
    for a in range(1, 6):
        for b in range(1, 6):
            maximum, p, q = primitive_max(a, b)
            brute = exhaustive_point_segment_distance(a, b)
            assert brute == Fraction(1, maximum), (a,b,brute,maximum)
            witness = bezout_in_segment_box(p, q)
            assert point_segment_squared(witness, (0,0), (p,q)) == Fraction(1, maximum)
            assert maximum == a*a+b*b if gcd(a,b)==1 else maximum < a*a+b*b
            cases += 1
    print('Exact point-to-segment brute-force checks passed:', cases, 'rectangles a,b <= 5.')
    for t in (1, 22, 43, 64):
        assert t % 21 == 1
        a,b=28*t,36*t
        maximum,p,q=primitive_max(a,b)
        assert (p,q)==(a-1,b-1), (t,maximum,p,q)
        x,y=bezout_in_segment_box(p,q)
        assert point_segment_squared((x,y),(0,0),(p,q))==Fraction(1,maximum)
        assert 4*b-2*a-7>0 and 4*a-2*b-7>0
        print('Interior-winner family check: t=%d, a=%d, b=%d, M=%d, witness=(%d,%d)' % (t,a,b,maximum,x,y))
    print('All integer/rational checks passed.')

if __name__=='__main__':
    main()
