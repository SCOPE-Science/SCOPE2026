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

The analytic proof is in `RESULT.md`. Run `python check.py` with Python 3 and only its standard library. The program computes the second- and fourth-power boundary integrals as exact rational polynomials, checks the area-correction identity, numerically integrates several nonintegral-exponent boundary moments as independent spot tests, checks the strict upper envelope and angular remainder, and brackets the unique critical exponent.

The actual execution produced:

```
EXACT_QUADRATIC_AND_QUARTIC_IDENTITIES_PASSED
INDEPENDENT_QUADRATURE_AND_STABILITY_PASSED
UNIQUE_CRITICAL_EXPONENT_AND_SHARPNESS_PASSED
ALL_CHECKS_PASSED
```

These checks do not exhaust uncountably many shapes or exponents. The assertions for all real parameters are supported by the integral representation, convexity/concavity arguments, elementary endpoint integrations, the scalar monotonicity calculation, and the exact second-derivative estimate in `RESULT.md`. The checked quartic identity is symbolic and exact for rational test parameters; its universal validity follows from direct polynomial expansion. Independent external validation was not performed.
