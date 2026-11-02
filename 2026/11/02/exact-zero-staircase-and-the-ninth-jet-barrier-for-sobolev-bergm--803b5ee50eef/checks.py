#!/usr/bin/env python3
"""Finite numerical and exact sanity checks for a jet-penalized Bergman kernel.
Requires Python 3.10+ and NumPy. Infinite-order root counts use the proof,
not these finite tests.
"""
from fractions import Fraction
from math import factorial, pi, sin, cos, sqrt, isclose
import cmath
import numpy as np

checks = 0
for m in range(1, 13):
    n = m + 1
    thresholds = [1 / (4 * sin((2*j+1)*pi/(2*n))**2) for j in range(n)]
    first = min(thresholds)
    expected_first = 0.25 if m % 2 == 0 else 1/(4*cos(pi/(2*n))**2)
    assert isclose(first, expected_first, rel_tol=1e-13)
    checks += 1
    for j, threshold in enumerate(thresholds):
        t = cmath.exp(1j*(2*j+1)*pi/n)
        assert abs(threshold*t**m*(1-t)**2-1) < 2e-11
        checks += 1
    for k in range(1, 25):
        c = n*(k/25)
        if min(abs(c-v) for v in thresholds) < 0.025:
            continue
        # P(t)=1-c*t**m*(1-t)**2; roots of polynomial numerator.
        coeff = np.zeros(m+3)
        coeff[0] = 1
        coeff[m] -= c
        coeff[m+1] += 2*c
        coeff[m+2] -= c
        roots = np.polynomial.polynomial.polyroots(coeff)
        actual = sum(abs(root) < 1-1e-7 for root in roots)
        expected = sum(c > v for v in thresholds)
        assert actual == expected, (m,c,actual,expected)
        # All roots are simple at the permitted coupling; polynomial residual small.
        assert max(abs(np.polynomial.polynomial.polyval(root, coeff)) for root in roots) < 3e-6
        assert min(abs(a-b) for i,a in enumerate(roots) for b in roots[i+1:]) > 1e-5
        checks += 3
    # Normalization of modified coefficient for rational Tikhonov penalties.
    for q in range(1, 7):
        tau = Fraction(q,100)
        D = tau*n*factorial(m)**2
        c = Fraction(n)*D/(1+D)
        a_new = Fraction(n)/(1+D)
        assert Fraction(n)-c == a_new
        assert 0 < c < n
        checks += 2
for m in range(1,45):
    n=m+1
    largest=1/(4*sin(pi/(2*n))**2)
    assert (largest<n) == (m<=8)
    checks+=1
print('VERIFY_OK',checks, 'finite assertions')
