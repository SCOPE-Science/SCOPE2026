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

# Verification and reproducibility

The proof supplies the exact inverse-return-cylinder identity, an all-index inverse-orbit recurrence estimate with its subprincipal logarithmic coefficient, uniform distributional expansions over the entire half-line, and an exact one-dimensional maximization. Those analytic steps certify the claims for all admissible parameters and all large indices; finite computations do not.

Run `python verify.py` with Python 3's standard library. The checker tests the inverse-branch recurrence and first-return cylinder boundaries across four selected parameters, and evaluates four initial-boundary profiles over three horizons each. Expected terminal status:

`VERIFY_OK return_cylinder_tests=52 weighted_cases=4 normalized_rate_checks=12`

The computed normalized errors approach their proved constants slowly; finite samples are not used to extrapolate the infinite limit. No independent audit or external validation is reported.
