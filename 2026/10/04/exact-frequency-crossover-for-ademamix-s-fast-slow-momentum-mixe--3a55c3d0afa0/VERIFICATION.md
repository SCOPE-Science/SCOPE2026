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
The package verifies the fixed-hyperparameter AdEMAMix fast-slow frequency crossover.

`verify.py` checks the closed EMA transfer-function magnitudes, strict monotonicity of the slow-to-fast ratio, the crossover equation and source-parameter periods, and direct recurrence simulations for the DC and Nyquist normalized-update gains.

The numerical calculations are transcription guards. Monotonicity, uniqueness, and the endpoint ratios are proved algebraically in `RESULT.md`.
