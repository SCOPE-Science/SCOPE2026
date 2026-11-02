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

# Reproducibility and limits

The accompanying `verify_minimal_cycle_powers.py` uses only the Python standard library. Run `python verify_minimal_cycle_powers.py` to reproduce all finite tests. The checker builds each \(C_n^r\) directly from graph distances, exhaustively tests its nonempty vertex subsets for domination and inclusion-minimality by deleting each selected vertex, and compares the observed cardinality distribution with an independently implemented dynamic program on cyclic gap words. It also checks that every intermediate size occurs and tests the odd/even upper-extremal formula for larger parameters.

A successful execution reports `VERIFY_OK graph_cases=32 direct_subsets=85304 parity_cases=35`. The graph instances range over four radii with vertex counts up to fourteen (depending on radius), and the parity tests include radii one through seven and quotient values two through six. Exhaustive finite tests do not certify the infinite theorem; that rests on the graph-theoretic and generating-function proof in `RESULT.md`. No independent audit has been performed.
