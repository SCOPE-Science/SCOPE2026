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

Run `python3 verify_total_domination.py` from the same directory as this file using Python 3 standard library only. The verifier reconstructs the adjacency of each edge-triangulated graph from its base edges, tests total domination by checking an open selected neighbor for every vertex, and tests inclusion-minimality by deleting selected vertices one at a time. It computes the complete bivariate counts for the two variable types separately.

The executable compares the general vertex-cover product with direct enumeration on 46 isolate-free labeled graphs of up to four original vertices, and both bipartite enumerators with direct enumeration on nine complete-bipartite instances. The direct checks involve 1,259,880 candidate vertex subsets in total. Another 121 arithmetic pairs check closed-form family coefficients and cardinality consequences.

The observed successful result was:

`VERIFY_OK general_graphs=46 biclique_graphs=9 direct_vertex_subsets=1259880 arithmetic_pairs=121`

The finite tests are corroboration only. The all-order theorem is supported by the explicit proof in `RESULT.md`. The review does not establish uniqueness in the published literature, does not address graphs with isolated base vertices in the general theorem, and has not been independently validated.
