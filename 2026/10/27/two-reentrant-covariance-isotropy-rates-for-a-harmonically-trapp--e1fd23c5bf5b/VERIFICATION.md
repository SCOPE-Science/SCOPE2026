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

# Verification of the two-reset-rate covariance theorem

The standalone `verification.py` is designed to be run with `python verification.py`, using Python with NumPy, SciPy and SymPy installed. It performs the following checks: symbolic expansion of the stationary moment numerator into the displayed quartic; exact evaluation of the negative sign at the reference angular diffusion rate; verification of the two small-/large-confinement rescalings; numerical two-root isolation and sign ordering for seven distinct trap and heading-diffusion parameter pairs; and cancellation of isotropic thermal diffusivity from the variance difference.

A separate quadrature reconstructs each of the stationary mean and two coordinate variances without relying on the stationary-generator moment equations. It samples the exponential last-reset-age law by Gauss–Laguerre quadrature, integrates pairwise Gaussian heading correlations by Gauss–Legendre quadrature, and adds the exact Brownian translational variance conditional on the age. For six test parameter choices, the maximum absolute discrepancy across the computed mean and covariance entries was below `7e-5` at the quoted quadrature resolution.

The exact root-multiplicity conclusion is proved by polynomial sign variation and strict evaluations at three points. A finite list of numerical roots is corroboration only: it cannot by itself establish universal existence, uniqueness or sign ordering. The auxiliary computations do not assess publication priority, higher moments, finite-sample inference, or independent scientific validity. Independent audit has not been performed.
