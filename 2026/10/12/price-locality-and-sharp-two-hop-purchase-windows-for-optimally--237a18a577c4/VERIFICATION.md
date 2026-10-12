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

Exact computations were performed with the accompanying `verify.py` via Python standard-library fractions. Its own output was `VERIFY_OK 154 exact tree/chord KKT tests; 47 finite two-hop extremal checks`. These are 154 deterministic seeded exact-rational tree/chord tests at orders \(3\) through \(9\) and 47 complete arithmetic checks of two-hop extrema for orders \(3\) through \(49\). The checker reconstructs the weighted Laplacian inverse, total resistance, rank-one derivative, cut variance, closed threshold, and split inequalities. The checks do not enumerate all trees, all prices, or an infinite family; the universal assertions rely on the analytic proof in RESULT.md. Neither external validation nor independent audit was undertaken.
