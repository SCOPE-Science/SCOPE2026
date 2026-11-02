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

Run `python3 verify.py` using Python's standard library. The direct-check routine constructs graph subdivisions and independently tests all vertex subsets for the induced maximum-degree-one condition and one-vertex extension maximality. It compares the resulting sets and their coefficient counts with the structural correspondence and with the two-by-\(b\) polynomial; it also runs separate double-sum arithmetic checks.

Observed successful output:

`VERIFY_OK general_graphs 157 bicliques 12 cliques 3 tested_subsets 2225046 arithmetic_bicliques 49`

The graph-level checks include exhaustive base-graph classes through four vertices, reproducibly seeded five- and six-vertex samples, bipartite examples, and complete graphs. The arithmetic checks extend through forty-nine two-by-\(b\) parameters. The program independently tests the graph property rather than assuming the partial-function characterization. The infinite theorem is proved mathematically; no finite enumeration is claimed to be an exhaustive all-order proof. Independent audit status is not performed.
