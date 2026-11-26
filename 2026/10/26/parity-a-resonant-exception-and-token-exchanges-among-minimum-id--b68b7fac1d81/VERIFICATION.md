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

The frozen L–L exclusion uses an unjustified implication: a single exchange can in principle destroy an adjacent-zero pair and create a disjoint pair next to a different old zero. Restricting the shift to ±1 needs more than the fact that just one zero was lost. The repaired proof verifies all shifts directly and leaves the theorem unchanged. Domination forbids 000, and separation of neighbors forbids two zeros at offset three; these also separate distance-two neighborhoods, and all other neighborhoods are disjoint. The seven-state determinant is checked by its four simple directed cycles and two disjoint pairs. At t=u²,z=w/u its factors are (1−w²)(1−uA−u²B), A=w(1+w⁴), B=w⁴/(1−w²); the coefficients at excesses zero, one and three yield the stated minima, counts and sole n=15 increment. The H and L rotations and exceptional periodic words attain these counts. For n=2m+3, changing vertex coordinates to v=2j turns H zero sets into intervals of length m and the normalized L zero set into {0}∪[2,m−1]∪{m+1}. Intervals overlap in m−1 points just at shifts ±1 in j, yielding ±2 in v. Exactly two intervals overlap the normalized L in m−1 points, [0,m−1] and [2,m+1]; translating back gives L_1 and L_5 from H_0. For an L–L translation by s, symmetry reduces to 1≤s≤m+1 without wrap, giving overlap m−3 at s=1, m−2 at s=2, and at most m+1−s for s≥3 because m is a hole. Thus no L–L exchange occurs. Alternating even codes differ in every coordinate. Each exceptional code keeps at least two of its three disjoint adjacent-zero pairs after one exchange, and two exceptional rotations share at most one zero residue modulo five, so these five are isolated. The odd cycle of H vertices and two neighbors per L give the claimed component and edge counts.

## originality

PASS

Prior work covers minimum sizes and includes the even alternating construction. The closest inspected indexed reconfiguration result gives exact token-jumping structure on C_11, outside the odd range, and a short table with two even instances. The credited result is the uniform classification of the minimum-code exchange graph on the stated parity ranges and the exact exceptional isolated component at 15, not the minimum cardinalities or the general reconfiguration setup. No compared primary passage or indexed record yields that classification. The unavailable close odd-order papers are explicit residual risks, not negative evidence.

## value

PASS

The quantity of interest is the natural reconfiguration graph on optimal solutions, not merely the well-studied minimum size. Exact adjacency gives the connected components and a uniform cycle-and-chord description; the five isolated C_15 codes show a genuine exception to odd connectivity that size bounds alone do not explain. The result is a complete graph classification across infinite ranges, with explicit templates and all possible exchanges.

The dated certificate retains the supplied scientific assessment, sources and limitations.
