---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For selected squares D the line-graph support H_D is bipartite on occupied rows and columns. Dominating every board square iff all rows or all columns occupied; induced graph connected iff the occupied-edge support is connected. If both sides full, deleting a cycle edge or a leaf edge preserves connected domination; inclusion-minimality forces exactly one side full. With only rows full the supporting graph must be a tree and every occupied column nonleaf; otherwise removing an edge preserves connectivity/domination. Conversely removing any edge either disconnects selected edges or isolates a full-side row, violating domination because another column is empty. Symmetry handles other family. Bipartite Prüfer words of lengths c-1 and p-1 have p^{c-1} possibilities and c!S(p-1,c) surjective column words, with binom(q,c) choices of columns; the dual summand similarly follows. The ranges yield [p,2p-2] U [q,q+p-2], including p=q=2. Independent original-graph subset enumeration and direct Stirling coefficient computation agreed on seven boards through 4x4; the tree bijection, not finite enumeration, proves generality.

## originality

PASS

Mertens 2024 evaluates the ordinary domination polynomial of rook graphs by row/column coverage, but counts dominating sets including disconnected and nonminimal configurations; its evaluated theorem does not give the one-sided-leaf-tree iff classification or Stirling minimal-connected polynomial. Abu-Khzam et al ESA 2022 give general minimal connected dominating set enumeration algorithms and lower bounds rather than this exact labeled rook-graph polynomial. Classical Prüfer counting is acknowledged; the new contribution is the exact structural two-family identification and gap spectrum. Full primary PDFs were accessible and examined in relevant mathematical sections. Unindexed equivalent rook-graph minimal connected dominating polynomial remains a priority risk.

## value

PASS

The distinction between minimum-size and inclusion-minimal connected domination is natural and mathematically significant. The exact polynomial enumerates all irredundant connected covering configurations via a nontrivial bipartite tree class; the complete achievable-cardinality spectrum has arbitrarily long holes already for two-row boards. This gap behavior is not implied by ordinary domination coefficients or general enumeration algorithms and can benchmark structural domination problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
