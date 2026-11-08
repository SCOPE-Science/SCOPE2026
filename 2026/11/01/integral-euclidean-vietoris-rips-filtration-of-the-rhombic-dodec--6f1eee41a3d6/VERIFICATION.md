---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Coordinates are exactly six ±2e_i and eight (±1,±1,±1), Euclidean inclusive thresholds; squared pair distances 3,4,8,11,12,16 with no other changes. At q=3 the rhombic dodecahedron one-skeleton has 14 vertices/24 edges and wedge11 circles. At q=4 the added 12 cube edges triangulate its 12 rhombi to a connected closed 2-manifold of Euler characteristic two, S2. For q=8, independently regenerated all 240 flag faces from actual coordinates and replayed all 80 recorded certificate pairs, verifying at each step present faces, codimension-one and exactly one coface; the remaining 80 faces are the induced complex on eight cube corners, whose complement four antipodal edges makes the join of 4 copies of S0 = S3. At q=11 seven missing edges are a perfect matching on 14 vertices giving (S0)^{*7}=S6. At q=12 each cube corner becomes a cone apex. Homology dimensions are separated at adjacent stages, giving the asserted complete reduced integral barcodes.

## originality

PASS

Checked actual theorems and their implications, original sources and relevant published exact results, including already-known special cases; none of those inspected entails the full target claim, subject to the explicit best-of-knowledge residual risks. This does not infer novelty from a failed search.

## value

PASS

The rhombic dodecahedron is a canonical Catalan solid with two distinct vertex orbit geometries. The exact entire Euclidean filtration and 80-step collapse prove an independently meaningful natural polyhedral invariant, extending the eight-corner cube subcase. Different noncontractible dimensions 2,3,6 are non-obvious and useful as a finite topological benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
