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

On n=2^(k-1) for k>=2, the exact identity C(n)=(M_k-1)/2-phi(M_k), M_k=2^k-1, follows from phi(2^(k-1))=2^(k-2) and sigma(2^(k-2))=2^(k-1)-1. For odd prime k, every q|M_k has order k mod q, so q>=2k+1. The number of distinct prime factors is <=k-1 (otherwise their product exceeds M_k). Product lower bound phi(M_k)/M_k >= 1-(k-1)/(2k+1)>1/2 gives C(n)<0; k=2 handled directly. For multiples of 12, 4095|M_k and phi(4095)/4095=192/455<1/2 imply C(n)>0. The five composite indices 4,6,8,9,10 complete the negative census k<12. Independent exact factorization/phi/sigma arithmetic for k=2..36 gives positives [12,20,24,28,30,36] and C(2048)=319. Euclid plus the progression 12Z supplies infinite negatives/positives; no unproved Mersenne-prime infinitude used.

## originality

PASS

Golomb (1993) proved both signs globally and considered powers of two but his infinite negative power-of-two example was conditional on infinite Mersenne primes. De Koninck–Luca (2007) prove order and density statements on unrestricted integers; those statements do not supply sign oscillation inside a zero-density powers-of-two subsequence. OEIS A065395 catalogs the unrestricted commutator and A116083 a different equality condition, not an all-prime exponent negativity rule with 12-divisible positivity. Focused Resultary and exact-query search revealed no dominating sequence theorem; unindexed elementary observations remain a risk.

## value

PASS

Replacing a conditional negative example with an unconditional infinite subfamily inside the SAME sparse powers-of-two sequence as an explicit positive progression resolves a natural restricted sign-oscillation problem. The result supplies concrete prime-index and 12-divisibility criteria and a sharp first positive instance n=2048. This is more than a routine composite calculation or finite list; the existence proof works for infinitely many exponents with distinct mechanisms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
