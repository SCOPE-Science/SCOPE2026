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

# Verification record

The standalone checker `check_hecke.py` uses the Python standard library. Run `python check_hecke.py` in the directory containing the file. It constructs Demazure products from an independently computed bubble-sort reduced word, enumerates all permutations on one through eight points, and tests the idempotent classification, pairwise commutation criterion, and support polynomial recurrence.

A successful run reports `ALL_TYPE_A_HECKE_IDEMPOTENT_CHECKS_PASSED 46233 [1, 4, 14, 48, 164, 560, 1912, 6528]`. All 46,233 permutations and 21,845 ordered candidate idempotent pairs are included. This checks only finite instances and is not an infinite-size correctness certificate. The theorem's general proof is contained in `RESULT.md`. There is no independent mathematical audit.
