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
The exact elimination is replayed by `derive_elimination.py` (SymPy), which must print `ELIMINATION_OK`. The arithmetic Galois certificate is independently replayed by `verify_galois.py` using only the Python standard library; it must print `VERIFY_OK`. The captured outputs are included. The source paper independently certifies total reality of the same exact matrix; that external certification is cited rather than re-authored here.
