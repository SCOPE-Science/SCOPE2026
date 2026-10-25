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

Reconstructed the two shells (12 cyclic (0,±1,±phi) and 20 cyclic (0,±phi,±phi^{-1}) or independent ±1 triples), six-generator zonotope Z=2phi P, 15 cross-product facet-normal pairs, and zonotope volume sum 8*sum|det(g_i,g_j,g_k)|=20(2phi)^3. Independent exact Z[phi] four-combination enumeration computed C(32,4)=35960, exactly 39 levels, 2340 dependent quadruples, maximum determinant 6+8phi with multiplicity 20. The 20 maximizing 4-sets intersect pairwise in at most 2 vertices. Multi-affinity of oriented determinant in each of four vertex positions and equality in convex combinations implies every global optimizer is supported on four vertices: a nonvertex would force two extreme 4-sets sharing three vertices, impossible. The code is an exhaustive finite certificate for this fixed 32-vertex point set, not an infinite-family theorem; ring sign comparisons use 2(a+b phi)=(2a+b)+b sqrt(5). Source exact 39-level table and all 30 rhombic facets inspected, but independent histogram check here corroborated its counts, max, and isolation rather than independently recreating the entire 39-entry table.

## originality

PASS

Best-of-knowledge original claim: the mathematical implication and same-object comparisons below show no identified covering result. The decisive proof and quantitative classification are distinct from established background; incomplete primary sources are named as priority risks, not cleared without reading.

## value

PASS

A maximal-volume inscribed simplex and complete exact 4-vertex determinant spectrum are natural geometric invariants of a canonical Catalan solid. The all-contained-tetrahedra equality rigidity is a stronger geometric assertion than a finite list of sample volumes; the exact 39-level spectrum can be reused in Catalan-solid triangulation/volume computations. The 12/20 shell interaction and absence of shared triples are not a textbook norm inequality or arbitrary coordinate slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
