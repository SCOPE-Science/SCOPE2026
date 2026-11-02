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

# Reproducibility and validation limits

Run `python check_matching.py` and `python check_dfs_templates.py` under standard Python 3. Both require only the standard library. The first outputs `MATCHING_ENUMERATION_ALL_2_EDGE_SWITCHES_PASS`; the second outputs `DFS_AND_EXPLICIT_TEMPLATES_PASS`.

The matching-based program builds both cubic graphs directly, enumerates every perfect matching by recursive branching on the least remaining vertex, complements it to obtain a spanning degree-two subgraph, and retains it only if a graph traversal finds all \(2n\) vertices connected. It then tests *every unordered pair* of Hamiltonian cycles for symmetric difference of four edges, not merely a prescribed subset of quadrilateral moves. It verifies the exact vertex counts, degree multisets and component sizes for every \(4\leq n\leq18\) and both seam types.

The other program uses a different construction: direct depth-first search over Hamiltonian vertex traversals without matching enumeration. It compares all resulting edge sets with explicit rim, paired-rung and all-rung templates. It then checks all four-edge symmetric differences for every \(4\leq n\leq13\) and both seam types. The small width \(n=4\) is checked for additional confidence but not included in the infinite claim.

Neither finite program is an exhaustive test of every integer \(n\). Infinite correctness rests on the proof in `RESULT.md`: the forced pairing of selected rungs, exact circuit count between paired cuts, parity classification of all-rung configurations, and complete four-cycle switch analysis. In particular, an orientation, a nonspanning two-factor, or an illegal intermediate state is not counted as a Hamiltonian cycle.

The source-inspection and originality review is a self-review. The 1998 McSorley full article was unavailable; only bibliographic/abstract material and the static Hamiltonian count could be examined, so independent validation and comprehensive historical priority checks remain unperformed.
