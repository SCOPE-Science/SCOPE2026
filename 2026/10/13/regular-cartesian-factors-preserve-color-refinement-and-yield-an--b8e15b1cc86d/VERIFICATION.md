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

At round zero colors are uniform. At each step in the product, the H-neighbors add exactly d copies of the old color of g to the G-neighbor multiset. Because the old color is included in the signature, compare only equal old colors, for which subtracting those copies restores the G signature. This gives equality of partitions at every round and equality of the first stable round, including d=0 and a singleton factor. In the connected relatively prime case the Imrich–Miller automorphism formula permutes only isomorphic Cartesian primes, so no coordinate crosses the G/H split; orbits are Cartesian products, proving the reverse implication. For sufficiency the coordinatewise subgroup already acts transitively on each color class even without that prime hypothesis. For P_m let δ be distance to the nearer endpoint: round t has classes given by min(t,δ). The first split when m≥3 is by degree; subsequently the saturated class splits off δ=t as exactly the vertices meeting the δ=t−1 class whenever t is below max δ. Reflection preserves final equal-δ pairs, so the depth is floor((m−1)/2), including m=2. For the witness apply lifting to P_m times the union C_n ⊔ C_3 ⊔ C_{n−3}. This equals the disjoint union of the two compared products, so their actual joint-refinement colors have equal multiplicities, not just their unordered block sizes. Connectedness distinguishes the graphs. The cycle symmetries and path reflection prove refinability.

## originality

PASS

The refinability/amenability distinction, regular cycle comparisons, Cartesian automorphism theorem and related exact depths on products of paths are established. The distinct contribution is the all-round regular-factor partition law, its exact orbit criterion under Cartesian relative primality, and a connected nonamenable but refinable family of unbounded exact depth. The checked closely related statements do not cover that combination or the general lifting law.

## value

PASS

The law is a reusable exact transformation covering arbitrary first factors, disconnected regular factors and every finite refinement depth. It links color dynamics to the full product orbit structure under a precise hypothesis. The cylinder application exhibits a connected family in which 1-WL recovers orbits at arbitrarily large, explicitly known depth but fails graph identification; neither notion is interchangeable with the other.

The dated certificate retains the supplied scientific assessment, sources and limitations.
