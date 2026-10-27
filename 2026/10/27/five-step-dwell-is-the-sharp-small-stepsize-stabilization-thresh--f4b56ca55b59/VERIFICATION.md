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

`check.py` independently reproduces the period-matrix trace and determinant formulas with exact polynomial operations, compares the four short-dwell \(p_m(1)\) polynomials coefficient-by-coefficient, and checks the quadratic trace coefficient for integers from 2 through 20. Numerical evaluation separately checks representative period-map spectral radii against the stability dichotomy and verifies the complex-to-real reduction.

The mathematical assertions for all real positive stepsizes and all integer dwell lengths rest on the analytical proof in `RESULT.md`; finite symbolic checks are not exhaustive for all integers or all real parameters. Verification does not test arbitrary switching patterns, finite-precision robustness, or the complete text of an inaccessible related article.
