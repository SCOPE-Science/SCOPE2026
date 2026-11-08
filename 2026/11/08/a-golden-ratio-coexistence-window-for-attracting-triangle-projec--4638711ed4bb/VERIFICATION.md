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

The analytical proof uses exhaustive cyclic itinerary types for least periods three and four; affine projection fixed points; strictly signed squared-distance comparisons; and the local return multipliers. In particular, no enumeration result is promoted to a proof over real heights.

The supplied standalone `verify.py` uses Python 3's standard library `fractions.Fraction` only. Its execution printed:

`CHECK_OK: 111 exact-rational triangle shapes; 488 assertions; period-(3,4) regimes: [((0, 0), 34), ((0, 1), 30), ((2, 0), 38), ((2, 1), 9)]`

The program independently generates and solves all cyclic projection itineraries of lengths three and four; it does not use the closed point formulas as its candidate generator. It checks strict winning distances, deduplicates rotations, and checks the analytic return multipliers. Finite exact checks are diagnostics, not a substitute for the universal argument. No independent audit has been performed.
