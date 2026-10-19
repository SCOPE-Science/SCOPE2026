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

The standalone `verify.py` uses Python's standard library. It runs 48 exhaustive word-enumeration comparisons, 15,351 finite sign-pattern tests, and exact-rational checks of signs \(+,-,+,-\) at heterogeneous sample sizes \(3,4,9,10\). Run `python3 verify.py` from this directory. Computations corroborate but do not prove claims over unbounded parameter ranges, which follow from the algebraic ratio comparison and logarithmic expansion in `RESULT.md`.
