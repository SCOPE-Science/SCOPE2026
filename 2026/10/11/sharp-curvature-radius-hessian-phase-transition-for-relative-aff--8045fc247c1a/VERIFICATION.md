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

# Verification of the curvature-radius Hessian

Run `python verify.py` with the standard Python library. The program numerically evaluates the full relative affine area along exactly area-preserving harmonic support paths for disk radii \(0.4\), \(2/3\), and \(0.85\) with unit reference ball radius, and Fourier modes \(k=2,3,6\). It compares finite-difference deficits to analytic eigen-coefficients and checks the predicted ordering over Fourier degrees \(2\) to \(19\). Its success message is `RELATIVE_AFFINE_HESSIAN_FINITE_CHECKS_OK`.

The theorem for all positive radii and arbitrary Fourier series is established by Taylor expansion and Parseval as written in `RESULT.md`; quadrature provides finite reproducibility evidence, not an infinite-dimensional certificate. No numerical or analytic check establishes claim novelty over all unindexed sources, and no independent audit has been performed.
