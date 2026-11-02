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

The independent checker `check_cycle.py` can be run with Python 3 and the `mpmath` package (`python check_cycle.py`). In the package's decoded directory it emitted exactly:

`PASS exact CTMC/LST, all-site balanced stochastic comparison, and random-gap inclusion-exclusion: 15742 assertions`

It (i) builds full finite SI Markov generators on cycles of size at most nine and evaluates rational Laplace transforms at positive rational parameters, (ii) independently evaluates the candidate Gamma-max Laplace transform and compares the rational results, (iii) checks strict balanced maximum of finite-time CDF over all seed sets of cycles through eleven at several positive deadlines, and (iv) compares exact maximum-gap inclusion–exclusion against brute uniform seed enumeration through twelve vertices. These checks cover finite cases only; they neither enumerate arbitrary cycles nor prove the Gumbel limit. Infinite conclusions use the analytic factorial-moment, Poisson-tail, and Chernoff arguments in `RESULT.md`. No independent audit or validation was performed.
