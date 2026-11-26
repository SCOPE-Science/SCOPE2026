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

A strong-resolving set must hit each MMD pair: a non-endpoint landmark would extend a geodesic past one of the pair's maximally distant endpoints. Conversely a shortest path through any prescribed pair extends to a geodesic with MMD endpoints; a chosen endpoint resolves the original pair. In a plane incidence graph the nonincident point–line pairs are at diameter three, whereas same-side pairs and incident pairs have neighbors witnessing failure of maximality. Thus a complement is allowed exactly when all its selected points lie on all its selected lines. Two points have only one common line, so every mixed complement has a singleton side. Counting the pure sides and both mixed orientations, subtracting the duplicated empty set and duplicated incident pairs as appropriate, yields the displayed polynomial. The mixed stars have size at most q+2<n and are inclusion-maximal exactly when the entire pencil or row is present. The two full pure sides are also maximal. Complementation gives the two bases, the 2n larger inclusion-minimal resolvers, and their size gap q²−1. The argument uses only the plane axioms. Independent computations matched the full distributions at q=2 and q=3 and checked strong resolution directly on all 16,384 subsets at q=2.

## originality

PASS

The MMD/vertex-cover reduction is standard and not credited as new. The claim supported as distinct is the full all-order enumerator and exact classification of inclusion-minimal strong resolvers for arbitrary finite projective planes. The closest same-auxiliary-graph theorem gives domination-sequence invariants, and the closest same-enumerator result concerns a different incidence family. No inspected statement covers the bound claim.

## value

PASS

Strong metric dimension alone cannot distinguish the two pure minimum configurations from the much larger inclusion-minimal ones. The full structural census on a canonical graph family gives both every cardinality and an unbounded q²−1 gap between minimum and merely inclusion-minimal certificates. Its dependence only on the plane order, without a field or coordinate hypothesis, gives a useful all-plane invariant and exact check for other methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
