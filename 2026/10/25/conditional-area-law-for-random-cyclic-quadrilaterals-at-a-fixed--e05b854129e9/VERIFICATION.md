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
# Reproducibility of the conditional area law

Run `python verify.py` with Python 3, NumPy, and SciPy. The executed checker generated 450,000 independent random four-vertex configurations on the unit circle, used a Cartesian shoelace area and determinant/dot-product diagonal-angle calculation, and compared the first two unconditional area moments against their stated values. Five disjoint narrow diagonal-angle bins were checked against the exact conditional first and second moments.

Four additional fixed angles were tested using 350,000 independent cosine-variable pairs each. For each, the checker independently compared four conditional CDF values against the displayed one-dimensional integral and compared simulated first two moments. It also rechecked the already-known angle marginal as a consistency test.

Actual terminal success markers from `verify.py`:

```
CARTESIAN_AREA_AND_TWO_GLOBAL_MOMENTS
CARTESIAN_CONDITIONAL_MEAN_VAR_OK
CONDITIONAL_CDF_1D_QUADRATURE_OK
KNOWN_CROSSING_ANGLE_MARGINAL_RECONSTRUCTED_OK
ALL_QUADRILATERAL_CONDITIONAL_AREA_CHECKS_OK
```

Monte Carlo, numerical quadrature and success markers are reproducibility checks, not a proof of universal quantified statements. The analytic proof is given in `RESULT.md`. No independent mathematical audit has been performed.
