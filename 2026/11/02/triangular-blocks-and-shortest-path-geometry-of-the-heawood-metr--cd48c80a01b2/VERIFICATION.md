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

I independently constructed the incidence triples {a,b,a XOR b} on the seven nonzero binary vectors, computed all graph distances by Floyd–Warshall, and tested all four- and five-subsets for distinct vertex signatures. No four-subset works, so monotonicity excludes smaller sets, and exactly 168 five-subsets work. The basis classification follows because a collinear point triple produces three duplicate pairs of line signatures, which cannot all be broken by removing two selected lines from the unselected-line comparison. For a noncollinear triple all line signatures differ; the two selected lines distinguish the four other points precisely when both are tangents, each meeting two of those points with one point common. The dual argument applies to line-majority bases. In the separate replay I joined bases through their shared four-subsets and used Floyd–Warshall again: all degrees are 5, exactly 56 triangles occur with the stated majority-triple partition, every row has shells (1,5,18,49,71,24), unordered pair totals are (420,1512,4116,5964,2016), and the excess over 5−|B∩C| is 0 for 9660 pairs and 1 for 4368. These checks also give both radius and diameter 5. The replay is /workspace/branches/heawood_exact_replay.py. For transitivity, GL(3,2) acts transitively on the noncollinear triples (unordered vector bases). The stabilizer permutes the three tangents, one per point of the triple, and swaps any two tangent choices; a point-line polarity switches the majority types. Part-preserving automorphisms are determined by the images of a vector basis, since each third point on a line is the sum of the other two. There are exactly 168 preserving the parts and a dual coset of equal size. Both frozen checkers were inspected, not executed.

## originality

PASS

The minimum size five is known, and independent priority for the basis classification is not established. The closest related Resultary record, on edge-metric bases, actually realizes the identical token-jump graph by the same subset family despite its different resolving condition; it also gives some of the same coarse graph invariants. It is indexed later, and the finer all-pairs shell and relative-detour census is not established by the compared passages. The supported distinct contribution is the detailed metric and partition of this exact exchange graph, not generic reconfiguration or metric dimension, subject to the recorded access risks.

## value

PASS

The Heawood graph is a canonical symmetric instance for testing how optimum landmark sets can be transformed without losing resolution. The ambient overlap bound is natural before enumeration. Showing that departures from it are uniformly at most one but occur for exactly 4368 pairs identifies a precise obstruction that basis count and diameter do not encode. The triangular decomposition and exact pair metric make this a useful complete finite benchmark, not an arbitrary choice of sample sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
