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

# Scientific verification

The exact finite-dimensional support-function equality can be reconstructed from stable-set indicator vectors and the elementary maximum identity. `check.py` requires NumPy and SciPy, generates independent Gaussian test directions, directly enumerates every admissible stable-set indicator in dimensions 2–9 for 864 tests, and checks both support and width formulas at a numerical tolerance of \(10^{-11}\).

The same program independently integrates the bivariate Gaussian distribution at the diagonal and checks the centered orthant–arcsine identity. In dimension 1,400, three 25,000-direction Monte Carlo experiments are compared to the limiting same-level probability and width mean and standard deviation. The seeded code and the observed output are both embedded as standalone files in this package.

The proof's unbounded-dimensional steps are analytic: triangular-array multivariate Gaussian-summand CLT, joint radial delta method, independence from vanishing block-size imbalance in covariance, a continuous-mapping and portmanteau argument, and Chebyshev for the outer regime. These are not purportedly proven by random samples, numerical integrals or finite exhaustive checks. The announced theorem has not received independent mathematical validation.
