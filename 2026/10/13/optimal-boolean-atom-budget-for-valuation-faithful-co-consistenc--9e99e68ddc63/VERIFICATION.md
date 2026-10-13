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

Run `python3 verify.py` in the directory containing the result. The Python 3 verifier enumerates all nonempty represented-state families over small Boolean algebras and, independently of the private-marker characterization, explicitly checks every subset of the finite world set against every available Boolean truth value. It also enumerates graph adjacency patterns and clique-cover minima, then checks the marker construction across all four-world graphs.

Recorded deterministic output:

```
BRUTE_MINIMUM_BY_ALL_BOOLEAN_VALUATIONS: [(1, (1, 1, 1)), (2, (2, 5, 3)), (3, (8, 34, 5))]
ALL_4_VERTEX_GRAPH_CONSTRUCTIONS: 64
COMPLETE_GRAPH_OPTIMA: m+1 for m=2..6
TRIANGLE_FREE_CYCLE_OPTIMA: 2m for m=4..5
VERIFY_OK
```

The triple `(world_count, (number_of_graphs, sum_of_optima, maximum_optimum))` reports the exhaustive minima through three worlds. The graph calculations on four worlds confirm construction correctness, not minimum budgets. The general all-size result follows from the private-coordinate lower bound and the edge-clique-cover upper construction proved in RESULT.md. The code requires only the Python 3 standard library; no external services or data files are required.

Independent audit has not been performed.
