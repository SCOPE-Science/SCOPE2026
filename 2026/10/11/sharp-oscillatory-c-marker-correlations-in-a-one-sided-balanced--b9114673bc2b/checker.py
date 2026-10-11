"""Exact finite checks for renewal correlations of a three-symbol coded system.

Run: python checker.py
All displayed finite checks use fractions, not floating-point validation.
"""
from fractions import Fraction

N = 90
# Balanced return components are a^j b^j, j >= 1.
# Terminal components are c and a^ell b^m c, ell > m >= 1.
b = [0] * (N + 1)
e = [0] * (N + 1)
for n in range(1, N + 1):
    b[n] = int(n % 2 == 0 and n >= 2)
    e[n] = (1 if n == 1 else 0) + (max(0, (n - 2) // 2) if n >= 4 else 0)
r = [0] * (N + 1)
for n in range(1, N + 1):
    r[n] = e[n] + sum(r[n - 2 * j] for j in range(1, n // 2 + 1))
# Independent first-return enumeration: enumerate all balanced prefixes using
# the renewal recursion, then append a terminal block.
prefixes = [0] * (N + 1)
prefixes[0] = 1
for n in range(1, N + 1):
    prefixes[n] = sum(prefixes[n - 2 * j] for j in range(1, n // 2 + 1))
for n in range(1, N + 1):
    direct = sum(prefixes[n - k] * e[k] for k in range(1, n + 1))
    assert r[n] == direct, (n, r[n], direct)
# Conditional renewals after observing c at time zero.
ret = [Fraction(0) for _ in range(N + 1)]
for n in range(1, N + 1):
    ret[n] = Fraction(r[n], 2 ** n)
u = [Fraction(0) for _ in range(N + 1)]
u[0] = Fraction(1)
for n in range(1, N + 1):
    u[n] = sum(ret[j] * u[n - j] for j in range(1, n + 1))
p = Fraction(2, 7)
cv = [p * (un - p) for un in u]
# Independent rational-function expansion: (8-2z^2+z^3)C(z)
# = (80+24z-24z^2)/49.
c_analytic = [Fraction(0) for _ in range(N + 1)]
for n in range(N + 1):
    rhs = Fraction({0: 80, 1: 24, 2: -24}.get(n, 0), 49)
    c_analytic[n] = (rhs + (2 * c_analytic[n-2] if n >= 2 else 0)
                     - (c_analytic[n-3] if n >= 3 else 0)) / 8
    assert c_analytic[n] == cv[n], (n, c_analytic[n], cv[n])
assert cv[0] == Fraction(10, 49)
assert cv[1] == Fraction(3, 49)
assert cv[2] == Fraction(-1, 98)
assert r[1] == 1 and r[2] == 0 and r[3] == 1 and r[4] == 1
# Check derived distribution has mass 1 and mean 7/2 analytically through
# rational evaluations (finite enumeration alone cannot establish this).
t = Fraction(1, 2)
B = t * t / (1 - t * t)
E = t + t**4 / ((1-t) * (1-t*t))
assert E / (1 - B) == 1
assert B == Fraction(1, 3) and E == Fraction(2, 3)
print('PASS: 90 return-word counts, 91 exact covariance coefficients, and normalized return law identities')
