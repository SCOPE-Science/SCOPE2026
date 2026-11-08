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

Run `python3 verification/check.py` from the directory containing the accompanying files. Only the Python standard library is required. The checker enumerates all bipartite adjacency matrices of sizes 2 by 2, 3 by 3, and 4 by 4, grouped by exact edge count; compares rational marginal, joint, and covariance moments against the formulas; verifies an independent factorial-product reduction; and samples exact finite-size signs. It performed 1,302 exact assertions successfully during the self-review.

The infinite-size statements are justified by the explicit uniform expansion and remainder estimates in RESULT.md. The finite computations cannot certify asymptotic claims by themselves. No independent audit has been performed.
