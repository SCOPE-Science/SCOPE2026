---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS. The squared-coordinate map x²=X,y²=Y,z²=Z realizes sextic as pullback of cubic G=X³+Y³+Z³+a(X²Y+Y²Z+Z²X)+b(XY²+YZ²+ZX²). Independent symbolic expansion at P=[1:1:1] with X=1+t,Y=1+w−t yielded exactly (a+b)w²+(b−a)t³+(a+b)t²w+b t w²+w³ mod3; nonzero w² and t³ coefficients give unibranch A2 cusp delta1. Excluding a=b prevents tangent cubic line component, genus-one cubic normalization is P1. Axis discriminant (ab)²−(a+b)³≠0 gives nine simple coordinate intersections; independent square classes force degree-four connected Kummer extension with nine e=2 branch points. Riemann–Hurwitz 2g−2=−8+18=10 gives g6, agreeing plane genus10 minus four cusps. Etale inverse image of P gives exactly four cusps and none elsewhere. Each unibranch cusp is split over every field of definition, giving point-count preservation; no extrapolation from finite F3/F9 tests.

## originality

PASS

Best-of-knowledge originality of the precise final claim after comparison to directly read primary results and published Resultary matches; older or less accessible sources and terminology remain explicit residual risks, not proof of novelty.

## value

PASS

PASS. This treats a naturally excluded characteristic of a studied cyclic sextic family and explains a four-cusp degeneration while preserving genus-six via an explicit nine-branch-point Klein-four normalization. Meaningful structural boundary resolution beyond special symmetric reducibility; no claims for excluded parameter divisors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
