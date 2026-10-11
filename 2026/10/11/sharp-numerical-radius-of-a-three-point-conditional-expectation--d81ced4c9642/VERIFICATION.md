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

The stand-alone `verification.py` uses the Python standard library only. From exact rational polynomial arithmetic it confirms both the full quartic Vandermonde numerator identity and the zero-sum cubic discriminant identity. Its root reconstruction verifies the displayed maximizing orbit to floating-point tolerance; a fixed-seed 60,000-trial stress test gave no counterexample. Expected lines are `EXACT_POLYNOMIAL_IDENTITIES_OK` and `NUMERICAL_SPOT_CHECKS_OK`.

The universal upper bound does **not** rest on numerical sampling. It is the analytic consequence of centering, the exact cubic discriminant feasible interval, the strict one-dimensional maximum in the cubic invariant, and a unique stationary point for the remaining positive parameter. This script is a reproducibility aid and a check of critical algebraic identities, not an infinite-domain certificate or independent audit.

The source date 2010-11-22 comes from the version-1 public arXiv record of the foundational paper. Later journal publication or revisions are not substituted for this date. Independent verification remains unperformed.
