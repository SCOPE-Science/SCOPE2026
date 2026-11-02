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

# Verification and reproducibility

The complete analytic proof appears in `RESULT.md`. The essential equalities follow from first-step equations for each target, the exact order-statistic maximum, a strict budget-improvement argument, and a one-dimensional strictly convex objective. No numerical threshold or finite sample is used as a substitute for an all-parameter argument.

Run from the directory containing the embedded files:

```bash
python3 verify.py
```

The reproducible output is:

```
VERIFY_OK 249020 checks; exact rational hitting systems and finite optimization probes
```

`verify.py` uses only Python 3's standard library. For \(3\le k\le8\) and 20 deterministic rational rate vectors per size, it solves the killed-generator linear equations for every target using exact rational Gaussian elimination and checks all starting states against the claimed first-step formulas. For \(3\le k\le10\) and 150 deterministic price/budget scenarios per size, it checks optimizer positivity, exact-budget saturation within floating-point tolerance, the proposed objective, and 200 independently generated feasible competing allocations per scenario. These tests also sample just above and below the sharp price threshold. Randomized finite probing cannot certify optimality for all positive real inputs; that conclusion relies on the mathematical argument.

All executable checks relate only to the enclosed claim. Independent external validation and scholarly priority review remain unperformed.
