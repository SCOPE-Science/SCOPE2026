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

The algebraic proof and exact domain are in `RESULT.md`. The standard-library-only command `python3 verify.py` independently constructs Apéry sets and gap memberships from the minimal positive generators and checks the exact complete pseudo-Frobenius sets, genus, Frobenius number, type, arithmetic symmetry test and almost-symmetry defect. Output: `VERIFY_OK common_generator_products= 897 symmetric= 93 nonsymmetric= 804 endpoint= 97`.

The finite checks do not prove claims for arbitrary parameters. The proof uses explicitly identified established three-generator and gluing results, and no independent audit has been carried out.
