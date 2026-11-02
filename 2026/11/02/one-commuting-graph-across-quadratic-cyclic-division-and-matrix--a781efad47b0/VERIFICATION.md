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
The executable `petit_commute_verify.py` implements finite-field addition and multiplication and explicitly computes every product of two algebra elements. It checks the commutant set of every element against the proposed formula for each of two parameters, one in and one outside the base field, over base fields of orders 2, 3, 4 and 5. It separately verifies the center, total ordered commuting pairs and the nonclosure witness. The recorded output ends `VERIFY_OK`.

Exact scope: 16, 81, 256 and 625 elements in the respective four-dimensional algebras. These tests are exhaustive for those particular fields/parameters, **not** exhaustive for all choices of parameters or all fields. The symbolic proof covers the universal quantifiers. Neither independent peer review nor formal independent certification has been performed.
