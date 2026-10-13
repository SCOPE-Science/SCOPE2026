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
The package verifies Lion's exact persistent-gradient-reversal response.

`verify.py` replays the scalar state, checks the closed forms for momentum and the pre-sign variable, verifies the exact stale-sign count, the immediate-reversal threshold, the ordering of the two reversal clocks, and the defining-default values.

The computations are transcription guards. The formulas are proved algebraically in `RESULT.md`.
