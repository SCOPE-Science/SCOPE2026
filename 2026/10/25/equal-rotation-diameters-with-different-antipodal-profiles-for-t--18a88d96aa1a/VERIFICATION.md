---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The recursive root/component decomposition enumerates each rooted elimination tree exactly once. The seven proper descendant tubes characterize maximal tubings, while deleting one tube leaves a ridge with two completions; their pair constitutes exactly one allowed single flip. A separate parent–child rotation interpretation agrees with these moves in the source. For each graph the independent C++ audit built induced-component elimination trees, tubes, ridge-pair adjacency, tested all 8!=40,320 candidate label permutations to get full automorphism groups, enumerated every orbit, and ran breadth-first search from each orbit representative across all states. It reconstructed Q3 16,752 states, 58,632 edges, 48 base automorphisms, 355 state-orbits (343×48+12×24), and M8 17,568 states, 61,488 edges, 16 automorphisms, 1,098 state-orbits; eccentricity distributions Q3 {17:1368,18:8280,19:6336,20:768}, M8 {17:976,18:5536,19:10800,20:256}, and all twenty pair distances matched the frozen theorem. Orbit multiplicity and division of ordered pair counts by two ensure entire distance distributions, not samples; connected BFS reaches all states. This is a genuinely exhaustive finite proof of the two specified graphs, not numerical extrapolation to other graphs.

## originality

PASS

Identifying the rotation graph with the one-skeleton of a graph associahedron permits direct comparison with general diameter bounds, hardness and FPT distance-computation results. None of the inspected graph-associahedron primary theorems supplies both exact Q3/M8 eccentricity histograms or all-pair distance distributions. A relevant published finite record determines the metric of K4,4 (29,616 states, diameter 22) rather than Q3 or M8; equal vertex count does not imply a metric reduction. The exact two-graph comparison appears original to best of knowledge, while an unindexed small graph-associahedron metric census remains a priority risk.

## value

PASS

Q3 and M8 are canonical contrasting connected cubic graphs of order eight. Their rotation graphs attain the same radius/diameter yet sharply different antipodal multiplicities and complete distance distributions. This isolates a natural limitation of diameter alone as a descriptor of graph-associahedron geometry, provides reproducible complete finite metric data, and supplies test cases for more general rotation-distance algorithms and heuristics. A finite census can be valuable on these canonical inputs without a general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
