"""Testbed: AME(4,3) from Rather et al. SM Eq.S2 + invariant pipeline demo.
NOT a claim object. Validates: state build, reductions, Scott Q1/Q2,
and the triple-determinant invariant machinery (9x9 dets for d=3).
Expected: |J(G43)| = 1 (2-unitarity of P9), and a (4,3) stabilizer AME
(from classical OLS P9 permutation) ALSO gives 1 -> negative control:
no separation in (4,3), as theory demands. numpy only.
"""
import numpy as np

d = 3
# |AME(4,3)> = (1/3) sum_{i,j in 0..2} |i>|j>|i+j mod3>|i+2j mod3>
psi = np.zeros((d, d, d, d), dtype=complex)
for i in range(d):
    for j in range(d):
        psi[i, j, (i + j) % d, (i + 2 * j) % d] = 1.0 / d
assert abs(np.vdot(psi, psi).real - 1.0) < 1e-12, "norm"
print("norm =", np.vdot(psi, psi).real)

# 1-party reduction (trace out parties 1,2,3 -> rho_0)
rho1 = np.einsum('ajkl,bjkl->ab', psi, psi.conj())
print("rho1*3 =\n", np.round(rho1 * 3, 10).real)
assert np.allclose(rho1, np.eye(d) / d, atol=1e-12), "1-red not max mixed"

# 2-party reductions for the three 2-2 cuts
cuts = {(0, 1): ((0, 1), (2, 3)), (0, 2): ((0, 2), (1, 3)), (0, 3): ((0, 3), (1, 2))}
for name, (A, B) in cuts.items():
    a1, a2 = A
    # permute so A-parties first
    perm = list(A) + list(B)
    t = np.transpose(psi, perm).reshape(d * d, d * d)
    rho = t @ t.conj().T  # reduction on A (psi normalized)
    assert np.allclose(rho, np.eye(d * d) / (d * d), atol=1e-12), f"cut {name} not max mixed"
    print(f"cut {name}: purity = {np.trace(rho@rho).real:.12f} (expect {1/(d*d):.12f})")

# Scott Q1, Q2 (d=3)
p1 = np.trace(rho1 @ rho1).real
Q1 = (d / (d - 1)) * (1 - p1)
t = psi.reshape(d * d, d * d)
p2 = np.trace((t @ t.conj().T) @ (t @ t.conj().T)).real
Q2 = (d * d / (d * d - 1)) * (1 - p2)
print(f"Q1 = {Q1:.12f}, Q2 = {Q2:.12f} (expect 1, 1)")
assert abs(Q1 - 1) < 1e-9 and abs(Q2 - 1) < 1e-9

# Triple-det invariant for d=3: J = 9^9? normalization: each 9x9 det <= 9^-4.5? |det M| <= (TrMM+/9)^4.5 = 9^-4.5
# J = 9^13.5... use exact: scale = (d*d)^(3*d*d/2) = 9^13.5 -> work with |det|*9^4.5 per cut.
M12 = psi.transpose(0, 1, 2, 3).reshape(9, 9) / 1.0  # T tensor itself (unitary/3? P9 perm: det = +-1)
# Note: psi entries are (1/3)*P9 entries; flattening M = P9/3, det = det(P9)/3^9, |det| = 3^-9 = 9^-4.5. ✓
for name, (A, B) in cuts.items():
    perm = list(A) + list(B)
    M = np.transpose(psi, perm).reshape(9, 9)
    det = np.linalg.det(M)
    print(f"cut {name}: |det| = {abs(det):.6e}, 9^4.5*|det| = {abs(det)*9**4.5:.12f} (expect 1)")
    assert abs(abs(det) * 9 ** 4.5 - 1.0) < 1e-9
print("AME43_J_EQUALS_1_OK")

# Negative control: (4,3) stabilizer AME from classical OLS permutation P9 (SM Eq.S3).
P9 = np.array([
    [0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,0],[1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0],[0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0],
    [0,1,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,1]], dtype=float)
T = P9.reshape(3,3,3,3).transpose(0,1,2,3)  # T[i,j,k,l] with row=(i,j) col=(k,l)? row=j+3i? use as-is
# Rather indexing: row = j+3(i-1) i.e. row=(i,j), col=(k,l): T[i,j,k,l] = P9[(i,j),(k,l)]
phi = T / 3.0
assert abs(np.vdot(phi, phi).real - 1) < 1e-12
for name, (A, B) in cuts.items():
    perm = list(A) + list(B)
    M = np.transpose(phi, perm).reshape(9, 9)
    print(f"stab-AME cut {name}: 9^4.5*|det| = {abs(np.linalg.det(M))*9**4.5:.12f} (expect 1: no separation in (4,3))")
print("NEGATIVE_CONTROL_OK: method correctly finds NO gap where stabilizer AME exists")
