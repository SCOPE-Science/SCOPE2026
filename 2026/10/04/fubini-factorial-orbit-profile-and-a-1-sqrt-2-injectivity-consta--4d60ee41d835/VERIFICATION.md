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

The bundled `verify.py` uses only the Python standard library. For each `n <= 5`, it enumerates set partitions of the labeled coordinate set, all global linear orders, and all quotient orders on equivalence classes. Each choice is converted into bit-matrix signatures for the actual relations `E`, `<1`, and the induced `E`-convex `<2`; the number of distinct signatures is checked against `n! * F_n`.

For arbitrary tuples through `n <= 5`, the verifier separately enumerates every coordinate-equality pattern, pulls each injective finite structure back along that pattern, records coordinate equality in addition to the three language relations, and confirms the exact Stirling-transform count. This is a relation-level replay rather than merely evaluating the closed formulas.

Finally, exact integer recurrences compute the two profiles through larger arities and verify numerical convergence of `a_n/b_n` toward `1/sqrt(2)` at `n = 20, 40, 80`.

Replay command: `python3 verify.py`. Expected final line: `VERIFY_OK`.
