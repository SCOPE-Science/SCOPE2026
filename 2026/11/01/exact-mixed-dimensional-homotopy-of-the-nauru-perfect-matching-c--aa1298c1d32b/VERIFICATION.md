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

PASS. For the explicitly labeled Nauru GP(12,5), the two independent least/greatest-uncovered-vertex matching enumerators agree on 120 perfect matchings of 24 vertices and 36 edges. Their full downward closure has 346,822 faces including the empty simplex, with f-vector (1,36,558,4692,21861,55872,85680,85176,57258,26208,7920,1440,120) in dimensions -1..11. Independently reconstructed the vertex-by-vertex edge-toggle Morse matching with 173,357 face pairs and precisely 22 critical 3-simplices, 67 critical 4-simplices, 19 critical 5-simplices; a complete directed Hasse topological sort visits all 346,822 faces and all 2,282,760 incidences, so acyclicity is exhaustive. Independently rebuilt signed 22x67 and 67x19 integral Morse boundaries from oriented face deletions and gradient elimination; ranks 16 and 19, zero composite and explicit maximal-rank unit minors of determinants +1 and -1 imply torsion-free reduced H3=Z^6,H4=Z^32. The Morse CW model has one base point and no positive cells below dimension three. Its 4-skeleton splits as 6 copies S3 and 51 copies S4 after primitive degree-4 attaching maps; π4 of that wedge is (Z/2)^6⊕Z^51 (no dimension-four Whitehead cross products). The 19 primitive 5-cell free coordinates can be canceled after absorbing their Z/2 components through homotopy self-equivalences that modify the S4 inclusions by maps into the S3 wedge. Therefore the actual homotopy type is ∨6 S3 ∨32 S4, not inferred from Betti numbers alone. Supplied full certificate.json entries/minor indices were read and independently reconstructed; CHECK_LOG alone would not suffice.

## originality

PASS

PASS. Best-of-knowledge originality after comparing exact mathematical objects and implications, not merely names: published Nauru independence complex is not a perfect-matching complex; known honeycomb/ladder perfect-matching theorems do not include the cyclic Nauru graph.

## value

PASS

PASS. GP(12,5) is a natural named symmetric cubic graph, and perfect-matching complexes are a motivated topological invariant. The complete integral mixed-dimensional sphere-wedge homotopy classification is genuinely informative beyond a face-count or mod-two census and could serve as an exact reference case for future generalized Petersen and perfect-matching-complex work. The finite nature of the object does not diminish its exact structural mathematical content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
