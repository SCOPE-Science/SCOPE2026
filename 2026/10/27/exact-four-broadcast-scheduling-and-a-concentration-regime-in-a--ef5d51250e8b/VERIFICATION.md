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

The proof in RESULT.md is analytic and applies to every real parameter \(0<p<1/2\), \(0<b_1,b_2<1\) with \(b_1\ne b_2\), and every integer silence budget \(G\ge0\). The accompanying `verify.py` independently calculates final consensus error by direct rational matrix iteration and by the derived closed formulas, checks every schedule with \(G\le10\) for nine distinct rational parameter families, and checks the concentrated-optimum example exactly. Observed stdout: `CHECK_OK exact_schedules= 3168 optimal= (0, 10, 0) error= 903373787686956792814241/4882812500000000000000000`.

The exact formulas, convexity step, polynomial root count and endpoint sign argument are the mathematical proof. Enumeration is only a check of selected finite instances and is not asserted to establish universal originality or correctness. No independent scientific audit has been performed.
