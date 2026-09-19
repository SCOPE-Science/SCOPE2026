from fractions import Fraction as F
from math import gcd

theta = F(1, 24)
rho = F(1, 1) / (2 - theta)
raw = F(1, 2) + 5 * theta
short = F(1, 2) + 7 * theta
long_root = 1 - rho + 5 * theta
raw_coefficient = F(1, 2) + 6 * theta - 4 * theta / (1 - rho)
long_coefficient = (1 - rho) - 4 * theta * rho / (1 - rho)

assert rho == F(24, 47)
assert raw == F(17, 24)
assert short == F(19, 24)
assert long_root == F(787, 1128)
assert long_root < short
assert raw_coefficient == F(113, 276) and raw_coefficient > 0
assert long_coefficient == F(341, 1081) and long_coefficient > 0

for r in range(2, 201):
    for s in range(1, r):
        p = r // gcd(r, s)
        assert (p == 2) == (r == 2 * s)

print("rho =", rho)
print("raw limiting exponent =", raw)
print("short-length limiting exponent =", short)
print("long-root limiting exponent =", long_root)
print("raw monotonicity coefficient =", raw_coefficient)
print("long monotonicity coefficient =", long_coefficient)
print("degree-two locus check: passed for 1 <= s < r <= 200")
