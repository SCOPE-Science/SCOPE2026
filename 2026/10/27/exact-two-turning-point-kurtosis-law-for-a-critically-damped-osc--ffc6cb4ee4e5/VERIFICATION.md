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

The stationary generator and all degree-one through degree-four moment equations were solved exactly with SymPy using `verify_kurtosis.py`. The code checks both homogeneous-matrix determinants, the two-wall fourth cumulant, the derivative's degree-nine numerator, both limiting coefficients, and the sharp positive-root count. It also simulates the conditional Gaussian covariance recursively over stationary Poisson reset intervals, independently of the moment equations; the two tested parameter values agree with the exact one-wall excess-kurtosis predictions within the finite-sample tolerance. See `verification_output.txt` for actual output.

The stochastic comparison does not certify the infinite-time stationary law or the number of algebraic roots. Those are established by the stationary convolution construction, finite-degree generator recurrence, and Descartes/intermediate-value argument in `RESULT.md`. The exact two-root count has only been established at critical damping, not for arbitrary damping.
