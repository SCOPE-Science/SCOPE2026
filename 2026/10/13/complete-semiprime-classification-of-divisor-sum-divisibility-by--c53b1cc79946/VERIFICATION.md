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

For n=p², gcd(p²+p+1,p)=1 would force p²+p+1|p−1, impossible. For n=2q distinct primes, (q+1)|2q(q−1) gives q+1|4, hence q=3, and n=6 works. For odd p<q write A=(p+1)/2, B=(q+1)/2. Exact divisibility is AB|pq(A−1)(B−1). Since gcd(B,q(B−1))=1, B|p(A−1); and gcd(A,p(A−1))=1, A|q(B−1). Since q>A prime, A|B−1. With B>A>A−1 and gcd(p,A−1)=1, B=pd for d|A−1. Because p≡−1 mod A, A|d+1 forces d=A−1. Thus q=p(p−1)−1. Conversely B=p(A−1), gcd(A,B)=1, B|p(A−1), A|B−1, and exact original condition follows. This covers all n with Ω(n)=2 and makes no claim about infinitely many such prime pairs.

## originality

PASS

OEIS A066995 defines exactly σ(n)|nφ(n) and lists examples including 6,15,95,287, but its inspected entry does not give the semiprime iff criterion q=p(p−1)−1. Other OEIS entries and frozen SCOPE records address reversed divisibility φ(n)|nσ(n), τ(n), or π(σ(n)), not the same predicate. The explicit all-semiprime criterion remains a best-of-knowledge separate classification.

## value

PASS

A natural semiprime layer of an established divisor-sum/totient divisibility sequence receives an exact arithmetic characterization in terms of simultaneous polynomial prime values. This supplies a structural necessary-and-sufficient test, not merely additional OEIS terms, and sharply excludes all prime squares. The prime-pair infinitude problem remains open and is not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
