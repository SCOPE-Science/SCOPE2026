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

# Verification
Run `python verify.py` in a directory containing the extracted files; only Python 3 standard library is needed. The checker reconstructs randomly rotated regular polygons by explicit Cartesian vertices, enumerates their Minkowski-sum vertices, computes their convex hull by a separate monotone-chain implementation, and compares areas with the mixed-area formula for triangles, squares and pentagons. All 380 direct hull experiments agreed to absolute error below \(1.5\times10^{-14}\). For regular polygons with 3, 4, 5, 7 and 12 sides, the independent Fourier-weight sums agree with exact geometric deficits and variances under the reported numerical tolerances. A reproducible 16,000-trial experiment for nine randomly rotated equilateral triangles found empirical area mean approximately 166.359 versus analytic 166.390, and variance approximately 22.530 versus analytic 22.191. The program exits after `ALL_ROTATIONAL_MINKOWSKI_CHECKS_PASSED`.

The analytical proof, not finite computation, justifies the convergence, exact all-body identities, sharp variance inequality and support of the limiting law. No independent audit or external certification has been performed.
