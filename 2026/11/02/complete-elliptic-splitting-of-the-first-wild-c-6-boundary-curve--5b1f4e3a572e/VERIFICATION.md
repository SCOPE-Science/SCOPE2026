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

# Reproduction
Run `python3 verify.py` with Python 3.8 or later. It uses only the standard library. The output is `VERIFY_OK: C/E/D counts n=1..6, functional equation and three elliptic factors`. The script enumerates every nonzero field element over the explicitly constructed fields for degrees one to six, applies exact binary trace tests, checks six point counts for each of the three quotient curves, and tests the six-degree zeta factorization and Jacobian order. A separate mathematical argument establishes genus and uniqueness of the zeta polynomial from initial counts; finite tests are not used to infer a general classification for larger exponents. Independent audit was not performed.
