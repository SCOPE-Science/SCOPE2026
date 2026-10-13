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
# Verification

Execute `python3 verify.py` using Python 3 and no external packages. It directly solves the basis-level Leibniz linear system modulo the tested primes and checks the arithmetic prediction by two independent counting implementations. Its second certificate directly substitutes the proposed Legendre-character operator for order eleven in characteristic three into every coefficient of every basis-pair Leibniz identity. Successful execution prints `VERIFY_OK`, `LEGENDRE_N11_P3_OK`, and `ARITHMETIC_FORMULA_OK`.

The tests cover all odd orders 3, 5, 7, 9, 11, 13, and 15 and the primes 2, 3, 5, 7, 11, and 13 that do not divide the order; they are finite sanity checks, not exhaustive mathematical justification for unbounded orders or arbitrary fields. The theoretical proof uses cyclic character orthogonality and a complete finite orbit-relation analysis. Independent audit has not been performed.
