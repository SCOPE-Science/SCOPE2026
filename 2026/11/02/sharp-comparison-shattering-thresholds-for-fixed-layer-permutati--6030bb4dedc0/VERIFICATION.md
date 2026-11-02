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

# Reproducibility

From this folder under Python 3 (no external packages required), execute `python verify_layered_comparisons.py` and `python verify_permutation_direct.py`. The first program reads `three_layer_first_gap_tree.json` relative to its own file path and checks all eight terminal cut-pair witnesses against their full query paths.

## Checks performed

- Exact mapping of positional comparison to absence of a cut in the corresponding interval: 21,878 tested pairwise comparisons.
- Exhaustive two-cut interval-hit VC/Littlestone recurrence on cut-position counts from two through nine, yielding `(VC,Ldim)` pairs `(0,0),(1,1),(2,2),(2,3),(3,3),(3,4),(4,4),(4,4)`.
- Independently generated three-layer permutations: orders three through nine for VC and through six for Littlestone.
- A complete depth-three decision-tree certificate with eight distinct witnesses at the first gap, and two-query-per-block sharpness gadgets for one through five cuts.

Both programs returned their respective all-checks-pass markers when run from the packaged paths. The all-parameter VC and growth theorems are mathematical proofs, not consequences of finite verification; independent external mathematical validation has not been performed.
