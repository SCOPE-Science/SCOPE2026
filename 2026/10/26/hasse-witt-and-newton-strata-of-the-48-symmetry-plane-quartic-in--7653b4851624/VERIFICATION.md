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

# Reproducible checks
Execute `python3 verify.py` in Python 3. The file uses only the standard library. For all primes \(5\leq p\leq109\), it computes the matrix of coefficients of \((X^4+Y^4+XZ^3)^{p-1}\) twice: first by multinomial coefficient enumeration, then by solving the three exponent equations. It checks exact equality, the claimed support for each residue modulo twelve, and stability of the matrix ranks under squaring and cubing. It prints `VERIFY_OK` upon success.

The infinite-characteristic statement is established by the congruence support table in RESULT.md; this finite script is a reproducibility check only. The complete 1993 Brock thesis was not available for a whole-document novelty comparison. Independent audit has not been performed.
