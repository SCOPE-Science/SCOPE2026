---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Starting from M∏(p−2)=∏(p−1)−1 for an odd squarefree Deaconescu number, one has M odd, M≥3 and M<∏(p−1)/(p−2). The modulo-3 classification is exhaustive: if 3 divides n, every other prime must be 1 mod 3; if 3 does not divide n, residue classes 1 and 2 mod 3 cannot mix. The resulting congruences force M≥5 or 7 in the 1-mod-3 patterns and M≥3 in the all-2-mod-3 pattern. Because each factor (p−1)/(p−2) decreases with p, the extremal products over the smallest admissible primes control every configuration with at most 2858 factors. I independently recomputed the exact integer cross-products: the two 1-mod-3 bounds are below 5, the first 2858 2-mod-3 factors are below 3, and the 2859th crosses above 3; the terminal primes are exactly 56569, 56599, 56081, 56087. Thus all r≤2858 cases are excluded and the claimed cutoff follows. The finite sieve certifies only the explicit prime/product thresholds; the universal exclusion uses the monotonicity and residue proof.

## originality

PASS

Hasanalizade's full 2022 paper proves oddness, squarefreeness and ω(n)≥7 and already uses M<φ/S2 as a small-support exclusion. Mandal's 2025 primary article raises the general bound to 17 and states that multiplier-3 solutions have all prime factors 2 mod 3 with ω(n)≥48. The audited result strengthens these by an exhaustive modulo-3 pattern split and exact prime-class extremal products to 2859 for every multiplier. Resultary and targeted literature searches found no stronger or equal published bound or the 56087 crossing. This is not a simple restatement of the prior ratio inequality because the decisive new content is the residue-class partition plus a much deeper exact product threshold.

## value

PASS

Improving a seven/17-factor obstruction to 2859 factors materially changes the known quantitative landscape of Deaconescu's conjecture, and the exact threshold exposes the current modulo-3 method's natural limit. The result combines a structural residue sieve with an exact finite cutoff rather than merely increasing a search bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
