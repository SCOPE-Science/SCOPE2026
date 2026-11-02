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

# Reproducibility and mathematical verification

Execute `python3 verify.py` with Python 3 and its standard library. It passed 4,997 supplementary checks, including exact-rational two-step formulas, the four Rademacher outcomes, crossing thresholds on a parameter grid, finite-step covariance constructed from the literal matrix recurrence, and large-iteration scaling.

The proof is analytic; these finite computations do not certify universal statements, independent review, historical priority, or behavior of an entire inverse-problem UQ pipeline. The sharp boundary concerns exact normal-operator eigenvector selection and the stated Gaussian noise model. The full proof and domain restrictions are in `RESULT.md`.
