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
The proof reconstructs the normalized two-state QHM matrix from the defining update.

`verify.py` checks the Jury boundary, the closed-form discriminant endpoints, the exact scalar minimizer against dense deterministic searches, the endpoint plateaus, and the nilpotent \(\nu=\beta\) slice using exact rational arithmetic where applicable.

The grid search is not used to prove optimality. The exhaustive argument in `RESULT.md` uses the exact root product, discriminant, and radius-scaled Jury inequalities.
