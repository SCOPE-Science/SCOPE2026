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
The package verifies the exact scalar SlowMo stability law.

`verify.py` reconstructs the tau-step fast SGD block and the source slow-momentum update, checks the eliminated second-order recurrence, compares the analytic Jury condition with direct eigenvalue calculations, and verifies the odd/even stability boundaries for the source-relevant choice \(\alpha=1\).

The computations are transcription guards. The necessary-and-sufficient stability theorem is proved analytically in `RESULT.md`.
