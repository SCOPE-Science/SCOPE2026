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

# Reproducible finite verification

Execute `python3 verify_spanning_tree_teaching.py`. Standard-library-only Python 3 is sufficient. This independently checks the exact definition of a teaching sample for all labeled connected graphs through four vertices and separately for every target spanning tree of \(K_5\) and \(K_{3,3}\), as well as the exchange matching formula on every labeled connected graph through five vertices. It independently tests the Nash-Williams graph partition and two-forest density conditions rather than treating the claimed equivalences as assumptions.

The observed output includes `LABELED_CONNECTED_PASS` for counts 1, 4, 38 and 728 (respectively 1, 6, 128 and 8000 target spanning trees), followed by `COMPLETE_BIPARTITE_PASS` at sizes \((1,4),(2,4),(3,3),(3,4),(3,5),(4,4)\), `INDEPENDENT_K5_TEACHING_PASS`, `NONEXTREMAL_BRIDGED_K5_PASS`, and `ALL_SPANNING_TREE_TEACHING_CHECKS_PASS labeled_graphs= 771 target_trees= 8135`.

The code does not test every unbounded graph; all-size conclusions rely on the proof and standard named matching/packing/decomposition theorems. Numerical-weight query models, other teaching notions, and historical novelty cannot be checked by this program. No external independent audit has been performed.
