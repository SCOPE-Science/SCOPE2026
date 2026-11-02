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

# Reproducibility and verification
Run `python3 verify_flex_pencil.py` using Python 3; no external libraries are needed. The program returns `VERIFY_OK` after exact sparse-polynomial verification of the full Hessian identity in four variables, the residual-quadratic discriminant identity, the branch/residual reduction, both exceptional perfect-square identities, flex-weight totals across integer parameters, and rational sample sign tests.

The universal proof uses the identities as polynomial identities, not empirical extrapolations: it combines the characteristic-zero Hessian/contact-order theorem with ramification and support counts. The finite parameter loop and sample real inequalities are merely regressions. The script does not establish any claims about dual singularities, historical originality, independent certification, or positive-characteristic curves.
