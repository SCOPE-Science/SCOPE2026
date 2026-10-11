---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Every convex n-gon with n>=4 has a nonacute angle. Centering at the preceding vertex makes distance along the next edge nondecreasing, so those two consecutive edges contribute at most one distinct circle intersection; the other incident edge contributes at most one and each remaining segment at most two, giving 2n-4. For a right/obtuse triangle the same monotonicity gives a center with at most two intersections and small circles give exactly two. For an acute triangle, each boundary point has at least two strict vertex maxima of the distance function, so a level just below the second-largest maximum yields four crossings; a vertex center gives the matching upper bound four.

## originality

PASS

The foundational paper states the invariant, proves finiteness for every convex body, notes the acute-triangle four-intersection phenomenon, constructs a 15-gon with N=6, and says no universal bound is known. It does not give the polygon-complexity bound, the nonacute triangle classification, or the quadrilateral/pentagon consequences.

## value

PASS

This gives an explicit complexity-dependent bound for the invariant underlying an open universal-bound problem and settles the complete triangle phase transition. In particular it proves uniform four- and six-intersection bounds for quadrilaterals and pentagons. That is a natural structural cutoff, not an arbitrary finite calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
