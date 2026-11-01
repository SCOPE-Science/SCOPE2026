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

For any u, each radius-R plane disk supports at R times the Euclidean norm of its two coordinate components. Hence h_K(u)=R sqrt(||u||^2-min_i u_i^2). A unique smallest absolute coordinate yields one supporting point, two equal minima yield a tie segment (occasionally degenerate on coordinate axes), and three equal nonzero magnitudes yield the eight equilateral triangular exposed facets. For each sign octant and each uniquely largest coordinate, a ruled patch F(phi,t)=(cos(phi),t sin(phi),(1-t)sin(phi)), 0<phi<pi/4,0<t<1, has normal (cos(phi),sin(phi),sin(phi)) and Jacobian sin(phi)sqrt(1+sin(phi)^2); 8*3=24 patches. Their interiors and the facets exhaust the 2D boundary except measure-zero seams/circle arcs. The patch integral is I=1/2-sqrt(3)/4+pi/12, triangle area sqrt(3)/4. This yields area 24I+8sqrt(3)/4=12-4sqrt(3)+2pi. The divergence theorem supplies 3Vol=24(1-1/sqrt(2))+8sqrt(2)/4=24-10sqrt(2), hence Vol=8-10sqrt(2)/3. Minimizing h on S^2 yields sqrt(2/3) at body diagonal normals, maximizing yields 1 at coordinate normals; central symmetry makes the centered extremal balls globally optimal. R scaling gives R^3,R^2,R. Independent SymPy cross-product/primitive/flux checks and SciPy polygonal hulls confirm the formulas numerically but are not the continuum proof.

## originality

PASS

Best-of-knowledge PASS for the combined exact primal area/volume and full 8-triangle/24-patch classification. Comparisons were made at implication level against both two-disk calculations and the potentially stronger common-diameter n-disk identity, general cospherical-circle classification and polar tricylinder values. The common-diameter condition fails for three mutually perpendicular planes; CHoCC's disjoint-cap condition fails for three equators; the polar tricylinder exact measures do not determine the primal intrinsic volumes. No actually inspected published statement entails the combined claim. The inaccessible 2020 CHoCC complete text and possible unindexed historical treatment remain explicit residual risks and are not treated as proof of novelty.

## value

PASS

Three congruent orthogonal equatorial disks give a natural octahedrally symmetric 3D convex body, whose polar is the classical tricylinder. Determining its exact volume, boundary area, both radii and all 2D boundary strata supplies intrinsic and structural data for a canonical object not implied by the established dual-cylinder table or the two-disk hull. A geometric researcher comparing cone/ruled-surface hulls or polar convex bodies could need these exact values and support-tie geometry. The result is a self-contained motivated exact invariant, not arbitrary small-instance parameter slicing; no downstream theorem is required for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
