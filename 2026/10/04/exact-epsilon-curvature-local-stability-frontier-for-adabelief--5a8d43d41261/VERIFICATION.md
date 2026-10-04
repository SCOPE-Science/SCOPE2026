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
The package reconstructs paper-form AdaBelief on a deterministic scalar quadratic.

`verify.py` checks the fixed second-moment floor, exact characteristic polynomial, Jury boundary, complex-root plateau, source-parameter curvature ceilings, and the constant corrected second moment along the debiased optimum orbit.

Numerical eigenvalue evaluations are transcription guards. The exact local frontier follows analytically from the Jacobian and Jury inequalities in `RESULT.md`.
