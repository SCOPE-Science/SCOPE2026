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

The standalone `verify.py` was executed using Python, NumPy and SciPy. It returned `VERIFY_OK: patch integrals, divergence flux, 9 polyhedral hulls, 300 support directions, facet geometry, radii and scaling` and `unit_volume=3.285954792089683 unit_area=11.354982076904077`.

The verifier computes the two one-dimensional integrals by independent quadrature, constructs polygonal approximations to the three input disks with 64, 256 and 1,024 boundary points per circle at three scales, and computes the three-dimensional convex hull and its area and volume with SciPy's ConvexHull. Both volume and area errors decrease with refinement; at 1,024 points per circle their relative errors are below \(10^{-5}\). It also checks 300 independently sampled support directions against dense direct circle samples, the equilateral triangle's side lengths/area/plane height, scale covariance, and the extremal support directions.

All these tests are finite. An approximated circle has smaller hull volume and surface area than the exact disk hull, and the convergence observed numerically is not used as an infinite proof. The continuum theorem rests on the supporting-face classification, exact surface Jacobian, divergence theorem, and analytic one-dimensional integration in `RESULT.md`. The proof and tests do not establish originality against all historical publications or independently certify any statement.
