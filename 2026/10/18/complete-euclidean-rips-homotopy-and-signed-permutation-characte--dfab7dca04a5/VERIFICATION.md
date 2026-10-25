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

From the fourteen coordinates all 91 pairwise squared distances have shells 3:24,4:12,8:24,11:24,12:4,16:3. Below sqrt3 the complex is discrete; at sqrt3 a connected 14-vertex/24-edge bipartite graph has first Betti 11. At r=2 the maximal triangles triangulate the twelve rhombic facets of the convex dodecahedral boundary, giving S2. At squared scale 8 the cube-induced subcomplex is the join of four antipodal 0-spheres, hence S3. For each nonempty compatible axis subset, its cube neighbors form a simplex; pairing each axis-containing face according to a distinguished compatible cube vertex gives acyclic relative matching; an explicit independently found sequence of 80 elementary free-face deletions confirms a genuine collapse to the cube S3 (not merely Betti agreement). At squared 11 all and only the seven antipodal pairs are forbidden so (S0)^*7=S6, while at squared 12 every cube vertex spans a simplex join factor and the complex contracts despite three absent axis-antipodal edges; sqrt16 adds no homology. Each positive homology degree appears in one interval only. G=signed permutations acts on S2 with determinant, on cube S3 with sign of permutation of four antipodal body diagonals, and on S6 via product; H1 of the graph has trace 1+pointwise-fixed-edges-fixed-vertices. Independently enumerated all thresholds with clique face totals 38,74,240,2186,6911,16383 and checked 80 sequential free-face collapses, complementing source certificate. No unsupported inference from finite samples: object itself is finite and geometric identifications prove integral types.

## originality

PASS

Best-of-knowledge new exact Euclidean fourteen-point Rips filtration and its full octahedral characters. Saleh–Titz Mite–Witzel work classifies Platonic vertex sets, notably a dodecahedron with 20 vertices; the rhombic dodecahedron is a distinct 14-vertex Catalan solid. The earlier Resultary cuboctahedron computation involves its 12 vertices (dual polytope, not equal Euclidean metric on fourteen rhombic vertices), different critical shells. General antipodal-pair joins cover S6-like endpoints, but not the scale sqrt8 all-vertex collapse or complete characters.

## value

PASS

A complete integral metric-persistence classification including a nontrivial certified relative collapse and full symmetry representation for a natural Catalan-solid vertex sample is a meaningful finite topology invariant. Its S2→S3→S6 transitions are not read off from the convex surface alone; the 80-pair collapse identifies the nonobvious intermediate stage and its equivariant orientation. This exact fact is reusable for finite Rips benchmarks and polyhedral comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
