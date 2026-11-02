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

The exact group-element classification, variance identity, CDF and optimizer implications are given in `RESULT.md`. Execute the included standalone `check.py` with the Python standard library: `python check.py`. The script independently searches 1,760 finite deck-image configurations, verifies the exact fourth-moment rational coefficient, checks 40 empirical CDF comparisons, checks 30 independent circle–rectangle area quadratures, and compares optimizer regimes with quadrature. It reports:

```
GROUP_ORBIT_MINIMUM_INDEPENDENT_RECONSTRUCTION_PASSED 1760
EXACT_FOURTH_MOMENT_AND_VARIANCE_CONSTANT_PASSED
CDF_PIECEWISE_INDEPENDENT_SAMPLING_PASSED 40
INDEPENDENT_RECTANGLE_QUARTER_DISK_AREA_PASSED 30
OPTIMIZER_PHASE_DIAGRAM_AND_SHARP_VARIANCE_PASSED
ALL_CHECKS_PASSED
```

Finite experiments cannot establish the universal claim. Its critical all-parameter proof steps are exhaustive parity classification of deck transformations, elementary planar-area integration, the identity \(\operatorname{Var}(U^2)=(a^4)/180\), and strict positivity of the cap-variance derivative. No independent audit was conducted. A published prior-art priority search is necessarily nonexhaustive; the geometry and nearest-clone exclusion description in the cited primary sources predate this calculation.
