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

# Verification scope

The all-integer theorem is proved analytically by an induction preserving alternating strict derivative signs. The critical ingredients are a bound independent of the new segment valuation, eventual negativity and decay of each existing revenue derivative, and the near-unit derivative of a sufficiently high-valuation new segment at any fixed price.

The included standalone `verify.py` is an optional finite certificate. It runs with Python 3 standard-library rational fractions, encloses the exponential at integer arguments by a 400-term Taylor series and a justified geometric remainder, and checks strictly separated positive and negative intervals for the derivatives in the one-, two-, three-, and four-segment examples. It reports 50 successful exact-rational assertions. The printed decimals are display summaries of certified rational intervals, not the basis for any sign decision.

Finite checks do not prove the theorem for arbitrary segment count; the full induction is in `RESULT.md`. The file contains no claim of external or independent validation.
