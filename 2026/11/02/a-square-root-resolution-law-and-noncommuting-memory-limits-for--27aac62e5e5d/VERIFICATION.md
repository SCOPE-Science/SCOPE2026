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

Run `python3 verify.py` with Python 3. This standalone code uses only the standard library and returns `PASS: 36 deterministic cross-checks (spectral, finite-block, asymptotic, bounds)` on successful execution. It checks the closed algebraic expression against an independent periodic frequency-domain quadrature for ten different parameter tuples. It forms actual forward and reversed Gaussian covariance matrices, solves the finite Gaussian relative-entropy trace problem, and compares the two-observation expression on eight parameter tuples. Three fixed-window experiments test the quadratic small-spacing trend; nine high-resolution experiments test the analytic square-root law; six further tests check noise contraction and resonance.

The numerical checks do not prove the infinite-block limit or a universal asymptotic expansion: those require the Toeplitz/spectral reduction, Poisson convolution and analytical expansions in RESULT.md. The tests are deterministic (no random sampling), and their tolerances cover floating-point and quadrature errors. Every physical and mathematical hypothesis is stated in RESULT.md. No independent expert or formal certification is represented.
