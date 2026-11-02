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

# Verification and limits

The standalone `verify.py` was run using Python 3 with SciPy. It completed **454 deterministic checks**, including normalization of the reset-scale distribution, independent exponential-age versus expansion-scale quadrature for the first four inverse-scale moments, positive variance and cubic covariance, root bracketing and residuals, strict decreasing weighted-mean grids, agreement with the closed formula when the root is inside the initial cloud, and finite-parameter checks of both asymptotic regimes.

Run `python verify.py` after installing the dependency specified in `requirements.txt`. The computation uses no simulation data, hidden service, or nonembedded files.

The check is deliberately finite. Strict uniqueness of the spatial sign threshold follows instead from monotone likelihood ratios and endpoint bracketing; the exact slow-resetting coefficient follows from the analytical logarithmic integrals. Numerical agreement does not certify mathematical originality, finite-particle quantum correlations, or uniform validity of the Thomas–Fermi approximation as the resetting rate tends to zero. No independent audit has been performed.
