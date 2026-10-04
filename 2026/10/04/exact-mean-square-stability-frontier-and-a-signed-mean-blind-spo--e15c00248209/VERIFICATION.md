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
The package verifies the covariance algebra for KGSM on the orthonormal two-equation system.

`verify.py` uses exact rational bivariate polynomial arithmetic to reconstruct the cubic Jury quantities from the covariance matrix coefficients. It verifies the sharp first-factor identity and recomputes the tensor-product degree-\((6,6)\) Bernstein certificate for the third Jury quantity, whose smallest coefficient is exactly \(3/16\).

The checker also replays the covariance recurrence at representative stable, marginal, and unstable parameters and checks the unsmoothed signed-mean quadratic. These finite trajectories are only transcription guards; infinite-time classification follows from the exact Jury analysis in `RESULT.md`.
