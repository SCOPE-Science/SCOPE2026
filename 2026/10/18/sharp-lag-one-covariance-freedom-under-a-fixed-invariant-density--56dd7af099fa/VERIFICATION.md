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

# Verification record

The analytical proof gives the invariance necessity/sufficiency for every measurable control by the half-branch CDF uniqueness argument. It derives the covariance as a linear functional of a pointwise bounded control, thereby proving global sharpness and attainment rather than relying on finite grid search. It establishes the selected-map label law by a conditional transfer-density computation.

Run `python3 verify.py` using Python 3 without optional dependencies. On execution, the program prints:

```
SHARP_COVARIANCE_INTERVAL 223/15360 913/15360
VERIFY_OK
```

Checks include exact rational integration of the canonical covariance bounds, symmetric intermediate value and width; pointwise admissibility at sampled rational values; and exact balance identities for several rational choices of branch parameters. These finite checks cannot prove the statement for arbitrary real parameters or every measurable control. No independent audit has been performed.
