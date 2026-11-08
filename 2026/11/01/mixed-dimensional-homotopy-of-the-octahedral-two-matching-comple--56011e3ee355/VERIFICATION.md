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

The graph has exactly twelve edges across three opposite vertex-pairs; a face is any selected edge set with degree <=2 at every graph vertex, equivalently avoiding each incident edge triple. An independent exact enumeration found 772 faces including the empty face. A sequential twelve-edge toggle matching has 378 pairs, sixteen critical faces (six in dimension three, ten in four) and an acyclic orientation over all 2940 Hasse incidences. Independently implemented generic integral unit-pivot Schur cancellations of all pairs, obtaining a 6x10 Morse d4 with rank three and Smith factors (1,1,1), hence H3=Z^3 and H4=Z^7 without torsion. Since the resulting CW complex has only 0-,3-,4-cells and pi3 of its 3-skeleton is Z^6, primitive attaching degrees can be diagonalized/cancelled to give the claimed wedge. No homotopy conclusion is inferred from mod-two Betti numbers alone.

## originality

PASS

The searched two-matching literature treats leaves, wheels, caterpillars and complete/complete bipartite families. Octahedral K_{2,2,2} is complete tripartite, not the standard complete or complete bipartite case. The ordinary matching complex and discrete Morse-vector-field complex on the same octahedral graph are different constructions and do not yield this 2-matching wedge. No inspected stronger theorem implies the exact mixed wedge; best-of-knowledge PASS.

## value

PASS

The regular octahedral graph is a basic Platonic graph and the first small canonical complete tripartite example outside commonly computed K_n/K_{p,q} two-matching families. Its nonpure complex surprisingly has a torsion-free mixed-dimensional integral wedge; a complete homotopy type, rather than just Betti numbers, supplies a meaningful benchmark and boundary case for higher matching-complex classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
