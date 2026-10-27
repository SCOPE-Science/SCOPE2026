#!/usr/bin/env python3
"""Independent elementary checks for the two-loss variance-oracle recursion.

This program uses exact rational arithmetic for finite-depth identities and
branch enumeration; it does not replace the infinite-product argument.
"""
from fractions import Fraction as Q
from itertools import product
import math


def T(x, sign):
    return x * (1 + sign*x) / (1 + x*x)


def alpha(x):
    return x*x/(1+x*x)


# Verify the actual population-gradient-to-second-moment oracle update.
for i in range(1, 16):
    x = Q(i, 17)
    a = alpha(x)
    assert a == x*x/(x*x+1)
    for sign in (-1, 1):
        assert x - a*(x-sign) == T(x, sign)
        assert 0 < T(x, sign) < 1
    expected = (T(x, 1)**2 + T(x, -1)**2) / 2
    assert expected == x*x/(1+x*x)

# Check exact finite-state expectations and Jensen upper bound.
x0 = Q(3, 4)
xs = [x0]
for n in range(1, 9):
    xs = [T(x, s) for x in xs for s in (-1, 1)]
    assert all(0 < x < 1 for x in xs)
    mean_square = sum(x*x for x in xs)/len(xs)
    assert mean_square <= 1/(Q(n) + 1/(x0*x0))

# Check the exact chosen rare path and its limiting scaled ratio.
plus = x0
for n in range(1, 21):
    event_endpoint = T(plus, -1)
    scaled_endpoint = (2**n) * float(event_endpoint)
    assert scaled_endpoint > 0
    if n >= 16:
        assert 0.40 < scaled_endpoint < 0.55
    plus = T(plus, 1) if n <= 10 else float(T(float(plus), 1))

# A separate floating-point replay stays in a numerically safe range.
y = 0.75
D_values = []
for k in range(15):
    D_values.append((2**k)*(1-y))
    y = y*(1+y)/(1+y*y)
assert D_values[-1] > D_values[0] > 0
assert 0.45 < D_values[-1] < 0.47

print('VERIFY_OK: 15 exact oracle recurrences; 8 complete rational binary trees; 20 rare-event endpoint tests; finite product scaling')
