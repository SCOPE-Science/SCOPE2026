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
The package verifies the exact constant-step NovoGrad eigencycle and its transverse spectrum on deterministic SPD quadratics.

`verify.py` checks the complete state recurrence on the proposed period-two orbit, validates the transverse characteristic polynomial and sharp curvature-order stability boundary, checks the complex-root modulus plateau, and compares the analytic transverse matrix with a finite-difference Jacobian of the full two-dimensional NovoGrad map.

Finite-difference calculations are transcription guards. The orbit, existence threshold, and transverse classification are proved analytically in `RESULT.md`.
