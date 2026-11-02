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

# Reproducibility and limits

The analytical derivation of the positive center curvature and of the small-window asymptotic is in `RESULT.md`. The attached independent numerical checker `hermite_interval_check.py` was executed from its actual standalone file using `python`, `mpmath` with 65 decimal digits, and reported `PASS 100 deterministic checks`. It cross-compares elementary antiderivatives to independent quadrature, differentiates the exact eigenvalue numerically, and checks the quartic displacement and fifth-order optimal value with controlled finite-radius tolerances. Numerical checks cannot establish universal quantifiers or historical originality. The value and originality comparisons are documented in `REVIEW.md` and `AUDIT.json`. Independent audit and validation have not been performed.
