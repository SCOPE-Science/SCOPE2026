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
The proof is analytic and finite-dimensional. The standalone verifier checks the rational simplex-frame eigenvalue identity for \(2\le m\le40\), then tests the global inequality on cyclic groups of orders \(4\) through \(32\) for every proper dual subgroup and replays the character-evaluation extremizers.

Command:

`python3 verify.py`

Observed output:

`VERIFY_OK exact_m=2..40 random_checks=2040 cyclic_extremizers=85`

The random checks are stress tests only. The infinite family is proved by the exact Gram-matrix diagonalization and coset decomposition in `RESULT.md`.
