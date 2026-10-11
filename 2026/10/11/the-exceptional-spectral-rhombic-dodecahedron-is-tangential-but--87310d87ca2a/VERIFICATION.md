---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The proof in `RESULT.md` is exact.

Critical checks:
- the rhombic-dodecahedron graph is represented as cube-vertex/cube-facet incidence;
- the displayed coordinate rows satisfy the adjacency eigen-equation with eigenvalue \(2\);
- the three arrangement columns are orthonormal;
- \(2\) is the second adjacency eigenvalue and has multiplicity \(3\);
- the six degree-\(4\) rows have squared norm \(1/4\);
- the eight degree-\(3\) rows have squared norm \(3/16\);
- the outer antipodal octahedron gives the unique minimum-enclosing sphere of radius \(1/2\);
- the twelve inequalities \(\pm x_i\pm x_j\le1/2\) are supporting facets and exhaust the facet count;
- all facet distances from the origin equal \(1/(2\sqrt2)\);
- opposite facet pairs force the incenter uniquely;
- every graph edge has squared length \(3/16\).

`verify.py` reconstructs all of these identities using exact rational arithmetic and exact symbolic characteristic-polynomial computation. The computation is a replay of the finite algebra in the proof and does not assess originality.
