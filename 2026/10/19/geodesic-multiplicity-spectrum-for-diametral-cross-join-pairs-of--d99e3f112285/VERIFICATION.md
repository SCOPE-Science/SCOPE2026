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

Run `python3 verify.py` with `diametral_pairs.csv` in the same directory. The checker has no third-party dependencies; it uses exact integer arithmetic.

It tests all 65,536 feedback pairings for one 32-cycle; independently builds the same 2,048 rotation classes using Eulerian graph search; checks every two-coordinate cross-join condition by an independent interlacing test; forms the full 2,048-vertex graph; computes breadth-first distances and shortest-route multiplicities; and compares the complete 368-pair CSV against recomputed counts. A distinct dynamic program on subsets of fourteen differing feedback coordinates independently reproduces each of the 368 diametral path counts.

Expected summary: `VERIFY_OK Eulerian_DFS=2048 pairings_tested=65536 graph_edges=38704`, `VERIFY_OK all_pairs=2096128 cross_join_diameter=7 diametral_pairs=368`, `VERIFY_OK geodesic_dynamic_program_agrees_with_BFS=368_pairs`, and `VERIFY_OK geodesic_levels=...` with fourteen values as in the result.

The proof is exhaustive only for the defined order-five finite domain. These are reproducibility checks, not an independent scientific audit or validation of priority.
