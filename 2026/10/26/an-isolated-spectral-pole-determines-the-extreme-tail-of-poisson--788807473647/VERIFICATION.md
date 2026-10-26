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
# Numerical checks and mathematical boundaries

Run `python verify_tail.py` with Python 3, SciPy and mpmath installed. The program compares two independently evaluated descriptions of the stationary law: the original renewal/Fourier formula and the spectral inversion density including its isolated atom. It checks probability mass, stationary variance and three Fourier frequencies for each of three environmental refresh rates (with \(b=D=1\)). It also evaluates the exact spectral-root equation at four additional slow-refresh rates using high precision. The output gives all numerical values and asserts agreement.

Analytical proof, not finite computation, establishes the exact spectrum support, the positive isolated weight, the uniform spatial remainder bound, and the joint asymptotic statements. The numerical tests cannot certify priority, exclude undiscovered equivalent results, or establish the mathematical limit by sampling. The statements are specific to exponential intensity draws, stationary Poisson refreshing, fixed-origin Cox resetting and Brownian diffusion.
