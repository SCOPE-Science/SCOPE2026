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
The package verifies the stationary SOAP stale-basis singular-value formulas.

`verify.py` checks the exact \(45^\circ\) condition number against direct eigenvalue calculations, verifies the fresh-basis condition number, tests the general angular half-saturation law, and numerically demonstrates the two noncommuting limiting paths.

The numerical calculations are transcription guards. The stationary moment limit, singular-value identities, and limit statements are proved algebraically in `RESULT.md`.
