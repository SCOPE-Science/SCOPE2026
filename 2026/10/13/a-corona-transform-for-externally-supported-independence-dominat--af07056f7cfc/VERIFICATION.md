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
# Verification of the corona ESI transform

The proof of the all-graph polynomial identity is self-contained in `RESULT.md`. This record describes actual finite, independent tests and their limits, not a claim of an external audit.

Run `python corona_esi_verify.py` using Python 3 and `networkx`. The script constructs each corona's adjacency bitmasks directly and tests all selected subsets against two clauses: independence and external support. It then computes the proposed polynomial from the base-graph neighborhood sum by an independent algorithm; separate routines enumerate domination sets and the graph's weighted differential.

The actual recorded execution in `corona_esi_verify_output.txt` printed:

```text
ALL CHECKS PASSED
unlabeled_base_graph_corona_profiles=278
full_vertex_subsets_enumerated=2576060
single_leaf_domination_reversal_checks=208
weighted_differential_extremal_checks=70
graph_orders=1..6; independent direct ESI-definition enumeration
```

Unlabeled base graphs of orders 1 through 6 were tested with leaf multiplicity 1, with multiplicity 2 for orders at most 5, and multiplicity 3 for orders at most 4. The full subset-space was examined for every tested corona. These tests check implementation and finite examples; only the symbolic proof establishes the statements for all base orders, graphs, and integers \(m\). The classical identity relating graph differential and Roman domination is cited, not reproved computationally here.
