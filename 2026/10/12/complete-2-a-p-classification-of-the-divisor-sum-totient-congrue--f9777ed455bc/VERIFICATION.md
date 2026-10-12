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

The proof in `RESULT.md` covers all exponents \(a\ge1\) and odd primes \(p\); no finite cutoff is used in the mathematical argument.

The attached `verify.py` uses a sieve of odd primes less than \(100000\) and tests all exponents \(1\le a\le24\). For each pair it computes independently the exact integers \(n=2^a p\), \(\sigma(n)\), and \(\varphi(n)\) and asserts the congruence is equivalent to the classification (2). It also checks all corresponding multiplier values and the elementary divisor restrictions for \(2\le a\le40\).

The fixed bound is a reproducibility check, not evidence of unrestricted exhaustiveness. The proof's exact divisibility and inequalities are the unrestricted certificate.
