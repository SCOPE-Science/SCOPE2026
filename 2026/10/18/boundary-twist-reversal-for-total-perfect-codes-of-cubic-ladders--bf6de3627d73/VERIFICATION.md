---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The mathematical proof derives the two recurrence relations, their period-three/anti-period-three solutions, the exhaustive nine binary words, and the two seam conditions. It also supplies the full six-triple intersection certificate used for unordered three-code partitions.

`VERIFY.py` constructs prism and Möbius graph edges independently and enumerates every vertex subset of both graphs for each \(3\le n\le9\). There are exactly 699008 tested labeled subsets across 14 graph profiles. The program directly checks all defining open-neighborhood equalities, equality of found solutions with the explicit periodic-word list, code cardinality, and all unordered triples of codes for a partition. It then checks formula counts for 296 profiles with \(3\le n\le150\). Output: `CHECKS.txt`.

These finite computations neither establish novelty nor substitute for the unlimited-width proof; they are definition-level boundary and arithmetic checks. Scientific checking beyond this documented proof and computation is not claimed.
