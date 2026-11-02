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

# Reproduction and limits

Run `python verify.py` with Python 3 using only the standard library. The program constructs ordinary graph squares from the original distance-two adjacency rule, enumerates proper named-colorings by a backtracking search, deletes edges to discover bridges, and independently calculates the product formula from those components. Successful output includes:

```
ALL_CONNECTED_LABELLED_GRAPHS_THROUGH_FIVE_OK 3088
RANDOM_BLOCK_TREES_EXACT_COLORINGS_OK 340
NONISOMORPHIC_BRIDGE_TREES_SAME_CHROMATIC_POLYNOMIAL_WITNESS_OK
NONCHORDAL_SIX_CYCLE_BRIDGE_WITNESS_OK
VERIFY_OK
```

The first check covers every connected labelled simple graph on one through five vertices with two, three, four, and five named colors. The randomized check is deterministic from its fixed seed and covers 340 additional graph/palette instances. The triangle-core example yields 192 four-colorings of both squares, with graph diameters seven and five; two length-six cycles joined by one bridge yield 768 four-colorings of the square. Numerical tests are finite sanity checks, not a proof of the theorem for all graphs. The preceding mathematical induction provides that proof; independent assessment remains unperformed.
