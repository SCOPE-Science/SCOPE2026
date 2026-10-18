#!/usr/bin/env python3
"""Reproducibility checks for the boundary conditional-law theorem.

Only standard-library arithmetic is used. Finite computations check identities
and sample convergence; the all-parameter limit is established in RESULT.md.
"""
from fractions import Fraction
from math import exp, log


def finite_exact_check():
    a = Fraction(9, 10)
    delta = 1-a
    lam = (1+a)/2
    b = a/2
    y = Fraction(1)
    for n in range(12):
        v = delta/y
        assert Fraction(0) < y <= 1
        next_y = lam*y-b*y*y
        assert next_y == lam*y*(1-(b/lam)*y)
        exact_reciprocal = v/lam + delta*b/(lam*lam*(1-(b/lam)*y))
        assert delta/next_y == exact_reciprocal
        # The exact leftmost-cylinder mass is (g_0'(0))**n = lam**n.
        # Its endpoint is y = (g_0)**n(1).
        y = next_y
    # Branch ranges and reverse transition probabilities.
    assert lam-b == Fraction(1, 2)
    assert (Fraction(1, 2)+delta/2+b) == 1
    for x in [Fraction(0), Fraction(1, 5), Fraction(1, 2), Fraction(1)]:
        assert (lam-a*x)+(delta/2+a*x) == 1
        assert 0 <= (lam-a*x) <= 1
        assert 0 <= (delta/2+a*x) <= 1


def bracket(a, z):
    delta = 1-a
    lam = (1+a)/2
    b = a/2
    y = 1.0
    n = 0
    while y > delta*z:
        y = lam*y-b*y*y
        n += 1
        assert n < 10000000
    return lam**n, lam**(n-1), delta*n, y/delta


def limit_check():
    for d in (0.01, 0.003, 0.001):
        for z in (0.25, 1.0, 4.0):
            low, high, t, yy = bracket(1-d, z)
            target = z/(1+z)
            assert low <= high
            assert abs(.5*(low+high)-target) < 0.045
            assert abs(t-2*log(1+1/z)) < 0.07
            assert yy <= z + 1e-12
    # Sharp cylinder endpoint normalization, not a claim of a planar density.
    for d in (0.02, 0.01, 0.005):
        lam = 1-d/2
        b = (1-d)/2
        y = 1.0
        product = 1.0
        for _ in range(int(65/d)):
            factor = 1-(b/lam)*y
            product *= factor
            y = lam*y*factor
        # lim lambda^n/y_n=1/prod(1-(b/lambda)y_j)
        norm = d/product
        assert abs(norm-1) < 0.13


if __name__ == '__main__':
    finite_exact_check()
    limit_check()
    print('VERIFY_OK')
