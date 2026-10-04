#!/usr/bin/env python3
from fractions import Fraction
from math import log, isclose

def cr(a,b,c,d):
    # Hilbert cross-ratio quotient for [c,d] inside [a,b].
    return (d-a)*(b-c)/((c-a)*(b-d))

def psi(a,b,x):
    return 0.5*log(float((x-a)/(b-x)))

tests = [
    (Fraction(-3), Fraction(5), Fraction(-1), Fraction(2)),
    (Fraction(-4), Fraction(2), Fraction(-2), Fraction(1)),
    (Fraction(-7,2), Fraction(9,2), Fraction(-1,2), Fraction(3,2)),
    (Fraction(-11,3), Fraction(13,4), Fraction(-5,4), Fraction(7,6)),
]
for a,b,c,d in tests:
    assert a < c < 0 < d < b
    r = cr(a,b,c,d)
    A,B = 1/c, 1/d
    C,D = 1/a, 1/b
    rp = cr(A,B,C,D)
    assert r == rp, (r, rp)

# Check the coordinate isometry against the cross-ratio formula on fixed samples.
for a,b,c,d in tests:
    x = c + (d-c)*Fraction(1,3)
    y = c + (d-c)*Fraction(4,5)
    direct = 0.5*log(float((y-a)*(b-x)/((x-a)*(b-y))))
    coord = abs(psi(a,b,y)-psi(a,b,x))
    assert isclose(direct, coord, rel_tol=1e-13, abs_tol=1e-13)

print("VERIFY_OK")
