---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A canonical word corresponds bijectively to the perfect matching of its paired positions, and a qualifying split puts one endpoint of each pair in each side. For fixed γ, the endpoints in the ordered first side match the γ-indexed endpoints in the ordered second side. I independently enumerated balanced position cuts with 0 on the first side, then every bijection between the two sides. Each pairing was recorded once per induced permutation using a set of matching codes; entering the same code at the inverse permutation accounts for the omitted swapped cuts. This exhausts both all words and all splits without counting multiple witnesses as extra words. All entries of both supplied tables for k=5,6 agree. At k=2,3,4 the maxima 2,9,33 have cyclic maximizers, with the listed maximizing sets. At k=5,6 the maxima and their entire argmax sets are 134 at 34521 and 54123, and 532 at 345621 and 651234. The cyclic lists in shift order are [42,115,123,123,115] and [132,396,508,278,508,396]. The word counts also agree with the double factorials.

## originality

PASS

The incidence graph, the identity degree, and the small k=3 calculation are established background. The exact k=5 and k=6 permutation-side maxima, their maximizing inverse classes, and the failure of cyclic shifts at k=5 were not found in the inspected sources. The original question asks for the maximum vertex degree; the frozen record gives finite permutation-side results, not a general solution.

## value

PASS

The primary paper motivates the precise maximum-degree invariant independently of the computation. The complete consecutive cases establish a boundary for the natural cyclic-shift candidate subclass, with gaps of 11 and 24 at k=5,6 and noncyclic maximizing inverse classes in both. This is useful finite extremal data for the stated problem, not just a count of shuffle representations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
