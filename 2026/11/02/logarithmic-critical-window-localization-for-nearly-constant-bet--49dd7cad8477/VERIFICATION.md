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

# Verification and reproducibility

The probability normalization and the joint conditional law were proved analytically by orthogonal diagonal coordinates and uniform control of the two Beta endpoint corners. The file `verify.py` is a Python standard-library-only independent numerical and algebraic cross-check. Run it with `python3 verify.py`.

The checks exercise exact geometry and normalization identities, the exponential-tilt integrals, symmetry under swapping endpoints and drifts, and a direct quadrature for the two-observation arcsine parent. The arcsine event has an exact one-dimensional integral after transforming each observation through its quantile representation; the script evaluates that integral without using the asserted probability asymptotic. Its finite-threshold relative error decreases over the evaluated thresholds.

At three observations the algebraic critical constant is checked against the published fixed-shape Beta variance formula after converting \(Q=2S^2\). Finite arithmetic and quadrature do not prove convergence for all parameters or arbitrary \(n\); the proof supplies that result. No independent external verification has been performed. The limiting theorem gives no certified remainder or finite-threshold error rate.
