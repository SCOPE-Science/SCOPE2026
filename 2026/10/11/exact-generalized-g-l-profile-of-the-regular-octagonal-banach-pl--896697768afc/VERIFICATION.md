---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The max-of-eight-support-functionals octagonal norm and the constraints N(x)=N(y)=N(x-y)=1 reduce to 8^3 ordered edge triples. Each feasible rank-two affine intersection is an interval; convexity makes every shifted norm attain its maximum at an endpoint. The inspected Q(sqrt(2)) verifier handles exact interval endpoints/support changes and reports 48 feasible families and 128 checked breakpoints. An independently coded numerical re-enumeration (all 512 triples) confirmed 48 feasible rank-two families, the exact predicted bound to floating tolerance, and no counterexamples; 32 rank-one triples have all parallel supporting edges and cannot be equilateral because a common norming functional of x-y would be in {-2,0,2} rather than +/-1. Independently checked explicit witness x=(1,sqrt(2)-1),y=(3-2sqrt(2),1) satisfies all three unit constraints and both shifted norms equal 2sqrt(2)-1. These finite checks are exhaustive only because of the proven convex-polyhedral reduction; numerical replay is corroboration, not sole proof.

## originality

PASS

PASS: the exact all-real-p family relies on a simultaneous coordinatewise upper bound. The same-object published p=2 sum and the product-based T_G value do not imply two separate uniform bounds, so they do not cover the new all-p profile.

## value

PASS

Natural extension of a named equilateral-triangle Banach-space invariant from one exponent to every real p>=1, with a structural common extremizer and sharp individual two-norm inequalities. This is more than a substitution of the known p=2 number; a researcher using generalized geometric constants can require the full profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
