---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For generic normals a vertex-only triangulation gives the truncated-power sum, with coefficient d times simplex volume divided by the vertex height differences. This normalization is the derivative of the simplex sublevel-volume formula, with unit-normal coarea factor 1. No triangulation interface contributes extra section measure in a generic direction: a shared facet cannot lie in a section plane when all vertex heights differ. Taking d distributional derivatives gives atoms of weight (d-1)! C_u. To verify noncancellation even at nonsimple vertices, choose a generic direction uniquely maximizing at u. Every simplex incident to u then contributes with the same sign (-1)^d, so the homogeneous rational coefficient is not identically zero and its zero set has empty interior away from poles. At the prescribed relative-interior edge normal only the two edge endpoints maximize. A small tilt gives one top vertex and one unique runner-up, within epsilon/3 of support. Select a generic such direction with nonzero runner-up coefficient; strict gaps and continuity then allow a fixed open interval J holding all runner-up heights for a small direction patch, no other vertex heights, and lying inside every support strip in that patch. The runner-up vertex is nonzero since zero is interior, so its projection is nonconstant on every open sphere patch for d>=2. Select infinitely many distinct projected heights. The restricted derivatives are distinct nonzero Dirac masses; testing a finite relation near each mass proves independence of the profiles. Restriction of a separated representation to J would put all profiles in a finite-dimensional span even if its factors have no regularity.

## originality

PASS

Credit is for the edge-local infinite-rank statement on one common absolute near-support interval, not for generic vertex-knot noncancellation, the simplex spline formula, or the separability framework. Generic noncancellation is already in Gravin–Lasserre–Pasechnik–Robins. Their projection-moment formulas and the known spline representation give the global atoms; they do not localize a moving atom in an arbitrary support strip and edge neighborhood on a product domain with a common interval. The smooth or centered-interval rank theorems inspected do not cover that problem.

## value

PASS

The result gives a concrete obstruction in the nonsmooth class omitted by the known smooth near-boundary theorem. It applies in each dimension, for any edge, even when the separated factors would be arbitrary functions. The local moving-knot proof exhibits a common interval and arbitrarily large independent families, substantially more than a statement about global spline complexity or a single pair of profiles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
