#!/usr/bin/env python3
from fractions import Fraction
import math

pi = Fraction(30, 1)
rA = Fraction(1, 6)
u = Fraction(3, 5)
a = Fraction(2, 1)

kA = Fraction(1, 2) * u * a * a
join_drift = pi * rA - kA

assert kA == Fraction(6, 5)
assert join_drift == Fraction(19, 5)

# Exact geometric-Brownian escape formula, evaluated at one source-listed noise intensity.
x0 = 0.8
sigma = 2.0
t = 0.05
threshold = (
    math.log(1.0 / x0)
    + (float(kA) + sigma * sigma / 2.0) * t
) / (sigma * math.sqrt(t))
tail = 0.5 * math.erfc(threshold / math.sqrt(2.0))

assert tail > 0.0
assert abs(tail - 0.19579567066266268) < 1e-15

# A boundary-vanishing repair coefficient is zero at both probability boundaries.
def repaired_drift(x, B):
    return x * (1.0 - x) * B

def repaired_diffusion(x, sigma):
    return sigma * x * (1.0 - x)

for x in (0.0, 1.0):
    assert repaired_drift(x, 3.7) == 0.0
    assert repaired_diffusion(x, 2.0) == 0.0

print("VERIFY_OK")
print("k_A", float(kA))
print("all_join_A_drift_after_deletion", float(join_drift))
print("escape_probability", repr(tail))
