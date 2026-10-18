---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: Reconstructed the prime divisor-sum lemma: sigma(t) prime forces a prime power q^e with e+1 prime, and odd e then equals 1. Since phi(n) is even, sigma(phi(n)) prime forces phi(n)=2^K; odd prime factors of n are distinct Fermat primes. Odd composite cases have >=4 nonzero binary digits but sigma(n-1) prime would force n-1 a power of two; for 4|n, n-1=3 (mod 4) implies exponent one and sigma(n-1)=n composite. Even composites must be 2∏F_j; j=0 gives n=6 excluded. For omega<=2 the remaining n=2F_j has 2^(2^j+1)+1 a power of 3. Modulo 8 forces even exponent 2h and factorization (3^h-1)(3^h+1)=2^(2^j+1) forces h=1,j=1,n=10. Prime inputs reduce precisely to the conditional Fermat/Mersenne criterion; no conjectural infinite-prime claim. Independent direct small-integer sigma/phi test through 11999 gave hits 3,5,10,17 with no contrary two-support case. Tests corroborative only.

## originality

PASS

PASS best-of-knowledge: OEIS A270414 gives the exact simultaneous-prime predicate and conjectures a global single composite example but does not establish the unrestricted omega<=2 subtheorem. G. L. Cohen and Luca–Pomerance study sigma(phi(n)) arithmetically, not this same conjunction. Semantic published-finding search returned nearby but different divisor-sum equations. A possible obscure elementary published proof remains a genuine risk.

## value

PASS

PASS: Resolves the first entire composite prime-support stratum of the long-standing natural OEIS A270414 joint-divisor-sum primality question for arbitrarily large integers, rather than merely extending a finite search. Distinctive structural two-factor obstruction and conditional prime classification give a useful exact boundary; no claim about omega>=3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
