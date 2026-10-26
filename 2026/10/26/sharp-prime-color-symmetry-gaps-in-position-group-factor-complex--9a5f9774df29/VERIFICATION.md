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

# Verification

The proof is deductive; the accompanying checker is a finite stress test only. Reproduce with `python3 check.py`. It enumerates all color-invariant subsets and coordinate subgroups at prime/length pairs (3,2), (3,3), (5,2), (7,2), checks the nonzero deficit gap, congruences, and equality rigidity, and constructs both sharp periodic families at primes 3, 5, 7. The final success marker is `FINITE_STRESS_TESTS_OK`. No finite computation certifies the universal quantifiers of the theorem; those are established by the class-orbit proof.
