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

## Reproducibility
Run `python3 verify.py` with standard Python 3. The recorded output was `OPTIMIZATION_CASES 896 EXACT_D8_x_C3^2_ELEMENTS 72 VERIFY_OK`. The matrix calculation uses exact coefficients in the quadratic cyclotomic field, represented by integer pairs in the basis \(1,\omega\), where \(\omega^2+\omega+1=0\).

The direct support optimizer enumerates all nonlinear-factor masks and numbers of constituents in bounded parameter families; it checks the numerical minimization independently of the closed expression once the central-character constraints are established. It does not enumerate irreducible character tables for all extraspecial groups, and is not an infinite classification certificate. The general proof relies on the standard extraspecial irreducible-degree theorem and the faithful-center criterion for finite nilpotent groups.

## Limits
Only the stated family and complex representations are covered. Independent validation has not been performed.
