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
# Reproducibility checks

Run `python3 check_h4.py` with a standard Python 3 installation. It requires no third-party packages. Output saved in `check_h4_output.txt` is a completed numerical cross-check of the explicit objective and its derivative.

For nine lengths \(m\), the checker independently forms the full \(m+2\)-coefficient residual and computes the fourth norm by literal autocorrelation, comparing it with the simplified closed-form quartic. Selected small and moderate lengths are independently checked by direct equally spaced boundary quadrature with adequate Fourier bandwidth. Finally, root bisection and the numerical constants are compared across multiple lengths through \(m=10000\).

These are finite numerical tests, not certificates of the all-length asymptotics. Universality rests on the exact algebraic autocorrelation, the strictly convex integral objective, the derivative signs, and the analytic uniform expansion in RESULT.md. The checker does not perform independent scientific auditing or establish external originality.
