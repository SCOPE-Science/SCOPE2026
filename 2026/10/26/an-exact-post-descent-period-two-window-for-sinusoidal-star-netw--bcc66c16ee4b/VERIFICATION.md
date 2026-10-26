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

The primary equations and eigenvalue decomposition are proved in RESULT.md. The auxiliary checker `star_period2_check.py` numerically repeats the interchange equation and computes the full two-step Jacobian for \(n\in\{4,5,8\}\) and \(\kappa\in\{2.1,2.5,\pi,3.5,5.0\}\); it prints `CHECKS_PASS` when all fifteen samples agree to absolute error below \(10^{-8}\). This is finite support only, not a proof of the all-parameter theorem.

The source model is arXiv:2610.10993v1, publicly submitted 2026-10-07, primary MSC 37C05. The novelty review compared the source's strict-descent restriction, older path-map local flip results, and related oscillator-network sources; older inaccessible articles remain a priority risk. Independent audit has not been performed.
