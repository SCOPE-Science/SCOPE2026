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

The analytic proof in `RESULT.md` establishes the statement for every positive reset rate and every nonnegative finite radius within the stated mean-field model. An additional stand-alone script, `verify.py`, performs two independent numerical quadratures for the covariance, compares them, tests representative sign changes, checks the beta-integral coefficient, and tests the rapid-reset asymptotic coefficients. The script needs Python >=3.10 and SciPy >=1.10.

Numerical tests do not establish the all-rate classification or asymptotic statements; these depend on monotonicity, dominated convergence, Taylor expansion of the expansion-factor ODE, and endpoint Laplace asymptotics. No numerical evidence is presented as independent expert validation.
