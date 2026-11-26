---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The universal line section has constant length m and is flat over the dual plane. Plane quadrics give all sections of L and their restrictions to a line span all quadratics there; restriction to its length-m divisor has zero kernel on those quadratics for m>=4. The support divisor recovers the line and then the kernel determines the constant direction. Thus the proper parameter image is closed, irreducible and three-dimensional. After splitting the quotient direction, the Quot kernel is L(-D) plus L. At rank exactly 3, the minors linearize to the map from the evaluation kernel H^0(L(-D) plus L) into the cokernel. The two Hom multipliers must send span(1,t) and span(1,t,t^2), respectively, into span(1,t,t^2) modulo the degree-m line-section polynomial. Testing 1 and t forces the first multiplier to have degree at most 1 and the second to have degree at most 1; testing t^2 for the second reduces that to degree 0. Every degree-3 obstruction in these tests is strictly below m, including m=4. The tangent dimension 3 equals local dimension, so the image is a component and is smooth at its transverse points. The family projects isomorphically onto its support divisors, hence is nondefective; over distinct projections the Hilbert and Quot descriptions identify locally as unordered sets of base points and directions with the same evaluation map. At m=3 the bound is automatic and the ambient Quot dimension is 6. The source checker was inspected, not executed: its rational row construction checks only a finite model of the exact multiplier computation, which was proved directly here.

## originality

PASS

The construction of low-rank divisors in one split summand and its rotation by constant changes of basis are closely anticipated. Credit only the exact tangent dimension and the resulting generically smooth component, not the rank-locus framework or existence of the family. No inspected result supplies the former statements or a dominating result establishing them.

## value

PASS

An explicit regular component for the complete linear system, on every smooth plane curve of the specified degree and with a sharp small-degree boundary, is useful for understanding special secant loci of scrolls and for testing possible dimension bounds. Membership of this family alone would not give this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
