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

Run `python verify_geometry.py` in an environment with Python 3, NumPy and SciPy. This standalone program uses only the explicit vertex definition and elementary Gaussian formulas. On the present evaluation it printed `VERIFY_OK`, including `FINITE_SUPPORT_AND_SOLID_ANGLE_PARTITION_OK 700`, `GAUSSIAN_MINIMUM_INTEGRAL_OK`, `QUANTILE_INTEGRAL_OK`, `EXACT_SATURATED_MEAN_MONTECARLO_OK`, and `TYPE_B_PRODUCT_POLYNOMIAL_OK`.

The checker enumerates all relevant generating vertices for dimensions 2–5 and label caps 1–5. It uses 700 independent Gaussian objective comparisons against exact brute-force linear maximization, checks angular-orbit normalization, numerically integrates the Gaussian-minimum identity and phase function, and compares finite-dimensional simulations to the asymptotic formula in dimensions 50, 200 and 800. Finally, it checks the Weyl-product polynomial coefficients in dimensions through 9. All random tests use a fixed seed.

The analytic proof is recorded in `RESULT.md`; finite computations cannot prove general asymptotics, infinite-dimensional statements or novelty. The cited type-B conic intrinsic-volume formula is a known external theorem, not independently proved by this checker. The numerical integration and simulations use floating point, with explicit tolerances visible in the code. No independent mathematical validation has yet been carried out.
