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

The standard-library `verify.py` enumerates all \(2^n\) rooted binary words at lengths \(1\) through \(11\), with all rotations, and independently enumerates every necklace with at least one one as cyclic positive-gap compositions. Both approaches return zero failing necklaces through length \(10\) and exactly three at length \(11\), with the same representative strings. The CSV supplies one explicit failing factor for every cut of each exceptional necklace, and the checker verifies all \(33\) inequalities.

The symbolic family proof handles every \(n\ge11\); checker tests for \(11\le n\le120\) serve only as additional consistency checks and are not a substitute for that proof. Both finite enumeration methods use integer-only comparisons, with no randomness, solver calls, external data or third-party libraries.

Correctness and overlap/value assessments are documented separately in `REVIEW.md` and `AUDIT.json`. Independent audit has not been performed.
