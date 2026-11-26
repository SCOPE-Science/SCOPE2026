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

The binomial interpolation converges uniformly because the kth term has valuation at least k−ν₂(k), and agrees with the combinatorial sequence at each positive index. At 0 and 1 its value is 2; at −1 and −2 it is −2 by the geometric and weighted geometric series, so its forward difference vanishes at 0 and −2. Cao–Pan Theorem 2 extends by continuity to the four residue classes. At even x the signs at x and x+1 are opposite, so the forward-difference increment for a shift by 2^α, α≥2, is 2^(α+2) modulo 2^(α+3). Summing an odd number of increments preserves this exact valuation, giving a distance factor of 1/4 on each even class modulo four. Anchoring at 0 or −2 gives ν₂(n)+2 or ν₂(n+2)+2, respectively; the other factor of n(n+2) has valuation one. On odd indices the α=1 congruence makes D_n constant modulo 16 along steps of two, with D_1=4. The two distinct exact-level classes modulo 2^(j−1) give the stated densities; index zero is correctly excluded. Independent exact rational sums of the displayed binomial series through n=64 checked all first-difference valuations through n=63 and residue sets at levels 4–6. The uploaded recurrence checker was inspected, not executed; neither finite check is the all-index proof.

## originality

PASS

The oldest resolved matching machinery supplies shifts of the sequence and its binomial coefficients, not the anchors or exact consecutive-difference valuation fibres. A distinct indexed record is exactly equivalent after normalization, but the evidence places that publication after the frozen finding and establishes no earlier coverage. This is a judgment on the frozen result against evidenced earlier work, not a claim of unique discovery or historical priority.

## value

PASS

An exact first-difference valuation, not just a congruence bound, for a classical combinatorial sequence determines every divisibility level and its frequency. The two explicit 2-adic roots and local isometry explain the full split of indices, including the missing level three. This is a usable arithmetic classification, not finite table reconstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
