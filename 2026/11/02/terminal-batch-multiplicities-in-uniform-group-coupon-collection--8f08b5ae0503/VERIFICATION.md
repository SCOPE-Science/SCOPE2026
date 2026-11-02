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

The analytic proof in RESULT.md gives the complete finite-parameter statement and its limiting arguments. The embedded standard-library Python file `checks/check.py` verifies the exact joint formula against an independently implemented hypergeometric count process and against exhaustive finite ordered-package enumeration; it also checks the strict-jump chain, finite collision bounds, factorial moments, and selected asymptotic diagnostics.

The standalone checker passed **1,162 assertions** in a local execution. It is finite evidence, not an exhaustive proof for arbitrary population sizes. The sharp sparse result depends on the displayed strict-decrease union bounds, while total-variation convergence in the bulk regime depends on the analytic Poisson limits and normalization of the limiting masses.

Only a self-review has been performed; independent audit and independent validation have not been performed. Literature comparisons identify unresolved historical-priority risk for older works whose complete text was unavailable.
