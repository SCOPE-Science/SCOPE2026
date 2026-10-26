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

The exact pair-payoff formula was checked independently by solving the four-state repeated-game payoff linear system over rational numbers for many parameter values. The bound and equality-class examples are checked with exact rational distribution sums. Reproduce with `python3 verify.py` using Python 3 standard library only.

Recorded check result: `VERIFIED 346 exact-rational assertions; illustration gap = 1/48`.

The continuum of possible probability laws, convex-order monotonicity and sharp extremizers rely on the analytical moment-series and convex-chord arguments in RESULT.md, not on exhaustive finite computation. No independent scientific audit has been performed.
