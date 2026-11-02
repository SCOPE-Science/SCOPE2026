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

# Reproducibility and verified checks

The theorem follows from a direct integrated-population identity, Parseval/Tonelli, factorization at the critical Bloch node, and a finite tridiagonal Gram-matrix eigenvalue argument. These analytic steps prove all permitted integer support lengths and all positive parameter values, not just those tested numerically.

The companion `check_critical_walk.py` file independently solves the two-dimensional continuous-time Lyapunov equation for each Bloch momentum, checks numerical quadrature against modal formulas for heterogeneous hopping, diagonalizes convolution Gram matrices for \(2\le L\le24\), checks the critical Fourier node and minimum against randomized coherent preparations, and tests the optimal-loss identity. Requirements: Python 3, NumPy, SciPy. Run `python check_critical_walk.py` from the same extracted folder. Result: `PASS: 231 tests; maximum relative discrepancy 8.211e-14`.

Finite numeric experiments do not prove asymptotic absorption at criticality, the infinite family of lengths, or source originality. The argument relies on strict positivity of \(v,w,\gamma\), continuous translation invariance, and exact coherent preparation. Independent scientific assessment has not been performed.
