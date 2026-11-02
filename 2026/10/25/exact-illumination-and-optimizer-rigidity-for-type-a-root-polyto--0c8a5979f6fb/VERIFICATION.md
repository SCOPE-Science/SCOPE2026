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

For every m>=3, root polytope R_m=Delta_(m-1)-Delta_(m-1)={x:sum x_i=0, sum |x_i|<=2}. For u in H_m with positive mass T and a_i=(-u_i)^+, b_j=(u_j)^+, the exact one-sided derivative at root e_i-e_j gives illumination iff a_i+b_j>T; derivative zero stays on boundary locally and cannot enter later by convexity. Two illuminated edges with distinct source and target contradict total masses, so every illuminated vertex set is a directed star of size <=m-1. Equality forces one sign on the unique star center and all other coordinates of opposite strict sign, giving the full outgoing/incoming stars. Vertex counting yields both I and finite-direction I* >=m; m outgoing stars illuminate all vertices and hence every boundary point by active supporting-facet inclusion. At fractional optimum all positively weighted directions are full stars and each vertex receives exactly one unit, so alpha_i+beta_j=1 for i!=j, forcing alpha_i=theta, beta_j=1-theta. Ordinary m-unit covers require theta in {0,1}. Independent exact integer-grid probes m=3..5 corroborate the star bound; proof is analytic for all m.

## originality

PASS

Best-of-knowledge PASS for the complete all-m optimizer family, not for existing planar and cuboctahedral special cases. The published fractional-illumination definition and general inequality do not yield the exact directed-star incidence or theta rigidity.

## value

PASS

The type-A root polytope is a canonical simplex difference body. Exact fractional AND ordinary illumination, plus a full one-dimensional optimizer-face classification and global rigidity in every dimension, constitute structural knowledge far beyond the already-known low-dimensional hexagon/cuboctahedron values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
