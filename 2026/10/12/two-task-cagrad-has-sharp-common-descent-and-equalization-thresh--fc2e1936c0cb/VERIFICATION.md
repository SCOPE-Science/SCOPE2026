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
The package verifies the two-task CAGrad phase diagram.

`verify.py` checks the closed branches against the exact scalar dual optimality conditions, verifies the common-descent crossing, the equal-progress transition, the one-third obstruction, and the equal-norm specialization.

The computation is a transcription guard. The threshold identities are proved analytically in `RESULT.md`.
