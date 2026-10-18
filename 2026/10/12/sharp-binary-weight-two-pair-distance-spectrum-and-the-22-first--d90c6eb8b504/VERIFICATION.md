---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Disjointness of two-support codewords follows from shared-one Hamming distance two and d_pair≤4. For disjoint P,Q, d_pair=8-e(C_n[P∪Q]), so each union has at most one cycle edge. Incidence counting excludes n=7,8 with three supports and n=9 with four. Circulant simple connected 4-regular graphs provide Euler tours at all even n≥10; inserting a common zero does not lower pair distance, providing odd n. At full even support each position receives one word label twice and no adjacent same-label positions, and pair-distance forces no repeated graph edge. Independent exhaustive enumeration of all 945 perfect matchings of 10 coordinate positions, using direct cyclic pair-distance rather than the submitted Euler recurrence, found exactly 22 admissible matchings and three dihedral orbits of sizes 2,10,10. The source independent K5 tour checker was read and gives 528 tours from a fixed start, agreeing 5*528/5!=22.

## originality

PASS

Prior Chee et al. use K5 Euler tours to construct other MDS pair codes; that graph idea and likely numerical optimal-size portions are not new. The complete converse classifying all even full-support extremizers and exact 22-set/three-orbit census are separate from inspected generic pair-weight bounds. The highly relevant 2025 Zhao–Chang paper is not available in complete text and could overlap the classification, a material priority risk.

## value

PASS

The first attained full-partition case and complete equality-set and dihedral classification answer a natural extremal coding theory question; an exact equality census is meaningful even if broader code-size bounds were established previously.

The dated certificate retains the supplied scientific assessment, sources and limitations.
