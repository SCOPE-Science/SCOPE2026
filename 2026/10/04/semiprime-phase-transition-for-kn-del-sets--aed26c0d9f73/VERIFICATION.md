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

The unrestricted proof is symbolic and appears in `RESULT.md`.

For distinct primes \(p<q\), the checker compares two predicates:

\[
\operatorname{lcm}(p-1,q-1)\mid pq-k,
\]

which is exactly the Knödel condition on the unit-group exponent, and the
classification stated in the theorem.

It checks every \(1\le k\le200\) and every pair of distinct primes
\(p<q\le997\), subject to \(pq>k\). It also prints the semiprime members found
for \(k=2,3,5,7\) in a small range.

The finite check does not prove the infinite statement. Infinitude for prime
\(k\) uses Dirichlet's theorem for primes in the progression
\(1\pmod{k-1}\), and the asymptotic uses the prime number theorem for arithmetic
progressions. Composite \(k\) has only the finite alternative \(p<q<k\).
