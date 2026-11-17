---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Gaussian change of measure gives h_s(u)=sqrt(s)exp((1-s)Phi^-1(u)^2/2)1_{u>=Phi(z/sqrt s)}. Mills ratio gives near-endpoint v^{-beta}(log(1/v))^{-beta/2} with beta=1-s, and interval-by-interval centering yields an L1-convergent endpoint sum; for beta<1/2 the proof extends L2 for the variance series. The first interval has the stated Pareto tail while the other centered intervals are uniformly bounded by a summable oscillation bound. At p beta=1 the remaining (log)^{-1/2} singularity causes divergence. For s>=1, only the indicator jump cell has nonvanishing n-scaled variance, and its Bernoulli phase follows exactly; smooth-cell oscillations vanish. Independent exact Gaussian cell moment computation verified all tested s=1 Bernoulli phases and s>1 asymptotic phases, not the limit distribution itself.

## originality

PASS

Published general randomized quasi-Monte Carlo importance-sampling and singularity papers provide broad rate and boundary-growth bounds. They do not, in inspected material, determine the exact heavy-tail limiting series and Pareto coefficient for the one-point-per-quantile-stratum Gaussian tail indicator, nor the s>=1 arithmetic jump-cell Bernoulli law. The nearby published Gaussian quadratic-moment result has a smooth integrand and a distinct critical proposal regime. Best-knowledge novelty passes with a genuine specialist-literature priority risk.

## value

PASS

Gaussian one-sided rare-event integration with equal-probability proposal strata is a canonical numerical-estimation problem. The exact transition between infinite variance/heavy-tailed endpoint errors and threshold-driven arithmetic Bernoulli errors guides meaningful proposal-risk interpretation, with sharp constants, not a routine renaming or tiny computational observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
