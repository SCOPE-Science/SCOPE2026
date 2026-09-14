"""Exact rational verification for the inside-Voigt-Reuss enclosure.
Checks: primal J=119/100; ln2 series bounds; P(mu_hi)<889/1000;
monotonicity; and all strict-inclusion integer cross-products.
Uses only the Fraction class (exact arithmetic).
"""
from fractions import Fraction

# --- Primal two-point certificate ---
m = Fraction(5, 4)
v = Fraction(3, 16)
c0 = Fraction(4, 25)
c1 = Fraction(-4, 25)
J = m + 2 * v * (c1 - c0) + m * v * (3 * c0 * c0 + (c1 - c0) ** 2 + 3 * c1 * c1)
assert J == Fraction(119, 100), J
print("primal J =", J)

# --- ln2 series: S3 = 2*sum_{k=0..3} 1/((2k+1) 3^{2k+1}) ---
S3 = sum(Fraction(2, (2 * k + 1) * 3 ** (2 * k + 1)) for k in range(4))
assert S3 == Fraction(53056, 76545), S3
R = Fraction(1, 78732)  # certified remainder upper bound
assert S3 > Fraction(6931, 10000)  # 530560000 > 530533395
assert S3 + R < Fraction(6932, 10000)
print("S3 =", S3, "=", float(S3))
print("S3+R =", S3 + R, "=", float(S3 + R))

mu_lo = Fraction(4, 3) * Fraction(6931, 10000)
mu_hi = Fraction(4, 3) * Fraction(6932, 10000)
assert mu_lo == Fraction(6931, 7500)
assert mu_hi == Fraction(1733, 1875)
assert Fraction(92, 100) < mu_lo and mu_hi < Fraction(93, 100)

# --- Dual polynomial bound ---
def P(mm):
    return -mm**3 / 8 + mm**2 / 2 + Fraction(17, 16) * mm - Fraction(27, 64)

p_hi = P(mu_hi)
assert p_hi == Fraction(374876538179, 421875000000), p_hi
assert p_hi < Fraction(889, 1000)  # cross-diff 170336821000 > 0
assert 889 * p_hi.denominator - 1000 * p_hi.numerator == 170336821000
print("P(mu_hi) =", p_hi, "=", float(p_hi))

# --- Monotonicity of P on [0.92, 0.93] ---
dlo = Fraction(-3, 8) * Fraction(93, 100) ** 2 + Fraction(92, 100) + Fraction(17, 16)
assert dlo == Fraction(132653, 80000) and dlo > 0
print("P' lower bound =", dlo, "=", float(dlo))

# --- Strict inclusions ---
assert Fraction(1000, 889) > Fraction(11, 10)  # 10000 > 9779
assert Fraction(119, 100) <= Fraction(12, 10)
assert mu_lo > Fraction(10, 11)  # Reuss endpoint 3/(4 ln2) < 11/10
assert Fraction(119, 100) < Fraction(5, 4)  # below Voigt
assert p_hi > 0
print("1000/889 =", float(Fraction(1000, 889)))
print("ALL EXACT CHECKS PASSED")
