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

The local criterion was independently reconstructed in part-count variables: for an outside vertex in part \(i\), a valid geodesic triple with two selected vertices exists exactly when either the selected set meets its part and at least one other part, or some other part contributes at least two selected vertices. This criterion gives the stated minimum-number cases and exhausts all minimum sets: the whole graph for a complete graph, cross-part pairs plus two-vertex whole parts in the bipartite case, whole two-vertex parts for at least three parts, and otherwise the three listed size-three patterns. Independent brute force on every complete multipartite type through order nine reproduced both the minimum and the exact minimum-set count for 87 types.

## originality

PASS

The exact number and complete classification/count of minimum \((3,2)\)-dominating sets were not found in the foundational paper, older graph literature, or published SCOPE comparisons. The new local occupancy criterion is required to obtain the case split and enumerator, so the result is not implication-covered by ordinary or neighboring domination formulas.

## value

PASS

This is a natural complete classification for a canonical graph family in a newly introduced domination theory, and it goes beyond a single minimum number by identifying and counting every minimum set. The foundational paper explicitly calls for exact values on classical families, so the object/invariant motivation precedes the computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
