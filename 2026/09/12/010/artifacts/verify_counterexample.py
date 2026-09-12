"""Rigorous refutation of the claimed 15% cyclotomic smoothing-width improvement.

Extremal member: unit ideal lattice R = Z[x]/(x^1024+1) under the coefficient
embedding equals Z^1024, which is self-dual; hence L* = Z^1024 is a dual of a
power-of-two cyclotomic ideal lattice (dimension N = 1024).

Baseline (Micciancio-Regev/Banaszczyk, Lemma 3.3 form):
    s_B^2 = L / pi,  L = ln(2N(1 + 2^128)),  (lambda1(Z^1024) = 1).
Claimed width: s' = (85/100) s_B, so (s')^2 = (289/400)(L/pi).
First shell lower bound (2N = 2048 minimal vectors of norm 1):
    tail = rho_{1/s'}(L*\\{0}) >= 2048 exp(-pi (s')^2) = 2048 exp(-(289/400) L).
It suffices to show (289/400) L <= 101 ln 2, whence tail >= 2^11 * 2^-101
= 2^-90 > 2^-128 (margin 38 bits, factor >= 2^38).

All bounds use exact rational arithmetic (Fraction) plus certified wide
enclosures of ln2 and pi. Prints VERIFY_OK iff the refutation holds.
"""
from fractions import Fraction

N = 1024
TAIL_LOG2 = 128

# Certified wide enclosures: LN2_LO <= ln2 <= LN2_HI, PI_LO <= pi <= PI_HI.
LN2_LO = Fraction("0.6931471805")
LN2_HI = Fraction("0.6931471806")
assert Fraction("0.693147180559945") > LN2_LO  # true value ln2 = 0.6931471805599...
assert Fraction("0.693147180559945") < LN2_HI

# L = ln(2048 (1 + 2^128)) = 139 ln2 + d, 0 < d = ln(1+2^-128) < 2^-128.
TINY_HI = Fraction(1, 2**128)
L_HI = 139 * LN2_HI + TINY_HI  # rigorous upper bound on L

# pi cancels exactly: pi (s')^2 = (289/400) L <= (289/400) L_HI.
C2 = Fraction(289, 400)  # (85/100)^2 exactly
Y_HI = C2 * L_HI         # rigorous upper bound on pi (s')^2

# Target: Y_HI <= 101 ln2  <=>  Y_HI <= 101 * LN2_LO.
K = 101
assert Y_HI <= K * LN2_LO, f"gap: {float(K * LN2_LO - Y_HI)}"

# Hence tail >= 2048 * e^{-101 ln2} = 2^11 * 2^-101 = 2^-90.
LOG2_TAIL_LO = 11 - K  # = -90
assert LOG2_TAIL_LO == -90
assert LOG2_TAIL_LO > -TAIL_LOG2
margin_bits = LOG2_TAIL_LO - (-TAIL_LOG2)  # 38
assert margin_bits == 38

# Strengthening: ANY uniform factor c with c^2 < 139*LN2_LO/(L_HI) fails,
# i.e. no constant improvement at all is possible for this member.
# c=0.85 gives c^2 = 0.7225 << 1 - 2^-120.
assert C2 < Fraction(139) * LN2_LO / L_HI

import math
L_fp = float(139 * Fraction("0.69314718055994530942"))
sB_fp = math.sqrt(L_fp / math.pi)
sp_fp = 0.85 * sB_fp
first_shell = 2 * N * math.exp(-math.pi * sp_fp ** 2)
print(f"L <= {float(L_HI):.10f}  (true ~{L_fp:.10f})")
print(f"pi (s')^2 <= {float(Y_HI):.10f} <= 101 ln2 = {float(K * LN2_LO):.10f}")
print(f"tail(Z^1024 at s'=0.85 s_B) >= 2^-90 ~= {2.0**-90:.3e}")
print(f"target bound 2^-128 ~= {2.0**-128:.3e}")
print(f"violation margin: {margin_bits} bits (factor >= 2^38 ~= {2.0**38:.3e})")
print(f"[float x-check] s_B~{sB_fp:.6f}, s'~{sp_fp:.6f}, "
      f"first-shell~{first_shell:.3e}, ratio to 2^-128 ~{first_shell / 2.0**-128:.3e}")
print("VERIFY_OK")
