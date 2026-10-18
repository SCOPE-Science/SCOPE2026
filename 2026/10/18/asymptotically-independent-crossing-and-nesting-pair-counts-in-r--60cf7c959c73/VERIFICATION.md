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

# Verification procedures and scope

Execute `python verify.py` from the directory containing this document. The script enumerates all perfect matchings through six chords and checks means, variances and covariance exactly using rational arithmetic. It separately checks the three-chord local mixed and same-type joint probabilities. The unrestricted theorem follows from the explicit polynomial integration and the Hoeffding decomposition in RESULT.md, not from the finite enumerations. This is a finite symbolic/exhaustive check and a self-review, **not** independent audit.
