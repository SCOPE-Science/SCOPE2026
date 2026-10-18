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

# Verification details

The calculation is analytic. The covariance of two second-factorial Poisson counts follows from differentiation of the bivariate generating function with a common Poisson overlap. Integrating that covariance over one temporal period gives the exact variance; Parseval and Fourier orthogonality give the spectral penalty. Nonnegative spectral penalty, equality and strictness follow from Fourier uniqueness and the strict inequalities for positive arc masses. The normalized pulse sequence establishes sharpness of the unattained supremum.

The standalone Python script `verify.py` checks the sinusoidal Fourier coefficients, the independent two-dimensional overlap integral, and the sharp bounds at several intensity and modulation parameters. It does not verify a general stochastic-process limit theorem by finite sampling. The Gaussian limit uses the standard one-dependent central limit theorem with finite second moments, and the non-Gaussian finite observations are not substituted for that theorem.

Scientific limits: continuous strictly positive normalized one-periodic intensities, one-dimensional Poisson counts in unit windows, physical-time averages, and the linear and second factorial-count observables only. No independent audit has yet been performed.
