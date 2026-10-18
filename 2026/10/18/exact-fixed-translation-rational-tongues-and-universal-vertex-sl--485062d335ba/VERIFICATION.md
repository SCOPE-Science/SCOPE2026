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

The finite check can be run with `python check_exact.py` in a directory containing the included file. It uses Python standard-library `fractions.Fraction` and checks 5,972 reduced-rational parameter triples up to denominator 70, polynomial identities, cyclic boundary itineraries, interior inequalities and derivative signs, and separate first-order endpoint tests near contraction ratio one. The complete infinite-parameter argument instead uses the ceiling/floor mechanical-word prefix inequalities and the differentiated periodic recurrence given in RESULT.md. Numerical or finite tests do not certify all denominators; the mathematical proof does not depend on their exhaustion. Independent audit has not been performed.
