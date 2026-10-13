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

`verify.py` replays the rational formulas using exact arithmetic and returns `VERIFY_OK`. It checks the coefficient/tail identities by polynomial arithmetic, the rational bracket for the unique positive root, and exact negative/positive six-state witnesses.

The checker is not an exhaustive proof over all real step sizes. The interval classification additionally uses the analytic sign estimates, Descartes' rule of signs, continuity, and the explicit negative diagonal for \(h>3\) given in `RESULT.md`.
