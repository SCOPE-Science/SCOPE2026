"""Torsion-coefficient slope datum for t12533 (pure Alexander arithmetic).
AUDIT REPAIR: this script previously derived Ni-Wu d-values from a false
V0-via-alternating-sum identity. All d-invariant claims are withdrawn: no
Floer d-sum is computed or claimed. What remains is the exact torsion table
t_i = sum_{j>=1} j*a_{i+j} from the verified symmetrized Alexander polynomial
(slope datum only, not load-bearing for the exclusion).
"""
from fractions import Fraction as F
import sympy as sp

t = sp.Symbol('t')
# Unshifted Alexander (ordinary, Delta(1)=1):
D = (t**24-t**23+t**20-t**19+t**17-t**16+t**15-t**14+t**12-t**10+t**9-t**8+t**7-t**5+t**4-t+1)
P = sp.Poly(D, t)
coeffs = {e: int(P.nth(e)) for e in range(25)}
print("Alexander coeffs (t^0..t^24):")
print([coeffs[e] for e in range(25)])
# symmetrized: Delta_sym(t) = t^{-12} D, coefficients a_j for j=-12..12
a = {}
for j in range(-12, 13):
    a[j] = coeffs.get(j + 12, 0)
print("symmetric check:", all(a[j] == a[-j] for j in range(-12, 13)))
print("a_0 =", a[0], " sum =", sum(a.values()), "(want 1)")

# torsion coefficients t_i = sum_{j>=1} j*a_{i+j}, i = 0..11
tors = {}
for i in range(12):
    s = 0
    for j in range(1, 13):
        s += j * a.get(i + j, 0)
    tors[i] = s
print("torsion coeffs t_0..t_11:", [tors[i] for i in range(12)])
print("t_0 =", tors[0], " genus g = deg/2 =", 12)
# AUDIT REPAIR: everything below the torsion table (V_0 alternating sum,
# Ni-Wu d-values, self-gate) is deleted. No d-invariant is claimed.
print("No Floer d-sum claimed (audit repair).")
