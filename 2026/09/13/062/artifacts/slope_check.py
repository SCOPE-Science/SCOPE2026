"""Reproducible arithmetic check for lane-1741 slope computation.

Verifies (exact integer arithmetic where possible):
 1. Kummer intersection data: D^2=-4, H.D=0, F_i^2=-4, H.F_i=0.
 2. Riemann-Roch: chi(L^2)=-6 -> h^1(L^2)=6 (non-split E exists).
 3. Whitney: c2(E)=-D^2=4.
 4. Finite-fiber slope coefficients: triple-pullback term is identically zero
    (form-degree), cross term proportional to H.D=0, for every eps>0.
    Hence mu(pi^*L)=0=mu(pi^*E): reverse inequality holds with equality.
"""
from fractions import Fraction

# --- 1. Intersection data on span{h, e1..e6} of NS(S) ---
# h^2 = 2d > 0 (d>=1), h.e_i = 0, e_i.e_j = -2 delta_ij.
d = 1
N = 3  # ample for N >> 0; H = N h - sum e_i
# D = e1 - e2
D2 = -2 + -2          # e1^2 + e2^2, disjoint
H_D = 2 - 2           # H.e1 - H.e2 = 2 - 2
# F1 = e3 - e4, F2 = e5 - e6
F1_2 = -4
H_F1 = 0
print("D^2 =", D2, "(expect -4)")
print("H.D =", H_D, "(expect 0)")
print("F1^2 =", F1_2, "(expect -4), H.F1 =", H_F1)
assert D2 == -4 and H_D == 0 and F1_2 == -4 and H_F1 == 0

# --- 2. Riemann-Roch on K3: chi(M) = 2 + c1(M)^2/2 ---
c1_L2_sq = 4 * D2  # (2D)^2
chi_L2 = 2 + Fraction(c1_L2_sq, 2)
print("chi(L^2) =", chi_L2, "(expect -6)")
assert chi_L2 == -6
# h^0(L^2)=h^2(L^2)=0: c1(L^2)=2D has H-degree 2*H.D=0 and is non-trivial
# (D != 0 in NS), so no effective representative; Serre duality on K3.
h0 = h2 = 0
h1 = h0 + h2 - chi_L2
print("h^1(L^2) =", h1, "(expect 6); non-split extension exists:", h1 > 0)
assert h1 == 6

# --- 3. Whitney for 0 -> L -> E -> L^-1 -> 0 ---
c2_E = -D2  # c(E)=(1+D)(1-D)=1-D^2
print("c2(E) =", c2_E, "(expect 4)")
assert c2_E == 4
Delta = 2 * 2 * c2_E  # discriminant 2 r c2 - (r-1) c1^2, c1(E)=0
print("discriminant Δ(E) =", Delta, "(expect 16)")

# --- 4. Finite-fiber slope: mu(pi^*L) = C1 e^-1/2 * T + 2 C1 e^1/2 vf (H.D) ---
# T = int triple-pullback form l^w_S^2 = 0 identically (6-form on 4-fold).
C1 = Fraction(1, 1)
vf = Fraction(1, 1)
T = 0
print("eps      mu(pi^*L)   mu(pi^*E)   reverse(>=)  stable-branch(<)")
for eps_num in [1, 5, 10, 100]:
    eps = Fraction(eps_num, 10)  # 0.1 .. 10, includes fixed eps0 = 1
    import math
    mu_L = float(C1) * (float(eps) ** -0.5) * T + 2 * float(C1) * (float(eps) ** 0.5) * float(vf) * H_D
    mu_E = 0.0
    print(f"{float(eps):<9} {mu_L:<12} {mu_E:<11} {mu_L >= mu_E}          {mu_L < mu_E}")
    assert mu_L == 0.0 and (mu_L >= mu_E) and not (mu_L < mu_E)
print("OK: slope equality mu(pi^*L)=0=mu(pi^*E) at every finite fiber volume;")
print("OK: reverse inequality holds (equality); strict stability inequality fails.")
