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

Reproduction: run `python3 CHECK.py` using Python 3 and no external dependencies. The output ends in `VERIFY_OK` after exact finite-field computations for the twelve listed primes. The general theorem is proved by the monomial Frobenius computation, Lucas valuation of boundary derivatives, coefficient differential equations, recurrence uniqueness, and the simple-root contradiction; finite examples do not establish the unrestricted prime quantifier. A separate independent scientific validation has not been carried out. The calculation does not enumerate all algebraically closed parameters numerically; root counts are proved by degree and separability.
