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

The complete finite certificates are reproduced by `python3 verify.py` (Python 3 standard library only). The script constructs the six-factor numerator of degree 1605 over the integers reduced modulo 32, proves the four projected numerator identities coefficient-by-coefficient, verifies the two polynomial equations over the integers modulo eight that identify the Thue–Morse sixth power, and checks the final numerator identity modulo 32. A separate recurrence checks 32768 partition coefficients as an additional guard. The exact certificate gives an infinite proof because the formal-series functional equation has a unique solution with the specified constant coefficient. The finite recurrence comparison is not used to extrapolate an infinite statement. The result identifies a subset of all exceptional indices; it makes no assertion about their full density. Independent audit has not been performed.
