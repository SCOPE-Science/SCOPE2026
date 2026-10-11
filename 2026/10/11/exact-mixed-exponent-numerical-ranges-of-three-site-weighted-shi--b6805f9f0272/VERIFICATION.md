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

# Verification and limits

The analytical argument in `RESULT.md` establishes the claim for **every real exponent** \(1<p<\infty\), every complex weight pair, and every unit vector. The supplementary standard-library script `verify.py` re-evaluates the unique positive mixed-exponent root by bisection, constructs and independently evaluates the stationary witness, checks conjugate-exponent duality across representative exponents and weights, and samples independently generated positive unit vectors. Its reproducible success message is `THREE_SITE_WEIGHTED_LP_NUMERICAL_RADIUS_CHECKS_OK`.

The exact check for the asymmetric \(p=4\) witness uses rational arithmetic, testing the signs of \(Y^3-Y^2-4096\) and \(Y^3-16Y^2-1\) at \(Y=65/4\). These signs and the uniqueness of each positive root certify the strict ordering. The finite randomized checks are not an exhaustive search and are **not** used to prove the infinite family of exponent values or the entire numerical disk. The boundary-perturbation argument, the strict mixed-root monotonicity, and the connectedness argument provide those steps.

No external independent audit or validation is asserted. A possible earlier unindexed equivalent is an originality residual risk, not evidence of coverage.
