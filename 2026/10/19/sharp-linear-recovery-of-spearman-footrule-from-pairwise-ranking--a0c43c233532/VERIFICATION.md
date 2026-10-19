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

The accompanying `verify_footrule_projection.py` uses Python's standard library and exact fractions. Run with `python verify_footrule_projection.py`. The completed standalone execution reported 1,004 assertions based on exhaustively enumerated permutations of sizes 2 through 7 and 396 rational checks of the closed finite-sum identities for sizes 2 through 100.

The checker computes all pairwise comparison covariances, all footrule/comparison covariances, the covariance-matrix normal equations, the explicit predictor's explained variance, and the residual variance. Its checks are supplementary: the proof for every \(n\ge2\) uses the exact cut-pair count, incidence identity, random-assignment variance identity, finite power sums, and a positive polynomial factorization. No independent scientific audit has been performed. The historical-priority assessment remains limited by the unavailable complete texts identified in `RESULT.md`.
