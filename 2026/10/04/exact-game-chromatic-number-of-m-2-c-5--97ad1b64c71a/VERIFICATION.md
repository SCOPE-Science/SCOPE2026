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

The standalone source `artifacts/verify_game.cpp` reconstructs the generalized Mycielski graph \(M_2(C_5)\) from its defining layers and root. It checks that the graph has \(30\) edges and that each of the ten dihedral maps used in state canonicalization preserves adjacency.

For a fixed palette size, every position is evaluated by exact minimax. Completed positions are Alice wins; positions with an uncolored vertex seeing every available color are Bob wins. At Alice nodes the recurrence is existential over legal moves, while at Bob nodes it is universal from Alice's perspective. Canonicalization uses only verified graph automorphisms and a global relabeling of colors.

The finalized replay produced:

`M2(C5), q=3: Alice_win=0, canonical_states=241`

`M2(C5), q=4: Alice_win=1, canonical_states=3734489`

`ALL CHECKS PASSED`

There is no search-depth cutoff, randomized branch selection, floating-point criterion, or timeout-based conclusion. The computation proves only these two finite game outcomes. The equality follows because three colors fail and four colors succeed.
