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

Run `python paired_split_verify.py` in a Python environment with the numerical libraries specified in `requirements.txt`.

The script (a) differentiates the exact rational resolvent matrices symbolically and confirms all Taylor coefficients through second order; (b) enumerates each of the \(2^n\) order sequences for \(n=1,2,3,4,5\) at rational steps, comparing the direct means and covariances with the exact analytic recurrence; (c) verifies that a commuting pair has identical forward and reversed blocks; and (d) computes independent quadratures of the bias, paired covariance, and iid covariance, comparing each against deterministic finite-step recursions. All checks printed `ALL CHECKS PASSED` upon execution.

For the positive-definite two-by-two example at \(T=1\), the paired trace ratio at \(N=800\) is approximately \(0.997515\), and the independent-sampling trace ratio at \(2N=1600\) solves is approximately \(1.000859\). The symbolic checks are finite exact computations. The distributional and infinite-mesh results are proved separately in `RESULT.md`; no simulation or numerical convergence plot is treated as an infinite proof.
