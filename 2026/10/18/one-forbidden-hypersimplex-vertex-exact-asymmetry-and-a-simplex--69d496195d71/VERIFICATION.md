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

The one-vertex-deleted hypersimplex equals the full Δ_{n,k} intersected with x(H)<=k-1: every exchanged-basis edge crosses that integral hyperplane only at an original surviving vertex. For k,l>=3, reflected containment is exactly 1<=z_i<=(s), z([n])=k(s+1), z(H)<=s(k-1)+max(0,k-l), where z=(s+1)c. The four coordinate/block-sum obstructions give s=max{M/m,m/(m-1)} (m=min(k,l),M=max(k,l)). Saturation uniquely fixes z all 1 or all s for gap>=2; balanced gives blockwise 1/s unique; gap-one leaves a capped (m+1)-coordinate residual simplex of dimension m, yielding the proposed complete center locus. Independent exact-rational reflection checks over all surviving basis vertices for k,l=(3,3),(3,4),(4,3),(3,5),(5,3),(4,5),(5,5), including affine simplex barycenters; all satisfy inequalities. These finite tests supplement the all-parameter halfspace proof.

## originality

PASS

Rank-two and corank-two matroid base-polytope Minkowski-center classification is preexisting and correctly excluded (k,l>=3). Generic robust LP for Minkowski centers could compute instances, and circuit-hyperplane split sources describe the vertex deletion geometry, but the exact all-(k,l) asymmetry jump and transition to a full m-simplex of minimizing centers is not stated by them. Best-of-knowledge structural specialization distinct from mere software LP output.

## value

PASS

Single-basis deletion of a uniform matroid is a natural extremal perturbation of a hypersimplex. Discovering the exact conditions for zero symmetry loss and that nonunique optimizing centers form a whole m-simplex at rank/corank gap one is a motivated, complete polyhedral-geometric classification with exact parameter boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
