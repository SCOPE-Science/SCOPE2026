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
The package verifies the alternating-gradient input response of source-form AdaMomentum.

`verify.py` replays the exact source recurrence, checks the closed first-moment transient, confirms the asymptotic bias-corrected second moment and normalized update, compares the raw-gradient second-moment ablation, checks monotonicity of the restoration factor, and reproduces the source-table crossover scale.

The finite calculations are transcription guards. The limits, sharp restoration factor, and zero-damping cancellation are proved algebraically in `RESULT.md`.
