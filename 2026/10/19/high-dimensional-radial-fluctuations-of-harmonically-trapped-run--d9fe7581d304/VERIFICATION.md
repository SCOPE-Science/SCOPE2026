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

# Mathematical verification

The proof is analytical. The stationary stochastic convolution and Poisson renewal intervals yield exactly beta stick-breaking weights; conditional spherical covariance identities yield an exact finite-dimensional mean-square coupling error. A multivariate central limit theorem for products of independent Gaussian coordinates gives the finite-pair fluctuation law; a uniform conditional second-moment tail bound justifies passage to infinitely many intervals.

To reproduce the supporting finite checks, run `python check.py` with Python 3.10 or later. It uses no third-party packages and a fixed pseudorandom seed. It checks 73 assertions, including rational beta-moment identities, known two-dimensional beta-law variance, and mean/variance/conditional-error comparisons on finite simulated spheres.

The finite tests are not proof of convergence, nor do they certify originality. The conclusions are conditional on isotropic independent orientations, exponential tumbling intervals, a fixed positive relaxation rate, and the absence of Brownian thermal forcing. No independent audit has been performed.
