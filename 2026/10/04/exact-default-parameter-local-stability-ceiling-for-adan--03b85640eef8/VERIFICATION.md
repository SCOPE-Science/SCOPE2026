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
The package derives the default-parameter Adan local cubic after the adaptive denominator reaches its epsilon floor.

`verify.py` reconstructs the polynomial with exact fractions, evaluates the cubic Schur inequalities, verifies the \(-1\) boundary root, and checks roots just below and above the threshold.

Numerical roots are secondary checks. The exact interval follows from the rational Schur inequalities in `RESULT.md`.
