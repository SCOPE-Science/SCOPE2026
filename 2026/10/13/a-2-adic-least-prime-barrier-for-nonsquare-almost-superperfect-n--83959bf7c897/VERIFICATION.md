---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For n>1 odd nonsquare satisfying sigma(sigma(n))=2n-1, Fang establishes odd n and square sigma(n). Odd nonsquare implies even sigma(n), so b=v2(sigma(n)) is positive even. Since I(n)I(sigma(n))=2-1/n<2, I(sigma(n))>=I(2^b)=2-2^-b and I(n)>=product over prime support (1+1/p), the strict product bound <2^(b+1)/(2^(b+1)-1) and least prime P>2^(b+1)-1 follow. 2-adic LTE on sigma(p^a) for odd a gives v2(p+1)+v2(a+1)-1. Independent exact checks for odd primes<60 and exponents1..19 confirmed parity and LTE. No existence or nonsquare solution is claimed.

## originality

PASS

Fang supplies indispensable premises square sigma(n), odd n, a special 3-divisor implication and the abundancy identity, but its inspected complete four-page text does not state the stronger b-dependent least-prime threshold or exclude 5 and 7 for a nonsquare branch. The result combines those premises with a previously unused full 2^b local index, yielding an invariant-sensitive exponential bound. The derivation uses elementary known tools and could appear as an informal earlier corollary, but no direct prior stronger statement was located.

## value

PASS

The almost-superperfect equation is an unresolved Diophantine classification. A necessary prime-support sieve P>=11 that becomes exponentially stronger with even b is a mathematically motivated obstruction for hypothetical nonsquare solutions, not merely a parity or normalization check. The explicit prime-factor LTE formula permits further structural pruning. The result is conditional and does not resolve existence or all square solutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
