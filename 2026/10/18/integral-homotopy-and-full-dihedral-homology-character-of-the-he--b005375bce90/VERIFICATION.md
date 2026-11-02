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

For the explicit 11-vertex 18-edge graph, independently enumerated all matching faces by edge-combination generation: 752 including empty, f=(18,111,280,270,72). Independently reproduced the specified 18 edge-toggle matching with 369 incident pairs and exactly one critical vertex plus twelve critical 3-simplices. Constructed all 2,502 nonempty Hasse cover incidences and verified directed acyclicity by visiting all 751 nodes, so Forman discrete Morse gives an integral CW complex with one 0-cell and 12 3-cells and hence wedge of twelve 3-spheres. Independently enumerated the full 12 graph automorphisms via GraphMatcher (not assumed from code), obtained six signed reduced-Lefschetz class traces (12,0,−3;−2,2,1), decomposed by exact S3×C2 character inner products into multiplicities (1,0),(0,1),(2,3), and verified fixed-line dimension 1. Independent simplicial boundary ranks over primes 2,3,5,101 were 17,94,186,72, yielding ordinary b3=12. The full integral homotopy conclusion rests on the exhaustively checked acyclic discrete-Morse matching, not finite-field ranks alone. No integral isotypic group-lattice splitting asserted.

## originality

PASS

Best-of-knowledge novel integral homotopy type and full rational S3×C2 homology character for M(H)=Ind(L(H)). Actual highly relevant prior theorem statements were compared by mathematical implication, including noncoverage of outerplanar/manifold/complete graph hypotheses and the distinct published Ind(H). Relevant full primary texts were materially read where accessible; one broad monograph chapter remains an explicitly named access risk. No negative search was treated as a proof of priority.

## value

PASS

The Herschel graph is the canonical smallest-edge 11-vertex non-Hamiltonian polyhedral graph, and the ordinary matching complex Ind(L(H)) is a natural graph-topological invariant. Its exact integral wedge type distinguishes homotopy, rather than only rational Betti numbers; the full twelve-element symmetry character and nonzero invariant line distinguish equivariant topology beyond a matching polynomial or sphere multiplicity. A precise finite natural object and complete nontrivial structural invariant can be worth citing without requiring a universal graph-family theorem. The calculation is not a renaming, arbitrary slice, or known-table recomputation in the inspected literature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
