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
The proof was checked at the level of slices, rank-one operators, coordinatewise distances, convex hulls, and Hahn--Banach separation.

For the pointwise direction, a \(\Delta\)-coordinate can be varied inside any ambient slice while the other coordinates remain fixed. Conversely, if every norm-attaining coordinate fails to be a \(\Delta\)-point, norming functionals with \(\|I-f_i\otimes x_i\|<2\) combine into one thin ambient slice in which every coordinate remains uniformly below distance \(2\).

For the convex-hull direction, a single factor with convex-DLD2P is enough because only that coordinate needs to vary. If every factor fails the property, each closed convex hull of factor \(\Delta\)-points has a strict supporting-functional gap; summing these finitely many functionals gives a strict gap on every ambient \(\Delta\)-point and hence on its closed convex hull.

No numerical experiment or finite enumeration is used. The theorem is limited to finite real \(\ell_\infty\)-sums.
