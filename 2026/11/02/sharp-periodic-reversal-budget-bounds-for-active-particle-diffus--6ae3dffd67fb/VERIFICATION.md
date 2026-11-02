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

The exact proof is in `RESULT.md`. Reproduce deterministic checks with `python3 periodic_flip_checker.py` using Python 3.9 or later, requiring only the Python standard library. The checker confirms homogeneous equalities; strict inequalities under generic piecewise-constant rate allocations; narrow-pulse convergence toward the supremum; and agreement of an exact backward-resolvent solution with separate covariance quadrature for selected rates. It prints `PASS: 188 independent deterministic assertions`.

No finite numerical test certifies all integrable control functions. Universality, equality conditions, and impulsive-limit sharpness follow from the analytic proof. The singular limiting protocol is **not** a finite-rate admissible control.
