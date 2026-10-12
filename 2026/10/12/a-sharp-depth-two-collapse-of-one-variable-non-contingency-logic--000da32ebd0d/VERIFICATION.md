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
# Verification evidence

The accompanying `check_normal_form.py` enumerates every valuation and pointed world of the complete irreflexive frame with \(n\) worlds, for all integer sizes \(1\leq n\leq9\). The program independently refines truth partitions at modal depth zero, one, two and three, taking all Boolean unions of previously available type classes before applying \(\Delta\). It checks that the predicted exact spectra are \((4,4,4,4)\), \((4,16,16,16)\), and \((4,16,64,64)\) in the three respective size regimes; it also compares the explicit four distinguishing formulas with the combinatorial type description and applies \(\Delta\) to every Boolean union of those types. It checks that \(\Box p\) is not among the definable truth sets for sizes at least two. `CHECK_OUTPUT.txt` records the real successful run ending in `VERIFY_OK`.

Run with Python 3.8 or newer: `python3 check_normal_form.py`.

**Scope of certification:** only the stated finite instances are exhaustively computed. The universal claim for all finite sizes rests on the symbolic successor-class argument and structural induction in `RESULT.md`. Originality rests on the comparison set described in `REVIEW.md` and `AUDIT.json`, not on the checker. No independent audit was performed.
