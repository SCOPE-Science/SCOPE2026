---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

I independently reconstructed the complex from the degree-at-most-two definition. It has 1081 faces including the empty face and f-vector \((12,66,204,360,324,114)\). Replaying the stated toggle order leaves exactly 539 matched pairs and two critical nonempty faces: one vertex and one six-edge simplex. I independently oriented all 4488 nonempty Hasse covers according to the Morse matching and topologically sorted all 1080 nonempty faces, confirming acyclicity. Hence Forman theory gives a CW model with one 0-cell and one 5-cell and no intervening cells; the unique 5-cell attaches to a point, giving \(S^5\). The repository verifier additionally contains an independent mod-two boundary-rank check.

## originality

PASS

Singh's full primary paper gives exact homotopy types for the shellable range \(m>r\ge n\) and for the balanced boundary \(M_{n-1}(K_{n,n})\). After ordering \(K_{3,4}\) as \(K_{4,3}\), the audited case has \(r=2<n=3\), so neither theorem applies. The same paper notes Reiner--Roberts rational homology formulas for broad higher chessboard complexes, but rational homology does not imply the homotopy-sphere statement. Resultary search returned the assigned finding and other graph-complex computations, not a prior \(K_{3,4}\) homotopy theorem.

## value

PASS

This is the first unequal complete-bipartite case immediately outside Singh's exact regimes and a natural small boundary in higher matching complexes. An exact homotopy type, certified by a complete Morse matching rather than only homology, is a useful structural benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
