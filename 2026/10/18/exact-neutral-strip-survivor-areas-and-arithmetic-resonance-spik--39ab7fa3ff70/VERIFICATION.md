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
Run `python3 verification/neutral_strip_check.py` with Python 3.9 or newer. The self-contained program uses only Python's standard library. It reconstructs the neutral-strip normals from the matrix, intersects closed half-planes by polygon clipping, and independently computes Euclidean area by the shoelace formula. Exact fractions check selected rational rotations; floating checks selected nonresonant and higher-denominator rational cases. A successful run prints `NEUTRAL_STRIP_POLYGON_AREA_CHECKS_OK`.

# Scope of verification
The exact-rational tests check parameters \(c=1,2,3\) with \(h=1\), including the saturated all-time polygons and separate two-step areas. Floating tests include an irrational angle and a rational angle of reduced denominator \(11\) at multiple horizons. These are reproducible finite checks of the formula and normalizations, not a substitute for the mathematical proof of the infinite-time limit or of dense arithmetic discontinuities. The source's qualitative polygon/ellipse dichotomy is prior knowledge, not re-certified independently here.
