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

Run `python3 check_square_roots.py`. It requires only the Python 3 standard library and returns `VERIFY_OK` and `CASES 23` when all comparisons pass. It constructs the morphic words, enumerates every distinct length-\(p\) factor whose square occurs within each tested finite prefix, and tests exact equality with the predicted set. It separately checks the base-digit characterization. The finite checks cover bases 3 through 7 and available substitution depths up to 4; the checker does not prove universal coverage at infinitely many lengths. The structural argument in `RESULT.md` proves the infinite theorem. No independent audit has been performed.
