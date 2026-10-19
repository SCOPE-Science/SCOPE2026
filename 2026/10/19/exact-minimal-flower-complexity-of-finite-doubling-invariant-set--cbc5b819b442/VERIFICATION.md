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

The mathematical proof is in RESULT.md. The attached `verify.py` independently evaluates finite examples using exact rational arithmetic and checks a finite-state lower-bound minimization for small prescribed supports. It does not certify arbitrary-size cases; the infinite quantified statement follows from the proof rather than from enumeration. Run `python3 verify.py` in a directory containing that file. Independent audit has not been performed.
