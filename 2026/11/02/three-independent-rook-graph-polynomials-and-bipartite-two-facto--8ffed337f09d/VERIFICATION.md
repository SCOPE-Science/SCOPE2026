---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The rook graph is exactly the line graph of K_{m,n}. A selected edge uv has induced rook degree d_H(u)+d_H(v)-2, so the constraint is d_H(u)+d_H(v)≤4. If a vertex has degree three, all neighbors are leaves and the component is K_{1,3}; otherwise components are alternating paths, even cycles or isolates. The labelled two-sort exponential formula sums exact path, cycle, star contributions, including removal of the forbidden two-cycle. In a square, |E(H)|≤|V(H)|≤2q, with equality iff H is a spanning bipartite two-factor. For total domination when max(m,n)≥5, a chosen vertex has at least 5 rook neighbors, at most 2 chosen; a complement vertex with no complement neighbor would make four chosen vertices in a row/column clique, contradicting max degree two. Direct subset tests of boards up to 3×4 and exact 2×2,3×3 maxima corroborate but do not prove universal statements.

## originality

PASS

Qualified best-of-knowledge originality of the precise joint final claim; searched published mathematical records and compared primary statements, stronger methods and equivalent formulations. Earlier bounds, 2-factor enumeration or induced-forest counts cannot imply all coefficients without constructing the exact paths/cycles/stars component enumeration. All residual priority/access risks are recorded.

## value

PASS

The exact three-independence polynomial is a natural coefficientwise graph invariant beyond known extremal k-independence numbers. The spanning two-factor extremizers give exact multiplicities, and a nontrivial large-board equivalence produces total outer three-independent domination polynomials; these are useful precise quantities and not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
