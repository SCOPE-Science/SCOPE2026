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

# Verification record

The proof uses exact rational cyclotomic irreducibility, positivity, a standard Weyl-character diagonalization and Cauchy--Davenport. It is unrestricted in the odd prime and rational coefficients. The standard singular-value identity is explicitly attributed to earlier work.

`verify.py` builds the complete lifting directly, without using the cyclotomic rank claim in its matrix construction, and checks its numerical singular values against the ambiguity formula and exact predicted kernel size. Its execution yielded:

`VERIFY_OK exact_support_prediction_and_independent_lifting_SVD_cases=348 fields=[3,5,7,11] zeros=PASS rank=PASS singular_values=PASS`

This finite floating-point verification does not certify all primes or historical novelty. Reproduce with `python verify.py` and NumPy installed.

## Scientific limits

Zero-free ambiguity does not entail a uniform positive singular-value bound over the rational-positive class. A full-support nonconstant positive real example can have zero ambiguity, showing why rationality is essential. No independent audit was conducted.
