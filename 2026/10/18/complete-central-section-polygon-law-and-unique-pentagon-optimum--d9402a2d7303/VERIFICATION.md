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

# Checks and their limits

`checker.py` is a standalone, deterministic numerical consistency checker using NumPy and SciPy. Execute `python checker.py`. It samples independent Gaussian vectors (equivalent to uniformly distributed plane normals), counts crossings of all nine genuine prism edges, and verifies the three probability predictions at five aspect ratios. It checks probability normalization, the exact-mean relation, the stationary-height root, the sign of the analytic derivative expression on a numerical grid, and numerical superiority of the claimed optimum on another grid. The executed checker completed successfully, including 1,100,000 orientation trials in total.

The proof of the closed-form distribution is the six-sign-pattern classification, spherical-hexagon area identity, and independent nine-edge angular expectation. The uniqueness proof uses an explicitly negative derivative for all positive arguments. Neither grid checks nor Monte Carlo samples prove statements at untested real parameters. Bibliographic comparisons do not establish absolute novelty, and an inaccessible relevant numerical section-angle study remains an external-reading limitation.
