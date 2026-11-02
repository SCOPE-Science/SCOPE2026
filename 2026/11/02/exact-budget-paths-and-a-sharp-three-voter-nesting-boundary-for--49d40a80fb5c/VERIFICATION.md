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

# Reproduction and scope

Run `python3 verify_mes.py` using Python 3 standard libraries only. The program implements exact budget accounting and determines each candidate's minimum feasible uniform contribution by sorting supporter balances. It then independently predicts the sunflower result from the closed-form floor thresholds and compares the two for 156,245 exact rational instances. It separately replays the three-voter, four-candidate counterexample at both budgets, asserting exact choices and prices. Expected terminal line:

```
PASS: 156245 exact sunflower formula cases; three-voter nonnesting witness, budgets 3 and 4.
```

The nontrivial symbolic steps needed beyond these tests are: common-core projects cost \(1/n\) per supporter and dominate every private price \(1/n_j\) with \(n_j<n\); once the core is exhausted, group balances remain equal and independent; private purchases occur precisely at the stated aggregate-funding thresholds; and two distinct approval ballots decompose into the common intersection plus disjoint differences. The explicit three-voter trace supplies the constructive sharpness witness.

Limits: finite checking is not an exhaustive certificate over all voter counts, candidate counts, or real budget values. The claim is restricted to approval utilities, unit costs, fixed cross-budget tie priority and the uncompleted purchase phase. No independent audit has been conducted.
