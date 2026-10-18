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

Execute `python CHECK.py` with Python, NumPy, and SciPy. The script's expected last line is `ALL_CHECKS_PASS`.

The actual execution produced `SUPPORT_OK: 1600 direct polytope comparisons`, `EXACT_ANGLE_OK` (the precise trivariate orthant value agreed with one-dimensional quadrature within \(2\times10^{-12}\)), `NORMAL_CONES_OK: 131072 quasi-random exposures`, `TILT_STATIONARITY_OK` (independent saddle-point equations), and `RATE_OK: unique-root numerical cross-check`, then `ALL_CHECKS_PASS`. The computed root was \(0.688633060895689\).

The exact support-function identity, symmetry reduction, large-deviation rate, envelope derivative, strict convexity, and crossing argument are proved in `RESULT.md`. Finite enumerations, numerical integration, and quasi-random samples cannot prove those assertions for arbitrarily large dimensions. The root decimal is an approximation, not an interval-certified exact algebraic value. No independent audit has been performed.
