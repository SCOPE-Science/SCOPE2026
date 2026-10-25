---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

The fixed edge order is [(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7)]. Each cube vertex has 3 incident edges, so exactly the 8 full-stars are forbidden 3-edge subsets, masks (7,25,98,168,772,1296,2624,3200). INDEPENDENT Python reconstruction enumerated all 4095 nonempty edge-subsets and confirmed 1698 allowable faces; f=(12,66,212,423,516,352,108,9). Reimplemented greedy sequential pivots i=11,...,0 and obtained pair counts (665,94,51,18,8,0,7,0,2,1,1,0), 847 disjoint cover pairs, critical masks 888,1235,1421 (three five-dimensional simplices) and 2048 (one 0-cell). Built all 7980 directed Hasse cover arrows and independently topologically sorted all 1698 nodes, proving this matching acyclic rather than relying on certificate output. Forman CW theorem then has one 0-cell and three 5-cells, so attaching maps to the point are constant and M2(Q3) ≃ wedge of three S5 integrally; no torsion. The line graph equivalence uses Q3 triangle-free, so 3 pairwise incident edges necessarily share a vertex. Only this finite cube/degree-cap case is proved.

## originality

PASS

The final finite homotopy classification is distinct from ordinary matching and cut complexes of the cube and its line graph. Resultary covered ordinary cube matching complex wedge4 S2, cuboctahedral ordinary matching complex wedge57 S3 and three-cut complex mixed-dimensional, not M2(Q3). The primary 2-matching methods and clique-free shellability theorems inspected do not state or imply this nonpure Q3 homotopy classification. Best-of-knowledge original; not proof of exhaustive literature priority.

## value

PASS

The cube and its degree-constrained matching complex are canonical graph/topological objects; the 49 facets occur in three dimensions (4,36,9 across dims 5,6,7), making this nonpure complex a legitimate exact homotopy classification rather than a routine purity/shellability corollary. Explicit acyclic collapse to 3 spheres supplies a reusable integral finite benchmark, not merely its Betti numbers. This natural unknown exact invariant is self-contained and mathematically worth recording.

The dated certificate retains the supplied scientific assessment, sources and limitations.
