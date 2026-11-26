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

For an exact block p^a, phi(p^a)*sigma(p^a)=p^(2a)−p^(a−1), giving both the product identity and F(p^a)=p^(a−1). For n=m p^a q^b with distinct p<q and gcd(m,pq)=1, the remaining normalized product is in (0,1]. Thus F(n) is at least m² p^(a−1)q^(b−1)(p^(a+1)+q^(b+1)−1), which is at least 2²+3²−1=12. Equality forces m=1, a=b=1, and p=2,q=3, and F(6) really is 12. On n>1 the smaller fibers follow by enumerating p^(a−1)=1,2,...,11: 1 gives precisely the primes, 6 and 10 are not prime powers, and positive prime-power targets p^j give the single input p^(j+1). No power of one prime gives 12. The sub-12 equivalence is on n>1, as stated by the proof; F(1)=0 if one includes the unit. The supplied verifier was inspected but not executed; the symbolic bound proves exhaustiveness independently of the finite range.

## originality

PASS

The defect itself, prime and prime-power evaluations, individual terms, positivity, and the product formula need not be new. The comparison supports the distinct sharp lower bound on all mixed-support inputs, including its equality case and the resulting unrestricted low-fiber completeness. No inspected statement establishes that restriction by a bound or forces it from a table alone.

## value

PASS

This is the first possible defect for mixed prime support, not an arbitrary numerical cutoff. Up to the cutoff the exact defect determines whether the input is a prime power, and for 2≤F(n)≤12 it determines the entire fiber, including two gaps and the first mixed case. The contribution is modest but structural; listing the known prime-power evaluations alone would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
