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

# Computational verification

With Python 3.10+ and the dependency from `requirements.txt`, run `python verify.py`.

This independently performs an exact ordered-height polynomial integral for the triangle-area first moment, computes the covariance matrix by direct slice integration, verifies the squared-area determinant identity's resulting rational formula, factors the full derivative exactly and checks endpoint expansions. It also directly samples 120,000 triangles for each of five test cases, using independent point-in-trapezoid draws and determinant-based triangle areas, including a sheared trapezoid.

Expected success markers:

```
EXACT_AREA_MOMENTS_AND_MONOTONE_VARIANCE_PROFILE_PASSED
DIRECT_UNIFORM_TRIANGLE_SIMULATION_PASSED
ALL_CHECKS_PASSED
```

The exact symbolic identities are finite computations of algebraic integrals. The universal claims additionally require the analytic arguments in RESULT.md: positive derivative factors, affine normalization, and strict integral inequalities. Monte Carlo examples are not a proof of all shape parameters. No independent mathematical audit or independent validation is asserted.
