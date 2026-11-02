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

## Checks

The proof supplies exact orbit-cell and equivalence-class classifications, inclusion-exclusion and Bell-number asymptotics. Reproduce the finite tests using `python checker.py` (Python 3 standard library). The checker enumerates named/fresh orbit signatures, admissible finite equivalence partitions, and support-essentiality permutations; it reports `ALL_CHECKS_OK` after checking every stratum for context sizes 0 through 5 and all binary predicates at context sizes 0 through 3.

The finite tests are independent finite-instance consistency checks, not proofs of infinite statements. The infinite assertions use the symbolic arguments in `RESULT.md`; the only asymptotic input from the literature is the classical consecutive-Bell-number estimate. The high-priority 2021 binary-relation article and 2026 companion paper were identifiable but their complete texts were not available for comparison.
