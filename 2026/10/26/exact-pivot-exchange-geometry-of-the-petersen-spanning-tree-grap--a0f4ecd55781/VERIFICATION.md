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

# Reproducing the finite certificate

Execute `python3 verify_petersen_pivots.py` with Python 3.9 or later, from the directory containing the supplied file. The script requires only the standard library and reads no data files. It completes with `VERIFY_OK` after every stated assertion succeeds.

The graph is specified as disjointness among the ten two-subsets of a five-symbol set. All 5,005 nine-edge subsets of its 15 edges are classified by disjoint-set connectivity and cycle tests. The result is checked against the exact 9-by-9 Laplacian determinant (2,000). Two independently coded definitions produce identical pivot neighborhoods for all trees; every neighborhood has 12 members, with symmetric adjacency.

Breadth-first search is executed from each of the 2,000 trees. In addition, all 120 natural automorphisms of the Petersen graph are explicitly constructed, the 2,000 trees are partitioned into 21 orbits, and a second, independently generated adjacency graph is used to reproduce all distance and detour tables using only representatives with orbit weights. The 150 maximum-excess pairs are partitioned into group orbits of sizes 30 and 120 and have 60 endpoints in one tree orbit.

The exact computed unordered-distance counts for distances \(1\) through \(8\) are \((12000,72000,266940,588060,678350,327080,52500,2070)\). Eccentricities are \(7\) for 1,040 trees and \(8\) for 960. The excess counts for values \(0\) through \(4\) are \((565010,1045740,363290,24810,150)\). The first histogram sums to \(1,999,000\) unordered pairs. All counts are exact integers; there are no random tests or floating-point thresholds.

This verifies the finite computational claim only. It neither establishes a new general theorem about all graphs nor constitutes an independently performed audit or a proof of research novelty.
