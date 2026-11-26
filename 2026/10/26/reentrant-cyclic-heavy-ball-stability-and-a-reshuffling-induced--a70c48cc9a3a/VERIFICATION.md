---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

`python3 verify.py` reconstructs the two rational epoch propagators, their common characteristic roots through trace and determinant, and the positive-definite certificate for uniform conditional mean-square amplification. The accompanying trace and determinant grid is supplementary. The conditional expectation argument in `RESULT.md` proves the all-state and all-epoch bounds. It does not prove almost-sure divergence.
