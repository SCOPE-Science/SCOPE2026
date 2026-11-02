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

# Reproducible checks

Run `python3 verify_circular.py vc7_witnesses.json ldim9_tree.json` using the Python 3 standard library. The verifier recomputes all 720 oriented cyclic orders and all 35 query signatures directly from permutations; it does not trust any separately recorded concept-pattern matrix.

Observed output:

```
VC_SEVEN_WITNESSES_PASS 128
VC_EIGHT_EXHAUSTIVE_OBSTRUCTION_PASS counts=[0, 1, 28, 290, 1572, 3669, 2903, 711, 0]
LITTLESTONE_NINE_TREE_PASS nodes=511 leaves=512
LITTLESTONE_TEN_CARDINALITY_OBSTRUCTION_PASS 720<1024
SMALL_ORDER_CARDINALITY_AND_VC_PASS n=3..6
CYCLIC_ORDER_ALL_CHECKS_PASS
```

The first JSON file is a mapping of all 128 response strings to cyclic-permutation indices. The second JSON file is the complete recursive binary query tree for depth nine. Each of its 512 leaf witnesses is checked against all responses on its path. The exhaustive VC upper check normalizes one selected triple by label symmetry and tests every further query choice with a necessary cell-cardinality condition, ensuring that no potential eight-query shattered support is pruned. The tree proves a lower bound only; the cardinality bound proves its upper bound.

Computations are deterministic, with finite loops and integer bit operations. These checks are not substitutes for an independent scientific audit or historical-priority determination.
