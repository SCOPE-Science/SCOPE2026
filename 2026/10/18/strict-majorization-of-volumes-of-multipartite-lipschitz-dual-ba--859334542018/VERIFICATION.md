---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Reconstructed the anchored minimum-coordinate decomposition: spread r<=1 contributes N; spread r>1 forces extremal pair within one part and contributes n_i(n_i-1) integral_1^t r^(n_i-2)(2-r)^(N-n_i)dr. Endpoint beta/binomial calculation yields finite binomial tails. For fixed N the integrand second discrete difference is r^(s-3)(2-r)^(N-s-1)[2u^2+4s u d+s(s+1)d^2] with u=2-r and d=2(r-1), strictly positive for 1<r<t, proving transfer-majorization. Dominated convergence for balanced k>=3, central binomial asymptotics at k=2, and concentrated endpoint expansion give all growth regimes. Independently counted Ehrhart lattice points and recovered six exact n=4 anchored volumes, including fractional t.

## originality

PASS

The complete two-level signed-chain polytope of Resultary record 84c1d3d87a65 is exactly the rooted K_{1,p,q} endpoint t=2 subcase, including a strict imbalance law; this substantial known part is expressly excluded from novelty. The wider k-partite continuous-t integral and all-part majorization go beyond that two-parameter endpoint. Prior Alexander et al. equilateral volume, Higashitani et al. facets, and a more recent interpolated metric facet census concern other invariants. No general dominating dual-volume statement located, but priority risk remains.

## value

PASS

An infinite family of nontrivial metric dual bodies receives a natural exact volume functional, a sharp majorization extremal principle, and distinctly scaled k=2 versus k>=3 balanced growth; valuable for finite-dimensional Lipschitz-free and symmetric-edge polarity geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
