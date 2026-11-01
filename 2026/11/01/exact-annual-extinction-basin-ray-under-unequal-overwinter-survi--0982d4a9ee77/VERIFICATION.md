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

The proof is analytical. Below is actual output from running `python verify.py` on the included standard-library script. Its finite RK4 tests check the explicit slope against the annual ratio map in all three cases and verify planar ray invariance to numerical tolerance. They are not mathematical certification of the all-parameter basin theorem.

```text
positive_C q_star 0.205227687711 annual_ratio_relative_error 5.995e-15 axis_x 0.84801618 axis_y 1.06079517 PASS
zero_C q_star 0.667455185957 annual_ratio_relative_error 4.885e-15 axis_x 1.98044243 axis_y 0.63265460 PASS
negative_C q_star 0.089330214976 annual_ratio_relative_error 4.885e-15 axis_x 1.60266225 axis_y 0.90221217 PASS
FINITE_NUMERIC_DIAGNOSTICS_PASS
ALL_PARAMETER_GLOBAL_BASINS_REQUIRE_ANALYTIC_PROOF
```

The strict global convergence conclusions follow instead from the quotient-map monotonicity, separated-flow fixed-point identity, and reciprocal logistic recurrences proved in RESULT.md. No independent audit has been performed.
