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

The proof is self-contained in `RESULT.md`. The accompanying standalone `check_joint_ellipsoid.py` requires Python 3 and NumPy. Execute `python check_joint_ellipsoid.py`. The actual execution returned `ELLIPSOID_JOINT_SECTION_SHADOW_CHECKS_PASSED`.

The checker conducts these independent computations: direct two-dimensional ellipse calculations by restricting the inverse ellipsoid quadratic form to a random plane; direct projection ellipses from the compressed shape matrix; comparison with the derived determinant formulas on 1,200 random normals across three triaxial ellipsoids; inversion of squared normal coordinates and the joint-density Jacobian; 240,000 random directions per selected example of dimension 3–5 for covariance and upper-tail dependence; and 30,000 independent beta-product reconstructions of a seven-coordinate Dirichlet vector.

These tests can detect normalization, algebraic-inversion, and geometry errors, but finite samples do not prove association or distributional equality. Those statements are proved analytically by the gamma–Dirichlet/beta-product construction, a product-measure covariance argument, and exact finite-dimensional change of variables. Numerical thresholds used in the simulation are deliberately coarse, and no claim is made that the tests exhaust the continuum of normals or possible ellipsoids.
