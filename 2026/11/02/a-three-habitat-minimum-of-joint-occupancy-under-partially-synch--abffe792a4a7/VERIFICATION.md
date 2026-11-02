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

Run `python3 CHECKER.py` next to this file. The checker uses only the Python standard library and performs direct exact-rational stationary generator solves, independently of the reported closed-form law. Its checked output is `VERIFY_OK assertions= 18755`, with exact witness values `21/62`, `504/1489`, `63/185` at catastrophe fractions zero, one quarter, one. It covers 3,750 parameter tuples and five additional rational witness assertions. The all-real-parameter classification rests on the algebraic proof in `RESULT.md`, not on this finite verification. No independent audit or external scientific certification has been performed.
