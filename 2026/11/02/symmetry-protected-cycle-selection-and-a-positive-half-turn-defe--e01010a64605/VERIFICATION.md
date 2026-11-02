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

# Reproducibility and verification

The analytical proof is in RESULT.md, and the executable cross-check is `verify_abel.py`. Its execution from the provided source file printed:

```
kappa= 0.04 D= 0.00631172080165 Floquet linear= 0.0872664625997 error at 0.008= 5.547e-09 error at 0.004= 1.349e-09
kappa= 0.25 D= 1.30758273289 Floquet linear= 5.58505360638 error at 0.008= 0.0003519 error at 0.004= 8.8e-05
PASS: 42 numerical identity and convergence checks
```

For each parameter, the script solves the full-period condition in the reciprocal coordinate, integrates its variational equation, evaluates the half-period difference, and compares opposite signed perturbations. It also differentiates the closed formula for the profile and verifies the predicted error reduction. The rigorous infinite-family argument is independent of finite sampling and invokes an explicitly identified external uniqueness theorem with hypotheses checked in the proof. These results are not independent scientific audit or external validation.
