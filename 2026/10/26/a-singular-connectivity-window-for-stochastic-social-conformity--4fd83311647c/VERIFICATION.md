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

Run `python3 verify.py` with Python standard library. The program builds the exact finite absorbing transition matrix in rational arithmetic, solves the linear first-step equations and asserts both high-conformity and joint-limit predictions in three small finite populations, exact two-group crossover, and strict interior improvements at finite conformity. Twenty-nine assertions pass, including explicit source-clock normalization and positivity checks. The program uses exact rational Gaussian elimination, not stochastic simulation. The infinite-family claims rest on the finite-chain renewal, fast-chain projection, and birth–death proof in `RESULT.md`, not on numerical extrapolation. A full formalization and independent audit were not performed. The 2008 network fixation paper was accessible only to abstract-level comparison, so broader implication coverage remains a residual literature risk.
