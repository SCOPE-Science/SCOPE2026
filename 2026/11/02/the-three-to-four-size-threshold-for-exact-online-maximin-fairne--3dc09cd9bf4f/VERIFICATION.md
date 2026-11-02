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

Run `python verify.py` with Python 3.9+ using only the standard library. The script exhaustively tests the canonical constructive rule on all size-\(1\)/size-\(r\) histories of length fourteen for the two positive values \(r=2\) and \(r=3\). It recomputes MMS independently by enumeration of high-good and low-good splits, checks both individual count conditions equivalent to injective itemwise upgrades, and checks EFX inequalities. It separately enumerates the five-item obstruction for all integers \(4\le r\le30\).

Executed output:

`VERIFY_OK histories=32768 prefix_checks=458752 ratios=2,3 obstruction_ratios=4..30`

The computation verifies finite instances only. The general theorem and sharp impossibility are proven symbolically in RESULT.md. The algorithm assumes strictly positive identical additive valuations with exactly two denominations and two agents; its failure or success is not asserted outside that model. No external scientific audit was performed.
