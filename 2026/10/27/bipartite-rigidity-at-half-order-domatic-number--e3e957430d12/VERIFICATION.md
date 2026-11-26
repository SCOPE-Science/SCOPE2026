---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A universal vertex in a connected bipartite graph forces a star, whose domatic number is 2. Therefore at domatic number m≥3 every class in an m-class partition has size exactly two. A same-side dominating pair must exhaust that side; the other side then has 2m−2>2 vertices and cannot be partitioned into dominating pairs wholly contained in it. Thus the m pairs cross the bipartition, giving equal sides, and each pair requires all off-diagonal incident edges. This proves the missing edges form a matching. Conversely diagonal partners dominate across all off-diagonal edges. Both sides have size at least three, so no singleton dominates; hence γ=2 and there cannot be more than m classes. This family is connected since two same-side vertices have a common neighbor and every vertex has a neighbor. Each deleted matching edge forces precisely its endpoint pair, and the free vertices are paired by a bijection of the two sets of size m−t, counting each unordered partition once, including t=m. If t<m, deleting an unused diagonal edge stays in the family. In the crown, deleting any edge creates an endpoint of degree m−2, hence at most m−1 domatic classes by its closed neighborhood. Merging the two distinct endpoint classes of the original partition yields an (m−1)-class partition after deletion. The domatically perfect consequence only requires even order, forced by equality with γ=2. Inspected the frozen finite checker without running it. Its degree filter is necessary and checking for a partition into pairs is sufficient at these sizes by the preceding no-singleton argument; no finite enumeration is used for the classification.

## originality

PASS

The supported distinct claim is the full bipartite half-order characterization with its exact optimum partition multiplicity. The degree-based critical deletion and universal domatic inequality are not distinct general principles. The closest available comparisons address different invariants or only generic bounds. Matsumoto is a substantive unresolved primary-text risk; the inaccessible source neither establishes coverage nor certifies novelty.

## value

PASS

This solves a natural connected bipartite equality case for the domatic bound at γ=2. The structural description explains why only matching deletions occur, and the exact multiplicity distinguishes the freely permutable classes from forced ones. Those facts are useful for working with extremal partitions in this family even though the edge-critical corollary then takes only a degree argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
