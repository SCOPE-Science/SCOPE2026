---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Constructed from scratch the 24 signed coordinate permutations of (0,1,2), edges at Euclidean squared distance 2: cubic graph with 36 edges. Enumerated the entire ordinary independence complex: 37075 nonempty faces, 219216 oriented Hasse incidences. Independently implemented greedy vertex-toggle discrete-Morse matching: 18535 nonempty pairs, one critical zero-cell and four critical five-cells with exact bitmasks 1575960,2149378,2441252,8603650. Full directed Hasse graph topological sort visited all 37075 cells, establishing genuine acyclicity and an integral wedge of four S^5. Independently enumerated all 56 induced six-edge matchings (12-vertex crosspolytope boundaries). Rebuilt all 64-term oriented fundamental cycles, 5083 matched 5/6 cancellation pairs, a complete acyclic elimination dependency graph, and exact Z^4 critical-face coordinates: all 56 have gcd one and nonzero class. Enumerated 48 signed coordinate graph automorphisms and support orbits of sizes 8,12,12,24. The unique size-8 orbit has determinant-one 4x4 minor on support indices (0,1,6,28); other three orbit matrices have rank exactly three and gcd of their 3x3 minors one, hence primitive rank-three sublattices. Independently recomputed all 48 reduced Lefschetz character traces over every face, obtaining multiplicities {-4:1,-2:6,-1:8,0:18,1:8,2:6,4:1}, and matched every trace with the central-inversion sign twist of sign(S4)+standard(S4). Since inversion is order two and its rank-4 trace is -4, it acts as -I integrally. The standard sharp flag-support lemma gives lower bound 2d+2=12 for any nonzero H5 on a minimal vertex-induced support, and equality forces a 6-crosspolytope boundary; combined with exhaustive 56-match census, this proves all shortest carriers. No finite field surrogate was used for integral primitivity.

## originality

PASS

A previously published result on the EXACT SAME 24-vertex truncated-octahedral/permutahedral graph already proves the nonequivariant wedge of four 5-spheres and vertex deletion/link splitting, explicitly credited and read in full. Neither it nor generic Barmak results determines the minimal induced 12-vertex carrier census, integral orbit generation and primitive proper sublattices, or the complete octahedral homology character. The retained new contribution is these exact integral generators and symmetry refinements.

## value

PASS

A canonical finite, highly symmetric graph has known H5 rank 4, but abstract Betti numbers say nothing about the smallest induced subgraphs supporting cycles or how their orbit spans the integer lattice. The exact minimum-support 56-carrier census, a unique 8-class saturating orbit, and three primitive nonspanning orbits provide a structurally motivated integral geometry-of-generators classification. The explicit O_h character is a nontrivial invariant beyond the previously published vertex-local homotopy type. This self-contained finite fact is worthwhile without a higher-dimensional family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
