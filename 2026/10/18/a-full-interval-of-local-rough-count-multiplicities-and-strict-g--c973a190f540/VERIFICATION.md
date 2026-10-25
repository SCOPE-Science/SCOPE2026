---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For even h=P−1 with P≥7 prime, CRT sets b≡2 mod p for toggled primes T⊂U_h={h/2<ℓ<h primes excluding divisors of h+2}, otherwise b≡1 mod p. At any p<h, both endpoints b,b+h remain units, by P=h+1 prime and the ℓ∤h+2 exclusion. An interior position m=i+1 is killed by an untoggled divisor if composite or prime ≤h/2. Large untoggled primes are killed at themselves; selected large primes survive all p, because for toggled p the even m=ℓ+1≤h cannot be divisible by odd p>h/2, and untoggled p≠ℓ does not divide ℓ. Hence rho_h(b_T)=|T| and distinct T give ≥binomial(t_h,k) admissible classes for each k, without gaps. PNT along prime P gives t_h unbounded; with pre-established finite positive series c_r and positive even-h singular terms, c_{r+1}−c_r≥Σ(h)binomial(t_h,r)/|A_h|>0 for each r≥1. Independently checked exact CRT classes and all selected subsets at P=7,11,13,17,19. Claim does not assert unconditional actual-prime-gap frequencies.

## originality

PASS

Best-of-knowledge mathematical noncoverage after statement-and-implication comparisons. Resultary local sieve/prime-gap search retrieved unrelated residue/census findings without the all-r exact-count construction; it is non-exhaustive. No negative search establishes absolute novelty.

## value

PASS

The natural exact local rough-count distribution underlying the published prime-gap cumulative constants acquires full consecutive support on arbitrarily large intrinsic prime anchors, proving previously unestablished strict positivity of every adjacent difference c_{r+1}−c_r. Positivity of cumulative constants or zero-rough case alone cannot give strictly increasing entire sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
