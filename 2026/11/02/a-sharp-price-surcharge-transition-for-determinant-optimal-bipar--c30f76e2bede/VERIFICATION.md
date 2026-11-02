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

# Verification notes

Execute `python3 verify.py` from the same directory; requirements are Python 3, NumPy, and SciPy. The recorded execution yielded:

```
EXACT_DETERMINANTS_OK 8
DIRECT_DETERMINANTS_OK 175
OPTIMALITY_POLYNOMIAL_AND_BUDGET_OK 175
ASYMMETRIC_FEASIBLE_COMPARISONS_OK 2100
UNRESTRICTED_SLSQP_COMPARISONS_OK 18
CRITICAL_WINDOW_CHECKS_OK 18
ALL_CHECKS_PASSED
```

Eight rational Gaussian eliminations compare the exact grounded determinant with the spectral expression for \(m=3,4\), including complete deletion of the designated matching. Numerical determinant tests cover \(3\le m\le9\). Other checks verify budgets, the quadratic first-order equation, random asymmetric feasible competitors, and independently optimized ungrouped weights for \(m=3,4,5\). The scaling checks concern finite sizes and are not substitutes for the limiting argument.

The analytical certificate is the strict log-determinant concavity, injectivity of the simple-graph grounded-incidence representation, Matrix–Tree spectral factorization, derivative sign classification, and asymptotic expansion in `RESULT.md`. The code checks sampled instances and therefore cannot independently establish global or infinite-dimensional claims. Independent audit has not been performed.
