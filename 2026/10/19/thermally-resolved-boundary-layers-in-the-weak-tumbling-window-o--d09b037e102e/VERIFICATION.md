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

The stationary density is derived analytically from the finite-chain balance equations, not inferred from finite numerical experiments. To reproduce independent finite-chain checks, run `python verify.py` in a Python environment with NumPy and SciPy. The script builds the original Markov generator, normalizes its zero-eigenvalue stationary vector, and compares that direct solution against the closed marginal expression over fifteen distinct parameters. It independently verifies exact normalization and strict convexity, then evaluates the infinite-volume predictions at increasing lengths.

Observed maximum absolute error against direct finite-chain equilibrium: \(2.11\times10^{-15}\). At length \(L=1000\), hopping rates \(u=2.5,v=1\), and \(L\alpha_L=1.7\), the wall-site probability was \(0.092152390\), versus limiting \(0.091836735\); the rescaled central probability was \(0.346932803\), versus limiting \(0.346938776\).

No finite generator computation certifies an infinite-volume limit: the recurrence derivation, uniform edge bounds, geometric summation and bulk Riemann limit in the proof supply that step. No independent audit or external mathematical certification has been performed.
