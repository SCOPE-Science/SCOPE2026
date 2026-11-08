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

# Reproduction and limits

Run `python3 verify.py` with Python 3 and no third-party packages. The program uses exact rational arithmetic and independently checks RSD, deferred acceptance and the known coupon-singleton law.

The observed check output ended with `PASS 285 independent distribution, moment and exhaustive comparisons`. The enumeration covers every independent uniform strict-student preference profile through four RSD students, every three-by-three DA profile with all strict school priorities, and each of the 216 fixed priority profiles separately for three schools. The coupon singleton integral is expanded into finite rational sums, not approximated by simulation. Moment identities are checked for market sizes up to nine and orders through five. No external solver, random seed or inaccessible artifact is needed.

The mathematical proof in RESULT.md establishes the infinite-size claim. Finite checks cannot establish the exponential limit, the absence of an equivalent theorem elsewhere, or independent validation. The cited literature's singleton coupon formula and harmonic mean remain prior results, not newly certified discoveries.
