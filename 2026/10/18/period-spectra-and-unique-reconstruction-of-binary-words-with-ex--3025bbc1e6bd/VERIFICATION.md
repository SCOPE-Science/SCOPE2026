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

# Verification of the two-marker period-profile formulas

The self-contained `verify.py` uses direct binary bitmask comparisons at every shift to compute periods. For every length from 2 through 100 it compares the direct result with the structural formula for every one of the possible two-marker words, independently groups equal direct profiles, and compares the class count and singleton count with the claimed formulas. It also tests the closed sum against the stated modulus-six quasipolynomial and performs deterministic random large-length comparisons at lengths 101, 128, 177, 256, 512, and 1000.

Run `python verify.py` under Python 3 with only the standard library. The successful output is `PERIOD_TWO_MARKER_CHECKS_PASSED checked_pairs 172650 complete_lengths 2..100 large_spot_lengths 101,128,177,256,512,1000`.

These finite checks test edge cases and arithmetic. They do not constitute a proof for arbitrary lengths. The infinite proof is in `RESULT.md`; there is no external independent audit or formal verification claim.
