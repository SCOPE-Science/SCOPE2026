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

# Reproducibility and verification

Run `python checks/checker.py` from the package root. Required packages: Python 3 with SymPy, NumPy, and SciPy. A successful run ends with `EXACT_ALL_TESTS_PASSED` and prints the direct Gaussian-integral numerical posterior weights and scaled log-density checks for \(\delta=0,1,4\) and \(L=100,500,2000,5000\).

The source of the analytic proof is the exact reset-age Gaussian mixture in `RESULT.md`. The checker symbolically confirms the rate derivative factorization, critical stationary ages, equality of minimal costs, one-sided slopes, Hessians, young/old weight ratio, Gaussian covariance determinant, and the independent path-action variational calculation. Numerical quadrature also directly integrates the exact finite-scale stationary propagator, *without inserting the limiting rate function in the integrand*, across two sides of the competing age saddle.

**Mathematical limits.** All claims concern fixed positive parabolic-ray parameter and fixed finite longitudinal diffusion. Numerical tests at finite scales or on finite parameter grids do not establish global uniqueness, nondegeneracy, or the asymptotic posterior; these follow from the analytic root comparison and Laplace localization proof. Independent audit has not been performed.
