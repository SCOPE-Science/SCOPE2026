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

# Reproducibility and scope

Execute `python verify_bistar.py` using Python 3.10 or newer; no external dependencies are required. An actual execution yielded:

```
EXACT_ZERO_SUM_QUADRATIC_IDENTITY_OK 1550
CRITICAL_ROOT_INTERVAL_AND_RANK_OK 576
FIXED_LEAF_BUDGET_BALANCE_DIAGNOSTICS_OK 1521
ASYMMETRIC_LARGE_BRANCHING_LIMIT_DIAGNOSTICS_OK
ALL_UNBALANCED_DOUBLE_STAR_NEGATIVE_TYPE_CHECKS_OK
```

The exact-arithmetic test enumerates every pairwise distance in selected double stars and compares the resulting zero-sum quadratic form against the claimed completed-square identity. The finite numerical tests check critical roots, endpoint kernel signs, strict order under balancing for many leaf budgets, and asymptotic behavior. The analytic proof in RESULT.md, not those tests, establishes all universal inequalities and limits. Independent scientific audit has not been performed.
