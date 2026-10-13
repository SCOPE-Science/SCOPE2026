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
The package verifies the practical M-SVAG response to a deterministic alternating gradient.

`verify.py` checks the finite bias-corrected first-moment formula, exact second-moment identity, source finite-sample correction, asymptotic corrected variance, variance-adaptation factor, complete update gain, constant-gradient response, and the exact source-coefficient specialization.

The computations are transcription guards. The asymptotic response is proved algebraically in `RESULT.md`.
