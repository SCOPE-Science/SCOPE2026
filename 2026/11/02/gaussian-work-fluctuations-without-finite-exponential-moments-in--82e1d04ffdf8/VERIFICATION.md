---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For stationary two-state symmetric rate-q on/off harmonic diffusion, the stationarity equations yield a=E[X^2 1_{S=0}]=D/k+D/q and b=E[X^2 1_{S=1}]=D/k. The work jump compensator is g=qk(1-2S)X^2/2, mean c=kD/2. The exact Poisson corrector h_0=kX^2/2,h_1=-kD/(2q) satisfies Lh=c-g; the corrected work M=W-cT+h(T)-h(0) has jump magnitude kD/(2q), continuous bracket 2Dk^2 integral_0^T X_t^2 1_{off} dt and switch bracket k^2 D^2 T/(4q). Stationary ergodicity gives sigma^2=2D^2k+9D^2k^2/(4q); bounded jumps and finite fourth moments justify the martingale CLT and exact variance-rate limit. The conditional position MGF equals exp(Du^2/(2k))*(1-Du^2/q)^(-q/(2k)-1+S), finite only |u|<sqrt(q/D), thus E exp(cX^2|S=s)=infinity for every c>0. Exactly one off-to-on switch yields E exp(theta W)=infinity for theta>0, and one on-to-off for theta<0 using Jensen, for EVERY finite T>0. Polynomial moments finite via gamma tails and finite Poisson switches. Independently checked rational generator and variance for parameter pairs (3/2,5/3,7/4) and (1,1,1) including 17/4 at unit parameters. No numerical CLT inference.

## originality

PASS

Frydel 2024 derives the same fluctuating harmonic stationary distribution and rate-independent average energetics, explicitly credited. Frydel 2026 studies more general waiting-time switching and mean injected power, but its available article statements do not include this Poisson accumulated-work variance and two-sided non-Cramér obstruction. Pal/Sabhapandit 2013 moves the trap center, a different observable/model. Generic martingale machinery alone does not supply the exact model coefficient. Qualified originality, potential unpublished work-current computations remain.

## value

PASS

A natural stochastic-thermodynamics work current has a completely explicit mean, Gaussian central limit and variance rate despite lacking every nonzero finite-horizon exponential tilt. This sharp contrast limits standard generating-function/large-deviation methods and quantifies the dependence on switching rate q.

The dated certificate retains the supplied scientific assessment, sources and limitations.
