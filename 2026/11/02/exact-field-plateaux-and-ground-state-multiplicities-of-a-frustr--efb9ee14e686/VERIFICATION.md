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

# Mathematical and computational verification

The full proof, including equality cases, appears in `RESULT.md`. The down-spin edge count, exact transfer eigenvalues and odd-length kink count apply for every integer \(n\ge3\); the finite tests below verify examples rather than supplying an infinite proof.

`checker.py` is self-contained Python 3 standard-library code. Execute `python3 checker.py` and compare with the complete `CHECK_LOG.txt` output. The verification computes all \(8^n\) spin assignments for four short lengths and separately solves the exact eight-state min-plus ring closure for 28 lengths, at six representative fields \(0,1,2,3,4,5\) in units of the common exchange constant. Exact integer arithmetic is used throughout. The tests include both critical lines, both open phases, and odd/even tube lengths.

No independent scientific audit has been performed. Historical novelty is supported by comparisons with the named original literature but cannot be conclusively certified by finite searches; a specific inaccessible zigzag-ladder primary article is described in `REVIEW.md` and `AUDIT.json`.
