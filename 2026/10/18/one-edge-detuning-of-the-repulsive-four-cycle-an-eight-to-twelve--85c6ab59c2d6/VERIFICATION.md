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

Run `python3 verify.py` with NumPy installed. The executable checks 1,852 exact-formula, floating-point spectral/Hessian-inertia, and Lyapunov-descent diagnostics at nine positive weights on both sides of one. It tests all explicitly listed stationary configurations, the predicted 8/12 counts and Morse-index histogram, closure and flux residuals, and random phase-dependent descent at step size 1.9/Lambda. These are finite diagnostics and do not establish completeness for all weights. The universal classification and measure-zero stable-basin argument are analytic. The source and comparison statements were reviewed for scope, with a residual historical priority risk.
