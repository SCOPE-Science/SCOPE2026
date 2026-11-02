---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For n>=5 independent unit-rate exponential circular gaps E_i and T=sum E_i, Dirichlet normalization makes the reciprocal-pair count R=sum 1{E_i < E_(i-1), E_i < E_(i+1)} and directed length L=(sum min(E_(i-1),E_i))/T. T is independent of both R and L. The four nonzero indicator/minimum overlap covariances per i are two -1/18 and two +1/24; other pairs use disjoint exponentials, giving Cov(R,Q)=-n/36 and Cov(R,L)=-1/36. Adjacent local minima are mutually exclusive and distance-two joint probability 2/15, yielding VarR=2n/45. Each minimum of two exponentials has mean 1/2, variance 1/4, adjacent minimum covariance 1/12; using T Gamma(n,1) yields EL=1/2 and VarL=1/[6(n+1)]. These imply the claimed correlation -sqrt(15)/12 * sqrt((n+1)/n). Independent exact rational gap-order enumeration over all 5!,6!,7!,8! permutations checks all moments, not extrapolated as proof.

## originality

PASS

Reflexive/mutual pair counts, weak component counts, and local minima are aliases; Bahadır–Ceyhan give separate reciprocal-count moments for interval samples. Penrose–Wade give total nearest-neighbor length results on intervals and online graph processes. Wilsher–Dettmann–Ganesh examine a probabilistic soft-geometric graph on a circle, not deterministic nearest neighbor links. Even exact knowledge of both marginal laws does not determine the mixed covariance. A fresh Resultary query did not surface this exact joint observable, though a broader stabilization covariance theorem or older stochastic geometry tables remain a residual risk.

## value

PASS

Reciprocal pairs equal connected components, and directed total length measures network wiring cost. Their exact negative covariance independent of n and nonzero limiting correlation are intrinsic, quantitatively useful dependency facts for circular stochastic geometric graphs, rather than a recomputation of known marginals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
