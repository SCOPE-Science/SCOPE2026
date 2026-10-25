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

# Verification of the theorem

## Source and analytic checks
The general convex Cheeger-radius theorem is read in Kawohl--Lachand-Robert (2006), Theorem 1. The 2021 paper by Cañete reproduces the statement and establishes the permitted primary geometry code. The most directly related outer-parallel paper by Ftouhi (2025) was inspected through its first-order variation theorem. These are premises/priority comparisons rather than novel certificates.

We checked independently by symbolic coefficient matching that the expansion for the rounding gap has linear coefficient \(2\pi T/D\) and quadratic coefficient \(\pi(4\pi CT^2-L^2)/D^3\). The one-sided second derivative gap for \(s=1/h\) simplifies to \(8\pi^2T^2(C-\pi)/D^3\), hence the claimed negative jump of \(h''\). The geometric inner erosion identity follows from shifted support halfplanes; no finite enumeration is used as an infinite proof.

## Reproducible numerical cross-checks
Run `python verify.py`. It constructs polygonal erosion independently via sequential clipping by inward translated halfplanes. At small offsets it compares polygon area against the derived inner-Steiner polynomial; around the critical radius it checks the Cheeger-root expansion by numerical bisection, including squares, equilateral and regular polygons, and one asymmetric convex pentagon. The program passed on the supplied package. The calculated examples neither certify arbitrary polygons nor establish publication priority.

## Boundaries
All objects are planar Euclidean convex polygons with genuine noncollinear vertices. The expanded inner Steiner formula is only asserted before the first edge vanishes. The second derivative is one-sided at the join. Independent mathematical and scholarly review has not been performed.
