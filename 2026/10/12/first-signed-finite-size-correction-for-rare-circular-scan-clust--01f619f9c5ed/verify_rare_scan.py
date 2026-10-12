#!/usr/bin/env python3
"""Exact local coefficient checks for rare circular-window cluster starts.

The analytic proof, not finite tests, establishes the general asymptotic.
"""
from fractions import Fraction
from math import factorial, comb

count = 0
for k in range(4, 33):
    m = k - 1
    # The Gamma(m,1) CDF Taylor coefficients at degrees m and m+1.
    c0 = Fraction(1, factorial(m))
    c1 = Fraction(-m, factorial(m + 1))
    assert c0 == Fraction(1, factorial(k - 1))
    count += 1
    # Integrate s^(k-3) (q-s)^2 /(k-3)! exactly.
    integral = sum(Fraction((-1)**j * comb(2, j), k-2+j)
                   for j in range(3)) / factorial(k-3)
    assert integral == Fraction(2, factorial(k))
    count += 1
    cluster_next = c1 - integral
    assert cluster_next == Fraction(-(k+1), factorial(k))
    count += 1
    # Local graph errors N q^(2k-2) and N q^(k+1), q=t*N^(-1/(k-1)).
    assert Fraction(2*k-2-(k-1), k-1) == 1
    assert Fraction(k+1-(k-1), k-1) == Fraction(2, k-1)
    count += 1
    # Existence of a in (1/(k-1),1/2) used in normalization.
    assert Fraction(1, k-1) < Fraction(1, 2)
    count += 1
print('VERIFY_OK', count, 'exact assertions')
