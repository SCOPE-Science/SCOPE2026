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

Execute `python verify_rooted_hardy.py` with the Python 3 standard library. The checker is deterministic, seeds its pseudorandom sample, and solves the secular equation by monotone bisection within its first pole interval. It numerically reconstructs the ground-state energy identity from elementary trigonometric integrals, tests a range of balanced transfers, and checks the quadratic stability and \(m^{-2}\) many-arm expansion against small perturbations and finite branch counts.

Expected output:

```
POSITIVE_GROUND_STATE_ENERGY_AND_MAJORIZATION_OK 252
QUADRATIC_EQUAL_BRANCH_STABILITY_OK 4
INFINITE_BRANCH_ENDPOINT_MASS_ASYMPTOTIC_OK 9
ALL_ROOTED_METRIC_TREE_HARDY_CHECKS_OK
```

These finite tests are not proof of universal statements. The rigorous argument is the variational ground-state transform, strict convexity/majorization comparison, and implicit-function expansion in `RESULT.md`. The absolute normalization is arclength on every edge; all graph vertices have measure zero. No independent audit has been performed.
