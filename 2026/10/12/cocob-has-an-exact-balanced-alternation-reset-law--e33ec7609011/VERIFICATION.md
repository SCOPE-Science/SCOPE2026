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
The package verifies the exact balanced-alternation law for theoretical COCOB.

`verify.py` replays the source recurrence, checks the wealth product, every-other-step reset, telescoping average, and numerical convergence to the stated \(n^{-1/2}\) and \(n^{-3/2}\) constants.

The finite calculations are transcription guards. The exact identities and asymptotic exponent are proved analytically in `RESULT.md`.
