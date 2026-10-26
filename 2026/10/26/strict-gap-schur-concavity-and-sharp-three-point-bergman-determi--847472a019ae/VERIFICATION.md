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

# Reproducible verification

Run `python3 checks/check_gram.py` with Python 3 and no third-party packages. The program checks exact rational identities for the three-by-three determinant, the positive derivative decomposition, and the equilateral closed form. It separately evaluates deterministic complex point triples. The output `CHECK_OK` records finite computational corroboration only, not a replacement for the proof of strict Schur concavity. The proof uses the standard Szegő Cauchy determinant formula plus explicit real-variable monotonicity.

Scope: positive radii strictly less than one; the endpoints are limiting statements, not included as configurations. No external audit has been performed.
