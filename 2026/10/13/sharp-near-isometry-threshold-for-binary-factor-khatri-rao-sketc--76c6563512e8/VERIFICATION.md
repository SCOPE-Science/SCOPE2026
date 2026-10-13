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

Run `python verify.py` with Python 3.10+; no additional dependencies are needed. The program passed 14,223 finite checks, including exact Walsh orthogonality, explicit tensor-to-label identification, exact Gram eigenvectors, exact full-rank inclusion–exclusion, Stirling-number and exhaustive small-instance comparisons, and the two large-deviation rate functions. The asymptotic probability-zero/one theorem and strict sample threshold are proved in `RESULT.md` by binomial local mass, Chernoff bounds, and negative-covariance second moments; they are not certified by computation.

Scientific scope: independent, two-coordinate real Rademacher tensor factors, full-space covariance near-isometry, fixed distortion strictly between zero and one, and asymptotic sample counts with coefficients strictly off the critical boundary. No independent audit or validation has taken place.
