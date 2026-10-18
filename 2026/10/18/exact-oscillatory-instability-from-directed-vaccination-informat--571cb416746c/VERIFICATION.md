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

# Reproducibility and limitations

Run `python verify.py` with Python 3, NumPy and SymPy installed. The checker differentiates the six nonlinear equations directly, directly reconstructs the characteristic polynomial for both directed and reciprocal channels, verifies the exact endemic example and threshold, checks the two-patch stochastic matrix eigenvalues, and evaluates 24 full six-dimensional spectra on both sides of the directed threshold. A successful run prints `PASS`. These calculations are supplementary finite/symbolic checks, not a replacement for the general analytic sign, minimality, or monotonicity arguments in RESULT.md.

The analytical conclusion is local linear spectral stability, not a certified nonlinear Hopf orbit or traveling wave. Independent scientific review or priority verification has not been performed.
