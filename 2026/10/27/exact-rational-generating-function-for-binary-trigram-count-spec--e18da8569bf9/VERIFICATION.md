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

# Reproduction

Execute `python3 verify.py` with Python 3.9 or later; no third-party packages are needed. The script implements the rational recurrence independently from the combinatorial flow count, computes all thirteen possible endpoint imbalances and checks them through 30 length-three windows, and directly enumerates all binary source strings of lengths 3 through 17. The observed results are `FLOW_VS_RATIONAL_OK 31`, `WORD_ENUM_VS_RATIONAL_OK 15`, and `VERIFY_OK`.

The rational identity for all lengths is proved in RESULT.md by explicitly summing the constrained lattice cones, with four boundary restrictions for the allowed loops. Finite verification is a check of implementations and examples, not proof of universal equality. No independent external audit was performed.
