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

The package contains `check.py` and `check_output.txt`. Run `python check.py` in the extracted directory, with Python 3 and the `mpmath` and `sympy` libraries installed.

The checker verifies four exact polynomial/rational identities, 2,557 high-precision recurrence and initial-sign calculations, all displayed critical quantities, and eleven *exact rational interval* tests based on Taylor's theorem for the signs required in the zero-count argument. Numerical checks are auxiliary: infinite-time eventual sign failure follows from strict dominance of the negative real root, the root count follows from a convexity argument, and the onset rates follow from explicit logarithmic formulas. The data are the five-decimal rational coefficients printed in the source, not inaccessible unrounded parameters. No claim is made about arbitrary PDE solution positivity or the corrected parareal method.
