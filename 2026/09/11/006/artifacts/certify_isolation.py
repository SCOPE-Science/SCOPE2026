"""FINAL certificate (stdlib only): isolation horn on mu in [1,2].

Setup (proved in DRAFT.md from the Albouy-Chenciner reduction):
  Square+center q1=(1/2,1/2),... (I=1) is a CC for every mu>0 (radial force).
  Eliminate q5 via COM (q5 = -(s1+...+s4)/mu), constrain I=1 with multiplier c.
  S(mu) = constrained Hessian in the 8-dim (s1..s4) space, with nu = 1/mu.
  Z2 = half-turn+swap splits S into even (in-section, 2x2) and odd
  (symmetry-breaking, 4x4) blocks. Exact Q(sqrt2) derivation in DRAFT.md gives:

  EVEN: E = [[Eaa,Eab],[Eab,Eaa]],
    Eaa = 12 + 3s + 12s/nu,  Eab = -12 + 3s + 12s/nu   (s = sqrt2).
  ODD: O = [[P,Q],[Q,R]], P = pI + bJ, R = pI - bJ, Q = qI, J = [[0,1],[1,0]],
    p = 8nu + 18s nu + 6 + 17s + 6s/nu,
    b = 24s + 6s/nu,
    q = 8nu + 18s nu - 2 + 16s.
  Since all blocks commute: det(O - lI) = [((p-l)^2 - b^2) - q^2]^2,
    so odd eigenvalues are p +/- sqrt(b^2+q^2), each doubled.

This script certifies with exact Fraction arithmetic + the rigorous enclosure
1.4142 < sqrt2 < 1.4143 (from 1.4142^2 < 2 < 1.4143^2):
  (a) even block PD (index 0, det > 0) for all nu in [1/2,1];
  (b) odd block PD (index 0, det > 0) for all nu in [1/2,1]:
        low eigenvalue p - sqrt(D) > 0 via p > 0 and Z := p^2 - b^2 - q^2
        = (p-q)(p+q) - b^2 = 2(4nu+1)L(nu)/nu > 0,
        L(nu) = (25+38s)nu - 84 + 36s, increasing with L(1/2) > 0.
  Hence both endpoint Morse indices are 0 and S(mu) is nondegenerate on all
  of [1,2]: equivariant degree constant (+1), no symmetry-breaking branch
  from the square+center family over (1,2): the TARGET's isolation horn.
"""
from fractions import Fraction as F

S2LO = F(14142, 10000)
S2HI = F(14143, 10000)
assert S2LO * S2LO < 2 < S2HI * S2HI, "sqrt2 enclosure"
print("sqrt2 in [1.4142, 1.4143]:", float(S2LO), float(S2HI))

# ---------- (a) even block ----------
# Eaa - Eab = 24 - 12s/nu... recompute: Eaa-Eab = (12+3s+12s/nu)-(-12+3s+12s/nu) = 24.
# Eaa + Eab = 24 + 6s + 24s/nu >= 24 + 6*1.4142 + 24*1.4142 = 24+30*1.4142 > 0.
# Eaa = 12+3s+12s/nu > 0. det = 24*(Eaa+Eab) > 0.
Esum_lo = 24 + 6*S2LO + 24*S2LO  # at nu=1, minimal
Eaa_lo = 12 + 3*S2LO + 12*S2LO
print(f"Eaa-Eab = 24 exactly; Eaa+Eab >= {float(Esum_lo):.4f}; Eaa >= {float(Eaa_lo):.4f}")
assert Esum_lo > 0 and Eaa_lo > 0
print("PASS (a): even block PD, index 0, det = 24*(Eaa+Eab) > 0 on [1/2,1].")

# ---------- (b) odd block ----------
# p(nu) = 8nu + 18s nu + 6 + 17s + 6s/nu >= 6 + 17*1.4142 + 6*1.4142 + (8+18*1.4142)/2 > 0.
p_lo = 6 + 17*S2LO + 6*S2LO + (8 + 18*S2LO) * F(1, 2)
print(f"p >= {float(p_lo):.4f} > 0")
assert p_lo > 0
# L(nu) = (25+38s)nu - 84 + 36s; slope > 0; L(1/2) = -71.5 + 55s... exactly: (25+38s)/2-84+36s = 25/2+19s-84+36s = -143/2+55s.
# -143/2 + 55*1.4142 = -71.5+77.781 = 6.28 > 0.
Lhalf_lo = F(-143, 2) + 55*S2LO
slope_lo = 25 + 38*S2LO
print(f"L(1/2) >= {float(Lhalf_lo):.4f} > 0; slope >= {float(slope_lo):.4f} > 0")
assert Lhalf_lo > 0 and slope_lo > 0
# Z(nu) = 2(4nu+1)L(nu)/nu > 0 on [1/2,1] since all factors > 0.
print("PASS (b): Z > 0 on [1/2,1] => p^2 > b^2+q^2 => low odd eigenvalue p-sqrt(D) > 0;")
print("         high odd eigenvalue p+sqrt(D) >= p > 0. Odd block PD, index 0, det = Z^2 > 0.")

print()
print("CONCLUSION: transverse Hessian PD (Morse index 0) at mu=1 and mu=2,")
print("nondegenerate for every mu in [1,2]. Equivariant degree constant (+1/-1 same),")
print("no degree jump: TARGET isolation horn established; no symmetry-breaking branch")
print("bifurcates from the square-with-center family over (1,2).")
