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

The standalone `verify.py` requires Python 3 and SymPy; run `python verify.py` in the extracted directory. It reconstructs the exact source matrix at the specified parameter values, checks the quadratic coefficients in the shifted first affine coordinate, and verifies the discriminant factorization into four local analytic branch factors. It evaluates the branch-coordinate Jacobian determinant exactly and verifies the matrix rank at the collision. The holomorphic square-root and inverse-function arguments are supplied in `RESULT.md`; finite computation is not invoked as a proof of analytic triviality. The verification covers only the stated point and parameters.
