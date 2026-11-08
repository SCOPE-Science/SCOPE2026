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

Definitions and all quantifiers agree with the source: T any finite tree with t>=2 and m>=2, N=mt; Δ_2^t(K_m square T)=Cl(K_m square T)^vee. The N-vertex equivariant complement-chain Alexander duality produces reduced H_{N-4}(Δ;Z)=H^1(Cl(G);Z) tensor det(Z^N), giving precisely sgn(row)^t sgn(tree)^m. A clique involving >=3 vertices belongs entirely to a K_m fiber because the tree has no triangles; collapsing contractible fibers yields a graph with m parallel edges over each tree edge. Its chain boundary is the row-sum ε⊗∂_T and ∂_T is injective, so H1=ker ε⊗oriented_edges(T), and H^1=(Z^m/Z·1)⊗E_T integrally; replacing by the root lattice would be incorrect. Fixed-color/edge signed trace gives the printed character. Computing symmetric row-permutation coinvariants of the quotient lattice gives Z/m for t even, sign-twisted Z for (m=2,t odd), Z/2 for (even m>=4,t odd) and zero for odd m>=3,t odd. Independently constructed 10 integer presentations, m=2..6 with and without sign, and Smith normal forms reproduced all cases. The finite checks support, but do not replace, the all-tree proof.

## originality

PASS

Checked actual theorems and their implications, original sources and relevant published exact results, including already-known special cases; none of those inspected entails the full target claim, subject to the explicit best-of-knowledge residual risks. This does not infer novelty from a failed search.

## value

PASS

Natural representation-theoretic refinement of known total-two-cut topology on all clique-by-tree products, including branching families and an integral parity-dependent torsion invariant that rational characters and ordinary homology ranks cannot reveal. This exact global lattice is mathematically motivated beyond routine duality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
