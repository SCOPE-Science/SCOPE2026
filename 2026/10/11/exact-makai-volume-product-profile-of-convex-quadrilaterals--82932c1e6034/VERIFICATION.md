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

The exact claim follows analytically from affine diagonal normalization, the exhaustive six pairwise vertex-difference constraints defining the polar, complementary corner geometry and exact right-triangle area calculation. Sharp endpoints are proved through the nonnegative deficit expression and Eggleston's triangle-only equality theorem, together with an explicit continuous family of trapezoids.

Run `python verification/check_quadrilateral.py` in a Python 3 environment using only the standard library. The checker enumerates all ordered differences for a deterministic set of 148 rational parameter pairs, reconstructs all polar-polygon vertices as intersections of rational constraint lines, sorts the polygon vertices, applies the shoelace formula in exact arithmetic, and compares with the claimed formula. Expected output includes `EXACT_POLAR_INTERSECTIONS_OK 148`, `square 2`, `trapezoid 16/9`.

The checker verifies finitely many exact examples and does not certify all real parameter pairs. Analytic proof supports that continuum claim. No independent audit or outside mathematical verification has been conducted.
