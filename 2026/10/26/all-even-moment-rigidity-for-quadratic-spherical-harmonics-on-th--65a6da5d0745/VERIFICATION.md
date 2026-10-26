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

# Verification scope

Execute `python3 verify_even_moments.py` with Python 3 standard library only. The checker reproduces 291 exact rational assertions; see `VERIFICATION_OUTPUT.txt` for the observed run output.

It independently integrates spherical monomials for five distinct real traceless diagonal forms through normalized order ten, compares polynomial coefficients and strict inequalities through order nineteen, compares Legendre-zonal integrals through order thirteen, checks several complex traceless forms, and checks extremizing examples. The checker has no external data dependencies. All analytic quantifiers, strict monotonicity for every degree, and complex equality classifications are justified by the proof in `RESULT.md` rather than by these finite tests.

The code does not independently certify mathematical priority or supply independent review. Non-even moments and complex lower extremizers are outside its tested and proved scope.
