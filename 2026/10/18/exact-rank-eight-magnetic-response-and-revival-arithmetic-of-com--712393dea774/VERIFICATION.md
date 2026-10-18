---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the exact magnetic return spectrum

The proof is symbolic and self-contained. Independently reconstruct the finite matrix by running `python verify.py` in an environment with Python, NumPy, SciPy, and SymPy. The checker builds every oriented arc, forms the normalized incidence coisometry and Grover reflection, then constructs the one-edge magnetic flip directly. It does **not** use the characteristic polynomial to construct the matrix.

The executed checker reported: `PASS: 193 independent symbolic/matrix/period checks; rational period= 68`. The tests include three exact symbolic characteristic polynomials, ten graph/flux cases, numerical eigenvalue multiplicities, full-matrix unitarity, fourth-step operator/Frobenius norms, and an exact rational-angle test on \(K_{3,4}\) with \(\theta=\pi/17\). The numerical matrix comparisons used absolute tolerances no larger than \(3\times10^{-10}\) for the tested observables; the exact symbolic checks used zero simplification.

The finite numerical computations are not a proof for arbitrary sizes or fluxes. The all-size statement follows from the determinant lemma and rank-two Gram determinant in the analytical proof. In particular, the spectral factorization holds at eigenvalue collisions by a polynomial identity and unitarity, and the arithmetic period classification follows from the complete spectral multiset.

Unverified beyond the theorem: multiple magnetized bonds, graph families other than complete bipartite graphs, other coins, experimental finite phase precision, and independent external review.
