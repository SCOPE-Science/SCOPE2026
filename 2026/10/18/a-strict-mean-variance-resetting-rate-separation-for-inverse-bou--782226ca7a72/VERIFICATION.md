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

The proof supplies the exact fixed-budget time-Laplace transform, first two cumulants, a subordinator-based central limit theorem, and a global derivative sign argument. `verify.py` recomputes first and second log-Laplace derivatives at 80-digit precision for eight reset parameters and five positive/nonnegative budget values, checks positivity and the scalar critical root, and samples the strict relative-variance sign. Sampled checks do not establish the all-parameter conclusions; the factorized derivative and coercivity argument do.

To replay: install the pinned-compatible dependency from `requirements.txt`, then run `python verify.py`. Neither independent proof review nor independent scientific priority determination has been performed.
