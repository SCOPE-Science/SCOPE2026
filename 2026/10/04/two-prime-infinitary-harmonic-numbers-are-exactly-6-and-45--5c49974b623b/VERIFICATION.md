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

The proof is symbolic and unrestricted. Its critical checks are:

1. For fixed prime \(r\) and distinct \(i<k\), the factors \(r^{2^i}+1\) and \(r^{2^k}+1\) have gcd at most \(2\); for odd \(r\) the gcd is exactly \(2\), and for \(r=2\) it is \(1\).
2. Integrality of \(H_\infty(p^a q^b)\) allows no odd denominator prime outside \(\{p,q\}\); a same-base factor is never divisible by its base prime.
3. For odd \(r\) and \(i\ge1\), \(r^{2^i}+1\equiv2\pmod8\) and exceeds \(2\), so it has an odd prime divisor.
4. The only apparent four-component case forces \(q+1\) to be a power of \(2\), while \(q\mid p^{2^i}+1\) forces \(4\mid q-1\), an impossibility.
5. The published low-component classification then restricts the two-prime case to \(6\) and \(45\).

`verify.py` performs an exact rational check for all distinct primes below 100 and exponents from 1 through 15. Its finite range is corroborative only and is not used to establish the theorem.
