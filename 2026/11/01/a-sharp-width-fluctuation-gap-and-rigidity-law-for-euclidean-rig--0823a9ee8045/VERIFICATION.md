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

# Reproducibility of the all-dimensional prism fluctuation theorem

The mathematical proof is in `RESULT.md`. Run `python verify.py` using Python 3 with NumPy, SciPy and SymPy installed. The checker uses symbolic algebra for the dimension-three rational-square identity, independent numerical integration of spherical beta moments for dimensions 3–30, cross-dimensional defect tests, direct integration of circular-cylinder width moments, large-dimensional gamma-formula regression checks, and independent random-direction simulation of a square prism. The saved program reported `ALL_CHECKS_PASSED`.

The checker does **not** validate any arbitrary-dimensional identity by exhaustive enumeration. The infinite claims rest on support-function additivity, exact beta integrations, positive definite moment geometry, an algebraic square identity, and classical convergence of scaled sphere-coordinate moments to those of a standard Gaussian. No independent third-party audit has been performed. Historical priority is provisional.
