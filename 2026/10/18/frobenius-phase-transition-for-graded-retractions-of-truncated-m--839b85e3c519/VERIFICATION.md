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

The exact finite checker `verify_graded_retractions.py` uses only the Python standard library and is run with `python verify_graded_retractions.py`. Its 18 exhaustive cases compute the relations in the truncated polynomial algebra before enumerating allowed homomorphisms. It checks every coefficient of the full-endomorphism and retraction rank distributions by testing matrix ranks and idempotence on each admissible matrix.

Coverage: base fields of cardinalities 2, 3, 4, and 5; generator counts 2 and 3; truncation exponents 2, 3, 4, and 5 as listed in the script. The field of four elements uses polynomial reduction modulo an irreducible quadratic. Expected final check line: `ALL_EXACT_CHECKS_PASSED 18`.

This finite computation does not prove the all-parameter theorem: the proof is the binomial-coefficient criterion together with exact projection and weighted-function counts. Independent audit has not been performed.
