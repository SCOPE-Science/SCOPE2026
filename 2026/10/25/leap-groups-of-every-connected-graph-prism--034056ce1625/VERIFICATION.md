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

# Reproducible verification

The included `verify_leap_prisms.py` uses Python 3 and SymPy. Run `python verify_leap_prisms.py` alongside this file. Its independently constructed prism adjacency graph is used to enumerate every permutation sending each vertex to an adjacent vertex. It then forms the actual permutation group from these generators and compares its exact order to the claimed bipartite/nonbipartite formula. For every tested base edge it separately builds both four-cycle hop orientations and checks that their products with the vertical hop are single transpositions on opposite square corners.

**Actual checks:** 49 connected base graphs, including all 44 labelled connected simple graphs on one through four vertices, and the five-vertex path, five-, six- and seven-cycles, and the three-cube as additional bases; total graph-admissible hops checked: 77,477. The observed execution result was `VERIFY_OK connected_base_graphs=49 enumerated_hops=77477`. The last base, the three-cube, tests the four-cube prism.

**Scope of evidence:** These computations verify exact finite instances. The general conclusion is proved by the globally vertical matching hop, elementary four-cycle switches, the edge-transposition generation lemma, and the bipartite-double-cover connectivity argument in `RESULT.md`. Neither a failed computation nor the absence of a prior search hit is interpreted as a theorem. A separate independent scientific audit has not been conducted.
