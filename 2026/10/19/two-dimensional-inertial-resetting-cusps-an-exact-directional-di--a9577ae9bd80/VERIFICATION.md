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

The exact stationary renewal identity is derived from the linear kinetic stochastic differential equation and independence of angular and translational noise. The proof independently evaluates the two comparison integrals, using changes of variable that reduce them to Gamma integrals, and estimates all remainders uniformly in direction and mixture weight. The small-radius probability and directional-bias formulas follow by integrability against planar polar measure.

Run `python verify.py` with NumPy and SciPy. The script prints the constants and five successively smaller-radius evaluations for each of three tests: zero-velocity passive cusp, active angular-response derivative at zero activity with rotational Brownian heading, and Maxwellian velocity cusp. The script verifies that normalized errors decrease on the test grid and that each final relative error is under 1.2 percent. These finite computations corroborate, but cannot independently certify, the theorem for arbitrary parameter values or for nonzero activity beyond linear response.

Independent external validation was not performed. Literature comparisons and source-access limitations are recorded in the scientific review.
