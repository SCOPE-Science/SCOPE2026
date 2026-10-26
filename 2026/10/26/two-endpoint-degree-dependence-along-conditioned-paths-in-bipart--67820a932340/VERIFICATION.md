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

Run `python3 verification/check.py` from this package root. The checker independently enumerates connected acyclic spanning edge sets of all \(K_{a,b}\) with \(2\le a,b\le5\) and \(ab\le20\), then reconstructs distances and endpoint degrees without invoking the analytic inclusion-count formula. It checks the exact fixed-tree count, distance distribution, every admissible mixed factorial moment, the conditional covariance, and both strictly ordered conditional marginal tails. A run on the packaged script passed **574 exact rational comparisons**.

The mathematical proof covers all integers \(a,b\ge2\). The enumerated cases are finite sanity checks and do not establish universality, independence from unpublished earlier work, or correctness on arbitrary host graphs. Independent audit has not been performed.
