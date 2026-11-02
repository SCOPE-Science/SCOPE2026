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

Represent vertices of Z4xZ4 by 0..15; define the r=2 faces exactly by induced maximum degree <=1, forbidding any selected center with two selected neighbors (triangles also prohibited). Exhaustively enumerate all 65536 masks per graph, yielding Shrikhande face numbers [1,16,120,384,544,240,32], rook [1,16,120,384,528,144]. For common pivot order (9,2,13,7,12,6,15,14,8,3,0,10,4,1,11,5), independent full Hasse-graph construction finds 639 and 543 matched pairs, 4960 and 4224 directed incidences, and verifies acyclicity by complete topological sort. Critical cells are a single 0-cell and 57 vs 105 3-cells. Forman discrete Morse theory produces a CW complex with those cell counts; every 3-cell attaches to the one-point 2-skeleton, hence a wedge of S3 integrally. This is a complete finite proof certificate over all faces, not inference from partial enumeration or modular Betti numbers.

## originality

PASS

Best-of-knowledge: the submitted full statement was compared by actual implication to the specific prior primary statements and published mathematical index. NOT_APPLICABLE_TO_THIS_PAIR: No theorem in materially inspected relevant classifications contains the two nonchordal (16,6,2,2) graphs. ; CHORDAL_CONDITION_NOT_MET: Both target graphs contain induced 4-cycles. ; COVERS_R1_ONLY: 23 versus 15 ordinary sphere counts are correctly credited; they cannot imply r=2 exact wedges.. An inaccessible plausible source alone was not treated as failure; meaningful risks remain listed below.

## value

PASS

These two cospectral nonisomorphic strongly regular graphs are a canonical test pair. The reverse strict inequality between ordinary and two-independence sphere multiplicities is a motivated homotopy-level distinction not given by SRG parameters or the ordinary independence calculation. A finite exact homotopy computation is itself a useful invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
