---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Invariant affine hyperplane measure restricted to those intersecting a simplex gives normal density proportional to width and conditional offset Lebesgue uniform. The k-th offset interval is the gap of consecutive vertex projections, so P(K=k) is ratio of expected gaps to expected range. Projecting standard Gaussians onto the zero-sum subspace gives direction independent of radius and the same ratio of ordinary Gaussian spacings. Integrating the event #{G_i<=s}=k gives binomial integral. Each crossed simplex edge yields a section vertex, giving K(N-K); the barycentric rescaling preserves the entire face lattice of Δ_(K-1)×Δ_(N-K-1). Summation of pairwise Gaussian absolute differences gives E V=N(N-1)/(sqrt(pi) M_N). Gaussian maxima M_N~2sqrt(2log N), and the width-normalized auxiliary Gaussian level S/sqrt(2log N) tends to Uniform[-1,1]. For each compact interior level z the smaller binomial count has log exponent 1-z² by Mills and Chernoff bounds; boundaries have vanishing probability. Thus log V/log N ⇒2-U², and V/E V→0 since the limit has no mass at exponent 2.

## originality

PASS

Best-of-knowledge PASS with a concrete recent-slicing full-text access risk. The studied invariant affine Crofton hyperplane distribution differs from central Haar sections and uniform-normal-then-offset sampling; known Gaussian-simplex identities are acknowledged as input but do not yield the stated continuous exponent without the spacing/level analysis.

## value

PASS

The invariant Crofton cut is a natural canonical sampling law on a regular simplex. An exact finite-N face-lattice/vertex-count law paired with an unusual continuous log-exponent limit and failure of mean normalization is a substantive geometric probability distinction, not an arbitrary parametric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
