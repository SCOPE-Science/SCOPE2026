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

# Verification

The analytic proof in `RESULT.md` establishes all infinite-range results, including uniqueness, strict boundary inequalities and the nonattained supremum. The source's physical squeezed-bath normalization was independently reconstructed using a four-dimensional stationary Lyapunov equation and a partial-transpose symplectic-eigenvalue calculation.

Execute `python verify.py` with dependencies declared by `requirements.txt`. The program checks the exact derivative factorization, the stationary Gaussian covariance from an independent Lyapunov solver, the partial-transpose eigenvalues, optimizers and scaled thresholds. Its completed execution passed 1057 assertions. Finite tests are not an infinite proof and no independent external audit has been performed.
