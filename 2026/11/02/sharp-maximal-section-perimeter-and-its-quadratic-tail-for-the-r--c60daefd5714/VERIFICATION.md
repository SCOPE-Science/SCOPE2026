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

Run `python3 check.py` from this directory. It needs the Python standard library only. The script constructs the fourteen vertices and all twenty-four edges of the rhombic dodecahedron, computes section polygons by a planar convex hull rather than reusing the analytic clipping formula, and evaluates their Euclidean perimeters.

The reproducibility check compares four coordinate-axis orientations against \(8\sqrt2\), verifies 12,000 seeded random orientations against the global bound, tests fifteen local cusp ratios near an axial normal, and compares 500 randomly chosen clipping-chamber orientations with the exact local formula. All tests completed successfully.

The analytic theorem proves a universal bound and an asymptotic probability. Finite numerical sampling alone cannot prove either; the exact projection argument and the uniform local polygon formula are indispensable. Unchecked cases are controlled by those arguments, not extrapolation from finite data. Independent audit remains unperformed.
