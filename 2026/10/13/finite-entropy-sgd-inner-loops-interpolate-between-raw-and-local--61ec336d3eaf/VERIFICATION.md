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
The package verifies the finite-inner-loop Entropy-SGD spectral filter on SPD quadratics.

`verify.py` reconstructs the expected source recurrence, checks the closed modal response over randomized parameters, verifies the one-step identity, checks the finite-\(K\) condition-number interpolation, and tests both limiting regimes.

The computations are transcription guards. The exact filter and condition-number inequalities are proved analytically in `RESULT.md`.
