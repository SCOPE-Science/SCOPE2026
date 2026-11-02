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

The Python verifier `verify_primary.py` independently enumerates binary edge orientations, uses graph DFS to test acyclicity, enumerates permitted single-edge reversals, and compares complete degree histograms with the block-formula values for ten part-size pairs with \(1\le a\le b\le4\). It also checks the simple-vertex independence property for all such pairs where both part sizes are at least two and checks four additional nonexhaustive larger symbolic enumerators. Printed status: `PRIMARY_DIRECT_DAG_AND_COMPOSITION_PASS 14`.

The C++17 verifier `verify_alt.cpp` instead accepts binary matrices with nested row neighborhoods and tests every single-bit flip. It exactly compares degrees and the simple-count formula for six indicated bipartite graphs, including \(K_{4,5}\). Printed status: `ALTERNATIVE_NESTED_MATRIX_PASS 6`.

Both checks have been executed on the decoded embedded files. Source inspection and the all-parameter algebraic proof establish the infinite-family claims; enumerations cannot independently certify infinitely many parameters. External independent scholarly audit remains unperformed.
