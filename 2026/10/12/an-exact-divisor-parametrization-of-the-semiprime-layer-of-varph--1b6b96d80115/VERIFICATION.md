---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Prime squares fail modulo p and twice an odd prime fails by parity. For distinct odd primes, put u=(p−1)/2, v=(q−1)/2. Writing pq=2(2uv+u+v)+1 reduces the test exactly to uv dividing (u+v)(u+v+1). At u=ga, v=gb, coprimality of ab with a+b and of g with g(a+b)+1 shows the equivalent two conditions g|a+b and ab|g(a+b)+1. With h=[g(a+b)+1]/ab, expansion gives (ha−g)(hb−g)=g²+h and the factors equal (ga+1)/b and (gb+1)/a, hence are positive and strictly ordered. The inverse factor-pair search must retain g|a+b, coprimality and primality as stated. The bound h≤floor((3g+1)/2) uses a≥1 and b≥2. Reduction modulo v gives v|u(u+1), yielding q≤(p²+1)/2. A separate bounded direct test of 407,284 semiprimes up to 2,000,000 and reverse divisor enumeration for g≤499 agreed on exactly the eight listed values. This corroborates but does not prove the unbounded algebraic classification.

## originality

PASS

The base predicate, examples and even exclusion are known. The supported distinct result is the exact bidirectional fixed-gcd divisor parametrization with its finite h-range, not a new integer sequence or the claim that the examples were previously unknown. No checked statement provides or entails this classification via an equivalent parametrization.

## value

PASS

This classifies the entire first composite layer of a longstanding natural divisibility sequence, replacing unrestricted testing with a finite ordinary divisor search for each gcd and giving a separate fixed-smaller-prime size bound. The structural bidirectional result, not the eight example values, provides the utility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
