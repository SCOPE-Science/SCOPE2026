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

# Reproducibility checks

Run `python verify_kuramoto.py` after installing the standard `mpmath` Python package. The checker reads no external files and performs deterministic high-precision integration of the stationary exponential reset age. It checks the explicit subcritical, supercritical, and critical flow solutions against the differential equation; verifies their initial amplitudes; independently reconstructs the critical incomplete-gamma coefficient; and tests approach to the predicted off-critical exponentials and critical three-halves factor.

Actual execution of the packaged checker: 37 assertions passed. Critical normalized covariance ratios for the chosen test case at lags 30, 100, and 300 were approximately 0.8701771614, 0.9569046001, and 0.9851735734; each approaches one in accordance with the explicit analytic remainder. Cases with relaxation below and above the coupling threshold and above/below the nonzero equilibrium were included, along with the zero-coupling boundary.

The proof in RESULT.md, not finite numerical checks, establishes the universal infinite-lag claims. No independent audit, formal proof certification, or finite-population tests are asserted.
