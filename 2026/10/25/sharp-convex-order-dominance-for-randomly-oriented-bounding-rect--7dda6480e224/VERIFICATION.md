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

# Reproducibility and limits

The proof establishes the all-body convex order by an exact boundary-tangent identity and Jensen's inequality. Parseval gives the infinite variance series; strict equality follows from the first Fourier mode and convexity of the underlying body. Numerical checks are corroboration only, not independent mathematical certification.

Execute `python3 verify.py` using the standard Python 3 library. The program independently constructs bounding boxes from rotated vertex coordinates and sums projected tangent-edge lengths for 81,920 polygon-orientation pairs. It compares numerical orientation averages with the exact Fourier variance series for five convex polygons and tests multiple convex penalty functions, the first-mode angular-dispersion bound, the exact rectangular survival formula and the equilateral triangular spectral selection rule. The computations cannot certify the theorem for arbitrary convex bodies or exclude all earlier literature.

Completed run output:

```text
DIRECT_ROTATED_VERTEX_SUPPORT_VS_TANGENT_INTEGRAL_OK 81920
FOURIER_VARIANCE_COVARIANCE_IDENTITY_OK 5
SHARP_RECTANGLE_EQUALITY_AND_NONRECTANGLE_STRICTNESS_OK
UNIVERSAL_CONVEX_RISK_COMPARISON_OK 6
POSITIVE_STABILITY_DEFECT_FOR_NONRECTANGLES_OK
RECTANGLE_ALL_THRESHOLD_CDF_FORMULA_CHECK_OK
EQUILATERAL_TRIANGLE_TWELVEFOLD_SPECTRUM_OK
ALL_BOUNDING_RECTANGLE_PERIMETER_CHECKS_OK
```

The proof and numerical checker address common-uniform-angle rotated bounding-box **perimeter**, not box area or minimum-area enclosures. Unindexed mathematical predecessors remain a historical-priority risk.
