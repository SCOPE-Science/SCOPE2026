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

# Reproducibility checks and limitations

The theorem's critical nonstandard step is the reset-generator identity \(\mathbb E[X_{U_t}B_t]=\mathbb E[B_t^2]/t\) for uniform sampling from the full prior path, which determines the singular term in the closed ODE. The result then follows from the exact Laplace integral, Kummer inversion and its three distinct large-argument limits. This analytic argument is the proof; finite checks alone cannot certify it.

Run `python -m pip install -r requirements.txt` then `python verify.py` using these exact packaged files. The checker performs 349 exact-rational, high-precision residual, Laplace-transform, asymptotic and finite simulation assertions. The approximate sampled-path simulation is deliberately a separate finite diagnostic: it cannot verify an infinite-time theorem or prove independence, and samples a time-discretized recollection protocol.

All hypotheses are positive \(D,\mu,r\), an exactly equilibrium-initialized OU process, independent Poisson resetting and recollection of a uniformly selected prior **time**. It proves unconditional second moments and convergence in \(L^2\), not a distributional central limit theorem or pathwise convergence. General memory kernels, nonlinear confining forces or non-equilibrium initial laws are not covered. Broader research-priority comparison and any independent audit remain outstanding.
