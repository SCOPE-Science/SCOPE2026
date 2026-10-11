---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a candidate fort F in a complete multipartite graph, an outside vertex in part i has exactly \(|F|-|F\cap X_i|\) neighbors in F. This condition immediately yields the complete minimal classification: same-part pairs in non-singleton parts, pairs of singleton vertices, and 3-part transversal triples with at most one singleton. The count formulas follow by choosing these edges. The fort-number formula is supported by the exchange normalization of triple forts and the parity-leftover argument; the fractional zero-forcing formula follows from all pair constraints and explicit half-weight feasible solutions (with the lone singleton weighted zero when q=1). A fresh definition-level brute-force replay through order 8 reproduced the entire minimal-fort hypergraph, edge counts and exact maximum matching for every part profile; the package also records a larger order-10 LP replay. Finite computation is corroborative only.

## originality

PASS

The decisive 2023 fort-hypergraph source and 2024 minimal-fort enumeration paper were inspected in full accessible arXiv text. They cover complete bipartite graphs (including the exact special-case fort/fractional values) and several other graph families, but not arbitrary complete multipartite graphs. The audited theorem introduces a genuinely new rank-3 transversal-triple phenomenon once three or more parts interact and derives arbitrary-profile matching and fractional-transversal formulas. Exact searches and Resultary did not locate prior complete-multipartite coverage.

## value

PASS

Minimal forts are the irredundant obstruction hyperedges underlying fort-cover formulations of zero forcing. Complete multipartite graphs are a canonical family, and the transition from pair-only bipartite forts to rank-3 transversal triples is structurally meaningful. The theorem simultaneously resolves the full minimal-fort hypergraph, its edge count, maximum disjoint-fort packing and fractional transversal number for every part profile, so it is mathematically useful rather than a routine finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
