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

For p dividing b, unequal digit valuations make v_p(a+c) their minimum, already met by both terms. When the valuations are equal, the term in the lower position has strictly smaller valuation than the other; hence the valuation of n is exactly v_p(a)+i v_p(b). This proves the exact lower-position cutoff, including i=0. The coprime part of the sum divides n iff c(b^(j−i)−1) vanishes modulo it, so division by gcd(q,c) gives the order modulo h, with h=1 unobstructed. For positive gap t k, the admissible lower positions number max(L−I−tk,0), which gives the floor expression even for L≤I. At N=L−I≥0 the exact sum is N²/(2t)−N/2+r(t−r)/(2t), including N=0; expansion proves the stated coefficients and bounded nonnegative periodic remainder. Independently, python3 /workspace/branches/independent_replays.py, function niven, recovered the nine decimal frequency classes for all 81 ordered pairs directly from modular divisibility, not the frozen valuations/order implementation, and verified 1483/48, 623/6 and 1483/1944. Direct decimal counts gave Θ(20)−Θ(4)=−2/3 and Θ(29)−Θ(5)=−1, ruling out periods 16 and 24. Every proper divisor of the already proved period 48 divides one of these two, so the least period of the tail is 48. The normalization is 81 binomial(L,2) in base 10, not 10^L, and only the remainder is periodic.

## originality

PASS

Credit is restricted to the exact all-base ordered-pair cutoff/order law, its closed all-length sum, and the sharp decimal phase and density. Fixed-sum studies already supply an implicit exact decimal counting procedure on this subpopulation by restricting to the union of classes with two occupied positions. They are prior coverage of the existence of residue-class counting, not evidence for novelty of quasi-polynomiality by itself. The inspected procedure does not identify each pair's sharp base-prime cutoff and exact gap progression in arbitrary base or extract the least collective decimal phase and constants.

## value

PASS

Exactly two occupied positions is the first support size where digit interactions can change divisibility. Splitting the exact lower-position cutoff from the exact admissible gap reduces the full population law to a finite digit-pair census for every base. The exact decimal proportion and the least collective phase quantify a natural conditional population not resolved by unrestricted Niven asymptotics. The useful contribution is the classifier and sharp arithmetic data, not merely observing that finite residue classes yield polynomials.

The dated certificate retains the supplied scientific assessment, sources and limitations.
