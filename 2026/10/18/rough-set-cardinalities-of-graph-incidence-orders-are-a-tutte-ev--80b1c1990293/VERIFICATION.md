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

Run `python3 verify.py` with a standard Python 3 interpreter. It requires no third-party packages and uses integer arithmetic throughout. The checker constructs the order neighborhoods explicitly, enumerates each candidate source subset, creates the actual ordered approximation pairs, and deduplicates them. It compares the result with the independently evaluated height-two monochromatic-neighborhood formula. It also compares graph-incidence counts with two separate representations (vertex-spin sums and connected-component edge-subset sums), deletion–contraction including loops, and closed forms for standard graph families.

Observed result:

```
VERIFY_OK height_two_hypergraphs=689 hypergraph_subsets=37477 simple_graphs=76 multigraph_deletion_contraction=108 paths_cycles_complete_n_le_8=PASS
```

The height-two enumeration includes empty neighborhoods. The simple-graph enumeration covers all undirected simple graphs on at most four vertices; there are additional exactly enumerated families through eight vertices. Exhaustive finite comparisons do **not** certify the theorem for arbitrary finite size, do not independently establish the cited graph-complexity classifications, and do not certify bibliographic novelty. The universal identities are proved in `RESULT.md`, with externally established complexity theorems cited there.
