---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The centered independent Poisson/Gaussian specification has variance one exactly. Expanding its cumulant-generating function gives M(t)=1+sum_{n≥1}2[p+(1-p)(-b)^n]t^n/(n+2)!, with optimal right scale c=max(0,sup_{t>0}(1-1/M(t))/t). Its local coefficient m=[p-(1-p)b]/3 and sign of a_2-m^2 produce the explicit upper quadratic root p_*(b). For p≥p_*, positive coefficients obey a_(n+1)/a_n≤m via the uniform ratio bound; geometric-series domination proves global c=m, with strict inequality for positive t at the boundary. Below p_* the local derivative or positive upper jump forces a strict finite positive maximizer. Analytic implicit-function and a strict compact-away-from-zero gap prove local uniqueness and quadratic crossover; the rare-p asymptotic follows by splitting t at (1-eps)log(1/p) and testing t=log(1/p)+3loglog(1/p). Independently evaluated the MGF and variational profile on both sides of p_* for three b values (six phase tests); the b=0 coefficients evaluate exactly to 3/4,40/3,5/9. Fixed b<1 and only right variance-exact subgamma, not left-tail or b=1 new claim.

## originality

PASS

Best-of-knowledge PASS for the unequal-amplitude b∈[0,1) explicit surface and its quadratic crossover, not for the general signed remainder variational identity or equal-jump Skellam endpoint b=1. Chen–Wang 2026 publicly states the latter and rare-jump first order, and Chen 2026 treats general spectrally positive laws with an implicit M-class local-control test. The specialized explicit p_*(b), unique near-critical optimizer and coefficients are not stated in the inspected full Chen paper or the accessible Chen–Wang abstract. Chen–Wang complete text was inaccessible after lawful open-access attempt and Oxford connection returned vpn_disconnected, a genuine priority risk, not proof of novelty.

## value

PASS

Optimizing a variance-fixed exponential tail scale is a natural concentration invariant not determined by skewness alone. The explicit unequal-positive/negative jump parameter surface, the Gaussian-smoothing endpoint and quadratic onset locate a genuine transition between local cumulant and global MGF control; the rare-positive-jump exponent connects this phase picture to extreme-event domination. These exact natural boundaries go beyond restating a general variational formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
