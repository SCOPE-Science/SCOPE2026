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

The identities a_n=a_(n−1)(1+b_n), b_n | n, and b_n=n/gcd(n,a_(n−1)) are exact. The initial values a_3=6, a_4=18, a_5=108, a_6=216 give persistence of 2 past index 3 and 4 past index 6. Thus at 2p the gcd is 2 or 2p. If p divides a_(2p−1), one factor 1+b_k in its product must be p or 2p, since 2≤1+b_k≤2p. For b_k=p−1, divisibility forces k=p−1 or 2p−2. The former would require gcd(p−1,a_(p−2))=1 despite both being even; the latter would require gcd(2p−2,a_(2p−3))=2 despite both being multiples of 4 (p≥5). The other possibility b_k=2p−1 forces k=2p−1, and gives the reverse implication by inserting the factor 2p. Independently, for prime q≥5, q cannot divide a_(q−1): the only possible factor would be 1+b_(q−1)=q, again excluded by evenness. Hence b_q=q. This proves the unconditional direction when 2p−1 is prime, and only the local prime-or-one assumption forces primality in reverse. The standalone private replay `python3 /workspace/checks/finite.py 4` uses actual unbounded integers and gcds through n=6000 (428 tested primes p), corroborating both equivalences on that range. The bundled exponent-based run through 200000 is recorded evidence, not the basis for the infinite proof or the unproved converse.

## originality

PASS

The supported distinct content is the unconditional dependence of b_(2p) on the maximal increment at its preceding index, and hence the conditional composite-index detector in the original K=1 recurrence. The two-value restriction and prime-step facts are background, not novelty. The closest prime-detection theorem inspected changes the recurrence to K=2 and uses prime indices and a different adjacent argument; it does not imply this biconditional.

## value

PASS

The result determines exactly which mechanism can supply a missing prime factor by the even semiprime index 2p, an infinite structurally defined family in the original recurrence. It replaces the naive global prime-or-one premise for the detector with the exact local statement needed and gives an unconditional adjacent-increment test. This is more than the two-value restriction and it neither assumes nor claims a proof of infinitely many prime pairs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
