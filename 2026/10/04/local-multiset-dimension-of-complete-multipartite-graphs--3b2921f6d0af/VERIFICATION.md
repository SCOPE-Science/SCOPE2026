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

The proof derives exact distance-multiset signatures from the part-count vector and reduces the minimum problem to distinct-count assignment under part capacities.

The included checker independently constructs every tested complete multipartite graph, computes each vertex's distance multiset directly for every candidate subset, and tests all adjacent pairs. It compares the observed valid sets, minimum size, and number of minimum sets with the theorem.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 87
vertex_subsets_checked = 22932
finite_types_checked = 51
basis_count_checks = 51
orders = 2..9
```

The computation is finite corroboration only; the all-orders theorem follows from the proof.
