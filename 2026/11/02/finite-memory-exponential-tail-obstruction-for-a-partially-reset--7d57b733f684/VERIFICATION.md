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

The accompanying `checks/check_kernel.py` is a finite, self-contained symbolic and numerical consistency check. Run with Python 3 and SymPy: `python checks/check_kernel.py`.

It checks the quadratic generator identity, the reset-free linear drift propagator and Gaussian variance, the saddle minimizer and rate, and the limiting variance of the separate quasistatic Gaussian mixture. The checker supports exact algebra, but does not establish positive Harris recurrence, Poisson last-reset conditioning, Jensen's inequality, Gaussian tail asymptotics, literature priority, or any infinite-time or infinite-distance theorem. Those mathematical steps are supplied analytically in RESULT.md.

No claim is made of an independent audit or external certification. The exact finite-\(g\) exponential tail rate, finiteness of the moment-generating function below the reported divergence threshold, and a rigorous stationary \(g\to\infty\) limit remain unproved.
