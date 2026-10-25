---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For overlapping Poisson windows with shared intensity rho=lambda*A_(1-h)(t), the bivariate factorial generating function exp(lambda(z+w)+rho zw) gives Cov((S(t))_2,(S(t+h))_2)=4lambda²rho+2rho². The unit-period integrals B_j depend only on Poisson increments in (j-1,j+1], making a strictly stationary 1-dependent sequence with finite moments, so the standard m-dependent CLT applies. Integrating covariance over period and separation yields V=4lambda³+4lambda² integral_0^1int_0^1 A_L². Parseval gives integral A_L²=L²+sum_{k!=0}|etahat(k)|² sin²(pi*k*L)/(pi²k²), whose L integration yields the stated spectral penalty. Lower equality iff all nonzero Fourier modes vanish; positive arc masses give strict upper V<4lambda³+2lambda², while smooth approximate delta pulses approach it. The linear-count variance uses only first overlap moment and is lambda. Independent 2D trapezoidal quadrature of overlap masses agreed with the harmonic spectral formula within 6e-6 on three modulation/lambda cases.

## originality

PASS

Best-of-knowledge distinct final theorem after comparison of equivalent objects, broader implications and exact accessible primary statements; not a historical priority guarantee. Identical Poisson marginals alone do not imply equal asymptotic variance for overlapping-window nonlinear statistics. Classical covariance/CLT formulas must be combined with periodic overlap Fourier analysis and extremizer argument, not stated in the motivating paper.

## value

PASS

A practical natural uncertainty question: all periodic intensities have identical one-time Poisson target, yet nonlinear physical-time pair-count sampling incurs an exact nonnegative frequency penalty. Unique uniform optimum, sharp unattained worst case and a contrast with the unchanged linear estimator provide an explicit design theorem, not just a CLT corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
