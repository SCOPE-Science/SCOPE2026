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

For φ(n)=1 the derivative is zero. Otherwise D(2^e)=e·2^(e−1). Dyadic φ forces odd prime factors to occur once with p−1 a power of two, and primality forces p=2^(2^j)+1. For n=2^a P with T the sum of those distinct 2^j, odd n would require e=T and T·2^(T−1)=P odd: T≥2 is impossible and T=1 gives 1≠3. For even n, the equation is e=a−1+T=2^(2−T)P; since P is odd and e is integral, T≤2. Substitution yields n=32,192,80 for T=0,1,2, respectively. The three advertised totients give the original equality directly. This excludes every additional prime or prime support without assuming a list of all Fermat primes. Gauss–Wantzel gives the polygon interpretation for n≥3. The recorded sieve is a finite cross-check through 10^6, not the completeness proof; no uploaded code was run.

## originality

PASS

The individual witnesses and the Fermat-prime description of the admissible domain are known. The supported distinct claim is the complete dyadic-totient intersection: the strongest verified indexed theorem covers two of the three witnesses on a different domain, and does not rule out the other possible odd prime supports allowed by the dyadic hypothesis. No inspected source supplies that exclusion. This is a best-of-knowledge judgment, not a priority claim.

## value

PASS

This is a complete classification on a classical intrinsic arithmetic domain, not an arbitrary cutoff or a recomputation of known witnesses. The valuation constraint rules out unboundedly many possible prime supports, including any involving as-yet unknown Fermat primes, and identifies exactly the regular constructible polygon indices satisfying the equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
