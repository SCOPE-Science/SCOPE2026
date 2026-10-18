---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Li's theta reduction f(n)≡[q^n]Θ(q)^2 (mod 3) holds formally. For N=20n+9, pair (a,b) maps bijectively to X=5(a+b)−3,Y=5(a−b) with X²+Y²=N, X≡2 mod5,Y≡0 mod5 and theta sign (−1)^Y. Every Gaussian-unit orbit for odd N≡4 mod5 has exactly one canonical representative. In Z[i], inert p≡3 mod4 of odd exponent forbid orbits; altering a split prime factor for p≡1,9 mod20 preserves Y parity, while p≡13,17 mod20 flips it after canonical quarter-turn. Thus a local alternating exponent sum annihilates odd exponents of the latter; surviving |g(n)|=∏_{p≡1,9 mod20}(e_p+1). Mod3 adds e_p≠2 mod3. Independent direct partition dynamic programming, Gaussian norm sums and factorization agree for n=0..400 including n=31,N=629; unlimited theorem follows Gaussian UFD and parity.

## originality

PASS

Li 2026 establishes exactly the theta-square reduction and inert-prime progression congruences, and its Section 8.2 explains a limit of that progression technique for split primes. The present all-index if-and-only-if prime exponent rule incorporates p≡13,17 mod20 cancellation and p≡1,9 mod20 (e+1) factors. Neither Li's restricted progression theorems nor the classical sum-of-two-squares existence criterion implies signed-weight cancellation; arithmetic of Gaussian factors supplies it. Best-of-knowledge, with potential earlier Hecke-character coefficient description risk.

## value

PASS

The original restricted partition function and modulo-three vanishing support are a motivated arithmetical object; a complete prime-factor criterion for every n is stronger than partial progressions and answers exact nonvanishing, including 629=17·37 where ordinary sum-of-two-squares permits representations but signs cancel. Exact necessary-and-sufficient support is a natural independently useful invariant, not a routine parity check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
