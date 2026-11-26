---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Every disconnected graph on five vertices is a subgraph of a spanning K₄+K₁ or K₃+K₂. Each has exactly three two-edge matchings, and removal of any edge destroys one, proving the equality support. For nonnegative p, the expected number of two-edge matchings is the sum of 15 marginal products, at least 15p² by matching independence; for p<0 the claimed upper bound is trivial. At the boundary every product and then every marginal is tight. Equating perfect matching products on four vertices implies b_uv+b_wx=b_uw+b_vx=b_ux+b_vw. The first three labels define t₁,t₂,t₃ from their three pair values; the identities then determine b_uv=t_u+t_v for all pairs. With S=Σt_v, the mass a_z=1/5−S+t_z and the marginal on uv is 3/5−2(t_u+t_v), so equality of marginals forces constant t. The resulting masses are positive, sum to one over the fifteen states, and have the requisite disjoint-edge probabilities. For full independence only sizes 2+2 and 2+3 are nontrivial. For a triple the triangle has probability b+2a, with joint probability b for the complementary edge; b=p⋆(b+2a). The other three triple outcomes are equiprobable single edges even conditional on that edge's indicator, by the now-proved symmetry. No exchangeability was assumed in deducing the law.

## originality

PASS

The stronger-class threshold, explicit fifteen-state construction, exact masses, and subgraph independence of that construction are known. The pass is for the matching-independent upper bound on five vertices and the uniqueness argument in that weaker class, which also shows that every disconnected matching-independent boundary law is automatically subgraph independent. The strongest inspected results neither prove the weak-class upper bound at this value nor classify nonsymmetric equality laws.

## value

PASS

The five-vertex case sharply separates what must be proved from pairwise disjoint-edge constraints from what is given by stronger independence assumptions. An exact boundary law resolves the gap at this order and gives a concrete rigidity result: the weaker class has no additional disconnected boundary laws. The matching-count witness and the nonsymmetric uniqueness step supply a meaningful finite benchmark, not just another numerical construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
