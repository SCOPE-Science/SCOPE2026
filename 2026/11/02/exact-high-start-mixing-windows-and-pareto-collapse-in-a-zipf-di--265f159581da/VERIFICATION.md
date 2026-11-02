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

Run `python check.py` with standard-library Python 3 only. `check_output.txt` contains the output reproduced from the packaged code: 10,523 assertions passed. The program uses exact `fractions.Fraction` transitions for ten parameter/initial-state/horizon triples, rigorous rational integral-test brackets for stationary zeta values, and independently recomputed first-reset renewal probabilities. It checks the sufficient finite inequality, the strict positive/negative sign pattern, the total-variation singleton formula and two integer mixing thresholds.

The infinite-dimensional path limit and the eventual all-initial-height sign statement are proved analytically in `RESULT.md`. Numerical computations cannot certify all parameter values or infinite-horizon claims. Stationary zeta comparisons use rigorous rational integral-test bounds; the analytic proof and explicit finite sufficiency criterion do not depend on finite checking. Self-review was performed; independent audit has not been performed.
