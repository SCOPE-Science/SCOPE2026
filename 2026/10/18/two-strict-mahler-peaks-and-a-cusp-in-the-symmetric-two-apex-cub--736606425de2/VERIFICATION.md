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

For every t>=0, K_t is the symmetric convex hull of [-1,1]^3 and the two antipodal adjacent-corner-apex pairs. Inspected actual verify_two_apex.py: its triangulations are suggested at sample t=1 and 3 but then every primal supporting-plane inequality and polar inequality is certified for entire chambers t=2u/(1+u) (0<t<2) and t=2+u (t>2) by one-sign polynomial coefficients; outward closed boundary triangularizations and dual facet reconstruction justify signed determinant volume sums. Multiplying exact primal/polar volumes yields the displayed two rational branches, continuous at t=2 and valid t=0 by cube continuity. Independent ConvexHull primal/polar numeric integrations at t=.5,1,1.7,2.3,3,10 matched closed forms; independent symbolic derivatives factor into -8(t²+2t−4)(t³+10t²+36t+56)/(9(t+2)²(t+4)²) and -256(3t²−16)/(9t³(t+4)²). Thus strict peaks t1=sqrt5-1, t2=4/sqrt3, cusp minimum t=2 with left/right -88/81 and 32/81, and strict M(t)>32/3 for finite t>0 with limiting equality at infinity. Numeric samples alone do not establish full chambers; inspected exact support certificates and algebra do.

## originality

PASS

Best-of-knowledge original final claim: compared specific mathematical statements and implications against the retrieved Resultary indexed records and relevant original primary texts; known normalizations, generic tools and special cases are not counted as new. No positive coverage result was established; inaccessible/unread alternatives remain explicit risks.

## value

PASS

An explicit finite-dimensional centrally symmetric cubical perturbation with two strict Mahler-product peaks, a nonsmooth combinatorial transition, a strict interior cusp minimum and cube-limit behavior is a motivated sharp example for volume-product geometry. The complete piecewise rational profile and exact extremum ordering are nontrivial information not provided by general local minimum inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
