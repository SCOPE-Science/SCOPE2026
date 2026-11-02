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

# Reproducibility and limits

The analytic proof in `RESULT.md` proves all rates \(\gamma>0\), all confinement rates \(\mu>0\), all propulsion speeds \(v_0>0\), and all physical thermal diffusion strengths \(D\ge0\), including singular zero-noise and large-rate limits. The general noise-kernel result is restricted to independent strictly symmetric-unimodal densities. The independent mathematical review channel is not performed.

Run `python verify.py` with Python 3, NumPy, SciPy and SymPy installed. The script checks the state Fokker–Planck equations and beta moments symbolically, evaluates the Bayes accuracy by independent quadrature methods, confirms the direction map, compares near-asymptotic formulas with finite examples, and tests independent joint samples. The reported `PASS 899` result is diagnostic, not an exhaustive proof of universal claims.

Stationary-state sampling uses the beta law and a posterior Bernoulli sign law, rather than numerically integrating a stochastic differential equation; therefore the Monte Carlo sample checks reproduce the established joint law, not an independent derivation of it. All reference statements and model rates are reproduced in `RESULT.md`. No certificate of independence, novelty priority, or third-party mathematical validation is asserted.
