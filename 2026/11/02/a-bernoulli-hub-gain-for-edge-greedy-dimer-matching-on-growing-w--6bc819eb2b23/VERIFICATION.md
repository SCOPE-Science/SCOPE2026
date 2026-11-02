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
# Verification

The scientific claim is checked at the following levels:

1. The vertex-deletion coupling is proved for every fixed finite graph and edge ordering by induction on processed edges. In a wheel, it gives the exact binary range of the matched-edge increment for each common-priority realization.
2. The first-edge path recurrence is solved by a generating function. The coefficient formula and the exponential remainder are derived analytically, not inferred from numerical experiments.
3. The early hub-spoke event has an elementary geometric tail bound. A conditional uniform-position bound makes the early removed blocks separate with high probability. The exact remaining-path expectation identity then gives the wheel constant, with rare-event contributions controlled by uniform integrability.
4. The standard-library script `checker.py`, executed on the files packaged with this result, passed 49,615 exact rational and deterministic enumeration assertions and numerical asymptotic diagnostics. It checks the path coefficient formula for lengths up to 64, wheel Markov recursions for rim orders up to 12, exhaustive common-priority edge orders on three- and four-vertex rims, and the deletion lemma over the enumerated finite graph/order cases. It also reports wheel-minus-cycle mean gains at rim orders 8, 10 and 12.

A finite enumeration is not evidence of the general limit without Steps 1–3. No formal proof assistant or external mathematical audit has been used. This check does not establish worldwide priority: one highly relevant 1991 paper was available only as an abstract. The result applies to the *coupled* difference, not to differences of independent samples.
