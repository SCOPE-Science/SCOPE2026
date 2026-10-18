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

# Computational verification

Run `python3 verify_fibonacci_catenary.py` using Python 3 and no nonstandard dependencies. The script constructs all atomic factorizations of each integer up to the stated finite cutoff for each \(3\le a\le11\). It replays every canonical normalization with integer preservation and distance-three assertions and verifies unique terminal forms and the two special factorizations of \(3F_a\).

The successful finite replay had 35,703 checked factorizations and 185,705 local moves. This cannot certify the infinite theorem by itself: its completeness follows from the explicit termination/uniqueness proof in `RESULT.md`. No independent mathematical audit has been performed.
