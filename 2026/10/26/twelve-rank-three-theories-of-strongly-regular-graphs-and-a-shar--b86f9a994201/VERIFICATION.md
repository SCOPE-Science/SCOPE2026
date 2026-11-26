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

For every vertex in the specified nontrivial strongly regular family, equality, adjacency and distinct nonadjacency are all realizable for the second move. For distinct selected x,y, the four third-vertex multiplicities are (lambda,k−1−lambda,k−1−lambda,n−2k+lambda) on an edge and (mu,k−mu,k−mu,n−2−2k+mu) on a nonedge. Only existence matters at the third move; repeated selections are available on both boards. Each support bit also has a rank-three existential test. The edge double count (n−k−1)mu=k(k−1−lambda) partitions cases: mu=0 forces equal clique components by the absence of induced two-edge paths; mu=k makes nonadjacent vertices have identical neighborhoods, yielding equal independent parts of a complete multipartite graph. Each case has four signatures from whether the number and size of blocks attain the relevant thresholds. In the remaining case the complement is not a disjoint union of cliques; its nonedge common-neighbor count is positive, and the double count gives k−1−lambda>0. The four surviving free bit combinations are the triangle-existence bits in the graph and its complement. A separate adjacency reconstruction confirmed all twelve rows, including the four primitive witnesses. For the Petersen support a smaller graph would be primitive and triangle-free. With n<10 Mantel gives k≤4. The degree-two connected cases are C4/C5 (diameter at most two); neither has the support. Degree three forces n=4+6/mu and leaves no smaller even-degree-sum primitive candidate. Degree four forces n=5+12/mu and the only smaller primitive candidate is (9,4,0,3). On the eight-dimensional zero-sum subspace its adjacency matrix satisfies z²+3z−1; the rational matrix has equal multiplicities of the two conjugate roots, so the total trace would be 4+4(−3)=−8, impossible. Complementation also preserves the minimum under the corresponding signature permutation. Thus ten is the sharp uniform ceiling within the family, not a minimum claimed separately for each listed row.

## originality

PASS

The exact ordinary rank-three quotient and its sharp uniform representative bound for the entire nontrivial strongly regular family are distinct on the inspected evidence. General EF theorems, standard strongly regular parameter constraints and classifications of proper graph subfamilies cover ingredients or individual types, but not the full quotient and the minimum obstruction within this family.

## value

PASS

Strongly regular graphs are a natural algebraic graph family and ordinary rank-three equivalence is a concrete logical invariant. The census determines exactly which parameter information survives in that language, unifies primitive and both imprimitive cases, and gives optimal finite witnesses without classifying all SRG parameter sets. The ten-vertex obstruction and realizability of all twelve types are useful exact information beyond the generic game theorem or any of the narrower family tables; the claims of novelty and value do not rest on the verification script.

The dated certificate retains the supplied scientific assessment, sources and limitations.
