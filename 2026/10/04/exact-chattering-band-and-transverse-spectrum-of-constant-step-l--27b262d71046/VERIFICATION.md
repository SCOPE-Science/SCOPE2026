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
The package verifies the exact constant-step scalar Lion period-two family.

`verify.py` reconstructs the source recurrence, checks exact closure and strict sign margins across multiple parameter choices, verifies the if-and-only-if band condition, measures the transverse two-step multiplier, and reproduces the default band and objective floor.

The finite calculations are transcription guards. The continuum classification and Floquet spectrum are proved algebraically in `RESULT.md`.
