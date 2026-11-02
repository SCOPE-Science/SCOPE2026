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

Run `python verification/check.py` with SymPy in the package root. It reconstructs exact moment recurrence characteristic polynomial, seven Cayley–Hurwitz positivity families, noncanceled generating-function pole, its critical residue, deterministic expected-state Schur stability at the exhibited parameter, and exhaustive coordinate path enumeration through seven generations.

Verification of finitely many sample paths is used only as corroboration. The analytic recurrence and exact rational certificates prove the infinite-horizon theorem. This verification is not an independent audit.
