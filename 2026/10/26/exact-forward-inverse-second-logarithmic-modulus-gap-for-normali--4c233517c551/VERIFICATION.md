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

# Verification details

The proof establishes the statement for every convex map and every admissible second coefficient, including the endpoint cases. The supplied `verify_coefficients.py` and `requirements.txt` reproduce supporting checks under Python 3 with SymPy 1.14.0.

Command: `python verify_coefficients.py`

Observed execution:

`VERIFY_OK symbolic_identities=6 exact_signed_conditional_extremizers=202 random_interior_tests=500`

The symbolic tests cover the coefficient relations through degree three, the direct/inverse logarithmic identities, and the two cancellation configurations. The 101 rational radius cases per sign check the exact conditional extrema; random admissible jets check the inequality numerically. These tests do not certify all complex parameters. The infinite parameter statement and uniqueness of equality cases instead rest on the derivation, the two-sided triangle inequality, and Schwarz–Pick equality in `RESULT.md`.

The manuscript comparisons concern different, successive-index functionals; prior-art coverage is not proved exhaustive. No independent mathematical audit or external validation is claimed.
