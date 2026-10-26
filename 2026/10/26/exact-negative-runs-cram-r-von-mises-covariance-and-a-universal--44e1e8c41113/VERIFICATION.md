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
# Reproducibility and boundaries

Run `python3 verify.py` from this artifact directory with Python 3. No nonstandard packages or network access are required. The script enumerates every fixed-count binary word for lengths 2 through 12 and checks exact means/covariances via `fractions.Fraction`; separately evaluates each conditional transition influence from hypergeometric moments for all class compositions through length 55. It also checks large-size asymptotic consistency against the variance limit used in the analytic argument. The replay passed 57,127 checks. This tests many instances, but neither enumeration nor numerical convergence proves an all-size identity or limit; those rest on the proof in `RESULT.md`.

All computations are internal exact-rational equalities apart from the explicitly labeled large-size floating consistency checks. The independent-audit channel has not been performed.
