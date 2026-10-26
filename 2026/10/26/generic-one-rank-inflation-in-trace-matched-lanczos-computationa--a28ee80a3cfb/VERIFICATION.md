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

The proof follows the exact-rank decomposition into the two-dimensional boundary covariance and the positive isotropic bulk. The only strict step is \(p_1p_3>p_2^2\), verified from Cauchy--Schwarz and the nonzero next Lanczos residual coefficient.

`CHECK.py` reconstructs the fully specified rational three-dimensional matrix, exact inverse, Schur moments, target and approximate posterior covariances, exact determinants, and strictly positive variance in the measured direction. It checks additional exact-rational parameter cases. Finite tests do not prove the universal statement; the analytical argument covers all permitted dimensions and positive-definite matrices.

The Gaussian-support comparison assumes exact zero-noise linear observations. The KL statement does not concern finite-precision observations or the separate full-rank covariance approximation.
