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

# Reproduction and limits

From the containing directory, run `python verify.py` using Python 3.8 or newer. It uses only the Python standard library and checks the rational parameter witnesses, the exact positive left and right nullvector identities for the threshold comparison matrix, the exact n=2 Hill upper bound, and finite supporting concentration tests at Hill orders 2 through 10.

Successful execution prints `VERIFY_OK`. The strict-subcritical comparison inequality and the critical omega-limit argument in `RESULT.md` constitute the infinite-domain proof. Numerical samples do not establish the theorem for arbitrary Hill orders, concentrations, or parameters. No independent mathematical or external validation has been performed.
