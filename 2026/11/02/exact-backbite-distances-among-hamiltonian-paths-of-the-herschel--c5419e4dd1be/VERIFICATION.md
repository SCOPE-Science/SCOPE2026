---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The Herschel graph is explicitly reconstructed from three core vertices, two poles and six degree-three pair/pole vertices (18 edges); bipartition 5+6 forces path endpoints into degree-three part, with exactly two unused edges at each endpoint. The code enumerates all spanning simple paths via canonical reversal, generates precisely the stated Pósa endpoint rotations and performs BFS from all 222 paths. An independently implemented DFS plus backbite BFS regenerated 222 paths, 444 undirected edges, 4-regularity, connectivity, exact histogram (444,1152,2436,4326,6348,6189,3078,546,12), eccentricity multiplicities 198 at 8 and 24 at 9, and 12 disjoint diameter-9 pairs. Exhaustion is finite and exact rather than a timeout or sample.

## originality

PASS

The original Pósa backbite move and connectivity criteria are established; Herschel graph combinatorics are known. Kazazi 2026 sufficient condition requires a spanning squared path, which would force a triangle and is impossible in this bipartite graph. The other retrieved Herschel-specific Resultary item concerns its independence complex, not its spanning-path reconfiguration graph. The exact 222-state all-pairs metric is not implied by the checked general claims.

## value

PASS

A complete finite reconfiguration metric for the smallest non-Hamiltonian polyhedral graph answers a natural boundary question for endpoint rotations, including a sharp nine-move requirement and an exceptional antipodal matching. Finite here is essential: the full natural state graph is classified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
