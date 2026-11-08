---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

In the two-sided stationary Poisson renewal model, backward excursion age A~Exp(r) is independent of the event of no reset across lag t, contributing factor e^{-rt}. Conditional on no reset, (X0,Xt) is centered bivariate Gaussian with variances 2K A^beta and 2K(A+t)^beta and correlation (A/(A+t))^{beta/2}. The folded-Gaussian absolute bivariate moment gives exactly the displayed covariance as age-covariance plus a strictly positive within-excursion h(q) term. For b=beta/2 in (0,1), concavity and exponential moments justify dominated convergence: the first term scales b^2 Gamma(1+b) r^{-1-b} t^{b-1}, and the h(q) term scales Gamma(1+3b) r^{-3b} t^{-b}/2. The powers cross at beta=1, yielding the three stated strictly positive coefficients and Brownian contributions 1/4 age and 3/4 within excursion. Bounded independent quadrature at beta 0.6,1,1.4 agreed in sign and normalized asymptotics, but analytic dominated-convergence supplies infinite-t proof.

## originality

PASS

Taźbierski, Metzler and Magdziarz (2025) already treat complete/incomplete resetting with a broad two-time positional law and an explicit signed-coordinate scaled-Brownian autocovariance. That law allows the nonlinear modulus observable to be integrated but is not itself the explicit folded-Gaussian stationary covariance, its two competing algebraic powers, or the beta=1 coefficient partition. Méndez and Cristín (2026) analyze integrated absolute area, not instantaneous lag covariance, based on accessible abstract material only. Stojkoski et al. (2022) consider ordinary Brownian resetting autocorrelations. The incremental claim is the evaluated exact modulus law and asymptotic crossover; possibility of an uninspected specialty derivation remains.

## value

PASS

The modulus is a natural measured observable of motion: unlike signed displacement it retains age-memory under reset. The exact switch in dominant physical mechanisms at beta=1 and the split of the Brownian leading constant quantify two distinct sources of long-lag correlations, a motivated nontrivial stationary stochastic-process asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
