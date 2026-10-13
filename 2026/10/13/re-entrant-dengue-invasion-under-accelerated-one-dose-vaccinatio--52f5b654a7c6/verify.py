#!/usr/bin/env python3
"""Exact rational interval check of the three invasion multipliers."""
from fractions import Fraction as F
from math import factorial


def partial(n):
    return sum((F((-1) ** k, factorial(k)) for k in range(n + 1)), F(0))

lo, hi = partial(29), partial(30)
assert F(0) < lo < hi < F(1)


def val(coefficients, e):
    return sum((F(c) * e**k for k, c in coefficients.items()), F(0))


def interval(coefficients, denominator=1):
    lower = val({k: c for k, c in coefficients.items() if c > 0}, lo)
    lower += val({k: c for k, c in coefficients.items() if c < 0}, hi)
    upper = val({k: c for k, c in coefficients.items() if c > 0}, hi)
    upper += val({k: c for k, c in coefficients.items() if c < 0}, lo)
    return lower / denominator, upper / denominator


def sub(i, j):
    return i[0] - j[1], i[1] - j[0]

B0 = interval({0: 1, 2: 1000, 3: -1000, 4: -2, 5: -1000, 6: 1000, 8: 1}, 2000)
C_inf = interval({0: 1, 4: 1000, 6: -1000, 8: -2009}, 4000)
C_one = interval({0: 1, 4: 5000, 6: -7000, 8: -10041}, 8000)
B_inf = sub(B0, C_inf)
B_one = sub(B0, C_one)
N = (1-hi**4, 1-lo**4)


def multiplier(i):
    assert i[0] > 0 and N[0] > 0
    return 28*i[0]/N[1], 28*i[1]/N[0]

K0, K1, Kinf = map(multiplier, (B0, B_one, B_inf))
assert K0[0] > F(117, 100) and K0[1] < F(118, 100)
assert K1[0] > F(91, 100) and K1[1] < F(92, 100)
assert Kinf[0] > F(105, 100) and Kinf[1] < F(106, 100)
assert K0[0] > 1 > K1[1] and Kinf[0] > 1
assert B_inf[0] > B_one[1]
for name, band in [('K(0)',K0), ('K(1)',K1), ('K(infty)',Kinf)]:
    print(name, 'in (', float(band[0]), ',', float(band[1]), ')')
print('VERIFY_OK')
