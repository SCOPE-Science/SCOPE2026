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

## Mathematical check
Consecutive closed neighbourhoods and monotonic right endpoints follow from the proper interval umbrella ordering. The formula for a vertex's number of neighbours in the preceding root-distance layer determines its left endpoint; the succeeding-layer neighbour count determines its right endpoint, while in the final layer that endpoint is maximal automatically. Stable equitable colours recover these counts after separating distance layers, and true twins are swapped by a root-preserving automorphism. The complete-or-empty block argument establishes identification against arbitrary rooted graphs. Fractional automorphisms are blockwise bistochastic by the stable-cell invariance argument.

## Computational corroboration
From a directory containing the four files `rooted_unit_check.py`, `rooted_unit_layers.py`, `rooted_unit_check.out`, and `rooted_unit_layers.out`, execute:

```
python3 rooted_unit_check.py 12 > reproduced_check.out
python3 rooted_unit_layers.py 12 > reproduced_layers.out
cmp reproduced_check.out rooted_unit_check.out
cmp reproduced_layers.out rooted_unit_layers.out
```

The first implementation enumerates nondecreasing endpoint encodings and compares actual iterative colour refinement with equality of closed neighbourhoods. The second independently calculates BFS layers and tests the adjacent-layer count criterion. Each exhausts all encodings through twelve vertices. These computations do not establish the theorem for larger instances or verify priority in the literature.

## Scope and status
The result concerns connected proper interval graphs distinguished at a leftmost vertex; no assertion is made for arbitrary rooting, disconnected graphs, arbitrary interval graphs, or higher-dimensional counting logic. Independent audit has not been performed.
