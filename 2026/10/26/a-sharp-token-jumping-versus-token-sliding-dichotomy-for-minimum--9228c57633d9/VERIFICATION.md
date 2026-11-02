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

Built GP(8,3) directly from outer 8-cycle, spokes and 3-step inner edges, then independently enumerated every C(16,k) subset for 0<=k<=6 and applied legal blue-to-unique-white-neighbor closure; counts [0,0,0,0,0,0,1704]. Constructed all jump-neighbor six-subsets differing by one element and checked original edge adjacency for slides: exactly 16560 undirected jumps and zero legal slides. Breadth-first search from each of all 1704 configurations reaches the full graph with eccentricity exactly 6. In the frozen package, a second separate LCF [5,-5]^8 encoding, explicit isomorphism and sequential force implementation agree. BFS and bounded brute force are complete finite proofs for this one 16-vertex graph, not asymptotic evidence.

## originality

PASS

Best-of-knowledge originality of the exact final statement, rather than its standard background ingredients: The full geometry of optimum-solution reconfiguration is a motivated invariant: jump connectivity with uniformly small diameter contrasts sharply with complete slide immobility. The specific graph is a classical symmetric cubic test case; the result is more informative than recomputing the previously known scalar zero-forcing number. The searched and materially inspected primary results do not directly cover the full exact statement; plausible uninspected generalizations remain residual risks.

## value

PASS

The full geometry of optimum-solution reconfiguration is a motivated invariant: jump connectivity with uniformly small diameter contrasts sharply with complete slide immobility. The specific graph is a classical symmetric cubic test case; the result is more informative than recomputing the previously known scalar zero-forcing number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
