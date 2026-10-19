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

## Checks performed

The self-contained `verify.py` script was executed using NumPy and SymPy and passed 4,513 finite checks, including randomized positive-definite matrices, independent direct Gaussian-KL calculations, sharp two-eigenvalue orientations, near-singular Schur complements and symbolic determinant/trace identities.

The mathematical proof in `RESULT.md`, not the finite tests, establishes the formulas for all allowed real parameters and all positive-definite input matrices of the stated structure. No finite numerical computation certifies a global optimum without the analytic one-variable extremization in the proof.

## Limits

Checks use double precision and exact symbolic algebra where stated. They do not examine floating-point Lanczos errors, higher-dimensional covariance approximations, Monte Carlo trace-estimation errors, or any purported independent review.
