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

# Reproducibility and proof boundary

Run `python3 CHECKER.py` in the same directory. It uses only the Python 3 standard library. It performs three separate checks: direct bit-mask enumeration of all subsequence words against an LCS dynamic program for all 1,022 binary inputs through length nine; exhaustive LCS-output analysis of all 8,190 nonempty binary words through length twelve, including the exact four shortest exceptions; and exhaustive analysis of all 1,024 five-run parameter tuples with each positive run length at most four. The reported successful marker is `ALL_FIVE_RUN_LCS_CHECKS_PASSED`.

The checker includes all tie branches, including skips when two compared symbols agree, so it enumerates **all** distinct LCS words rather than one algorithmically selected solution. The direct enumerator is an independent recurrence-free check for the smaller domain. The unrestricted five-run theorem is proved by run-pattern partition and coordinatewise embedding bounds in `RESULT.md`; no finite experiment is used as an infinite proof. External independent scientific audit has not occurred.
