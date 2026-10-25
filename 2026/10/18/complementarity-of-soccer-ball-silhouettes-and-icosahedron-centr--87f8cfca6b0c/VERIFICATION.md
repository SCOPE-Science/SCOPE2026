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

The original icosahedron has 12 vertices, 30 edges, 20 triangles; its regular one-third truncation has 60 vertices and 90 facet-adjacency edges. On a generic direction an edge is on the projection silhouette exactly if incident outward facet normals have opposite signs; central I section vertices count old edges with opposite endpoint signs. Each regular hexagonal facet has three opposite pairs of edges; on its facet-normal wall exactly three adjacent facet signs face each way, so crossing those additional walls leaves N_T unchanged. Original opposite vertex normals induce six great circles with no triple crossings: 32 regions. Inspected exact Z[sqrt5] program establishes one representative of each 32 sign masks: 12 give shadow/section (20,10), 20 give (18,12). Thus N_T+S_I=30 throughout all generic chambers, beyond random samples. Independently rebuilt actual 60 coordinates, projected in 600 pseudorandom directions and computed convex hulls and central edge crossings: all complementary; this is corroboration only. Previously known spherical chamber area 20(3θ−π) yields exact probabilities and mean.

## originality

PASS

Full prior section-probability RESULT.md supplies the central I law as a used input, not a silhouette law for T. QFBox lists special truncated-icosahedron projections including 18 and 20 vertices, but not all generic directions or their pointwise complementarity. Koca et al. construct T, not its shadow distribution. No identified prior implying the cross-polytope identity; fullerene stereology priority is a risk.

## value

PASS

The icosahedron/truncated-icosahedron pair are canonical dual-related polyhedra. An all-direction combinatorial identity linking two distinct geometric operations and exact Haar silhouette probabilities is an intrinsic, testable geometry fact not a mere re-report of previously known section areas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
