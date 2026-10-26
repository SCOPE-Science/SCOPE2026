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

# Verification of alternating two-jumble radius-two count

Run `python3 verify_alternating_jumble.py` with Python 3 standard library. The script uses independent longest-common-subsequence dynamic programming on every binary word of even length 2 through 12. It compares the resulting threshold with the equal-adjacency criterion, checks the balanced counts 2, 6, 19, 53, 126, 262, and compares the quartic formula with the run-composition sum for m=1 through 499. The observed result is `VERIFY_OK`.

The finite check does not prove the general case and is not an independent scientific audit. The general proof is in RESULT.md; in particular the critical steps are the greedy alternating embedding formula and the non-first deletion reduction of equal adjacencies.
