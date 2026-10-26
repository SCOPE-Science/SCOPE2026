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

# Reproducibility and scope of checks

Run `python verify.py` with Python 3, NumPy and SciPy. The script computes the exact Laplace positive-part integral for six detunings and its Fourier transform at four frequencies. It independently solves nearest-neighbor finite-volume Markov stationary equations for the McKean drift at nine combinations of reset rates and detunings. It checks probability conservation and agreement of the scaled finite-rate mean correction with the theorem's predicted profile. At packaging, all 28 analytic and finite-volume assertions passed.

The finite-volume calculation is a discretized model, not an infinite-resolution proof. The mathematical argument in RESULT.md uses an exact exponential-age resolvent identity, the Laplace law of exponentially sampled Brownian motion, globally Lipschitz stochastic path bounds, and contraction of the averaged fixed-point map. No external or independent scientific audit has been performed.
