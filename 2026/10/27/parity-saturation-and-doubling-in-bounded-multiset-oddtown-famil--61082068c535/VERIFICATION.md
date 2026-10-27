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

Run `python3 verify.py` with Python 3.10 or later and no optional libraries. The program defines the complete parity-odd candidate universe for six small graph cases, independently computes maximum compatible cliques by branch-and-bound, enumerates all eight-pattern maximizing families via dynamic-group exhaustive recursion, compares those six families to the coordinate-permutation orbit of the displayed witness, and tests every padded direct-sum example through ground-set size eighty. It checks each pair using the actual coordinatewise-minimum definition rather than relying on a precomputed table. Output observed:

```
VERIFY_OK exact_graph_cases=6 optimal_four_coordinate_families=6 group_dfs_nodes=437 direct_sum_orders=77 max={(3, 1): 3, (3, 2): 3, (3, 3): 4, (4, 1): 4, (4, 2): 6, (4, 3): 8}
```

Every maximal odd-diagonal family has at most one member of each parity class. Hence the exhaustive eight-class recurrence is complete for the claimed eight-member extremizers. Direct-sum testing across a finite range supplements the algebraic disjoint-support proof and does not establish cases beyond the tested range on its own. The n>4 maximum itself remains unknown, and no independent audit has been performed.
