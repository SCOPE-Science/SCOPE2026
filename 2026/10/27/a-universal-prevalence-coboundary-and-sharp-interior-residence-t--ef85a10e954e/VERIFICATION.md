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

With Python and the packages in `requirements.txt`, run `python verify.py`. The script checks the exact derivative identity symbolically, the strictly positive supercritical equilibrium using rational arithmetic, and fifteen integrated finite-time balances with numerical tolerance below `2e-8`. It also evaluates one hundred positive strip-residence bounds. On the supplied run, all checks passed with maximum finite-time absolute error `9.394775894733254e-10`. The script reads no outside data. The proof in `RESULT.md` establishes the general quantifiers; finite computations are only corroboration.

The stationary-measure conclusion requires compact support bounded away from zero infection and boundary risk. The residence bound requires both risk and infection stay in the prescribed strip. Existence above threshold requires a suitable choice of vaccine costs; neither global convergence nor stochastic consequences are claimed.
