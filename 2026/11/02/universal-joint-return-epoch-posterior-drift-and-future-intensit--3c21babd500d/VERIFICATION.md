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

# Reproducible verification

Run `python3 checker.py` using the Python standard library. The checker prints `PASS: 2335 reproducible exact/numerical assertions` and exits unsuccessfully if an assertion fails.

The exact checks compare two different rational beta-integration procedures for return-count survival, independently enumerate first-return paths for short walks, and test the balanced-urn joint posterior survival identity. The numerical timing checks compare a conditional finite-index first-return transform with its proposed limit and independently integrate both the drift-mixture and inverse-exponential representations of that limit. They test the normalization and the factor of two in the timing scale.

All finite checks have finite scope and do not certify an infinite limit. The infinite results follow from the analytic steps in RESULT.md: exchangeability, conditional renewal, posterior Laplace localization, Scheffé convergence, convergence of conditional generating functions and exact density mixing.

The most relevant available earlier text is Jiang et al., arXiv:1402.4536, particularly Section 5.3, whose finite indexed-tie probabilities can imply part of the marginal timing calculation for balanced masses. This verification does not establish independent historical priority or independence of review.
