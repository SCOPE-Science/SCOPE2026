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
The package reconstructs source-form diffGrad on a deterministic scalar quadratic.

`verify.py` checks the limiting characteristic polynomial, exact Jury boundary, unit-root factorization, complex-root plateau, and the second-order disappearance of the nonconstant friction term through shrinking-state evaluations of the nonlinear map.

The finite computations are transcription guards. The strict local frontier follows analytically from the limiting Jacobian and the exponentially vanishing bias-correction perturbation described in `RESULT.md`.
