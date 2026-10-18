---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For uniform iid n-coupon draws, B in {2,...,n+1}. For B=b<=n, exactly b-1 distinct coupons seen; from time b complete coverage adds independent geometric waits G_k for k=b-1..n-1. Therefore E[T|B=b]=b+nH_(n-b+1), while the boundary B=n+1 means T=n. Common coupled geometric G_k yield nonincreasing first-order stochastic order with strict comparisons, and K=first initial run of G_k=1 yields Cov(B,T)=-sum_{j=2}^n S_{n,j}sum_{k<j}k/(n-k)<0, including n=2 negative 1/2. Birthday survival bound leads B/sqrt n=>Rayleigh R; quadratic-regression asymptotic m(B)-nH_n=1-B²/(2n)+o_L²(1), giving Cov/sqrt n->-sqrt(pi/8) and n*Corr->-sqrt(3/[2pi(4-pi)]) via coupon-collector variance pi²n²/6. Independent exact rational prefix enumeration n=2..5 checked conditional laws and covariance, with n=3 -8/9, n=4 -37/32 and n=5 -844/625; nonasymptotic proof not finite enumeration.

## originality

PASS

Flajolet–Gardy–Thimonier 1992 full paper sections 3/4 analyze birthday collision and coupon collection separately through language generating functions, but neither there nor Anceaume–Busnel–Sericola 2014 marginal generalized-collector results state the joint conditional stochastic ordering, exact mixed covariance and n*correlation constant. Myers–Wilf 2003 study variants/singletons, not this pair. Published Resultary semantic searches returned missing-mass and reset-coupon findings rather than dominating paired-stopping-time laws. Holst 1986 broad urn treatise is plausible but unavailable for full-text reading because Oxford auth returned vpn_disconnected; recorded material-access risk does not alone force originality failure. No prior implication sufficiently established.

## value

PASS

First birthday collision and complete coupon collection are canonical stopping times at sqrt(n) and n log n scales. An exact strictly negative joint regression with full stochastic order, finite covariance and nontrivial Rayleigh quadratic regression shape quantifies their dependence on the SAME draws; not reducible to known marginals or trivial finite tabulation. The exact 1/n Pearson correlation coefficient is a natural cross-scale invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
