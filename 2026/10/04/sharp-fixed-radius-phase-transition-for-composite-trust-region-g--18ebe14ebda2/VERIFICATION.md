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

The mathematical proof classifies the exact scalar trust-region subproblem by the signs of the two slopes of \(xz+\theta|z|\). The critical quantity is \(\theta=\lambda/a\).

`artifacts/verify_trgm_l1_phase.py` uses exact rational arithmetic. It checks the piecewise minimizer intervals, representative arbitrary choices at the two threshold states, finite absorption for subcritical radii, the critical selector-induced cycle, and unique supercritical two-cycles.

The finite replay does not prove the quantified statement; the slope classification and interval argument in `RESULT.md` do. Multidimensional, stochastic, approximate, and variable-radius variants are outside the claim.
