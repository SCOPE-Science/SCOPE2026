#!/usr/bin/env python3
"""Exact rational certificate for the quartic Gaussian Fock counterexample."""
from fractions import Fraction as Q
from math import factorial

r = Q(2063, 2500)
a = Q(99, 100)
b = Q(1, 7)
f = (r, r*b-a, -a*b)
g = (-a*r, 1-a*r*b, b)

def gaussian_fourth(coefficients):
    square = [sum((coefficients[j] * coefficients[k-j]
                   for j in range(len(coefficients))
                   if 0 <= k-j < len(coefficients)), Q(0))
              for k in range(2*len(coefficients)-1)]
    return sum((Q(factorial(k), 2**k) * square[k]**2
                for k in range(len(square))), Q(0))

f4 = gaussian_fourth(f)
g4 = gaussian_fourth(g)
difference = g4 - f4
expected = -Q(23857292957391399561, 18757812500000000000000000)
assert difference == expected
assert difference < 0
assert Q(1,2) < r*r
assert r**4 < Q(1,2)
assert Q(0) < 1-a*a
print('PASS: exact polynomial Gaussian fourth-moment identities')
print('norm_f_fourth =', f4)
print('norm_g_fourth =', g4)
print('norm_g_fourth - norm_f_fourth =', difference)
print('PASS: pointwise factor coefficient and radius bounds')
