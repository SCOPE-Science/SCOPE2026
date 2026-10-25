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

Run `python3 CHECK.py` in the directory containing this file. This standard-library-only script performs four independent finite tests using integer arithmetic and prints their exact totals. Expected output:

```
PASS binary sequences lengths 0..12: 8191
PASS full suffix-state invariant checks lengths 0..10: 2047
PASS arbitrary-positive-integer words lengths 0..3, values 1..9: 820
PASS counterexample family k=3..20: 18
```

The checker enumerates both greedy trajectories and optimal final costs by finite-state dynamic programming. For the suffix inequalities, it independently computes exact Bellman values at bounded integers. For the four-item family, it checks both the greedy path and the optimal value. These tests do not establish infinitely many sequence lengths or real scaling parameters: the analytic induction and explicit construction in RESULT.md provide those proofs.

The scientific analysis is limited to two agents with identical positive additive singleton values in the exact ratio \(2\); zero-valued arrivals, heterogeneity, and a different temporal objective are not covered. Publication priority has not been independently validated. No independent audit was conducted.
