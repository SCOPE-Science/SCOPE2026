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

PASS: Rectification of the standard 12-vertex icosahedron gives 30 edge-midpoint vertices with 12 pentagonal and 20 triangular facets. To illuminate edge midpoint ab, a direction has strictly negative dot product with the two pentagon normals a,b, hence illuminated edges lie in an original icosahedral antipodal transversal of six vertices. The exact symmetric 6x6 signed adjacency matrix A satisfies A²=5I; for s in {±1}^6, the induced transversal edge count is (15+sum_{i<j}A_ij s_i s_j)/2. Spectral bound on the odd sum is <=3sqrt5<7, hence <=5 and at most 10 induced edges. Independently enumerated 64 transversal edge-count distribution {5:12,6:20,9:20,10:12} and checked all active facet inequalities in Q(sqrt5) for u=(-2,0,-1), strictly lighting ten midpoint vertices. Therefore alpha=10. Any fractional cover has weight >=30/10 by summing vertex constraints; averaging this direction under the edge-transitive rotation group attains weight exactly 3 and covers the whole boundary. This analytic bound covers the continuum of directions; no finite direction-sampling extrapolation.

## originality

PASS

Qualified: Naszódi introduced the same fractional parallel-direction invariant, and previously published Platonic polytope exact evaluations give i*=4 for the icosahedron and dodecahedron. The new result is their 30-vertex rectification i*=3, established by a signed 6x6 conference matrix and a ten-vertex illumination witness. Kiss–Oloff de Wet do list the icosidodecahedron but evaluate a mathematically different norm-weighted external-light-source parameter, not its fractional direction number. No precise same-invariant result identified.

## value

PASS

PASS: Fractional illumination is a canonical convex-geometric invariant, and the regular icosidodecahedron is the canonical rectification of two Platonic dual solids whose values were already computed as four. Establishing the strict decrease to three and its exact signed-conference obstruction is a natural new benchmark, not an unmotivated small integer table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
