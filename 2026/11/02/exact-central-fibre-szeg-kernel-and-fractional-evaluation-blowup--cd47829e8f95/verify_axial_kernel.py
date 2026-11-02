#!/usr/bin/env python3
"""Independent arithmetic checks for a restricted reproducing kernel.

The theorem for all degrees and parameters is established in the accompanying proof.
This script verifies a finite set of exact coefficients and sample analytic values.
"""
from fractions import Fraction
from math import comb, asin, sqrt, pi, isclose

def reciprocal_moment(k):
    return Fraction(4**k, comb(2*k,k))

def closed_form(t):
    return 1/(1-t)+sqrt(t)*asin(sqrt(t))/(1-t)**1.5 if t else 1.0

# Exact independent evaluations of the torus moment via Vandermonde sums.
for k in range(0,51):
    moment = Fraction(sum(comb(k,j)**2 for j in range(k+1)),4**k)
    assert moment == Fraction(comb(2*k,k),4**k)
    assert 1/moment == reciprocal_moment(k)
    if k:
        assert reciprocal_moment(k)/reciprocal_moment(k-1) == Fraction(2*k,2*k-1)

# Elementary kernel formula against an absolutely convergent coefficient sum.
for t in (0.0, 0.1, 0.25, 0.5, 0.75):
    partial = sum(float(reciprocal_moment(k)) * t**k for k in range(400))
    assert isclose(partial, closed_form(t),rel_tol=3e-13,abs_tol=3e-13), (t,partial,closed_form(t))

# Three-term boundary expansion: error is O(sqrt(1-t)), not O(1).
for u in (0.05, 0.02, 0.01):
    t=1-u*u
    approx=(pi/2)*u**(-3)-(pi/4)*u**(-1)+Fraction(1,3)
    assert abs(closed_form(t)-float(approx)) < 2.0*u
print('PASS: 51 exact torus moments and coefficient recurrences; 5 kernel evaluations; 3 boundary checks')
