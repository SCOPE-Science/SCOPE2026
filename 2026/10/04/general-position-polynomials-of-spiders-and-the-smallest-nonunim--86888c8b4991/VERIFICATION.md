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

The symbolic proof classifies every general position set of size at least three by unique paths in a spider and derives the coefficient formula directly.

The included `verify.py` has a definition-level branch that builds each tested spider as a graph, computes all-pairs distances, enumerates every vertex subset, and rejects a subset whenever one selected vertex lies on the geodesic between two other selected vertices. This direct branch checks all 103 spider isomorphism types of orders four through eleven and 112080 vertex subsets.

The cutoff branch independently enumerates every integer partition of order minus one into at least three positive arm lengths through order twenty-two. The resulting 3374 spider isomorphism types are tested for coefficient unimodality using the proved formula. `cutoff_certificate.json` records the per-order totals and shows zero nonunimodal types through order twenty-one and exactly one at order twenty-two.

Recorded verifier output:

```text
VERIFY_OK
direct_spider_types_checked = 103
direct_vertex_subsets_checked = 112080
formula_cutoff_spider_types_checked = 3374
orders_direct = 4..11
orders_cutoff = 4..22
unique_nonunimodal_spider_through_order_22 = S(1,1,1,1,2,15)
unique_order_22_coefficients = 1,22,231,226,249,137,30
family_S(1,1,1,1,2,m)_nonunimodal_iff_m_ge_15_checked_for_m_1..100
```

The finite cutoff proves minimality only within spiders. It does not assert that order twenty-two is the minimum among all trees.
