#!/usr/bin/env python3
"""Finite reproducibility checks for the stated three-column determinant facts.

The analytic uniqueness proof and continuous parameter bounds are given in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import sqrt


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def matrix(r):
    return [[r if i == j else -1 for j in range(3)] for i in range(3)]


def value(p, r):
    return abs(det3(matrix(r))) / (abs(r)**p + 2)**(3/p)


def root(p):
    lo, hi = 0., 1.
    for _ in range(100):
        m = (lo+hi)/2
        if m+m**(p-1) < 1:
            lo = m
        else:
            hi = m
    return (lo+hi)/2


def run():
    for s in (Fraction(-5, 2), Fraction(-1, 1), Fraction(0),
              Fraction(1, 3), Fraction(1, 2), Fraction(3, 4),
              Fraction(1), Fraction(2), Fraction(7, 2)):
        assert det3(matrix(s)) == (s+1)**2*(s-2)
    max_abs = 0
    winners = 0
    for a in product((-1, 1), repeat=9):
        m = [a[k:k+3] for k in (0, 3, 6)]
        d = abs(det3(m))
        max_abs = max(max_abs, d)
        winners += (d == 4)
    assert max_abs == 4 and winners > 0
    phi = (1+sqrt(5))/2
    rr = (sqrt(5)-1)/2
    assert abs(value(3, rr)-phi) < 2e-14
    assert phi**3 > 4
    for p in (2.001, 2.4, 3., 4., 7., 30.):
        r = root(p)
        assert abs(r+r**(p-1)-1) < 1e-13
        b = (1+r)*((1+r)*(2-r))**(1-3/p)
        assert abs(value(p, r)-b) < 2e-12
        assert value(p, r) > value(p, max(0, r-0.02))
        assert value(p, r) > value(p, min(2, r+0.02))
    print('CHECK_OK: 512 exact sign matrices; rational determinants; golden root; sample exponent identities.')


if __name__ == '__main__':
    run()
