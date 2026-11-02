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

# Reproduction and limits

Run from this directory:

```
python3 verify_coefficients.py
python3 verify_cartier.py
```

`verify_coefficients.py` computes three central coefficient polynomials exactly modulo the listed primes, checks the factorization identities and squarefreeness, and checks that excluded singular values are not roots. It concludes `COEFFICIENT_IDENTITIES_OK`.

`verify_cartier.py` separately expands the affine defining polynomial into monomials to construct the Cartier coefficient matrix directly. It checks all smooth prime-field coefficient values for six primes and concludes `CARTIER_EXTRACTION_OK`.

The finite tests do not certify the statement for arbitrary primes or parameters in algebraic closures. The all-prime claim rests on the symbolic coefficient-ratio and differential-equation proof in `RESULT.md`. The displayed use of semilinear Cartier rank is correct because the coefficient matrix is diagonal; no unverified substitution of ordinary matrix rank for stable rank is made. No independent external audit has been performed.
