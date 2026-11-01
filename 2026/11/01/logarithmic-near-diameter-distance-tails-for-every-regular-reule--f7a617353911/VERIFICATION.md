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

# Reproducibility and scope

Run `python verify_reuleaux_log_tail.py` with Python 3, NumPy, and SciPy. The executed verifier reported `REULEAUX_FINITE_CHECKS_OK: 278 checks; 3, 5, 7, 9, 11 vertices`. It evaluated exact trigonometric identities against quadrature, numerically computed intersections of translated unit-disk families by vertical slices, and checked the predicted middle-direction quadratic cap and transition-direction three-halves scaling.

These finite tests cannot establish a limiting asymptotic for every odd vertex count. The proof uses the explicit covariogram identity, wedge asymptotics uniform on trimmed angular sectors, the endpoint cap estimates, and exact angular integration. The result is self-reviewed only; no independent mathematical audit has been performed.
