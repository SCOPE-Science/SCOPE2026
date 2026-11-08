---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For connected simple base graph order n>=3, a connected dominating set of a full edge subdivision induces a connected vertex cover S, selected interior subdivision vertices must form a spanning tree T of G[S], and each excluded original x needs exactly one selected incident subdivision neighbor. Inclusion-minimality further forces every tree leaf to have an outside-S neighbor. All selected vertices are indispensable under those conditions. Weighted matrix-tree theorem and Prüfer-word surjection count give the K_{a,b} Stirling polynomial; n+|S|-1 verifies degrees and K_{2,b} gap. Independent verification: Independently built full-edge-subdivided K_{2,2}, K_{2,3}, K_{2,4} and brute-enumerated all connected inclusion-minimal dominating sets. Obtained labeled count polynomials {6:8}, {7:12,8:6}, {8:32,10:8}, exactly the specialized Stirling formula. Inspected the full standalone verifier; finite cases only corroborate the general leaf/tree proof.

## originality

PASS

Best-of-knowledge: inspected accessible closely related primary PDFs, searched published mathematical records for aliases/stronger results, and compared implications. General enumeration algorithms do not logically entail the displayed closed coefficient polynomial; a prior same weighted bipartite-tree kernel for a rook graph is expressly credited and not claimed new. Residual priority limitations are explicit.

## value

PASS

The exact arbitrary-base subdivision tree-cover characterization is structurally reusable; its K_{2,b} specialization yields unbounded gaps in cardinalities of inclusion-minimal connected dominating sets even for bipartite 2-degenerate graphs. The labeled polynomial is a natural enumerative invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
