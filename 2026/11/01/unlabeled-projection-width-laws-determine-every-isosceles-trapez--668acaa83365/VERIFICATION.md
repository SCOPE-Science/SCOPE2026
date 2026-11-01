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

Deterministic scientific checks: `python3 check.py`, using the standard library only.
The checker compares the piecewise support-function width against direct vertex projections, differentiates independently measured angular-preimage probabilities away from singularities, verifies normalization by exact antiderivatives across phase boundaries, and checks the stated parameter inversions on representative strict and boundary configurations.

Verified run output:

```
DIRECT_VERTEX_VS_TWO_BRANCH_WIDTH_PASSED
PIECEWISE_DENSITY_VS_INDEPENDENT_CDF_DERIVATIVE_PASSED
NORMALIZATION_ALL_PHASES_AND_ENDPOINTS_PASSED
INVERSE_PARAMETER_FORMULAS_AND_LOWER_ENDPOINT_CLASSIFICATION_PASSED
ALL_CHECKS_PASSED
```

These finite checks are corroborative. The unrestricted quantifiers over positive dimensions and aspect ratios follow from the analytic proof in RESULT.md. No independent audit has yet been performed, and no noisy-sampling claims are made.
