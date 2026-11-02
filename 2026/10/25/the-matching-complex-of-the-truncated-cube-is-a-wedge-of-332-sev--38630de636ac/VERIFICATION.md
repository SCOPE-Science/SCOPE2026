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

The 24-vertex truncated-cube skeleton built from 8 corner triangles and 12 axis-connection edges has exactly 36 undirected graph edges. The ordinary matching complex consists of ALL pairwise vertex-disjoint edge subsets. An independently authored C++ reconstruction (not opaque source execution) generated every one of 1,019,739 nonempty matchings and the exact matching-size distribution (36,558,4876,26421,92016,206676,292872,249420,117600,26928,2304,32). Independently repeated the 36-stage pivot matching: 509,667 matched pairs and residual one 0-cell, 368 7-cells, 36 8-cells. Exhaustive topological sort of all 7,220,436 oriented Hasse covers visited all 1,019,739 faces. Independently computed the exact signed integral Morse 368-by-36 boundary with 698 nonzero ±1 entries; elementary Z row/column steps obtained 36 unit pivots, all intermediate absolute entries ≤2. Hence its image is primitive rank 36, and since the 7-skeleton is 6-connected, Hurewicz turns the attaching maps into their integer degree vectors; 36 unit pairs cancel, giving ∨^332 S7 with no torsion. Logs alone, Euler characteristic alone and mod-two ranks would not prove this homotopy statement.

## originality

PASS

Published Resultary complete primary RESULT.md computes the independence complex of the SAME 24-vertex truncated cube as ∨⁴S⁵∨∨¹¹S⁶; this is a distinct functor Ind(G), whereas the assigned matching complex is Ind(L(G)) on the 36-edge line graph. Published cuboctahedral matching complexes and truncated-tetrahedral matching complexes are other graphs, not hidden reformulations. The outerplanar matching-complex theorem is inapplicable because this cubic graph has minimum degree three while every finite nonempty outerplanar graph has a vertex degree at most two. No inspected earlier article gives the 332-seven-sphere integral homotopy classification.

## value

PASS

The truncated cube is a canonical Archimedean solid and cube-connected-cycles graph, making its ordinary matching complex a natural finite topological invariant. Its million-face structure reduces to a clean 332-sphere integral wedge only after a substantial full Morse and unimodularity calculation, a meaningful exact classification rather than a known-table recomputation. The result is useful as a benchmark for matching-complex topology on symmetric cubic graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
