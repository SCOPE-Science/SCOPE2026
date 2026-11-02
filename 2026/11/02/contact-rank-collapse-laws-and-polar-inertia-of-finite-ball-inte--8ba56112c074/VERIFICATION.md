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

# Reproduction notes

Run `python VERIFY.py` with NumPy and SciPy. The checker generates a regular triangle's active unit normals, computes exact radial exit distances from the intersection of equal balls, and confirms the asymptotic leading volume \(3\sqrt3\) and relative first correction \(-\varepsilon/R\) as \(\varepsilon\) decreases. It checks the exact volume \(2\pi R\varepsilon^2+(4\pi/3)\varepsilon^3\) of a three-dimensional lens arising from antipodal active centers. It independently estimates the rank-two collapse of an equilateral active triangle embedded in three-space with Sobol integration, and compares a nonsymmetric triangle with the polar-inertia correction computed from its polygon triangulation.

The checker outputs `ALL_CHECKS_PASSED` and `NONREGULAR_SECOND_ORDER_PASSED` when all its assertions succeed. These are numerical and symbolic spot checks, not infinite-dimensional certification or a substitute for the analytic proof in `RESULT.md`.

Mathematical scope is fixed finite point configurations with a common enclosing-ball radius and positive-spanning active contacts. No claims are made about unequal-radius intersections or uniform statistical estimates. Independent audit has not been performed.
