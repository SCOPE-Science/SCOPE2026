---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

For n=2^k p q, M=2^(k+1)-1 and a=M(p+1)-h q with h=p-M. In the strip p>M and p>h^2, h is even and at least two. The exact semiperfectness obstruction from Iannucci is equivalent to the nonexistence of a bounded representation a=r+s p+t q. When 0<a<q and a<Mp<pq, t must be zero, so weirdness is equivalent to a mod p>M. Reducing a modulo p gives a≡-h(q+1) mod p, so this is exactly h(q+1) mod p in {1,...,h-1}, equivalently q≡-1+u h^{-1} mod p. The strict abundance inequalities give M(p+1)/(h+1)<q<M(p+1)/h. These are both necessary and sufficient in the stated strip. The one-third-scale bound follows from q>M(p+1)/(h+1) and h>=2. For every proper divisor, the 2^j, 2^j p and 2^j q cases are deficient; for 2^j p q with j<k the abundance is U(1+p+q)-pq<0 because U=2^(j+1)-1<= (M-1)/2 and p,q>M. Thus the constructed weird numbers are primitive. The verifier source compares the exact interval predicate with direct divisor-subset sums for small k; finite tests are not used as the proof.

## originality

PASS

Iannucci already gives the exact semiperfectness obstruction, the abundance identity and a conjectured one-third bound; the general three-quarter bound is also a prior result. The present claim is a narrower, motivated near-Mersenne strip with an exact q residue-class classification and a one-third-scale abundance bound on that strip. The broader three-quarter theorem does not imply this stronger restricted statement.

## value

PASS

The prime gap h=p-(2^(k+1)-1) defines a natural near-Mersenne regime tied to an open abundance bound. The result gives an exact congruence-and-interval classification for q and a stronger abundance bound in that strip, rather than a small numerical census or a restatement of the general criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
