---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Equal barycentric coordinates within reflection orbits identify the geometric fixed locus with the orbit complex, including fixed points inside permuted simplices. A bipartite face uses at most six vertices and its independence number is its size minus its matching number. For odd n, the center singleton in the middle row is a cone point. With zero or one off-axis orbit, sets needing an edge after adjoining it acquire a central vertical edge, and the case of both outer central singletons and one off-axis orbit uses a second edge to that orbit. With two off-axis orbits and zero or one outer central singleton, admissibility requires adjacent off-axis orbits; there is then a matching edge in each half, and a central matching edge if needed. Two off-axis orbits and both outer central singletons cannot be perfectly matched: after matching each central endpoint into its own row the unused vertices are in the nonadjacent outer rows. Three off-axis orbits with no central vertex give two odd halves, so cannot be a face either. For even n=2h, a selected six-vertex set needs a perfect matching with an odd number of axis crossings. One crossing leaves an edge in each folded half; three crossings mean the whole central column of orbit vertices was selected, which also satisfies the one-crossing face test. The resulting complex is the join of three discrete central vertices with the connected off-axis graph, plus three edges and seven triangles. Collapsing three paired edge–triangle additions shows the intermediate space is simply connected; the remaining four disks attach along null loops, adding four S² summands. The join gives two suspensions of a connected graph of cycle rank 2h−4, so the total is 4h−4=2n−4 spheres, including h=2 where that graph is a tree. Barycentric subdivision permits the Lefschetz trace to count fixed simplices, so the reduced Lefschetz number is the fixed Euler characteristic minus one. The all-width proof is integral. Fresh direct orbit-face enumeration and mod-two elimination for 3≤n≤12 found all odd cases to be cones and even beta_2=4,8,12,16,20 with no other reduced Betti numbers, bounded corroboration only. Replay and output: /workspace/branches/109f032f-0243-4981-a430-a9b0c286d4e2/independent_check.py and independent_check_output.txt in the same directory.

## originality

PASS

The supported distinct result is the all-width geometric column-reflection fixed-space classification for the three-row four-robust complex. Same-day catalogue work on finite ambient complexes overlaps in object and parameters, not this invariant; nearby fixed-locus work uses the matching complex. At width four an ambient reflection-character entry determines the same reduced Lefschetz number but does not determine the fixed homotopy type. No same-day priority inference is needed.

## value

PASS

Column reversal is a natural involution, and its geometric fixed space is an invariant not recovered from ambient homology. An exact integral homotopy classification for every width, with a parity split and a simple linear sphere count, is useful for equivariant comparisons even without an ambient four-robust classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
