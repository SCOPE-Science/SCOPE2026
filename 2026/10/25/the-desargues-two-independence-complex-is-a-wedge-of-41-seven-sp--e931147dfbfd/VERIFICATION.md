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

The Desargues generalized Petersen graph GP(10,3) has 20 vertices, 30 edges and is cubic triangle-free. Ind_2 consists exactly of vertex subsets with maximum induced degree≤1, equivalently omitting all 60 length-two path triples. Independent complete enumeration of all 2^20=1,048,576 subsets reproduces 62,049 faces, f-vector and Euler characteristic −41. The sequential vertex-toggle matching has 31,001 matched pairs, leaving three critical 6-cells and forty-four critical 7-cells after an empty-to-vertex pair. Independent global directed-Hasse topological sort visited all 62,049 faces across 400,780 cover incidences, proving acyclicity. Independently reconstructed signed 44×3 integer Morse boundary has rank 3 and 3×3 minor determinant −1 (rows 0,3,14), proving primitive surjectivity onto the 6-cells and H7=Z41. Since the resulting CW six-skeleton is a wedge of three S6, π6 agrees with integral degrees; unit pivots cancel three 6/7 pairs, and remaining attaching maps are null, yielding integral homotopy wedge of 41 S7. Entire result is finite and exhaustive for exactly this graph, not an extrapolation.

## originality

PASS

The inspected accessible full primary papers Deshpande–Singh, Sawant, and Ghosh–Selvaraja concern higher-independence homotopy for complete multipartite graphs/cycles/whiskered graphs/trees and related shellability families. None of their described exact graph families contains the nonchordal girth-six Desargues graph. A published exact ordinary independence complex on the same graph has Ind_1≃S4∨5S5, not the Ind_2 complex. A Petersen Ind_2 result is a different graph and cannot supply the Desargues value. Qualified PASS with the ordinary caveat of unindexed specific computations.

## value

PASS

The Desargues graph is a canonical highly symmetric twenty-vertex incidence graph; higher vertex-independence homotopy is a natural object/invariant not determined by its ordinary independence complex. The complete integral wedge of 41 seven-spheres gives a precisely usable benchmark for small cubic graph topology and shows a nontrivial degree shift; the exact integer primitive boundary calculation is meaningful without a family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
