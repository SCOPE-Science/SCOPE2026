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

# Verification of the exact two-source phase classification

Run `python verify_mogi.py` from a directory containing that file, with `sympy>=1.12` installed as specified in `requirements.txt`. It checks exact symbolic derivative, discriminant, double-root and logarithmic-derivative identities, plus the stationary-point witness \((d_1,d_2,A_1,A_2)=(1,6,1,45)\), 1,800 deterministic parameter comparisons, 700 generated three-stationary-point examples, and four near-cusp checks of the strength-window constant. These finite tests are supplemental to the analytical proof.

The exact sign reduction and the quadratic discriminant in `RESULT.md` establish the universal result for all positive parameters, not only the tested cases. At the strength-window endpoints, a stationary shoulder need not be a second maximum; the program tests nondegenerate interior examples rather than treating approximate double-root detection as a mathematical proof. Experimental field validation, finite-size source mechanics, and independent external validation have not been performed.
