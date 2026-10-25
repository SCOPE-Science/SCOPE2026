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

Run `python verify_character.py` in the folder containing `verify_character.py` and `character_table.json` (standard Python 3, no external dependencies). The program builds the 32 vertices and 144 graph edges, checks every one of the 2304 coordinate symmetries, groups them into 40 conjugacy classes, and determines each degree-three trace with an exact recursive independence polynomial. It separately enumerates every one of the 136063 independent vertex subsets, including the empty subset, and checks signed fixed-face sums for each of 40 representatives. Finally, it computes exact multiplicities for all 40 candidate rational irreducibles and checks that precisely eight have multiplicity one and the rest zero.

The resulting character agrees at the identity with the rank 63 from the published homotopy equivalence; the finite program does not independently reprove that homotopy equivalence. This is a complete check of the finite character assertions, not an independent external mathematical audit. No extrapolation to arbitrary product sizes, integral representation splitting, or full abstract graph automorphism group is made.

Success marker: `TRIPLE_COMPLETE_GRAPH_INDEPENDENCE_EQUIVARIANT_CHARACTER_VERIFIED`.
