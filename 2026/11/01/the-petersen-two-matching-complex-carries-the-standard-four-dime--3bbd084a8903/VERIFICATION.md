---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS. The finite Petersen M_2(P) has 15 edge-vertices and faces exactly the edge sets with all ten graph degrees <=2. Independent reconstruction checked all 32768 subsets and obtained 10870 faces and cardinality vector (1,15,105,445,1245,2358,2985,2400,1095,215,6). A fresh sequential-toggle matching of the augmented face poset yields 5433 pairs and four cardinality-8 critical faces; removing the empty/singleton pair gives 5432 ordinary matched pairs, one critical vertex and four critical 7-simplices. Independently directed all 63780 covers and topologically sorted 10869 nonempty faces, proving acyclicity, hence X is a wedge of four 7-spheres. A separate all-120-permutation signed fixed-face computation verifies the seven conjugacy-class traces (4,2,0,1,-1,0,-1); simplex signs follow (-1)^(|F|-number_of_orbits). Lefschetz concentration in degree 7 yields trace fixed_points(sigma)-1 and rational Maschke semisimplicity identifies the standard Specht S^(4,1) module. This is NOT an assertion of equivariant wedge homotopy or integral lattice splitting.

## originality

PASS

PASS, best-of-knowledge. The previously published 4-sphere homotopy result for the identical Petersen M_2(P) is explicitly prior art, but its statement and proof supply only total homology rank, not the complete S5 trace or representation decomposition. The current claim is a nontrivial refinement obtained from exact orientation-sensitive fixed-face enumeration, not a renaming of a rank. Published studies of higher matching complexes and symmetry representations use different graph classes or ordinary matchings; nearby Petersen three-cut and graph Morse results have different simplicial face rules. An equivalent unindexed character computation remains possible.

## value

PASS

PASS. The full automorphism group S5 of the natural Petersen graph acts nontrivially on top homology, and identifying the actual irreducible four-dimensional character distinguishes standard symmetry from the multitude of 4-dimensional representations. The computation determines invariants under S5 and a point stabilizer S4, facts the known nonequivariant wedge type does not provide. This motivated equivariant invariant of a canonical graph complex is useful without a general cubic-graph classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
