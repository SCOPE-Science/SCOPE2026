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

# Reproducibility and limits

Run `python checker.py` with standard Python 3. The checker uses exact integer and rational arithmetic; in this package it reports 693 passing exact assertions, including exhaustive enumeration of 7,450 admissible finite subsets on the first three blocks, 48 deterministic sign-vector comparisons, 27 rational balanced-mass tests, and 495 indexed capacity checks. The tests support formulas but cannot certify the statements for arbitrarily many blocks or all bounded sequences; the full proofs are in `RESULT.md`. The weighted directedness comparison uses arbitrary integer anchor and block index, not finite enumeration. No independent audit has been performed.
