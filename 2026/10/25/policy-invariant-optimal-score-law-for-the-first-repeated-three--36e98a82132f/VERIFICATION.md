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
# Reproducible checks

Execute `python verify.py` in this folder using Python 3 standard library. Verified output:

```text
DECKS=90 STATES=11867 OPTIMAL_MEAN=271/90
ALL_MEAN_OPTIMAL_POLICIES_SAME_SCORE_DISTRIBUTION= (0, 0, 33, 30, 21, 5, 1)
SAMPLE_OPTIMAL_POLICY_FORWARD_ENUMERATION= (0, 0, 33, 30, 21, 5, 1)
OPTIMAL_SCORE_VARIANCE=7469/8100
VERIFY_OK
```

The program exactly enumerates all 90 possible card words and all Bellman choices at all memoized states, computes coefficientwise minimum and maximum score polynomials among policies attaining the optimal expected score, and separately simulates a lexicographic Bellman-optimal policy on every full deck word. All results use integer or rational arithmetic. No statement about larger decks and no independent audit is certified.
