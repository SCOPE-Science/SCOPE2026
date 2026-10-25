---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Independently regenerated M(F) faces (13,42,30) and M(K7) faces (21,105,105), exact integer boundary matrices, and Smith diagonals containing one nonunit factor 3 each. Ranks: ∂2_F over Q30/mod3 29; ∂2_K7 over Q85/mod3 84. Independently solved the F mod3 second-boundary nullspace, lifted a cycle z=∂2 c/3, mapped it naturally to K7 oriented 1-chains, and verified its mod3 class nonzero by augmented rank (so inclusion of order-3 subgroups is nonzero and hence an isomorphism). Independently constructed a detecting mod3 cocycle on K7 and checked its pairing on all 5040 vertex permutations equals permutation sign. Enumerated all 256 labelled supergraphs of F, canonicalized under S7 and obtained exactly 40 classes. Canonicalizing the supplied actual 40 Graph Atlas mask values gives equality of the entire 40-element sets (not only a matching count). Prior exhaustive Smith-form census proves these are all torsion-bearing graph classes; inclusion factorization plus torsion Z3 completes natural persistence and Aut(G) formula.

## originality

PASS

Bouc and Shareshian–Wachs already give Z3 torsion of M(K7); the 2026 published complete graph-atlas census already gives all forty types and unique F threshold. The increment survives solely as a naturality assertion: these classes all survive inclusion into the complete-graph torsion line, with its natural full S7 sign character transported to every graph automorphism. The prior graph-atlas RESULT was read and contains no inclusion map on torsion. This makes the overlap very substantial and the surviving mathematical contribution precisely bounded.

## value

PASS

This upgrades a known 40-row torsion table to a canonical persistent class under every edge addition within seven vertices, and determines its automorphism sign action. A naturality theorem about explicit inclusion maps is mathematically informative even for a finite graph range; it can be used in matching-complex filtrations and cannot be read directly from group isomorphism tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
