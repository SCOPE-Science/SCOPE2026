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

In the specified line graph a forcing step is monotone: enlarging a blue set either already colors the forced target or leaves it the only white neighbor of the same source. Iterating all eligible moves gives the maximal closure and dominates every other schedule round by round. I independently enumerated starting sets of sizes 0 through 7 using white Petersen-edge states and counts of white edges at the endpoints of each blue edge (replay: python3 /workspace/branches/replay_5.py). For this simple graph those counts sum to the number of white neighbors in the line graph. The first nonempty success class is size 7 with 2280 sets, and the round histogram is {3:120,4:1440,5:720}. All line-graph triangles come from stars of the triangle-free cubic Petersen graph; their intersections recover the Petersen graph. Independent four-sets of Petersen vertices are four pairwise intersecting two-subsets; without a common symbol there are at most three, so the five four-sets are exactly the symbol stars. Permuting them determines every original vertex, and every such permutation is realized. Thus the full acting group is S5. The independent calculation reproduced all 21 canonical-mask triples from ORBIT_TABLE.csv, with 17 orbits of length 120 and 4 of length 60. I built exchange adjacencies instead from buckets of shared six-element subsets and used exact BFS from each of the 21 representatives. Each BFS reached all vertices; summing distance counts weighted by source-orbit size and dividing by two counts each unordered pair once. This returned 28650,234120,765570,1004640,483480,78540,3060 at distances 1 through 7 respectively. This is an exact exhaustive result on one graph, not extrapolation. The frozen verifier was inspected, not executed.

## originality

PASS

The supported distinct contribution of the October 26 result is the complete optimum census with its propagation and exchange data, not the scalar size 7 or the general exchange definition. A strong, distinct November 2 catalogue entry duplicates the exchange polynomial and orbit sizes but is dated later by the publication metadata and does not state the parallel-time distribution. Its overlapping data are explicitly credited below; this pass is not a finding that the two entries are disjoint or that either one was first discovered independently. No inspected earlier result gives the combined exact classification.

## value

PASS

The canonical Petersen graph yields a natural edge-coloring instance of zero forcing. The combined census supplies a benchmark with the entire optimizer space, seed orbit types, three distinct parallel-time classes, and exact exchange distances, answering how many minimum seeds yield a given round count and how far apart optimal placements can lie under legal exchanges. Neither the known scalar minimum nor the general reconfiguration framework answers those questions. This is a motivated finite classification, not a claim about a whole graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
