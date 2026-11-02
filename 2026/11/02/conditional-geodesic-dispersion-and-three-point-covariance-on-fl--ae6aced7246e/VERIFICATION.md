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

# Reproducible verification

Execute `python checks/verify.py` with packages in `requirements.txt`. The checker expands the two interval-polynomials in the circular correlation using exact symbolic integration and verifies the exact fractional moments. Separately it integrates squared quotient distances obtained by enumerating the two nearest glide parity classes on 28 anchor/shape grids, then averages 192 independently integrated conditional values to check the shared-anchor covariance. Recorded execution output:

```text
EXACT_SECTION_CORRELATION_AND_BETA_MOMENTS_PASSED
INDEPENDENT_DECK_MINIMUM_GRID_PASSED 28
INDEPENDENT_SHARED_ANCHOR_COVARIANCE_GRID_PASSED 192
EXACT_SHARP_ENDPOINTS_AND_SCALE_NORMALIZATION_PASSED
EXACT_SHARED_EDGE_COUNT_AND_ASPECT_RECONSTRUCTION_PASSED
ALL_CHECKS_PASSED
```

The exact algebraic proof is contained in `RESULT.md`. Midpoint-grid tests are numerical corroboration and are not certification of statements over infinitely many geometric parameters. Independent audit has not been performed.
