#!/usr/bin/env python3
"""Rational inequality certificate and separate numerical probes for
ranked integer Fourier coefficients of the middle-thirds Cantor measure.
Uses only the Python standard library. Run: python check_cantor.py.
The finite probes are not the proof of the infinite theorem.
"""
from fractions import Fraction as Q
from math import cos, pi, prod

# These algebraic inequalities are exact: pi < 22/7 and
# cos(x) >= 1-x^2/2+x^4/24-x^6/720 for 0 < x < 1.
x = Q(176, 189)  # upper bound on 8*pi/27
cos_lower = 1 - x*x/2 + x**4/24 - x**6/720
tail_lower = 1 - Q(4, 729)*Q(22, 7)**2
assert cos_lower > 0 and tail_lower > 0
assert cos_lower * tail_lower > Q(9, 16)

# Lower certificate for the first multiplier modulus.
first_lower = Q(1, 2)*(1 - Q(44, 63)**2/2) * (1 - Q(22, 7)**2/324)
assert first_lower > Q(9, 32)

# The universal bound C=(9/32)cos(pi/9) exceeds 1/4.
cos_one_ninth_lower = 1 - Q(22, 63)**2/2
assert Q(9, 32)*cos_one_ninth_lower > Q(1, 4)

# Numerical consistency probes are deliberately distinct from the proof.
def f(n, depth=35):
    n = abs(int(n))
    while n and n % 3 == 0:
        n //= 3
    if n == 0:
        return 1.0
    return prod(abs(cos(2*pi*n/3**j)) for j in range(1, depth+1))

f1, f4 = f(1), f(4)
C = (9/32)*cos(pi/9)
assert 0.37 < f1 < 0.38
assert 0.265 < f4 < 0.266
assert f1 > f4 > C > .25
for n in range(1, 20001):
    m = n
    while m % 3 == 0:
        m //= 3
    value = f(m)
    if m == 1:
        assert abs(value-f1) < 1e-12
    elif m == 4:
        assert abs(value-f4) < 1e-12
    else:
        assert value < C + 1e-10, (n, m, value, C)
print('CANTOR_TWO_TIER_RATIONAL_CERTIFICATE_OK')
print('first_lower', float(first_lower))
print('second_ratio_lower', float(cos_lower*tail_lower))
print('gap_certificate_C', C)
print('f1', f1, 'f4', f4)
print('finite_probes', 20000)
