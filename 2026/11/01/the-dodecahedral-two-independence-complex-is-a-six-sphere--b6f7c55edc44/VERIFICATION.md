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

The dodecahedral graph is explicitly GP(10,2), with 20 vertices and 30 edges; Ind₂ allows each induced selected vertex at most one selected neighbor, equivalently forbidding 60 centered graph wedges. Independent code rebuilt all 63,143 faces (including empty), the complete face vector and deterministic 20-pivot Morse matching, obtaining exactly 31,570 matched cover pairs and critical masks {2048 (vertex),156434 (six-simplex)}. Independently built every nonempty-face Hasse incidence, reversed matched arrows, and topologically sorted ALL 63,142 faces over 410,500 arrows; acyclicity is a finite exhaustive proof, not partial enumeration. Forman gives a CW complex with only one 0-cell and one 6-cell, hence integral homotopy S6 without assuming field homology forces homotopy.

## originality

PASS

The fixed two-independence (induced max degree 1) complex on the 20-vertex dodecahedron is distinct from both ordinary independence (5,827 nonempty faces and wedge four S5) and the dodecahedral edge-matching complex. Known higher-independence theorems classify complete multipartite, whiskered, paths, cycles and perfect rooted trees, but not this nonchordal dodecahedral graph. The corresponding Petersen graph Ind₂=S3 is another graph, not a theorem implying the present result. No exact covered table located in Resultary or read primary mathematics; residual unindexed overlap remains.

## value

PASS

The first natural higher-independence complex of an iconic twenty-vertex regular cubic graph is an exact integral homotopy classification, not a tiny arbitrary slice. It contrasts with the ordinary independence complex and provides a nonchordal benchmark for higher-independence topological methods. A researcher investigating dissociation complexes of polyhedral or generalized Petersen graphs could reasonably need this precise S6 fact; no downstream theorem is required for its mathematical utility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
