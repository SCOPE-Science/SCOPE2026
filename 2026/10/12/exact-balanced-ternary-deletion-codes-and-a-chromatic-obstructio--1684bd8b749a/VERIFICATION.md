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

The finite statement was checked with `python3 verify.py` from the package, using the Python standard library. The program reconstructs the 90 distinct length-six balanced ternary inputs and 90 distinct length-five outputs. It verifies that the eighteen displayed outputs partition the inputs into eighteen five-parent cliques and hence prove the upper bound 18; an exhaustive 368-node search gives eight optimal codes, all matching the displayed twelve-word core plus three independent two-option blocks. It also checks the six-residue descent coloring on every confusable pair and exhaustively enumerates the maximal cliques, finding maximum clique size five.

Observed output:

`VERIFY_OK inputs=90 outputs=90 transversal=18 max_code=18 max_code_sets=8 common_core=12 search_nodes=368 clique_max=5 clique5=96 maximal_cliques=272 chromatic=6`

No timeout, floating-point computation, heuristic cutoff or inaccessible artifact is part of the proof. The checked domain is finite and exact; the result says nothing about other compositions or block lengths. No independent audit has been carried out.
