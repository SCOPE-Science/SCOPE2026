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
# Reproducibility and proof checks

Run `python verify.py` with NumPy and SciPy. On four distinct strictly subquadratic exponents, its reproducible implicit discretization tested 430,080 scalar analogues of both exact pathwise inequalities with zero observed excess beyond numerical tolerance. It also compares four Gaussian log-tail ratios with the known normal constant and checks the exponential-age mixture algebra at five quantiles. No Monte Carlo estimate is used as evidence for the limiting distribution.

The infinite-particle conclusion follows analytically from the deterministic last-zero comparison, the reflection-principle error tail with exponent \(2/(\alpha-1)>2\), Gaussian fixed-age large deviations, conditional maximum convergence, and bounded convergence over an independent exponential reset age. Reproduction requires no stored stochastic trajectory data. Finite tests cannot certify asymptotic tails, guarantee novelty, or replace the mathematical proof.

Independent audit: not performed.
