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
The package reconstructs the source-form memoryless Amos recurrence on a scalar strongly convex quadratic.

`verify.py` checks the autonomous buffer and affine parameter coefficients, the asymptotic constants for \(b_t\), \(c_t\), \(d_t\), \(r_t\), and \(s_t\), the convergence of the product/threshold approximants, and a concrete positive-branch trajectory.

For \(\xi=\eta=1\), long finite truncations give \(P_\infty\) near \(0.17236\) and \(X_\star\) near \(16.404\); initialization \(x_0=20\) remains positive and approaches a positive value over the replay horizon.

These finite calculations are transcription guards only. The infinite-time statements follow from the analytic buffer asymptotics, summability, infinite-product criterion, and exact affine-recurrence solution in `RESULT.md`.
