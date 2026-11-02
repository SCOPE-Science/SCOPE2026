#!/usr/bin/env python3
"""Exact-arithmetic checks for the homogeneous VA-II cold-start benchmark.

Uses only Python's standard library. Its finite checks supplement, not
replace, the algebraic proof in RESULT.md.
"""
from fractions import Fraction as F
from random import Random


def verify(e, R, h):
    assert e != 0 and R > 0 and R*R > e*e/2 and h > 0
    y = h*h*e*e/(8*R*R)
    if not (y < F(1, 3)):
        return False
    C0 = R*R - e*e/2
    g0 = e/R
    # First advection and first Riccati stage leave cold data untouched.
    # Independently solve the midpoint linear equations for (v+,r+).
    rmid = R / (1 + h*h*g0*g0/8)
    v = h*rmid*g0
    r = 2*rmid - R
    assert v == h*e/(1+y)
    assert r == R*(1-y)/(1+y)
    assert (v*v)/2 + r*r == R*R
    den = 1 - (h/2)*g0*v/(2*r)
    assert den == (1 - 3*y)/(1-y)
    assert den > 0
    g2 = g0/den
    # Last advection stage: moving uniform current v through half a step.
    g1 = g2 - (h/2)*v/r
    # Winding-aware periodic current deposition yields integrated current h*v/2.
    E1 = e - h*v/2
    dH = (v*v + E1*E1 - e*e)/2
    assert dH == h**4 * e*e*C0 / (8*R*R*(1+y)**2)
    assert dH > 0
    assert r*g1-E1 == 4*e*y*y/((1+y)*(1-3*y))
    return True


def pole_check(e, R, h):
    y = h*h*e*e/(8*R*R)
    if not (F(1,3) <= y < 1):
        return False
    g0=e/R
    rmid=R/(1+y); v=h*rmid*g0; r=2*rmid-R
    assert r > 0 and v*g0 > 0
    tau_pole = 2*r/(g0*v)
    assert tau_pole > 0 and tau_pole <= h/2
    return True


def main():
    rng=Random(16028)
    ok=0; singular=0
    for _ in range(1500):
        # Restrict to rational data with C0 positive.
        e = F(rng.choice([-1,1])*rng.randint(1,20),rng.randint(1,13))
        R = abs(e)*F(rng.randint(12,40),10)
        h = F(rng.randint(1,40),rng.randint(1,20))
        if verify(e,R,h): ok+=1
        if pole_check(e,R,h): singular+=1
    assert verify(F(1),F(1),F(1))
    assert verify(F(-1),F(1),F(3,2))
    assert pole_check(F(1),F(1),F(5,3))
    assert pole_check(F(1),F(1),F(2))
    # Equality threshold: e=3, R=3; h=sqrt(8/3) is irrational,
    # so inspect the exact polynomial denominator at y=1/3.
    y=F(1,3)
    assert 1-3*y == 0 and 1-y > 0
    assert ok>200 and singular>100
    print('PASS: %d well-defined rational cold-start runs and %d Riccati-pole runs'% (ok,singular))
    print('PASS: exact threshold algebra, modified energy, physical drift, and scaled-field discrepancy')


if __name__ == '__main__':
    main()
