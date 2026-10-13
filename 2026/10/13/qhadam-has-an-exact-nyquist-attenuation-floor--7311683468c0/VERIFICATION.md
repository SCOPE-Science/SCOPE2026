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
The package verifies the exact alternating-gradient response of bias-corrected QHAdam.

`verify.py` replays both moment recurrences, checks the exact parity law after first-moment bias correction, verifies exact second-moment parameter erasure, and reproduces the limiting attenuation factors including the WMT16 setting.

The finite calculations are transcription guards. The closed forms and sharp floor are proved algebraically in `RESULT.md`.
