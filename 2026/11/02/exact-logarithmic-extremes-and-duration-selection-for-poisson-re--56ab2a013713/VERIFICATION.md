---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Scaling of independent renewed excursions gives A=T^(1+beta/2)Y, with Y=sqrt(2K) integral_0^1 |B(u^beta)|du. Gaussian signed-area lower tail and Borell supremum upper tail give log P(Y>y) ~ -y²/(2v), v=4K/((beta+1)(beta+2)); positivity of covariance ensures this is maximal variance. Integrating over Exp(r) durations at t=x^[2/(beta+3)]u yields strict convex cost h(u)=ru+(2v u^(beta+2))^-1. Its unique minimum gives sharp cycle tail and the conditional winning-duration localization via constrained Laplace bounds. Independence of cycle marks gives maxima; exponential order statistics give the longest interval, and a renewal-count sandwich covers physical time without including the final incomplete interval. Independent exact kernel integration and saddle algebra checked beta=1/2,1,3/2, including Brownian 3/8 and duration 3/4. The finite checks do not prove the large-deviation limits; the Gaussian concentration and localized saddle argument do.

## originality

PASS

Méndez–Cristín (2026) Section VI supplies the general renewal-cycle maximum CDF and heavy-tail reset asymptotics, so generic max-CDF machinery is PRIOR. Its Poisson part treats aggregate-area moments/ergodicity; the relevant full-text sections do not give the exact Poisson one-cycle Weibull tail and joint selected-duration fraction m/(m+1). General Gaussian-extreme/laplace principles are also prior and used. The combined marked-cycle theorem is best-of-knowledge distinct; possible stronger general marked-renewal statements remain.

## value

PASS

The joint rare-event geometry of reset area and reset duration is a natural observable in stochastic renewal extremes. The exact sharp tail exponent and constant, asymptotic winning-duration fraction and strict mismatch with longest waiting time are quantitative facts not supplied by generic cumulative-area moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
