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

# Mathematical verification

Run `python verify.py` after installing dependencies in `requirements.txt`. The program independently computes the exponential-age excursion moments, the fourth cumulant rate from a tilted-generator eigenvalue recursion, and direct high-precision integrals for six choices of physical parameters. It factors the exact derivative of \(H\) and confirms an exact rational interval containing the sole positive critical reset-rate ratio.

The strict positivity at finite positive time and the existence of the long-time renewal-reward cumulant rates are proved analytically in `RESULT.md`. Numerical integrations and finite sampled checks are corroboration only; they are not used to extrapolate an infinite assertion. No independent external validation or publication-priority certification has been performed.
