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

## Reproduction

Run `python verify_temporal_galam.py` with Python 3.9+ and the standard library. The program makes 2,217 exact-rational checks of the displayed finite polynomial identities for a parameter grid and simulates a seeded logarithmic trajectory of 180,000 steps; it prints the observed and theoretical exponents and sign frequencies.

## Analytical checks and limits

The proof of universal contraction comes from an exact expectation of the squared multiplier, not from finite-grid testing. The exact almost-sure exponent uses a uniform logarithmic second-moment bound, martingale strong law, continuity and Cesaro averaging. The finite tests illustrate these identities but do not certify the infinite-time statements. Independent external audit has not been performed.
