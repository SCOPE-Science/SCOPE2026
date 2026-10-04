#!/usr/bin/env python3
from fractions import Fraction

gamma = Fraction(185, 10000)
delta = Fraction(1836, 10000)
H0 = 20736
R0 = 633
X0 = H0 + R0
X_endpoint = 68000

assert X0 == 21369
factor = (delta + gamma) / delta
correction = delta / (delta + gamma)
relative_excess = factor - 1
C_endpoint = Fraction(X0, 1) + correction * Fraction(X_endpoint - X0, 1)

assert factor == Fraction(2021, 1836)
assert correction == Fraction(1836, 2021)
assert relative_excess == Fraction(185, 1836)

f = float(factor)
ce = float(C_endpoint)
assert abs(f - 1.1007625272331154) < 1e-15
assert abs(ce - 63731.452251360715) < 1e-9

# Algebraic coefficient identity for any integral J >= 0:
# X-X0 = (delta+gamma)J, C-C0 = delta J.
for J in (Fraction(0), Fraction(1), Fraction(7,3), Fraction(1000)):
    dx = (delta + gamma) * J
    dc = delta * J
    assert dx == factor * dc

print("VERIFY_OK")
print("X0", X0)
print("increment_factor", repr(f))
print("relative_excess_percent", repr(100.0 * float(relative_excess)))
print("same_trajectory_C_at_X_68000", repr(ce))
