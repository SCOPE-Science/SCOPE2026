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

The standard-library script `verify_italian_rook.py` separately checks label assignments against literal graph neighborhoods and compares observed minima and labelled optimizer counts with the formulas in RESULT.md. Execute `python3 verify_italian_rook.py`.

Checks executed successfully: 1,152,264 complete assignments spanning fourteen small graph sizes; 696,634 additional assignments of weight at most the predicted optimum over four larger graph sizes. Each reported comparison passed. The restricted-weight enumeration does not establish anything about higher-weight labels; no finite check certifies the infinite theorem. The proof in RESULT.md handles every positive integer dimension.

No independent mathematical audit or bibliographic-priority certification has been performed.
