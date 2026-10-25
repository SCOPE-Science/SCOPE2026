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
The complete analytic argument is in `RESULT.md`. Execute `python verify.py` (requires NumPy). The checked script passed with the following output:

`PASS: d=1..7, 56 SPD inversion/volume checks; Monte Carlo covariance d=1..4 (600000 samples each).`

The script independently constructs random edge matrices, computes the exact barycentric covariance, inverts it using spectral roots, compares recovered Gram matrices and simplex volumes, and compares empirical Dirichlet covariances to the formula. Tests are finite numerical evidence, **not** the proof of the all-dimensional statement. The proof depends on the Dirichlet covariance identity and unique positive-definite matrix square roots. The script and this document cover the final claim only. Independent audit has not been performed.
