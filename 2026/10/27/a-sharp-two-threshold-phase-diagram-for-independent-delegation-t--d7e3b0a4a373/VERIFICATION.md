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

# Verification and limits

The standalone standard-library script `verify.py` was executed from this package and returned:

`VERIFIED: 225 independent five-voter exact enumerations, all phase boundaries, exact witness, and three-voter boundary`

The independent enumeration ranges over delegation bit-vectors, independent expert correctness, and independent ordinary correctness, weighing every possible profile by rational Bernoulli probabilities. It compares the resulting exact rational majority-correctness probability against the closed analytic formula over five ordinary competence values, their critical expert competence thresholds, intermediate expert competence values, and nine delegation-rate choices per pair. Symbolic identities were additionally differentiated and factored algebraically. The exact witness and three-voter boundary were checked.

The universal claim follows from the explicit derivative proof and sign changes; a finite enumeration alone would not prove it. Independent replication and audit have not been performed. General and strategic versions of the result remain outside scope.
