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

A pentagon vertex interior tangent cone has opening 3π/5; five evenly spaced inward bisectors at angular gaps 2π/5 imply a real planar direction illuminates at most two cyclically adjacent vertices and every adjacent pair is attainable with strict inequalities. Product tangent cones factor, so every product direction is contained in one of exactly 25 cyclic 2×2 tiles; this is a theorem about ALL real directions, not a finite-direction assumption. Each of five rows of the 5×5 vertex grid needs three covering tiles, while every tile intersects two rows: 2N≥15 gives N≥8. Independently checked the specified 8 tiles cover all 25 cells with exact row multiplicities and are realizable. Every vertex is contained in four tiles, so uniform weight 1/4 on all 25 achieves fractional 25/4; dual vertex summation 25≤4W gives optimality. Vertex illumination implies boundary illumination via active facet inclusion. Exact geometry plus combinatorial certificates prove all pentagon side lengths; finite tile checks alone would not prove the geometry.

## originality

PASS

Naszódi defines fractional illumination; Sriamorn covers polygon multiple illumination and hence I(pentagon)=3; Resultary publishes 5/2 fractional illumination for equiangular planar pentagons and an exact theorem for products of simplices. None of those inspected statements implies 8 (vs 9) for the non-simplex four-dimensional Cartesian product or its 25/4 fractional optimum. Cyclic torus tile covering may exist separately in design theory, recorded as risk.

## value

PASS

Strict nonmultiplicativity on a natural product family and the exact integral/fractional gap are motivated basic illumination invariants, with sharp unrestricted-direction proof and useful product-geometry counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
