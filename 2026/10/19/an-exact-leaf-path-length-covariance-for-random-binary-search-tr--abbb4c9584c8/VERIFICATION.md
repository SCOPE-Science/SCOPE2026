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

Exact-rational moment recurrences for the random binary search tree, including the independent mixed-moment recurrence, were checked for each \(2\le n\le80\). For \(2\le n\le8\), all \(n!\) insertion orders were independently enumerated (46,232 orders in total). These computations verified the stated covariance and corresponding variance formulas in their applicable ranges. `check_bst.py` is self-contained and requires Python 3.10 or later. Reproduce with `python3 check_bst.py`. The infinite theorem is proved by induction from the root-splitting law; finite checks do not constitute an infinite certificate. Independent scientific audit has not been performed.
