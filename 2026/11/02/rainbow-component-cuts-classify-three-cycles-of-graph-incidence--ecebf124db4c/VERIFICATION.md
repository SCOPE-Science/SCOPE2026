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

The graph-wide classification is proved in `RESULT.md` from the explicit rowmotion update, the even-weight constraint on three edge-presence bits, and the rainbow-neighbour requirement for vertices present in all three ideals.

`verify_direct.py` independently computes minimal omitted elements of the full incidence poset; it tested all 771 connected labelled simple graphs on two through five vertices, comparing period-three orbit counts against independently enumerated admissible vertex partitions. The observed pass marker was `DIRECT_MINIMAL_COMPLEMENT_ALL_771_GRAPHS_PASS`.

`verify_structural.py` constructs each of the three ideals from the component-colouring description and checks its successor with the \((S,T)\) update. Its tests include complete bipartite graphs with both part sizes between one and four, and cycles through length eight. The observed pass marker was `CONSTRUCTIVE_THREE_CYCLE_AND_BICLIQUE_PASS`.

Finite enumeration confirms selected inputs but is not a substitute for the all-graph proof. These checks are self-review reproducibility checks, not an independent scholarly audit.
