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

The analytic certificate is the proof in `RESULT.md`, including exact finite chord decomposition, joint rare-interval survival probabilities, exponentially bounded moments, the one-corner integral, convolution and AM–GM equality classification.

Execute `python verify.py` with Python 3 and no external dependencies. This implementation independently constructs planar convex hulls, compares physical perimeters to the corner decomposition for four polygon orders, integrates the exact one-corner cumulative distribution, checks regular-polygon parity and optimized products, and compares exponential-sum Monte Carlo means with their closed forms. The run reported `ALL_CHECKS_PASSED`.

These finite, randomized and numerical checks corroborate but cannot certify infinite quantifiers or historical originality. The theorem does not assert fixed-sample optimality, uniformity in vanishing weights, or statements for smooth curves. Independent audit: not performed.
