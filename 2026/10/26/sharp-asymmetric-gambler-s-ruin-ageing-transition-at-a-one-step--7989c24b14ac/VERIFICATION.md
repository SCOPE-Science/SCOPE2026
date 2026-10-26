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

The accompanying `verify_asymmetric_ifr.py` uses exact rational arithmetic for killed random-walk survival distributions; it requires only the Python standard library. It was executed from its actual package source path. Result:

`VERIFY_OK: 6 rational biases; b in {1,2,3,4,5,6,9}; grouped survival recurrences, b=4 determinants, and b>=5 initial IFR obstructions.`

The script verifies six rational drift probabilities and b in {1,2,3,4,5,6,9}, including the closed forms, b=4 Cayley–Hamilton recurrence and log-concavity determinants, and the strict initial hazard decline for all tested b>=5. The proof in RESULT.md independently handles all real p in (0,1) and every integer b>=1. Finite checks do not certify an infinite statement, and no independent mathematical audit has been performed.
