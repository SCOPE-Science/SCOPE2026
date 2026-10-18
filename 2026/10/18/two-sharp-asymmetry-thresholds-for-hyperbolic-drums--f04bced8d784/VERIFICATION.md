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

Run `python checker.py` in an environment with Python 3, SymPy, and mpmath. The checker expands both geometric one-cap functionals through sixth order, proves the exact coefficient cancellation symbolically, differentiates the deep-cut regular-coordinate expressions, and verifies both critical radii. It separately evaluates derivatives of the unexpanded functions with high precision and numerically inverts the one-cap area to exhibit exactly fixed-area unequal-cut perturbations on both sides of the sign transitions.

Observed checks: all exact symbolic coefficient identities and endpoint limit identities passed. The two radii evaluated as approximately 0.481211825060 and 0.985671632425. Four high-precision parameter cases at radii 0.3, 0.6, and 1.2 reproduced the shallow or deep asymptotic signs with relative prediction errors below 5%, and the fixed-area perturbation had the sign of the computed Hessian in every case.

These computational checks corroborate the proof but do not constitute a computer proof of infinitely many radii or cut angles. The analytic formula, local existence of the inverse area function, and the strict-sign arguments are all given in RESULT.md. The critical radii themselves are excluded from the strict-sign assertions.
