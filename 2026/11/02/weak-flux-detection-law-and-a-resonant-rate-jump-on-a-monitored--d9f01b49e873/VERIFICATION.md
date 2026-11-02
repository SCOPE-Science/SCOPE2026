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

Install Python 3, NumPy, and SciPy and run `python verify.py`. In the recorded execution this produced `PASS 49 independent numerical/structural tests`. The program independently exponentiates the actual three-site Hamiltonian, compresses it into symmetric/antisymmetric states, and compares it to the closed survivor matrix at 25 parameter pairs. It also computes first-detection mean steps using the exact finite-dimensional Lyapunov equation, evaluates long-run survival probabilities, and checks the two spectral-loss coefficients. These computations reproduce the two asymptotic rate regimes. Symbolic differentiation of the closed matrix gives the Taylor coefficients displayed in the proof.

For non-revival \(t=1\), computed \(\alpha^2\mathbb E[N_\alpha]\) at \(\alpha=0.020,0.010,0.005\) was \(0.222507670990,0.222293566422,0.222240057148\), approaching \(2/9\). At full revival \(t=2\pi/3\), the corresponding values were \(0.228217197671,0.228033768350,0.227987937706\), approaching \(9/(4\pi^2)\).

Numerical checking is neither a proof of a limit nor an independent audit. The analytic perturbation and uniform tail arguments in RESULT.md establish all quantified conclusions for every fixed positive observation interval. No stochastic numerical experiment substitutes for exact proof.
