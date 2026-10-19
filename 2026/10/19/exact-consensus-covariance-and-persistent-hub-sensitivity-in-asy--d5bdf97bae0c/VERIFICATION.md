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

Run `python verification.py` with Python 3.9 or newer. No external packages are required. The script enumerates each possible center/leaf update on stars of sizes \(m=1,\ldots,8\), checks fourteen distinct exact-rational configurations per size, and independently computes the expected center-of-mass and both disagreement-moment drifts. It verifies the exact quadratic harmonic invariant and finite-size all-equal-leaf formula. It passed 872 exact rational assertions.

For proof-level reconstruction, verify the hub update \(d_i\mapsto d_i-s/(m+1)\) and leaf update \(d_i\mapsto d_i/2\), sum their effects on \(M,E,T\), and substitute \(a=1/((2m+1)(3m+1))\), \(b=(m-1)/((2m+1)(3m+1)^2)\) to cancel both conditional coefficients. The nonnegative disagreement energy has geometric expectation decay; the weighted mean is a bounded martingale. The covariance follows from the bounded harmonic quadratic and scalar projections.

The checker does not certify infinite-time convergence, all graph sizes, literature priority or external independent review. Those limits are explicit in the analytical proof and review.
