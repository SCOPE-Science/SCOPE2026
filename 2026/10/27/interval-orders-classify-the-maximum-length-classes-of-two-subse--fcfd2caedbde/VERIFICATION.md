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

# Reproducibility

Run `python3 verify_interval_simon.py` with the Python standard library. The program independently (i) performs exhaustive breadth-first state exploration under append-one-letter updates and records minimum representative lengths, and (ii) enumerates all length-\(2q\) endpoint words in which each of \(q\) letters occurs exactly twice, evaluating pair subsequences and interval order relations separately. It validates both directions of the bijection, equality with the deepest automaton layer, and the depth criterion (all diagonal pairs present). The direct loops over positions are independent of the state-transition recurrence.

Observed execution:

```
q=1 all_classes=3 deepest_classes=1 doubled_words=1
q=2 all_classes=16 deepest_classes=3 doubled_words=6
q=3 all_classes=152 deepest_classes=19 doubled_words=90
q=4 all_classes=2326 deepest_classes=207 doubled_words=2520
q=5 all_classes=52132 deepest_classes=3451 doubled_words=113400
INTERVAL_SIMON2_PASS
```

# Limits

The computation enumerates alphabets of sizes at most five and is **not** an all-size proof. The universal classification follows from the first-last reduction, the interval-order bijection, and the explicit downset-based realization in `RESULT.md`. The numerical values of labeled interval orders and the asymptotic constants are existing external mathematics, cited rather than established by this checker. No external independent audit is represented.
