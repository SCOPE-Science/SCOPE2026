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

Run `python check_width_covariance.py` with NumPy, SciPy and mpmath. The checker (1) compares cube support functions to independent enumeration of all cube vertices, (2) computes the exact normalized-Gaussian mixed moment and compares with quasi-Monte Carlo independent directional sampling, (3) tests the strict Hadamard equality and global quadratic defect against randomly generated orthogonal frames, and (4) assesses the large-dimensional coefficient using high-precision gamma functions. The complete diagnostic executed successfully and reported `ALL_ROTATED_HYPERCUBE_WIDTH_COVARIANCE_CHECKS_OK`. Computations corroborate, but the universal statement is proved analytically in `RESULT.md`. Independent audit has not been performed.
