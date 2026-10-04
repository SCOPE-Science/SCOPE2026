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
The package verifies the exact local AMSGrad spectrum on a scalar quadratic when the running maximum is inactive.

`verify.py` reconstructs the four-state recurrence, compares a finite-difference Jacobian with the analytic Jacobian, checks the sharp Jury boundary, verifies the complex-root modulus plateau, and confirms the neutral retained-memory and current-second-moment eigenvalues.

The finite computations are transcription guards. The equilibrium manifold, threshold, and spectral formulas are proved analytically in `RESULT.md`.
