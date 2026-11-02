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

The independent `verify_rotation.py` script is supplied alongside the theorem. Run with `python verify_rotation.py` under Python 3.10 or newer; it requires only the Python standard library.

The program checks exact rational Bayesian-to-odds identity and orbit invariance for two rational-resonant and two irrational-ratio likelihood pairs. It performs 3,620 exact rational comparisons, checks the primitive periods of six rational-resonance configurations, verifies 200,000 rotation-itinerary wrap comparisons, and compares a 200,000-step orbit mean against the analytic invariant-measure integral. The script succeeds with output ending `All finite checks passed.` when extracted from this package.

The infinite statements require the explicit proof in RESULT.md. No finite program can establish the density of an infinite irrational orbit or uniqueness of a probability invariant under the rotation; those facts follow from the classical irrational-rotation argument given in the proof. The irrationality of the published parameters is certified by exact integer prime valuations rather than floating-point approximation. No independent validation or external certification is asserted.
