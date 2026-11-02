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

# Verifiable checks and limits

Run `python3 anchored_graph_checker.py` in the directory containing this file. It uses only the Python standard library and needs no external files or data. Expected final output: `ONE_EXTRA_ANCHORED_GRAPH_EQUIVARIANT_CHECKS_OK`.

The checker derives the finite graph cells from onto occupancy assignments and from choices of active particle, oriented graph edge and stationary bijection. It verifies connectedness, the first Betti rank by exact finite graph counting, signed cellular traces for every permutation of labels, and the doubled-incidence identity for invariant edge-orbit sums on six graphs, including two graphs with more than one independent cycle. No floating-point numerical calculations or probabilistic tests occur.

The all-graphs proof is in `RESULT.md`: leaf-fixing connectivity, free/permutation cellular modules, semisimple rational decomposition, integral invariant-boundary identity and explicit lifting of graph loops. Exhaustion of six finite examples is not an all-graphs proof, and this check does not determine the full integral group-ring module. Independent external review is not performed.
