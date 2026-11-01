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

# Verification status

The analytic proof is given in `RESULT.md`. A standalone Python 3 checker, `verify.py`, requires no third-party packages and can be invoked with `python verify.py` from the extracted package directory. It performs exact-rational planar endpoint/branch checks, independent planar polygon clipping across seven truncation ratios, direct area quadrature for five square-based frusta, off-axis perturbation checks, and numerical dimensional-crossover diagnostics. Observed output:

```
EXACT_PLANAR_THRESHOLD_AND_BRANCH_IDENTITIES_PASSED
INDEPENDENT_PLANAR_CONVEX_CLIPPING_PASSED 7
INDEPENDENT_SQUARE_BASE_VOLUME_QUADRATURE_PASSED 5
DIMENSIONAL_CROSSOVER_AND_MONOTONICITY_DIAGNOSTICS_PASSED
ALL_CHECKS_PASSED
```

Exact theory supplies the general proof for every dimension and centrally symmetric base; the finite computations are supporting diagnostics. Floating-point monotonicity near machine precision is checked up to roundoff, not asserted as exact. Independent mathematical audit has not been performed.
