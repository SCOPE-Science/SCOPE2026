---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Represent the fourteen vertices by eight inner sign vectors (±1,±1,±1)/4 and six outer axis vectors ±e_i/2. The cube-vertex/face bipartite incidence adjacency matrix has characteristic polynomial z^6(z²-4)^3(z²-12), so eigenvalue 2 is second largest with multiplicity three. The 14x3 coordinate columns are exact orthonormal 2-eigenvectors. Independent SymPy/rational checks reconstructed all of this without relying on the packaged verify log. The eight inner vertex squared radii are 3/16 and six outer squared radii 1/4; outer axis contacts force the unique minimum enclosing sphere of radius1/2. Exactly twelve inequalities ±x_i±x_j≤1/2 (i<j) support four affinely independent facet vertices each, giving inradius 1/(2sqrt2) and, via the opposite facet pairs, a unique incenter. Every edge length is sqrt3/4; finite exact checks cover entire 14-vertex polyhedron.

## originality

PASS

Winter shows the exceptional rhombic dodecahedron is second-eigenvalue spectral and not vertex transitive, and provides the orthonormal eigenpolytope definition. This fixes a canonical metric up to Euclidean isometry but does not state the twelve-facet inball nor the two exact radial shells in the examined sections. Licata–Powers had already shown self-reproduction; its full 1988 text was not accessible and remains a residual novelty risk.

## value

PASS

The rhombic dodecahedron is a structurally exceptional non-vertex-transitive spectral polytope. Its exact failure of vertex cosphericity alongside common facet tangent sphere gives a motivated complete canonical metric profile for an exceptional graph-eigenpolytope example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
