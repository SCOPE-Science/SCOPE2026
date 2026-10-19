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
# Verification protocol and limitations

Run `python3 verify.py` in the same directory as this file. The program uses the binary morphism directly and independently computes sequence symbols from their base-\((r+2)\) digit patterns. It verifies the greedy arch count, each listed forbidden subsequence by deterministic greedy matching, and the **exact cardinality of all** forbidden words at length \(2^k+1\) using the recurrence on earliest-occurrence positions. The shortest absence property follows because the arch count equals \(2^k\).

The two finite base words are checked by enumerating all thirty-two length-five binary patterns. The executed ranges are \(r=1\) with \(2\le k\le8\); \(r=2\) with \(2\le k\le6\); \(r=3\) with \(2\le k\le5\); \(r=4,5\) with \(2\le k\le4\); and \(r=7\) with \(2\le k\le3\). The exact program output ends in `VERIFY_OK`.

These tests do not constitute an exhaustive verification over all parameters. The all-parameter result rests on the explicit induction and boundary counts in `RESULT.md`. No independent audit, external certification, or formal proof assistant verification was performed.
