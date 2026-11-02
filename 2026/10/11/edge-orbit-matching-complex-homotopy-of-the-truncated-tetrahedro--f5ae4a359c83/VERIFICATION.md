---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The final claim applies to the explicitly labeled graph on twelve ordered distinct pairs (a,b) from {0,1,2,3}, with triangles at fixed first coordinate and six reversal edges. Independently reconstructed all 18 graph edges, full 1010 face masks including empty and f=(18,117,332,390,144,8). For each of the five exact complexes, rebuilt all simplicial faces from pairwise-disjoint graph-edge masks, greedily paired by first available bit (with empty pair converted to a critical vertex), and oriented EVERY nonempty Hasse incidence upward if paired and downward otherwise. Full topological sorts visited all 1009,819,189,793,215 vertices; critical cells respectively (0:1,3:22), (0:1,3:14), (0:1,2:8), (0:1,3:20), (0:1,2:2). No other critical dimensions survive. Forman discrete Morse theory then gives CW models comprising one point plus only 2- or 3-dimensional cells, so all attaching maps are trivial and the spaces are integral wedges, not merely field-homology equivalents. Checked S4 permutes graph vertices and acts transitively on exactly two edge classes of sizes 12 and 6. For every edge the simplicial link inclusion from a wedge of 2-spheres to the deletion wedge of 3-spheres is null-homotopic by pi2=0. The deletion-star cone cofiber splits into (14+8) or (20+2) S3. The independent calculation supports the entire exact finite claim; no extension to all planar graphs or an infinite family is claimed.

## originality

PASS

Best-of-knowledge PASS for exact integral homotopy types of the truncated-tetrahedral ordinary matching complex, its two edge-orbit deletions and links, and their nullhomotopic cofibration splittings; not for the general deletion-link identity or general Morse methods. The published outerplanar theorem excludes the candidate with its K4 minor and supplies no exact multiplicities; the polygonal-line, manifold and claw-free treatments also do not imply the five values. An indexed exact truncated-tetrahedral Rips result is for a different simplicial complex. The separately published cuboctahedral and rhombic-dodecahedral matching-complex results are different graphs. Equivalent graph aliases and full matching-complex formulations were tested. No independent prior theorem/table giving all five integral homotopy groups and the orbit distinction was found; this is limited priority evidence, not proof of absolute novelty.

## value

PASS

The truncated tetrahedron is a canonical Archimedean 3-connected cubic planar but nonouterplanar graph, and the ordinary matching complex is its natural topology-valued invariant. Establishing an integral wedge of 22 S3 and both complete edge-orbit deletion/link homotopy profiles (14,8) vs (20,2) is a motivated exact classification, not a textbook sign/normalization check. This provides a concrete nonouterplanar case of the published planar sphere-wedge conjecture, and the two distinct local decompositions give nontrivial edge-sensitive information beyond the global Betti count. Its value is a finite structural benchmark; no paper-sized or general-family theorem is asserted. The result could be independently useful when testing or building planar graph matching-complex decompositions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
