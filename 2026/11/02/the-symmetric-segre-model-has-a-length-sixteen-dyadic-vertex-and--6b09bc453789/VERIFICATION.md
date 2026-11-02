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

# Verification

The standalone `verify_segre.py` uses Python's standard library only. From the embedded file's directory run `python3 verify_segre.py`. Expected last line: `SYMMETRIC_SEGRE_CHAR2_JACOBIAN16_FANO_15PLUS6_ETALE_EXACT_OK`.

The program constructs the cubic in characteristic two by exact polynomial arithmetic, verifies the four derivative-square identities and the invertible coordinate transformation, enumerates the complete finite Grassmannians of 35 and 357 lines over the two finite fields, tests the four cubic-restriction coefficients for each, compares all fifteen pair-partition planes, tests Frobenius orbits, and checks all 27 first-order plane normal-deformation determinants. It verifies the integer Hessian determinant in the odd-characteristic comparison. The proof uses the 27-line theorem to conclude completeness over the algebraic closure; finite-field enumeration alone would not establish that bound.

The arithmetic statements apply to the specified integral equations. There is no claim of independent validation or of a good modular reduction at two.
