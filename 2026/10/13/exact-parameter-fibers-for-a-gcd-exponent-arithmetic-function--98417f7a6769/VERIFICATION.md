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

Equality of prime factorization values is exactly equality of vector (gcd(e_i,alpha))_i. Taking lcm coordinatewise gives gcd(L,alpha) by primewise max-min identity. Conversely gcd(L,alpha)=gcd(L,beta) implies every exponent gcd agrees. Divisors d|L index all distinct values; phi(L/d) counts parameters in one period; comparing inputs L and L+T proves L divides every period. Independent gcd tuple tests validated every fiber for exponent tuples of small support. Result holds n>1 and positive alpha.

## originality

PASS

Best-of-knowledge refinement from known L-periodicity and sufficient equality to a complete necessary-and-sufficient parameter fiber classification, orbit size, exact multiplicities, and least period. Later Mittou orbit study describes exponential-divisor inclusion, not all parameter fibers.

## value

PASS

The same-function parameter map has a natural finite orbit whose cardinality, period minimality and multiplicity are not supplied by known papers. Although proof uses elementary gcd/lcm, this is a complete motivated classification of the actual arithmetic function, not an arbitrary computed slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
