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
The package reconstructs source-form StableAdamW using the published bias-corrected moving-average recurrence and implementation-safe RMS detector.

`verify.py` checks the exact impulse formulas against direct iteration for randomized parameters, verifies that the published RMS clipping statistic is exactly zero on the zero-gradient tail, tests both sides of the \(\beta_1^2=\beta_2\) boundary, checks the exact boundary limit, and independently verifies the scalar update cap obtained by using the source-discussed squared-momentum RMS numerator.

Finite calculations are transcription guards only. The arbitrary-time, arbitrary-amplitude, and detector-cap statements are proved algebraically in `RESULT.md`.
