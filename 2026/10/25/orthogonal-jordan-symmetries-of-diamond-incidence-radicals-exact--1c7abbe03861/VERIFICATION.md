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

Run `python3 diamond_jordan_checker.py` with Python 3.9 or later. No external packages are used. The checker directly forms the linear equations for derivations on basis multiplication, rather than assuming the stated block normal forms, and evaluates their nullities modulo 2, 3, 5 and 7 for each branch count from 1 through 4. It tests predicted block forms in small characteristics. It also enumerates all possible linear maps for the split quadratic forms in ranks 1 over fields of size 2 and 3, and rank 2 over the binary field, and verifies the group-order recurrence and simplification of the group index. It prints `DIAMOND_JORDAN_OK` on success. The proof of all-field and all-rank claims is the symbolic argument in RESULT.md; enumeration is corroboration, not certification. No independent external review has been performed.
