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
# Verification of the one-symbol trifferent classification

The standalone `verify.py` uses Python's standard library only. It independently generates all candidate two-word fibers (complementary on their binary coordinates), checks every triple for the trifference condition, builds every tournament code, and checks equality of both resulting sets for lengths 2, 3, 4 and 5. The exact labeled counts are 1, 4, 32 and 512; the number of tournament orientations is 2, 8, 64 and 1024, each pair of converses representing one code.

Run: `python verify.py`. Expected stdout: `VERIFIER_OUTPUT.txt`. The classifying theorem for every length rests on the algebraic proof in `RESULT.md`, not exhaustive finite cases. Literature priority beyond material actually inspected and independent review remain unverified.
