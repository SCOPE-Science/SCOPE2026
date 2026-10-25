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
# Verification notes

The theorem has a complete analytic proof in `RESULT.md`, comprising: an exact integral formula from equal-length projected intervals; a support-function characterization of first contact; localization to precisely two antipodal normal caps by positive curvature; second-order Taylor expansion with the curvature-radius matrix; dominated convergence after \(\sqrt\varepsilon\)-rescaling; explicit integration of the unit paraboloid cap and normalization of the spherical measure.

`verify.py` is standalone Python 3 code without dependencies beyond the standard library. It computes the defect for 2D balls and for 3D balls from exact formulas, and integrates the 2D elliptical support formula for distinct semiaxes. It checks the limiting coefficients in dimension two and three, including the anisotropic curvature correction. To replay, run `python3 verify.py` in the extracted package directory.

Finite floating-point checks do not prove the arbitrary-dimensional or arbitrary-body theorem. This is a one-sided asymptotic; no claim is made for nonsmooth, zero-curvature, or multi-normal contact. No independent audit has been performed.
