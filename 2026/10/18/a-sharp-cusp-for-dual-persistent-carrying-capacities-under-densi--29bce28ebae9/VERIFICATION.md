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

# Verification and reproducibility

Run `python3 verify.py` with a standard Python 3 interpreter. The script verifies exact rational model reductions and derivatives, an explicit positive-coefficient certificate for the global derivative bound, the factorization underlying the cusp discriminant, and sampled exact-rational state transitions. An analytical proof rather than finite simulations establishes the global claims. The polynomial factorization and positivity can be checked directly from the equations in `RESULT.md`. No independent validation is represented.
