"""Target-route numeric checks (no claim object): fidelity-radius constants,
AM-GM determinant bound, phase-circle Lipschitz lower bound illustration.
numpy only.
"""
import numpy as np

# 1. Fidelity radius constants: rank<=18 cut -> F <= sqrt(18)/6 = 1/sqrt(2)
Fbound = np.sqrt(18) / 6
print("sqrt(18)/6 =", Fbound, " 1/sqrt(2) =", 1 / np.sqrt(2))
assert abs(Fbound - 1 / np.sqrt(2)) < 1e-15
r = 1 - Fbound
print("r = 1-1/sqrt(2) =", r, " vs 1/24 =", 1 / 24, " ratio =", r / (1 / 24))
assert r > 1 / 24

# Cauchy-Schwarz tightness demo: worst-case flat spectrum rank 18 -> equality
lam = np.zeros(36); lam[:18] = 1 / 18
F = (1 / 6) * np.sum(np.sqrt(lam))
print("worst-case flat rank-18 F =", F, "(expect 1/sqrt2)")
assert abs(F - 1 / np.sqrt(2)) < 1e-12

# 2. AM-GM determinant bound: random 36x36 M with Tr MM+ = 1 -> |det| <= 36^-18
rng = np.random.default_rng(0)
for t in range(3):
    A = rng.standard_normal((36, 36)) + 1j * rng.standard_normal((36, 36))
    M = A / np.sqrt(np.trace(A @ A.conj().T).real)
    assert abs(np.trace(M @ M.conj().T).real - 1) < 1e-9
    print(f"trial {t}: 36^18*|det| =", abs(np.linalg.det(M)) * 36 ** 18, "(must be <=1)")
    assert abs(np.linalg.det(M)) * 36 ** 18 <= 1 + 1e-6
# equality case: unitary/6
Q, _ = np.linalg.qr(rng.standard_normal((36, 36)) + 1j * rng.standard_normal((36, 36)))
print("equality case 36^18*|det(Q/6)| =", abs(np.linalg.det(Q / 6)) * 36 ** 18, "(expect 1)")
assert abs(abs(np.linalg.det(Q / 6)) * 36 ** 18 - 1) < 1e-9

# 3. Phase-circle Lipschitz lower bound: |e^{imθ}-1|g/θ -> m*g as θ->0
for m, g in [(6, 0.5), (108, 1.0)]:
    th = 1e-4
    print(f"m={m}, g={g}: ratio={abs(np.exp(1j*m*th)-1)*g/th:.6f} (expect ~{m*g})")
print("FIDELITY_RADIUS_CONSTANTS_OK")
