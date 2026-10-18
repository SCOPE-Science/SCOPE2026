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

The included `verify.py` uses Python's standard library and has no third-party dependencies. Run `python3 verify.py` from a directory containing this file.

The verifier independently constructs every labeled undirected simple graph on at most five vertices, counts contranominal submatrices directly by object-edge and attribute-vertex selections, compares them with dominating-complement degree products, and derives the domination number by exhaustive vertex-subset search. It constructs the formal-context intents from row intersections to check exponential lower bounds and the star equality criterion. It also computes path and cycle enumerators from the four-state transfer independently of graph subsets, checks complete and star formulas, and checks the polynomial matrix identity.

Expected successful output:

```
VERIFY_OK labeled_graphs= 1099 submatrix_witnesses= 44672 concept_totals= 15765 path_cycle_profiles= 20 max_n=11 complete_star_max_n=8 transfer_matrix_identity=PASS
```

Finite verification is limited to the stated graph sizes; the all-graph and all-size theorems depend on the supplied mathematical proof. No independently audited proof certificate is claimed.
