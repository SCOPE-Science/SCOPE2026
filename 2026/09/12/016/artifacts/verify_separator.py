"""Replay verifier: CFN separator f0 = q0000*q1111 - q0011*q1100 for D (single-triangle,
split 12|34, hybrid 1) versus S (4-sunlet order (1,2,3,4), hybrid 1).

Part A: exact symbolic check that f0 vanishes identically on the D parametrization
        (general symbols, sympy expansion).
Part B: exact rational (Fraction) stochastic witness on the S parametrization with
        f0 = 1/2400, certifying f0 does NOT vanish on S.
Part C: numeric sanity check that f0 vanishes on D at a stochastic point.

Run: python3 output/artifacts/verify_separator.py  -> prints VERIFY_OK
"""
from fractions import Fraction

# ---------- Part A: symbolic D vanishing ----------
import sympy as sp

A0, A1, B0, B1, C0, C1, D0, D1 = sp.symbols('A0 A1 B0 B1 C0 C1 D0 D1')
E0, E1 = sp.symbols('E0 E1')
F0, F1, H0, H1, K0, K1 = sp.symbols('F0 F1 H0 H1 K0 K1')
L = sp.symbols('L')

# D parametrization: q = A B C D E_{g1+g2} (L F_g1 H_{g1+g2} + (1-L) K_g1 H_g2)
M00 = L * F0 * H0 + (1 - L) * K0 * H0      # (g1,g2) = (0,0)
M11 = L * F1 * H0 + (1 - L) * K1 * H1      # (g1,g2) = (1,1)
q0000 = A0 * B0 * C0 * D0 * E0 * M00
q1111 = A1 * B1 * C1 * D1 * E0 * M11
q0011 = A0 * B0 * C1 * D1 * E0 * M00
q1100 = A1 * B1 * C0 * D0 * E0 * M11
f0_D = sp.expand(q0000 * q1111 - q0011 * q1100)
assert f0_D == 0, f"symbolic D check failed: {f0_D}"
print("Part A: f0 o psi_D expands to 0 identically (general symbols). PASS")

# ---------- Part B: exact stochastic witness on S ----------
# S parametrization: q = A B C D [L R_g1 S_{g1+g2} T_g4 + (1-L) S_g3 T_{g1+g4} U_g1]
# Witness (Fourier 0-params = 1; 1-params in (0,1); L = 1/2):
Lam = Fraction(1, 2)
p1, p2, p3, p4 = Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5)
r1, s1, t1, u1 = Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5)
one = Fraction(1, 1)


def qS(g1, g2, g3, g4):
     assert (g1 + g2 + g3 + g4) % 2 == 0
     P = {0: one}
     A = {0: one, 1: p1}[g1]
     B = {0: one, 1: p2}[g2]
     C = {0: one, 1: p3}[g3]
     Dd = {0: one, 1: p4}[g4]
     R = {0: one, 1: r1}[g1]
     Sv = {0: one, 1: s1}[(g1 + g2) % 2]
     T = {0: one, 1: t1}[g4]
     S2 = {0: one, 1: s1}[g3]
     T2 = {0: one, 1: t1}[(g1 + g4) % 2]
     U = {0: one, 1: u1}[g1]
     return A * B * C * Dd * (Lam * R * Sv * T + (one - Lam) * S2 * T2 * U)


v0000 = qS(0, 0, 0, 0)
v1111 = qS(1, 1, 1, 1)
v0011 = qS(0, 0, 1, 1)
v1100 = qS(1, 1, 0, 0)
f0_S = v0000 * v1111 - v0011 * v1100
print(f"Part B: q0000={v0000}, q1111={v1111}, q0011={v0011}, q1100={v1100}")
print(f"Part B: f0(S witness) = {f0_S} (expect 1/2400)")
assert f0_S == Fraction(1, 2400), f"witness failed: {f0_S}"
assert v0000 != 0 and v1111 != 0
print("Part B: stochastic witness (all 1-params in (0,1), L=1/2) gives f0=1/2400. PASS")

# ---------- Part C: numeric D sanity ----------
Lp = 0.37
dp = dict(A0=1.0, A1=0.8, B0=1.0, B1=0.7, C0=1.0, C1=0.6, D0=1.0, D1=0.9,
          E0=1.0, E1=0.5, F0=1.0, F1=0.4, H0=1.0, H1=0.3, K0=1.0, K1=0.2, L=Lp)
n0000 = float(q0000.subs(dp))
n1111 = float(q1111.subs(dp))
n0011 = float(q0011.subs(dp))
n1100 = float(q1100.subs(dp))
assert abs(n0000 * n1111 - n0011 * n1100) < 1e-12
print("Part C: numeric D evaluation gives f0 = 0. PASS")

print("VERIFY_OK")
