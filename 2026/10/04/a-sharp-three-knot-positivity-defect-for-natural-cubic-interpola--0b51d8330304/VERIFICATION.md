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

The natural three-knot equations leave one interior second derivative. Substitution gives the stated left and right cardinal coefficients. On the left, two coefficients are nonnegative and \(A_2=-t(1-t^2)/(2r(1+r))\le0\), so the data-cube minimum is attained at \((0,0,M)\); maximizing \(t-t^3\) gives \(2/(3\sqrt3)\). The right interval is the reflected calculation with only \(B_0\le0\), giving the \(r^2\) branch. Comparing the two branches yields \(C(r)=\max\{r^{-1},r^2\}/(3\sqrt3(1+r))\), uniquely minimized at \(r=1\) and divergent for skew meshes. Independent rational checks reproduced the basis identities/signs.

## originality

PASS

Prior spline literature establishes only the qualitative failure of positivity and methods that repair negative natural splines by adding knots. The closest Fischer–Opfer–Puri primary paper was inspected through its setup and optimization construction; it does not state an exact three-knot worst undershoot, mesh-ratio constant, or equivalent Lebesgue constant. Resultary and direct exact searches found no matching formula.

## value

PASS

This gives a natural minimal-size exact positivity defect, identifies the extremizing data and locations, and quantifies how mesh skew destroys positivity. The qualitative defect is known, but the sharp minimal-knot constant is independently useful for shape-preservation analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
