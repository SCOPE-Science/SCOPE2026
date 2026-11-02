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

The package contains `verify.py`, a standalone Python 3 program requiring no third-party modules. Its function `distribution(n)` uses exact `fractions.Fraction` arithmetic and the coefficient recurrence for an exponential generating function; `enumerate_columns(n)` directly enumerates independently chosen distinct maximum/minimum positions in each column. Execute `python verify.py`.

A successful run verifies exact agreement of the complete equilibrium-count laws for n=2,3,4 using 4, 216 and 20,736 equally likely column-extrema configurations, respectively; all coefficients are nonnegative and total to one, and the claimed analytical mean and variance agree for n=2,...,10. This is a finite independent computational cross-check of the all-n analytic argument. The program does not check the originality assessment or provide an independent scientific audit.
