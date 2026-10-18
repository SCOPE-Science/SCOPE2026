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

# Verification and boundaries

Execute `python verify.py` with NumPy and SciPy installed. The checker performs exact integral quadrature of the finite-particle Gaussian-mixture fixed-time positivity probability, finite-dimensional independent-extrema probability checks, seeded simulated trajectories of the minimum position, verification of the ordinary Brownian first-passage CDF, and an independent finite-difference calculation of the Dirichlet spectrum of the log-time Ornstein–Uhlenbeck operator.

The simulations, quadratures and eigenvalue discretization are numerical evidence only. The exact infinite-population crossover is proved by uniform pathwise Gaussian maxima and Brownian hitting-time continuity; the sharp mean threshold is proved by killed-Ornstein–Uhlenbeck spectral bounds and the positive polynomial eigenfunction at boundary \(1\). The checker does not establish novelty, convergence of finite-particle mean arrival times, or an independent audit. A failure in a finite numerical test is not interpreted as nonexistence of a limiting process.
