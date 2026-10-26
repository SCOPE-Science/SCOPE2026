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

# Reproducibility and verification

Run `python3 VERIFY.py` with a Python 3 standard-library installation. The program computes a closed binomial expression for the stationary covariance; independently checks the associated Lyapunov recurrence; compares spatially scaled covariances against the heat-kernel integral for three matrix sizes and several damping/offset combinations; and checks the fixed-damping bounded, square-root, and exponentially amplified variance regimes.

The executable returned `PASS 805 checks`, with maximum absolute finite-matrix Lyapunov residual \(2.14\times10^{-14}\) (rounded upward) and maximum absolute tested mesoscopic covariance discrepancy \(0.033461\) (rounded upward). The finite calculations do not prove convergence; the limit theorem is justified by a binomial local limit with a uniform small-time cutoff and the Gaussian covariance criterion in `RESULT.md`.

The model is a stationary, stable finite-dimensional Gaussian Ornstein–Uhlenbeck chain, with limit taken over growing chain sizes. No non-Gaussian or nonlinear extension has been verified. An independent audit has not been performed.
