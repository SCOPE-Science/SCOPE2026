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

The independent edge-bracket basis gives [x,y]=0 iff x_u y_v-x_v y_u=0 for every graph edge. For S=supp(x), edge equations force y=0 on N(S)\S, constant ratio y_u/x_u on each connected component of G[S], and arbitrary coordinates outside N[S]; therefore dim C_W(x)=c(G[S])+|V\N[S]|. A projective line [x] has no other commuting projective line iff this dimension is one, equivalent to S connected dominating. Decompose the complement graph into components H_i on blocks V_i. The original graph is the complete join of its induced block graphs: any multi-block support is connected dominating and isolated, and no commuting edge crosses different block supports. Each nonisolated block-supported projective point reaches a basis line in its block within at most two commuting edges (by a non-neighbor if its support fails to dominate, or by restriction to a disconnected support component otherwise). The basis lines reproduce connected H_i, giving one nontrivial component for each |V_i|>=2, of size [m_i]_q-D_i(q) and diameter <=4+diam(H_i). Supports have (q-1)^(|S|-1) projective lines, giving the weight D_i. In any tree, connected dominating sets are exactly the sets containing all non-leaves; summing over leaf additions gives q^ell(q-1)^(n-ell-1) isolates. Independent actual determinant-based commutation counts agreed with connected-domination prediction across 92 graph/field instances with n<=4, q=2,3; finite tests supplement the all-size proof.

## originality

PASS

PASS restricted to complete co-component decomposition and exact weighted counts, not the general projective-isolation centralizer criterion: Sriwongsa 2025 Theorem 2.12 already states the complementary noncommuting-graph dominating-vertex criterion for arbitrary Lie algebras.

## value

PASS

The graph-algebra construction is motivated by transferring combinatorial invariants to Lie-theoretic commutation geometry. Computing all projective commuting components (including exact weighted sizes and a diameter bound) for arbitrary input graphs is substantially richer than a routine centralizer test; the tree specialization encodes a natural leaf invariant. The result is an exact structural classification, not just code correctness or novelty by renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
