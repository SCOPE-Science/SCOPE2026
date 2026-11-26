---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The stated radius-two vertex model spans R⁴ and is centrally symmetric with the origin in its interior, so every nonzero normal gives a full three-dimensional central section. An exact reconstruction verified that the four stated simple reflections preserve the 120 vertices, their root rows are independent, and every vertex has simple-root coefficients all nonnegative or all nonpositive. This gives coverage even without invoking a chamber theorem: the reflection group is finite because it permutes a spanning set; in each orbit maximize the dot product with the sum of the dual basis vectors. A negative simple-root dot product would be strictly improved by reflection. Inside the resulting chamber the sign pattern depends only on which of the four simple dot products are positive, and all 15 nonempty supports occur by using sums of dual basis vectors. Independently rebuilt the 720 original edges and 600 tetrahedral cliques by field arithmetic. Each clique is exposed by the sum of its vertices (4+6φ on the clique versus at most 8φ off it), and the conventional 600-cell facet count gives exhaustion. Each section vertex is an old zero vertex or an interior crossing of an edge, and the two-dimensional intersections with tetrahedral facets are triangles or quadrilaterals; duplicates on original ridges must be identified. I computed section edges as intersections of distinct section facets with two common vertices. This reproduced every row, 11 distinct inventories, the 42–144 vertex bounds, and the generic (144,360,218) vector with 152 triangles and 66 quadrilaterals. Every non-interior support has old zero vertices, so the stated definition of generic is exact. Replay: python3 -B /workspace/branches/independent-checks/record2.py. Scope is face inventories of central sections, not face lattices of arbitrary affine sections.

## originality

PASS

Best of current knowledge: classical H₄ structure and selected 600-cell sections are precedents, but the inspected sources do not cover the complete central all-normal face inventory or its sharp extrema.

## value

PASS

Central sections of an exceptional regular polytope are natural objects and their inventories describe the complexity and polygonal structure of the section. The full census distinguishes singular normals that have the same vertex count but different edge and facet inventories, and establishes attainable sharp ranges and a generic baseline. Neither the generic row alone nor the known chamber structure resolves these questions. The result is useful as exact data without claiming a classification of section isomorphism types.

The dated certificate retains the supplied scientific assessment, sources and limitations.
