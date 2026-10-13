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

# Reproduction and boundaries

The analytic proof establishes the nonnegative mixed-density bound and boundary necessity for the entire real parameter region, and derives the two directional conditional-tail limits. The numerical checker (`CHECK.py`) uses arbitrary-precision arithmetic to compare the analytic density with central mixed finite differences at 150 interior settings. It also compares the opposing-tail limits, second/third-order upper-right asymptotics, equality of diagonals with unequal weights, and negative density outside the domain.

Run `python -m pip install -r requirements.txt` followed by `python CHECK.py`. These checks were executed successfully with Python and `mpmath` version 1.3.0. Numerical checks are finite precision and cannot establish positivity everywhere, asymptotic limits, or global scholarly originality without the written proof.

The scientifically relevant unproved limits are arbitrary signed directional weights, general nonlinear reciprocal exponent functions, and sampling/distributional inference using estimated tails. Independence of any review has not been established.
