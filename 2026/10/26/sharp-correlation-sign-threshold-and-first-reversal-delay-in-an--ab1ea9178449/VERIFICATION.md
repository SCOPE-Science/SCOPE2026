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

Execute `python verification.py` with installed NumPy and SciPy. The program solves independent stationary three-variable Lyapunov equations for a covariance-matched Gaussian Ornstein–Uhlenbeck force. The match of the two-time covariances is exact for linear filtering, notwithstanding the very different non-Gaussian higher-order statistics of the physical telegraph force. It also numerically integrates the independent positive Fourier spectral density and compares it with the analytical three-exponential/trigonometric formula.

At review, the checks passed 200 randomized 3-by-3 matrix/Lyapunov covariance comparisons (maximum relative error approximately \(6.22\times10^{-15}\)), 35 independent Fourier integrals, 500 randomized underdamped slow-switch positivity parameter checks, analytic sign-change sample tests, all first-zero brackets for five near-critical switching rates, and critical/overdamped sample checks. For the explicit example with \(m=1\), \(\gamma=2\), \(\mu=2\), \(a_0=1.3\), and \(\rho=0.505\), the first positive zero was \(23.6974613845\) to the stated numerical precision.

The source `RESULT.md` proves the universal quantifiers analytically; numerical data cannot certify positivity at all infinitely many lags nor the existence of infinitely many sign alternations. Source-literature comparisons support but cannot establish priority against every historical publication. No independent audit or validation is represented here.
