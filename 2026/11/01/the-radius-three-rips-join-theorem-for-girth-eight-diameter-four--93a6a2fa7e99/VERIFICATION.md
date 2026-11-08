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

PASS: For finite connected simple bipartite diameter-exactly-four graphs without 4- or 6-cycles, opposite-side distances are 1 or 3; same-side distances are 2 or 4. At threshold 3 the flag complex is literally L_A*L_B. A same-side clique of size >=3 with pairwise distinct centers would give a 6-cycle; uniqueness of centers is from no 4-cycles. The block-simplex expansion with separate apex for each neighbor center collapses both to L_A and to original G (descending free-face order), including leaves/forest case. Consequently L_A and L_B have homotopy type of G and K_3 ≃ Σ(G∧G) ≃ wedge^{b²}S³, b=e-n+1. Adamaszek 2011 Prop 2.2 at r=2 requires girth>=7, so K_2 collapses to K_1 and actual inclusion preserves integral H1; K_4 is full simplex. The barcodes n-1 [0,1) in H0, b [1,3) in H1, b² [3,4) in H3 follow with integral free groups; no torsion or extrapolation. Independent exact first-principles GQ(2,2) duad-syntheme reconstruction gives both factors (15 vertices,45 edges,15 triangles), each 16 loops, hence 256 three-spheres. For order (s,t), incidence counts n=(st+1)(s+t+2), e=(st+1)(s+1)(t+1), yielding b=s²t²; q=3 gives 6561. No equivariant statement is claimed.

## originality

PASS

PASS as a bounded best-of-knowledge comparison: the earlier complete 2026 Tutte-Coxeter/GQ(2,2) proof already covers exactly the 256-sphere instance, but does NOT assert the all-graph or all-order (s,t) classification. Adamaszek 2011 Prop 2.2 only reaches radius 2 at girth 8 (radius 3 needs girth at least 10). Generalized-polygon approximation and first-homology persistence statements do not subsume the new Rips threshold-3 join argument. No stronger relevant published result surfaced in searched indexed records. An alternative unindexed incidence-complex homotopy formula remains possible.

## value

PASS

PASS: The claim identifies a nontrivial uniform structural reason for a sharp Rips dimension jump and gives a complete integral persistence classification on a natural class (girth-8, diameter-4 bipartite graphs), including all finite generalized quadrangles rather than a single computed sample. Fourth-power homology counts are useful exact incidence-geometry invariants and were not mechanically implied by the known order-(2,2) example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
