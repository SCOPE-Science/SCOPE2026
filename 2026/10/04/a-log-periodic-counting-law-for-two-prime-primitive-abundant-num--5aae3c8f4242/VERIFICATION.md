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

The exact symbolic checks are:

1. For odd prime support \(p<q\), the maximal possible abundancy ratio is less than \(15/8\), so no odd integer with exactly two distinct prime factors is abundant.
2. For \(n=2^a p^b\) and \(B=2^{a+1}\), abundance is exactly \((B-p)p^b>B-1\), while deficiency of \(n/p\) is exactly \((B-p)p^{b-1}<B-1\). These inequalities force \(b=1\).
3. With \(b=1\), abundance and deficiency of \(n/2\) reduce to \(2^a<p<2^{a+1}-1\).
4. The resulting bijection with non-Mersenne odd primes gives \(P_2(X)=\pi(U)-2-\mathcal M(U)\) exactly for \(X\ge16\).
5. Since \(\mathcal M(U)=O(\log U)\) and \(U/2^m\in[1,2]\), the usual prime number theorem is uniform over the required compact multiplicative range and gives the stated phase function.

The included `verify.py` uses only the Python standard library. It computes exact divisor sums through \(500000\), factors every integer in that range, checks every proper divisor for each abundant two-prime-support candidate, and compares the strict definition with the theorem’s factor criterion. It also checks the exact counting identity on 49 phase points. The successful output is:

`VERIFY_OK bound=500000 support_two_checked=150785 two_prime_pan=159 phase_identities=49 first=[20, 88, 104, 272, 304, 368, 464, 1184, 1312, 1376, 1504, 1696]`

This finite computation does not certify the infinite asymptotic. The infinite statement is established by the algebraic classification, exact counting identity, elementary Mersenne-prime bound, and prime number theorem.
