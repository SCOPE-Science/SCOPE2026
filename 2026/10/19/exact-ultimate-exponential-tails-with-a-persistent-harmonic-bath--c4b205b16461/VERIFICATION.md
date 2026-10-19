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

# Verification record

The proof relies on the explicit drift semigroup, exact two-noise covariance integrals, strict mean-square contraction of the reset-time bath chain, an exponential Lyapunov estimate for the conditional Gaussian variance, and matching Gaussian large-age lower / exponential-moment upper tail bounds. Every step is valid at fixed \(a,b,D_x,D_y,r>0\). In particular, both the moment-generating-function boundary and exact two-sided logarithmic tail constants are analytic conclusions, not extrapolations from data.

`python verify.py` uses Python 3 with NumPy and SciPy. It independently quadratures all 24 free-excursion covariance values from matrix exponentials, checks six stationary moment values against the Markov generator, and reproduces the exponent's saddle-point cost for six parameter sets. The checks passed. The tested values are only consistency witnesses; no finite computation verifies all positive real parameters.

The closest source literature concerns a singular large-memory Gaussian-profile approximation or a renewed-bath strong-coupling Laplace-profile calculation. This result does not establish the distribution's pre-exponential factor, the crossover distance, uniform memory-limit estimates, or arbitrary bath kernels. No independent audit has been performed.
