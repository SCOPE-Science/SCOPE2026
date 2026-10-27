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

# Reproducibility and verification

The analytical proof holds for every integer \(N\ge3\) and is independent of enumeration. The standalone `checker.py` uses Python standard-library `fractions.Fraction`; run `python checker.py`. This constructs actual grounded Laplacians and computes every surviving edge column for graph orders \(3\le N\le11\) using exact rational arithmetic.

The executed output was `DELETED_CLIQUE_EXACT_RATIONAL_OK graph_sizes=9 columns= 210`. The tests verify two exact rational orbit-column formulas and their maximizing classes. It does not cover arbitrarily large orders, which are covered by the symbolic proof; it does not evaluate nonorthogonal minimal projections or other graph families.
