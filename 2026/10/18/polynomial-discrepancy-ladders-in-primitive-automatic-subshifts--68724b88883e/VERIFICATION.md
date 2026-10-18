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

Run the complete embedded `verify.py` with Python 3 standard library by executing `python3 verify.py` after extracting it. In the assessed execution the program reported **1,822 passed integer diagnostics**. The main sampling covers \(1\le r\le3\), \(1\le d\le5\), \(0\le m\le7\). It independently expands full substituted words for feasible depths, compares every column function with the composed-column enumeration, tests primitivity and adjacent-zero witnesses, checks all nonconstant/constant kernel classes, and checks the binomial recurrence in broader ranges of parameters. All displayed counts are checked using integers, not floating-point approximations.

The universal proof in `RESULT.md` works for all \(r,d\ge1\) and \(m\ge0\). The finite computations are diagnostics only; they do not replace exhaustive mathematical reasoning. The tameness/nullness and amorphic-complexity consequences use Gröger–Krawczyk Theorems A and B. A historical equivalent construction has not been excluded, and independent scientific audit has not been performed.
