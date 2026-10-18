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

# Reproducibility and limits

Run `python3 verify.py` with a standard Python 3 interpreter. The checker computes facet normal lengths and tangent-facet counts as exact rational numbers, derives active-normal rank via rational Gaussian elimination, verifies nonzero perturbations along every predicted center-affine direction using rational inequalities after legitimate squaring of nonnegative sides, and separately checks balanced-even segment endpoints and duplicate sign labels in four examples.

Recorded program output:

```
VERIFY_OK profiles=49 facets=30676 tangent_facets=11312 positive_dim_profiles=46
VERIFY_ENDPOINTS_OK [(2, 5), (4, 20), (6, 70), (8, 252)]
```

Test domain: integer \(2\le p\le8\), \(p\le q\le11\); balanced-even endpoint tests use \(m=2,4,6,8\). The program assumes the published complete-bipartite facet theorem and is only finite corroboration. The paper's proof establishes all admissible integer parameters using exact formulas and linear algebra; neither enumeration nor numerical equality tests are an infinite proof. No external mathematical audit is asserted.
