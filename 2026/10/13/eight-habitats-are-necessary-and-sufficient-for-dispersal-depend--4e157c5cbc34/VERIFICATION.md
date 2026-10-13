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

# Exact proof-certificate verification

The complete `verify.py` requires standard-library Python 3.10+ and runs via `python3 verify.py`. It reconstructs every labelled tree through order eight from Prüfer sequences, checks unlabelled-isomorphism classes through center-rooted canonical codes, generates rooted-forest polynomials for all singleton and edge endpoint sets, and independently evaluates the same minors by fraction-free integer determinant at two positive coupling values. It compares every pair of edge correlations using exact rational/integer polynomial arithmetic, and certifies each mixed-sign case by polynomial factorization into a one-positive-root factor and a remainder with one coefficient sign. It also reconstructs the explicit witness rational identities.

Observed successful stdout conclusion:

```
n=2 tree_shapes=1
n=3 tree_shapes=1
n=4 tree_shapes=2
n=5 tree_shapes=3
n=6 tree_shapes=6
n=7 tree_shapes=11
n=8 tree_shapes=23
REVERSAL_SHAPES 6 PAIR_COMPARISONS 11
SHAPE_KEYS (((()()))((()))) (((())())((()))) (((()))((()))()) [((()()()))((()))] [((()())())((()))] [((()()))((()()))]
VERIFY_OK shape_counts=1,1,2,3,6,11,23 mixed_shape_count=6 mixed_edge_pairs=11 all_pair_comparisons=733 identically_tied=201
```

The finite computation is exhaustive only for tree orders two through eight. Its logical reach depends on the mathematical correctness of the Prüfer bijection, the canonical-tree coding, the rooted-forest minor identity and the Descartes factor argument, all explained in the proof. No general claim for larger trees or weighted networks follows from these computations. Independent scientific audit has not been performed.
