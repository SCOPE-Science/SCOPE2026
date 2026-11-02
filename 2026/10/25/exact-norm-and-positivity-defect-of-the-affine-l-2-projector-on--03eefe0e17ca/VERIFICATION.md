---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Normalized Hausdorff measure on ∂B_1^d decomposes into 2^d congruent facets: Y_i=epsilon_i U_i with independent symmetric signs and U distributed uniformly on the simplex (Dirichlet(1,...,1)). E Y_i^2=2/[d(d+1)] and cross moments vanish, giving kernel K(x,y)=1+[d(d+1)/2] x·y. The row L1 norm Phi(x)=E|K(x,Y)| is convex on B_1^d, so one of ±coordinate vertices attains its maximum. At a vertex, U_1 has Beta(1,d-1) density and averaging over sign gives max(1,c U_1). Integrating exactly yields 1+[(d-1)(d+2)/(2d)](1-2/[d(d+1)])^(d-1). Since every kernel row integrates to 1, max negative mass is exactly (norm-1)/2. For d=1 the two-point affine projector is identity. Independent symbolic integration agreed for d=2..9, but the convexity/integration proof is dimension-free.

## originality

PASS

Known sharp simplex local projector and broad smooth-manifold L∞ stability theorems have different measures/domains and do not entail this cross-polytope-boundary exact Dirichlet marginal constant. No equivalent cross-polytope Hausdorff-boundary formula identified by targeted primary and published-record inspection. Priority is best-of-knowledge.

## value

PASS

The cross-polytope boundary with Euclidean Hausdorff measure is a canonical polyhedral test geometry for affine least-squares approximation. Its exact L∞ amplification and loss-of-positivity constant grow linearly with dimension, a nontrivial quantitative stability calculation that can be independently reused; it is neither an arbitrary finite slice nor a generalization to unstudied measures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
