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

The proof is analytic. The accompanying checker performs an independent exact-rational replay.

It enumerates every recursive tree through \(n=9\). In a single pass for each \(n\), it accumulates the leaf count, every nonroot outdegree, and every possible child-attachment indicator. It then checks the exact mean leaf count, every instance of the local covariance identity, and every instance of the aggregate harmonic formula.

A second exact calculation precomputes rational harmonic numbers through \(n=500\), verifies the positive second discrete difference, and checks the full one-crossing sign pattern.

A final floating-point sanity check evaluates the finite threshold for increasing \(n\) and compares its ratio with the Lambert-\(W\) constant. This numerical check is supplementary; the convergence proof in `RESULT.md` uses harmonic asymptotics and sign bracketing.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK trees_checked=46233 leaf_mean_checks=8 local_cov_checks=84 aggregate_cov_checks=36 convexity_checks=123747 threshold_checks=494 asymptotic_checks=26`.
