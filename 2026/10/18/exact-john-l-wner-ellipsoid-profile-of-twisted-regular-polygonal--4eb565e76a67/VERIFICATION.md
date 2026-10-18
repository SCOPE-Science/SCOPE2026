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

# Verification of the exact regular-prismatoid ellipsoid profile

To reproduce the independent finite geometry regression, run `python verify.py` with Python 3, NumPy and SciPy installed. This checks (i) all facets of the three-dimensional convex hull for \(3\le n\le17\), (ii) the proposed John ellipsoid's maximum linear support against every hull facet, including lateral tangencies, for five interior twist fractions, and (iii) 75 exact-prediction versus independent-hull-volume comparisons including both twist endpoints.

The infinite-domain proof is the facet classification plus the strictly positive derivative of \(b(D^2-\Delta^2b^2/h^2)\) on the admissible interval, the unique outer-ellipsoid Lagrange optimum, and the planar mixed-area identity. A finite experiment does not replace any of these arguments. At coincident base rotations some triangular facets coalesce to quadrilaterals; continuity resolves those boundary cases. The end caps are tangent at their centers, and every generic lateral facet touches the John ellipsoid.

Historical comparison was performed against general ellipsoid theory, regular-polygon prism and antiprism sources, and the prior maximal-tetrahedron result for the same convex bodies. The latter is a different mathematical invariant. One plausibly relevant 2013 full text was inaccessible; its abstract cannot rule out special-case coverage. Unindexed work remains a priority risk. Independent audit has not been performed.
