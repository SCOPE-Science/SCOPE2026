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

# Verification record

Run `python verification.py` using Python 3.9 or later; it uses no nonstandard packages. During the self-review, the program returned `PASS: 569 deterministic kernel, finite-resolvent, and boundary-limit checks.` Checked items: the harmonic-oscillator mean, covariance, Dirichlet–Neumann boundary conditions and jump, tridiagonal discretized Brownian resolvent, early/late/cross covariance limits, endpoint factor-of-two variance, saddle stationarity/curvature, and exponential-tilt mean displacement.

The proof of the infinite-time microcanonical joint convergence is analytic in `RESULT.md`. The finite checks do not prove contour inversion, saddle domination, asymptotic independence, path tightness, novelty, or generalizability. Initial-window weak convergence and tightness are imported from the cited primary theorem with the fixed-drift assumptions made explicit. Independent auditing has not been performed.
