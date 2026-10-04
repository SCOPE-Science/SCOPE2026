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
The package verifies the exact first-step scalar source-form AdaBound map.

`verify.py` compares the closed-form objective ratio with direct recurrence evaluation, checks the necessary-and-sufficient upper-bound safety frontier over randomized parameters, verifies the constant upper-clipping amplification plateau, and reproduces the defining paper's stated default values.

The numerical calculations are transcription guards. The universal first-step theorem is proved analytically in `RESULT.md`.
