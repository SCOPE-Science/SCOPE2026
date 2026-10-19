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

# Reproducible checks and limits

The standalone `check.py` checks exactly the symbolic stationary probability current for the stated diffusion. With high-precision numerical integration it evaluates the total-variation distance using the unique sign-crossing point and compares against the proposed coefficients in representative subcritical, critical, and supercritical regimes. It also evaluates the Gamma integral giving the subcritical deficit-density normalization and three critical logarithmic CDF points. Execute with `python check.py`; requirements are in `requirements.txt`.

These finite-parameter calculations do not certify infinite-parameter asymptotics. The proof in `RESULT.md` supplies dominated-convergence, logarithmic integral, and \(L^1\) arguments. The stationarity density is independently known, and the existing 2021 mathematical literature supplies upper bounds rather than all asserted constants/localization laws. No independent review or external certification was performed.
