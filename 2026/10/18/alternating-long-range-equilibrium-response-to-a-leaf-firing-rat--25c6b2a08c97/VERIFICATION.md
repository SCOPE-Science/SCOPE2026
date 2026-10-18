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
# Reproducible finite checks

Run `python3 verify_tree_sensitivity.py` with Python 3 and no third-party packages. The program returns a nonzero exit status if any assertion fails. It checks nonlinear minimizer stationarity, positive tree-response recursions, a direct Hessian solve, finite-difference derivatives, finite (30 percent) leaf-rate perturbations, and mass conservation for 180 deterministic finite tree instances (paths, stars, balanced, irregular; up to ten vertices). The observed output was `PASS: 1440 independent derivative, conservation and tree-response checks`.

Proof-level critical step: for every child vertex \(v\), completion of squares in the local quadratic minimizes \(w_v(a+\sum_f x_f)^2+\sum_f C_fx_f^2\); all \(C_f,w_v\) are strictly positive, so every child coefficient multiplying \(-a\) is strictly positive. Strict convexity independently proves that the minimizer is the actual derivative of the equilibrium. The checker's finite samples do not establish general validity, and its numerical Newton stopping tolerance does not furnish an exact arithmetic certificate. Generality is proved algebraically in RESULT.md. No independent audit was conducted.
