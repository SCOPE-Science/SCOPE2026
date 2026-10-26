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

# Analytical and computational verification

The proof establishes skew position–velocity covariance from the stationary second-moment equation; applies Gaussian Schur-complement regression; diagonalizes the residual-noise quadratic form; calculates the exact moment-generating function; proves the quartic centered-evenness obstruction; and exhibits both sharp and symmetry-breaking stationary Langevin examples. The polynomial factorization is an identity for arbitrary positive eigenvalues, not a conclusion from a finite parameter grid.

Run `python verify_gyrator.py` (NumPy, SciPy, SymPy required). The provided script checks 255 fixed symbolic/numerical assertions, including stationary Lyapunov residuals, positive definiteness, equality with the general Gaussian-quadratic determinant transform, moment identities, and the sharpness-family covariance. Finite tests do not constitute a proof for all parameters. The rational covariance and eigenvalue discriminant are explicitly stated in RESULT.md; they are checkable independently by exact arithmetic.

The originating nonlinear orientation model is not claimed Gaussian; the theorem applies when the linearized one-time stationary law is Gaussian. The external scientific and originality reviews have not been performed.
