#!/usr/bin/env python3
"""Corroborative coefficient checks for the fixed-coupling low-band asymptotic."""
from math import factorial, pi, sqrt


def c_target(n):
    return 2 ** (n + 2) / (sqrt(pi) * factorial(n))


def c_even(m):
    # Ratio of the leading source-normalized decaying and E-derivative coefficients.
    value = (2 ** (2 * m) * factorial(m)) / factorial(2 * m)
    deriv = sqrt(pi) * factorial(m) / 4
    return value / deriv


def c_odd(m):
    value = (2 ** (2 * m + 0.5) * factorial(m)) / factorial(2 * m + 1)
    deriv = sqrt(2 * pi) * factorial(m) / 8
    return value / deriv


for n in range(13):
    got = c_even(n // 2) if n % 2 == 0 else c_odd((n - 1) // 2)
    want = c_target(n)
    assert abs(got / want - 1.0) < 2e-15, (n, got, want)

# Check the algebraic first-order Robin quotient numerically; the residual times a^2 stays bounded.
gamma = 0.7
n = 4
vals = []
for a in (50.0, 100.0, 200.0, 400.0):
    q = (-a + gamma + n / a) / (a + gamma - (n + 1) / a)
    residual = q - (-1.0 + 2.0 * gamma / a)
    vals.append(abs(residual) * a * a)
assert max(vals) < 20.0, vals
print('VERIFY_OK')
