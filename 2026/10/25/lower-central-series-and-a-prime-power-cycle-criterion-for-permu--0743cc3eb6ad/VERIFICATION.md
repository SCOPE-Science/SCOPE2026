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

Run `python verify.py` with Python 3 and `sympy` installed. The script uses exact arithmetic only and prints `VERIFY_OK` after checking all sixty-six integer partitions of sizes one through eight. It checks monoid/group multiplication and inverses, commutators of basis elements against the difference-operator formula, Smith invariant factors for the derived lattice, and the integral cyclotomic unit identity for order six.

The finite tests do not establish residual nilpotence in arbitrary rank. The infinite proof is the cyclotomic-eigenvalue and invariant-lattice argument in `RESULT.md`. The independent audit has not been performed.
