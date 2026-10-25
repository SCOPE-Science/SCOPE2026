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

The standalone file `punctured_bidirected_verify.py` is self-contained and uses only the Python standard library. Execute `python3 punctured_bidirected_verify.py` and compare its deterministic stdout with `punctured_bidirected_verify.out`.

The program exhaustively checks all seventeen vertex counts from 4 through 20. It enumerates exactly 164,172 dominating backward-face states and verifies acyclicity on all 1,070,871 directed Hasse covering relations of these residual filters; it also compares all critical faces to explicit bit-pattern formulas. A separate complete arc-compatibility face enumeration and direct forward-then-backward lexicographic matching are cross-checked for seven orders 4 through 10. The first-stage acyclicity and the geometric splitting are mathematical proofs in `RESULT.md`, not inferences from finite experiments.

The result does not cover larger cycle orders or other edge-removal patterns. No external independent validation has been performed.
