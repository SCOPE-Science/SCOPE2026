"""Reproducible verification of the exact classical energy identities and
rational lower bounds used in the disproof of the fractional-bubble rate claim.

Checks (all exact rational arithmetic unless marked float):
  T^3 = 288*pi        (two disjoint unit balls, T = 8*pi*r^2, r^3=3/(4*pi))
  S0^3 = 1000*pi/3   (standard double bubble, sum functional, S0 = 15*pi*a^2/2)
  C0^3 = 243*pi       (standard double bubble, cluster energy, C0 = 27*pi*a^2/4)
with a^3 = 8/(9*pi). Hence C0^3 < T^3 < S0^3 strictly, and
  S0/T = (125/108)^(1/3),  T^3 - C0^3 = 45*pi.
Quantitative gaps from rational bounds + pi in (3.14, 22/7):
  S0 - T >= 0.47,  T - C0 >= 0.50.
"""
from fractions import Fraction

# --- exact symbolic identities in pi (checked by hand algebra, verified numerically) ---
import math
pi = math.pi
r = (3 / (4 * pi)) ** (1 / 3)
a = (8 / (9 * pi)) ** (1 / 3)
T = 8 * pi * r * r
S0 = 15 * pi * a * a / 2
C0 = 27 * pi * a * a / 4
print("float: T=%.6f C0=%.6f S0=%.6f" % (T, C0, S0))
print("float cubes/pi: T^3/pi=%.6f (288), S0^3/pi=%.6f (1000/3), C0^3/pi=%.6f (243)"
      % (T**3 / pi, S0**3 / pi, C0**3 / pi))
assert abs(T**3 / pi - 288) < 1e-9
assert abs(S0**3 / pi - Fraction(1000, 3)) < 1e-9
assert abs(C0**3 / pi - 243) < 1e-9
assert abs((S0 / T) ** 3 - 125 / 108) < 1e-12
assert abs((T**3 - C0**3) / pi - 45) < 1e-9

# --- exact rational checks (no floating point) ---
# (i) ratio bound: (125/108)^(1/3) > 1.049  <=>  1.049^3 < 125/108
lhs = Fraction(1049, 1000) ** 3
rhs = Fraction(125, 108)
print("1.049^3 =", lhs, "=", float(lhs), " ; 125/108 =", rhs, "=", float(rhs))
assert lhs < rhs  # 1.154320649 < 1.157407407

# (ii) T > 9.67 using only pi > 3.14: T^3 = 288*pi > 288*3.14 > 9.67^3 ?
print("288*3.14 =", 288 * Fraction(314, 100), " ; 9.67^3 =", Fraction(967, 100) ** 3)
assert 288 * Fraction(314, 100) > Fraction(967, 100) ** 3  # 904.32 > 904.231063
# gap S0 - T = T*(ratio-1) > 9.67 * 0.049
gap_sum = Fraction(967, 100) * Fraction(49, 1000)
print("S0 - T >", float(gap_sum))
assert gap_sum >= Fraction(47, 100)  # 0.47383 >= 0.47

# (iii) T - C0 > 0.50: numerator T^3-C0^3 = 45*pi > 45*3.14 = 141.3;
# denominator T^2+T*C0+C0^2 < 3*T^2 (C0<T), T < 9.68 via pi < 22/7.
print("45*3.14 =", 45 * Fraction(314, 100))
assert 45 * Fraction(314, 100) == Fraction(1413, 10)
print("288*22/7 =", 288 * Fraction(22, 7), " ; 9.68^3 =", Fraction(968, 100) ** 3)
assert 288 * Fraction(22, 7) < Fraction(968, 100) ** 3  # 905.14 < 907.039
den = 3 * Fraction(968, 100) ** 2
print("denominator <", float(den))
assert Fraction(1413, 10) / den > Fraction(1, 2)  # 141.3/281.1072 = 0.5027 > 0.50
print("T - C0 >", float(Fraction(1413, 10) / den))

print("ALL CHECKS PASSED: |T - P0| >= 0.47 under either reading of P0.")
