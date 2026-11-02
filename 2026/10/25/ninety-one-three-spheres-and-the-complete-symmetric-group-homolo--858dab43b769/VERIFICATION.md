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

The object is the open-neighborhood complex of the 15 pair-vertices of L(K6). A fresh independent Python implementation reconstructed all 2,881 faces, exact f-vector (1,15,105,420,945,840,420,120,15) including the empty face, 1,395 simplex-toggle pairs with one augmented empty pairing, and 91 remaining four-vertex faces. It independently checked acyclicity by topologically sorting all 2,881 nodes and all 12,945 signed Hasse cover arrows; after restoring one critical 0-cell the Morse CW model is point plus 91 3-cells, hence an integral wedge of 91 S^3 (not deduced from mod-2 Betti). Signed reduced Lefschetz traces independently computed across all 720 underlying S6 permutations reproduce all 11 conjugacy-class values (91,-13,7,7,1,-1,1,-3,-3,1,1) and the trivial multiplicity 0; the actual source verifier includes exact Murnaghan–Nakayama inner products giving the claimed Specht decomposition. Orbit quotient rational reduced homology vanishes by finite-group transfer, not contractibility.

## originality

PASS

A published October 11 2026 full primary Resultary record already computes the same mod-2 β3(N(T6))=91, which is expressly not original here; it explicitly does not compute integral homotopy, attaching maps or S6 action. The entire new finite Morse certificate proves a torsion-free integral wedge, while the full rational S6 character is an additional invariant not implied by the known mod-2 dimension. Prior T5 four-cut representation is a different graph, definition and group. Kozlov/Matsushita–Wakatsuki are general equivalences/duality rather than calculations for T6.

## value

PASS

The fifteen-vertex T6 neighborhood complex is a canonical highly symmetric graph complex whose mod-2 Betti rank was already known. Exact integral wedge homotopy (not merely rank) and the entire 11-class S6 representation distinguish torsion/attaching information and yield the non-obvious absence of invariant 3-cycles, hence rational homology vanishing of its quotient. Such full equivariant topological classification is a motivated exact invariant, despite being one canonical finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
