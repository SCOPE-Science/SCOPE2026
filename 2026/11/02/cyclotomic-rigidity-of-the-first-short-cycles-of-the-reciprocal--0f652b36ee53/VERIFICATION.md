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
# Reproduction

Run `python3 verify_cycles.py` with the Python 3 standard library. The successful output was:

`VERIFY_OK prime_fields=168 extension_fields=19 all_exact_2_and_3_cycles_match`

The program implements polynomial quotient fields, tests irreducibility by bounded divisor enumeration, and directly enumerates all defined points of least periods two and three. Test coverage includes every prime \(p\le1000\) and nineteen nonprime finite fields (the largest tested has at most \(2500\) elements). The symbolic numerator identities and the integer resultant-one fact are proved by elementary polynomial algebra in `RESULT.md`; the finite examples are not used as an infinite proof. Scientific limitations and literature-access risks appear in `RESULT.md` and `REVIEW.md`. Independent audit is not performed.
