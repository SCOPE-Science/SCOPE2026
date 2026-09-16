"""Rank verification for the mass-transfer (linearized defect) matrices.

Mirrors the surjectivity lemma in DRAFT.md:
- orthant-pair generators span the 7-dim sum-zero subspace of R^8;
- per-section piece generators span the 3-dim sum-zero subspace of R^4;
- joint block system (interior bumps + section bumps, arbitrary 4D
  cross-talk C from section bumps) has full rank 19 = 7 + 4*3.
"""
import numpy as np

rng = np.random.default_rng(20490)

# --- orthant pairs: 8 pairs, generator P0 adds 2a to pair P0, 2a/8 to total
G_orth = 2.0 * (np.eye(8) - np.ones((8, 8)) / 8.0)
r_orth = np.linalg.matrix_rank(G_orth, tol=1e-9)
print("orthant 8x8 generator matrix rank:", r_orth, "(expect 7)")
# drop one pair (defect map uses 7 components); 7x8 matrix
G_orth7 = G_orth[:7, :]
r_orth7 = np.linalg.matrix_rank(G_orth7, tol=1e-9)
print("orthant 7x8 restricted matrix rank:", r_orth7, "(expect 7)")

# --- one section: 4 piece-pairs, generator Q0 spans sum-zero subspace of R^4
H_sec = np.eye(4) - np.ones((4, 4)) / 4.0
r_sec = np.linalg.matrix_rank(H_sec, tol=1e-9)
print("section 4x4 generator matrix rank:", r_sec, "(expect 3)")
H_sec3 = H_sec[:3, :]
r_sec3 = np.linalg.matrix_rank(H_sec3, tol=1e-9)
print("section 3x4 restricted matrix rank:", r_sec3, "(expect 3)")

# --- joint system: unknowns x (8 interior bumps) + y (16 section bumps)
# equations: f (12 section defects) = D y; e (7 volume defects) = A x + C y
A = G_orth7  # 7x8
D = np.zeros((12, 16))
for i in range(4):
    D[3*i:3*i+3, 4*i:4*i+4] = H_sec3
C = rng.normal(size=(7, 16))  # arbitrary cross-talk of section bumps on 4D volumes
J = np.block([[np.zeros((12, 8)), D],
              [A, C]])
r_joint = np.linalg.matrix_rank(J, tol=1e-9)
print("joint 19x24 matrix rank:", r_joint, "(expect 19)")

# dimension count
print("domain dim (S^3)^4 minus det=0:", 12, "| codomain dim:", 7 + 4*3)
assert r_orth == 7 and r_orth7 == 7 and r_sec == 3 and r_sec3 == 3 and r_joint == 19
print("ALL RANK CHECKS PASSED")
