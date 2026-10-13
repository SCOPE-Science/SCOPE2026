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
The package verifies the exact PowerSign/AddSign agreement phase diagram.

`verify.py` compares the closed EMA formulas with direct recurrence replay over randomized parameters, checks the three open amplitude-ratio regimes, verifies the exact upper-boundary zero state, checks the lower-regime odd-step switch index, and confirms the source-default window.

The numerical calculations are transcription guards. The recurrence solution and sign classification are proved algebraically in `RESULT.md`.
