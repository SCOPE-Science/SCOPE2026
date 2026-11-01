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

Run `python verify.py` in a Python environment with SymPy available. The checker evaluates all three components of the analytic conjugacy differential identity symbolically, proves the coordinate map has unit Jacobian determinant and preserves squared radius, differentiates the original polynomial vector field, checks the general cubic coefficients on the inner periodic circle, tests the exact signed Routh–Hurwitz margins at the stated rational parameters, and confirms the exact radial periodic circles.

Analytical proof supplies all global assertions: invertibility and smoothness across the axis, forward completeness, conjugacy of flows, and asymptotic-phase convergence in an attracting basin. No finite simulation is used to infer these infinite-time facts. The source's separate theorem supplying a nonempty global-Hurwitz region is treated as published prior work, not independently certified here. No independent audit has been performed.
