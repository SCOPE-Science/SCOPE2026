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

## Reproducibility
Execute `python3 verify.py` without dependencies beyond the Python standard library. The test performs deterministic trial division for every odd integer below 16384, then enumerates every six-word beginning at a positive integer and ending below the prime. No random seeds, approximate arithmetic or external data are used.

Successful output reports `VERIFY_OK`, 1,899 odd primes processed, 1,812 primes in the confirmed complete tail at least 461, 61 exceptional primes overall, and the final exceptional prime 457. At 457, exactly the six-residue word is absent. An alternate Euler-criterion implementation checks the same word support for primes up to 1009.

## Verification limits
The finite program proves only the stated bounded interval. The unbounded range is established by the independent exact character-sum argument in RESULT.md, using the classical Weil bound for squarefree polynomials. The output is a same-model reproducibility check, not an independent external audit.
