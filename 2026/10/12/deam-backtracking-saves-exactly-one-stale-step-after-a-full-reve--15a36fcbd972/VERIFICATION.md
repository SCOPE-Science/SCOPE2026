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
The package verifies DEAM's exact equal-magnitude permanent-reversal response.

`verify.py` reconstructs the source full-conflict recurrence, checks the momentum and parameter-increment closed forms, certifies the signs through the reversal using a rational enclosure of \(\pi\), and compares the source backtrack against the same angle-adaptive momentum rule with backtracking suppressed.

The computations are transcription guards. The stale-step counts are proved from the exact recurrences in `RESULT.md`.
