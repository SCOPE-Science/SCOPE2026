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

The frozen Shrikhande graph is the 16-vertex Cayley graph on Z4² with generators ±(1,0), ±(0,1), ±(1,1), giving 32 triangles. Independent full enumeration of all 65535 nonempty masks reproduced exactly 8950 triangle-free faces and f=(16,120,528,1452,2496,2568,1424,330,16). Independent lexicographic face-pair reconstruction gives 4465 matched pairs, 1 critical 0-cell, 5 critical 5-cells and 14 critical 6-cells, and the directed full Hasse matching is acyclic (8950 nodes, 48272 incidences). Signed gradient-path recursion independently reproduced the complete integral 5×14 Morse differential from certificate.json, including a determinant +1 minor on columns (0,1,4,9,11). Because the Morse CW five-skeleton is a wedge of five 5-spheres, the degree-five attaching maps are classified by π5=Z^5; unimodular cancellation leaves exactly nine 6-spheres. Raw mod-two ranks are only corroboration and alone would not certify integral homotopy.

## originality

PASS

The exact triangle-free induced-vertex CF3 complex of Shrikhande is not the clique complex or usual independence complex. Ghosh–Selvaraja’s chordal-type shellability hypotheses do not cover Shrikhande’s induced neighborhood 6-cycles. Published rook graph CF3=two-matching K4,4 gives 15 S5 (different graph despite same strongly regular parameters); published CF2 Shrikhande is also a different functor. No inspected result already gives this full Shrikhande integral homotopy type; priority subject to unindexed finite computation.

## value

PASS

A fully certified integral wedge homotopy of a natural canonical strongly regular graph is mathematically useful, especially because its cospectral rook counterpart has a different clique-free type. The unimodular Morse certificate rules out ambiguity from mere mod-two Betti tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
