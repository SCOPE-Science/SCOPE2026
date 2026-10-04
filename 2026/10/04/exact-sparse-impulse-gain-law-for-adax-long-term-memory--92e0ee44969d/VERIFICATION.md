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
The package verifies the exact one-coordinate sparse-gradient impulse response of source-form AdaX Algorithm 2.

`verify.py` checks the closed moment formulas, monotonic response kernel, displayed default gain, sharp ceiling, and the finite, critical, and divergent Adam impulse regimes.

The finite calculations are transcription guards. Summability, strict gain monotonicity, and the sharp limiting gain are proved analytically in `RESULT.md`.
