---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The rank-at-most-two determinant cubic is the image of factor multiplication, and unique factorization identifies its geometric fibers with unordered pairs. The induced finite birational map from the symmetric square is an isomorphism: the determinant hypersurface is normal, being a hypersurface regular away from the rank-one Veronese locus of codimension two. Pullback on cubics has the determinant as its entire kernel, and dimensions 56 and 55 imply surjectivity onto symmetric bidegree-(3,3) forms. Vanishing along the planes forces each factor to use the two-dimensional space of cubics through the reduced complete intersection, so the image is precisely its symmetric square. Incorporating the determinant gives four generators. The three remaining generators on the product are the symmetric product of the two pencil-value vectors; it vanishes exactly if one vector is zero. At a rank-two point with only one basepoint factor, a nonzero entry of the other vector is a unit and the three generators recover both local equations of the one plane. At a pair of distinct basepoints the ordered cover is étale and the transverse pencil values are completed coordinates; the ideal is (ux,uy+vx,vy) rather than the intersection (ux,uy,vx,vy). The extra degree-two class uy is independent modulo the first three generators and all four parameters kill it, giving a residue field. Unique factorization makes these 36 points distinct. At a repeated basepoint in the rank-one chart, exchanging the factors negates the two difference coordinates; their invariant quadratics a,b,c satisfy ac=b^2. The three generators set a,b,c to s_1^2,s_1s_2,s_2^2 in average coordinates, leaving the reduced power series ring in s_1,s_2. These complete local calculations faithfully detect the defect and show no other support; this argument does not assume the base scheme of any blow-up has that description.

## originality

PASS

Secci already obtains the four-dimensional cubic system and ninth-plane containment for a general-position configuration. The supported distinct increment is the exact ambient support and its nonreduced structure at every pair point for a transverse nine-point complete intersection. The prior plane containment, the sextic restriction to the rank-one locus, and the smoothness computation for general members do not determine the local rank-two ideal or the length-one defects.

## value

PASS

The cubic system is already a motivated natural object in the geometry of the Veronese-tangent configuration. Its ambient base support and its scheme structure are not interchangeable; in this case the latter adds a canonical residue field at every pair point, changing the Hilbert polynomial by 36. This is a uniform determination for the natural family and a concrete correction to treating the cubic base scheme as the reduced plane union, not a recount of the plane pairs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
