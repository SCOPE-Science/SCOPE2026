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

Run `python3 verify.py` from the extracted directory. The program uses standard-library integer arithmetic to verify all polynomial identities and signs asserted in the four- and three-household examples. Its exact comparisons avoid errors from numerical evaluation of logarithms. The general crossing upper bound is proved by polynomial degree, Rolle's theorem, and a limiting argument, and is not inferred from finite checks. Independent audit has not been performed.
