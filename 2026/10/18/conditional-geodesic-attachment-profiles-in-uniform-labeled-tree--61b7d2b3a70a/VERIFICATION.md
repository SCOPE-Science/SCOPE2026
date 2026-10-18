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

The standalone script `verify.py` uses the Python standard library to enumerate every Prüfer sequence through order eight and reconstruct the unique path between fixed vertices. It compares exact rational conditional probabilities of the entire excess-degree profile with the weighted-tree prediction, confirms distance-count normalization, and checks mean total attachment count and pairwise covariance. It completed 487 assertions across 280,392 trees.

Reproduce with `python verify.py`. The script does not simulate the Gaussian limit, verify infinitely many tree sizes, or establish novelty. The infinite-dimensional convergence proof is the binomial/random-index empirical-process argument in `RESULT.md`.

The supporting forest enumeration and earlier two-point correlation literature are acknowledged. Independent mathematical validation and historical-priority review have not been carried out.
