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

The radical a is the positive root of a^2+(n+1)sa/sqrt(n)+s^2=1, and b^2-a^2=sqrt(n)sa. These identities yield the global containment inequality 1-sqrt(n)sa(|u_1|-1/sqrt(n))^2. For s>0 equality identifies both contact latitudes; s=0 gives the unit ball. At 2n contact vectors derived from a regular simplex, the weighted mean is zero and covariance is identity. Each is a supporting contact with normal parallel to the contact vector. For any competing ellipsoid y+A B_n with A positive definite, the contact inequalities imply tr(A)<=n, so AM–GM gives det(A)<=1; equality forces A=I and y=0, proving unrestricted global optimality and uniqueness. The thin-lens limit follows from the exact slice integral and semiaxis asymptotics. The inspected verifier checks rational identities and finite diagnostics, not the continuum proof.

## originality

PASS

Finch's full accessible paper was inspected: it studies the same symmetric lens in R^3 and calculates volume, surface area and mean width, not the John ellipsoid. Resultary returned that all-dimensional mean-width record as a close same-body hit; the invariant is different. The accessible John-ellipsoid-of-revolution paper provides general constrained-affine optimality conditions but not the evaluated two-ball-lens semiaxes/contact latitude formula. The Güler–Gürtuna slab problem is a different body with planar facets, not an affine equivalent of the curved two-ball lens. An unindexed older explicit formula remains a priority risk.

## value

PASS

The all-dimensional exact John ellipsoid, unique global optimizer, offset-independent contact latitude, and nonzero thin-lens volume fraction are natural convex-geometric invariants. These are structural facts not determined by the known lens volume/mean-width formulas or by generic John optimality conditions; they provide a useful benchmark for ellipsoid approximation of a canonical body family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
