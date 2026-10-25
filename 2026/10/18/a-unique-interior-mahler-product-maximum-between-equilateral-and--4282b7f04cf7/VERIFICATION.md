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

The original four-point metric has unit adjacent distances and two common diagonals t in [1,2]. Direct molecule mapping by determinant-4 matrix sends the unit ball to K_lambda=conv(cube [-1,1]^3 and four axial points ±lambda e1,±lambda e2), lambda=2/t. Four disjoint exterior face pyramids have total added volume 16(lambda-1)/3; polar is an l1 octahedron clipped on two axes with four disjoint caps, volume [4-(2-t)^3]/3. Reciprocal coordinate Jacobians cancel in Mahler product, giving 8(t+4)[4-(2-t)^3]/(9t). Independent exact SymPy differentiation gives derivative 8(3t^4-4t^3-12t²+16)/(9t²); the quartic decreases strictly on (1,2), is +3 at 1 and -16 at 2, implying unique maximum t≈1.121915780903. At t=1 P=40/3, t=2 P=32/3. Interior vertices/facets 12/18 and polar 18/12 are consistent with raised-face enumeration. Six rational polyhedral tests are corroborative, not continuum proof.

## originality

PASS

Best-of-knowledge noncoverage is supported by the statement-level comparisons below; this is not a proof of absolute bibliographic novelty.

## value

PASS

A natural square-to-equilateral four-point metric interpolation yields an exact affine-invariant geometric profile with a surprising strict interior maximum, meaningful endpoint comparisons and a complete finite-dimensional face transition. Not merely a table lookup or arbitrary slice: the family joins canonical tree/cycle extremal geometries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
