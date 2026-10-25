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

Run `python check_seventh_order.py` with Python 3, NumPy, SciPy, and SymPy installed. The script produces the following success markers:

```
EXACT_DISK_CDF_SEVENTH_ORDER_OK
ELLIPSE_AFFINE_DISK_FIFTH_ORDER_OK a=1 b=1
ELLIPSE_AFFINE_DISK_FIFTH_ORDER_OK a=2 b=1
ELLIPSE_AFFINE_DISK_FIFTH_ORDER_OK a=3 b=2
ELLIPSE_AFFINE_DISK_FIFTH_ORDER_OK a=1.5 b=0.7
CURVATURE_RADIUS_SHARP_SIGN_OK m=2 sign=positive
CURVATURE_RADIUS_SHARP_SIGN_OK m=3 sign=negative
CURVATURE_RADIUS_SHARP_SIGN_OK m=4 sign=negative
ALL_SEVENTH_ORDER_COVARIOGRAM_CHECKS_OK
```

The disk test uses exact symbolic integration of the known two-disk intersection formula. Ellipse tests use an affine transformation of the disk covariogram, independent of graph-chart calculations. The remaining quadratures check the closed-form curvature-radius energy evaluations and distinguish both signs. These are finite cross-checks; no claim of independent audit or universal computational certification is made.
