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

The exact coefficient tests are reproducible with `python verify.py` in a directory containing this file and the accompanying result. The program constructs the coefficient arrays from first-cover transitions, exhaustively enumerates the proper words over alphabets of sizes two through five within the stated ranges, checks direct subsequence universality for short words, and reports `ALL CHECKS PASSED` when the comparisons succeed.

The general coefficient identity follows from the arch decomposition proved in RESULT.md; the finite tests are corroboration only. The asymptotic renewal assertions are mathematical consequences of the stated independent geometric waiting times and standard finite-moment renewal theorems, not extrapolations from finite samples. No independent audit was performed.
