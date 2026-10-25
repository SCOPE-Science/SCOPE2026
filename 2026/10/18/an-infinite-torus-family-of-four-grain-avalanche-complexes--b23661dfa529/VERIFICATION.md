---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For out-degree-one synchronous firing on directed C_n, the four 0/1 chips at {0,1,d,d+1} translate by one step, yielding precisely n facets F_i={i,i+1,i+d,i+d+1}. For d≥3 and n≥2d+5, cyclic steps 1,d−1,d,d+1 are unoriented distinct; each unique (d+1)-diagonal is free in its tetrahedron, giving n free-triangle/tetrahedron collapses, then exactly n free-edge/triangle collapses. Residual triangles A_i={i,i+1,i+d}, B_i={i+1,i+d,i+d+1} have face vector (n,3n,2n); the quotient of plane-triangulated Z² by kernel(a+db mod n) is a nonsingular oriented torus, with each edge exactly twice and 6-cycle vertex links. Cup product on H1 of T² is nonzero, ruling out wedge-of-spheres. Independently rebuilt all firing facets and all 2n free-face deletions for 190 (d,n) cases (3≤d≤12, 2d+5≤n≤2d+23) and checked residual torus combinatorics. The proof for all allowed integers is the universal cyclic-step and lattice argument, not finite tests.

## originality

PASS

A best-of-knowledge comparison of specific mathematical implications and exact model/normalization found no identified earlier theorem proving this new claimed part. Previously published overlapping objects, numerical invariants and limitations are credited. The four explicit checks, primary-source inspections and risk list below bound this assessment. Knowing a torus target or a nonwedge existence question cannot imply this particular four-chip complex collapses to it. Known three-chip families have different supporting configurations; this answers the structural existence question with an explicit all-parameter construction.

## value

PASS

This uniform two-parameter family directly answers the previously posed existence of an avalanche complex not homotopy equivalent to any wedge of spheres, using the nonzero integral H1 cup product of its torus target. The explicit 2n elementary collapses explain the dynamical-topological mechanism and are stronger than a finite Betti computation or merely rediscovering a known torus triangulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
