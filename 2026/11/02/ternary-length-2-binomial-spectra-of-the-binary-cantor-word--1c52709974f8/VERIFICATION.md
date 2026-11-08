---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For fixed point of 1→101, 0→000, length n=3^k and B=2^k, the ones in C_k occupy positions f(j)=2Σ epsilon_i(j)3^i. Every length-n factor is 0^n or a zero-padded prefix/suffix of C_k because the base word has no 11 and contains 00,01,10. Counting scattered 01 using first t one-positions gives exactly the two progressions t(m-t)-P_t and t(n-m)+P_t, m∈[f(t-1)+1,f(t) or n]. Counting their intersections using m+m’=n+t+2P_t/t proves b_{c,2}(3^k)=2·3^k+1−ΣO_t. For k≥3, t=3·2^{k-2} and the explicit paired lengths produce 2·3^{k-3}+1 distinct nonidentical factor pairs with equal binomial profiles; their differing last-one positions exclude literal identity. Independent brute-force scattered-subsequence profiles of actual substitution words for k=1..6 match the arithmetic family exactly. That finite test does not establish the all-k claim.

## originality

PASS

The source morphism is not Parikh constant, so Rigo–Salimov Parikh-constant-morphism binomial complexity theorem does not apply. The same Cantor sequence has k-abelian complexity literature, but k-abelian counts contiguous blocks rather than the scattered subsequences in 2-binomial equivalence. The exact power-of-three profile and linear collision family are best-of-knowledge additional results.

## value

PASS

The exact complete 2-binomial profile set at all ternary lengths is a natural infinite combinatorics-on-words invariant; explicit O(2^k)-term arithmetic counting avoids enumerating the 3^k factors, and linear nontrivial collisions elucidate information lost by binomial observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
