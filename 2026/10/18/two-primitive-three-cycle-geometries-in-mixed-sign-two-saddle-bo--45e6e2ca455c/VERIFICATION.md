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

# Verification record

The accompanying `verify.py` performs exact symbolic matrix multiplication for the two mixed three-letter itineraries, reconstructs every displayed first-coordinate formula and return determinant, checks the Floquet trace/determinant, and substitutes seven exact rational parameter choices into the three-step orbit identities, including the multiplier \(-1\) boundary. It also checks the explicit witness-line factors and strict itinerary signs.

Run `python verify.py` in an environment with SymPy installed. Expected output is the single `PASS:` line. Analytic inequalities in the proof, not finite sampling, establish the four-parameter theorem. No independent audit or external formal certification is asserted.
