---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Conditional positive-composition law follows since every internal gap composition at span r has exactly N-r left-endpoint placements. From (1,...,1), the transition g→g+e_i with probability g_i/r yields target uniform composition because sum_i(h_i-1)=r+1-m. Conditional E[(g_i+1_i)/(r+1)|g]=g_i/r gives the simultaneous vector martingale; absolute gaps cannot decrease. Jensen plus independent-copy covariance identity establishes opposite signed associations and strict boundaries for k≥3 and N>k. Independent exact rational enumeration tested all k,N through N=9, conditional moments, transition distribution and covariance formulas; no finite-experiment leap is used.

## originality

PASS

Kochar–Korwar 2001 already supplies sampling-without-replacement spacings and pairwise dependence; the Pólya and convex-order mechanisms are classical, and Calabrese 2012/2013 proves a related Pólya convex-order result with a different comparison parameter (replacement count at fixed draws). Their inspected statements do not assert the joint span-conditioned coordinate/normalized orders or exact span covariances. A general stochastic-order theorem could imply these after specialization; residual priority risk is explicit.

## value

PASS

The natural, statistically interpretable span, adjacency, and relative concentration statistics exhibit a provably opposing clustering order for all finite grid and sample sizes; the simultaneous coupling yields a family of inequalities, not a renamed identity. Precise negative adjacency covariance gives a finite-sample calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
