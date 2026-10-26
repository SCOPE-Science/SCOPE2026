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

# Verification

An executable standalone program, `verify.py`, uses Python 3 with NumPy and SciPy. It compares the killed-generator resolvent with the closed characteristic function, tests its independently integrated exponential density, evaluates the survival formula against matrix exponentiation, checks the derivative of the hazard, checks the inverse parameter envelope across an interior grid, and simulates 180,000 independently sampled trajectories. Reproduce with `python verify.py` after extracting the program from this package.

Numerical comparisons use stated tolerances, and stochastic checks use six-standard-error bounds. None are taken as a proof of the infinite-population formula; the matrix-resolvent inversion, quadratic inversion, and survival derivative are proved analytically in RESULT.md. The result is not asserted for position-dependent death, velocity-dependent rates, arbitrary initial directions, or non-Poisson turning. Independent audit has not been performed.
