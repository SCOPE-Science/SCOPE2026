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

# Numerical and analytic verification notes

The reference calculation is the scalar recurrence for normalized covariance \(s_n>0\) and normalized mean error \(v_n\), with \(h_n=\min\{H,\beta/|s_n-1|\}\) when \(s_n\ne1\), and \(h_n=H\) when \(s_n=1\). To avoid premature floating-point underflow, the standalone checker carries the log covariance \(u_n=\log s_n\) and uses `math.expm1` in the transition.

Running `python verify.py` in a Python 3 environment completed with `VERIFICATION_OK checks= 1152`. It examined parameter grids with \(0<H\le2\), a range of caps including \(\beta>1\), a broad range of initial log covariances, the gain maximizer \(s=1+\beta/H\), critical \(H=2\) convergence-rate comparisons, finite-time capture \(s_0=e^\beta\mapsto1\), and mean divergence for \(H>2\) starting at \(s=1\). The critical algebra was independently expanded symbolically: \(g(g(u))=u-4u^3/3+O(u^4)\) and the two-step mean multiplier is \(1-4u^2+O(u^3)\).

These calculations do not establish the universal claims by enumeration. The proof uses the exact logarithmic transition, Coppel's interval-iteration theorem, the cross-zero two-cycle contradiction, explicit piecewise minimization, and a local critical normal form. The numerical checker is not a formal proof system, and no independent audit has been performed. The theorem excludes Monte Carlo perturbations, multidimensional covariances, and finite-precision overflow or underflow.
