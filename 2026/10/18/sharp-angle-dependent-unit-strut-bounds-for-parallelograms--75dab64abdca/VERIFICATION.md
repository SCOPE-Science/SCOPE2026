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

For the side of length a the only inward candidate has height h=sqrt(1-a^2/4) and parallelogram coordinates (1/2-ch/(as), h/(bs)). Existence requires a<=2; containment is equivalent to h<=bs and 2ch<=as, including the valid midpoint when a=2. Squaring nonnegative quantities gives exactly the stated bounds. The opposite side is congruent; interchanging side types gives the other inequalities. A forbidden vertex requires a=2c,b=1 or the transpose, and feasibility of both side types then forces c<=1/2 and 1+16c^2(1-c^2)>=4, hence only c=1/2,a=b=1. For c>=1/2 the length floors give the sharp perimeter bound; equality forces a=b=2c and yields admissible nonvertex witnesses except at the excluded triple, approached by rhombi from above. For c<=1/2, ordering a<=b, the inequality b^2+4s^2a^2>=4 and strict convexity of (1-x)^2+4s^2x^2 on [0,1/2], with x=a/(a+b)>0, force the stated sharp bound and equality only at a=b. For c<1/2 this rhombus has witnesses in the relative interiors of the opposite sides. The two branches agree at c=1/2 and increase strictly in c, giving the unique square global equality. The check is analytic; checker.py uses exact rational predicates but high-precision tolerances for geometry and perimeter comparisons, and its recorded PASS is finite corroboration only.

## originality

PASS

The edge-strut definition and a general polygon bound are established; the distinct contribution is the complete parallelogram feasible set including witness exclusion, together with the sharp angle-resolved perimeter and equality/attainment classification. The available exact trapezoid profile is for two legs and permits vertex witnesses; it neither reproduces these statements nor contains this model as a matching specialization.

## value

PASS

This gives a natural complete classification for the first all-side centrally symmetric quadrilateral model of an established strut problem. In particular it identifies where the active obstruction changes and why the minimum is not attained at exactly 60 degrees; these facts are not conveyed by the global lower bound alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
