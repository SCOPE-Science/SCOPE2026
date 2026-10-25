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

Run `python verify_covering.py` with NumPy and SciPy installed. The checker independently generates a deterministic low-discrepancy sample of 262144 spherical directions and compares the actual fourteen-site support statistic to the chamber quadrature at six thresholds. It checks the exact 24 local minimum directions, the tangent-region coefficient identity, the disjoint-cap formula, several small-threshold ratios, and the 2002 published numerical near-covering benchmark.

On the supplied code, the following checks executed successfully:

```
INDEPENDENT_TANGENT_POLYGON_CONSTANT_IDENTITY_OK
PUBLISHED_COVERING_BENCHMARK_AND_EXACT_DISJOINT_CAP_BRANCH_OK
QUADRATIC_ONSET_CONSTANT_AND_24_GAP_VERTICES_OK 38.88415685179
DIRECT_SPHERICAL_SOBOL_VERSUS_CHAMBER_QUADRATURE_OK 262144
ALL_FOURTEEN_SITE_COVERAGE_CHECKS_OK
```

These numerical checks do not establish the exact covering theorem for infinitely many directions, its asymptotic limit, or novelty: see the independent mathematical proof in RESULT.md. The original 2002 configuration and covering radius are not claimed as new. No external mathematical validation has been performed.
