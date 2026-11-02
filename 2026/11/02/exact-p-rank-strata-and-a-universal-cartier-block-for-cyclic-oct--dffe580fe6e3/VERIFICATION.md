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

The package includes `check.py`. Run `python3 check.py` with Python 3 (standard library only). Its final output must begin with `VERIFY_OK` if all assertions succeed. The program forms the polynomials \(T_{m,j}\) by exact integer binomial coefficients reduced modulo each prime, verifies the determinant and scalar-factorization identities coefficient by coefficient, and separately constructs Cartier matrices by the exponent-selection rule for all \(r\in\mathbb F_p\) with \(r^2\ne4\). It computes their row ranks by modular Gaussian elimination and compares with the theorem for primes \(17,41,73,89,97,113,137,193\).

Actual execution returned: `VERIFY_OK: symbolic determinant and factorization, 8 prime characteristics, exhaustive rational parameters and independent Cartier ranks`.

The certificate is a finite check rather than an infinite-characteristic proof. The complete proof, including the nonstandard recurrences, differential equations, uniqueness bounds, and semilinear stable-rank reasoning, is in RESULT.md. Verification does not constitute independent mathematical review.
