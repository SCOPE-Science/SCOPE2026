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

# Exact verification

Run `python3 verify.py` using only Python 3's standard library. The program uses exact rational fractions and a separately implemented three-unknown Gaussian elimination routine for the symmetric Sylvester equation. It checks both corrected matrices and both Sylvester residuals exactly, verifies the strict positive-definite principal minors of \(Z\) and \(2Z-X\), and certifies the first-positive/second-indefinite iterate contrast by rational determinants. Successful execution prints `VERIFY_OK: exact_Sylvester_solves=2; positive_seed=true; strict_order=2Z-X_positive; first_iterate_positive=true; second_iterate_determinant_negative=true`.

The universal commuting theorem is proved analytically via the scalar recurrence, and the local linear attraction is proved analytically by positive-definite operator comparisons. Finite verification cannot replace those arguments or establish exhaustive originality. The program is for exact mathematical assertions only, not a finite-precision stability assessment.
