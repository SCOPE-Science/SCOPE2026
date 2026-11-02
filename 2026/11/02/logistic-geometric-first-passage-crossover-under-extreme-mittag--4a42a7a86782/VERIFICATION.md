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

# Verification of the claimed logarithmic-distance crossover

Run `python3 CHECK.py` from the directory containing `CHECK.py`. The program uses no third-party packages and evaluates two published integral identities, together with the proposed geometric limit. `CHECK_OUTPUT.txt` is the output of this execution; it records `PASS 40 checks`.

Analytical checks: the log-rate tail convergence follows by dominated convergence from the published Mittag-Leffler integral, with the exact limiting integral \(\int_0^1 e^\kappa/(r+e^\kappa)^2\,dr\). For the spatial process, the finite-variance martingale maximal inequality controls all slow refresh periods; reflection and the heat-kernel supremum estimate give a uniform fast-block absorption bound. Continuity of the logistic law removes the narrow ambiguous band. These steps prove convergence at every noninteger continuity point of the geometric limit, for every deterministic sequence satisfying the stated ratio condition.

The numerical sample includes exact spectral survival at integer refresh times for several shrinking positive indices and increasing initial distances, plus an example with a rapidly increasing redraw interval. Finite spectral samples do not establish asymptotic convergence or a rate of convergence. No moment convergence and no independent validation are asserted.
