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

For distinct triples, direct complement-based graph reasoning gives distances 1,2,3 exactly when intersections are 0,2,1, respectively. Exact independent construction of the 35-vertex square graph and exhaustive maximal-clique enumeration gives 56 five-vertex facets and f=(35,280,560,280,56). The deterministic two-stage free-face sequence removes 56 dimension (3,4) pairs and 224 (2,3) pairs, all verified to be currently free; the remaining 2-complex has 35 vertices, 280 edges, 336 triangles. An explicit spanning-tree basis of 246 edge cycles yields a signed integer matrix of shape 246×336. Independent reconstruction and exact Hermite normal form gave a full-rank lattice with 245 unit diagonal factors and one factor 2, so H1≅Z/2 rather than merely mod-2 evidence. H2 is a free kernel of rank 336−246=90; no higher homology after collapses. Scale 1 is triangle-free connected graph with 70 edges so H1=Z^36; the general clique-graph-power π1 surjectivity theorem makes the nontrivial order-2 class persist from scale one, while scale three is a simplex. The H2(F2) dimension 91 follows by universal coefficients. This is a complete finite exact calculation, not inference from sampled graphs.

## originality

PASS

Qualified best-of-knowledge ORIGINALITY PASS for the specific final claim, NOT a declaration that known nonequivariant calculations or general frameworks are new. Adamaszek, Clique complexes and graph powers (arxiv:1104.0433), Fact 2.1 supplies clique-inclusion fundamental-group surjectivity and Proposition 2.2 a collapse for girth≥3r+1; at r=2 this requires girth≥7, while O4 has girth six. Thus this general theorem neither forces vanishing nor covers the explicit torsion, although a general persistence implication is prior art. Kong–Lv–Wang, The Terwilliger algebra of Odd graphs (arxiv:1112.0410), studies representation/adjacency algebra for the same graph family, not simplicial flag Rips homology. Residual priority risks are stated; no stronger indexed result was identified which logically implies the assessed claim.

## value

PASS

The natural smallest well-known 35-vertex Odd graph occupies the exact girth-six boundary just beyond the girth≥7 radius-two collapse theorem. Genuine integral order-two torsion gives a sharp coefficient-sensitive persistence phenomenon invisible over Q; a complete machine-reconstructible simplicial certificate is a reusable natural finite invariant, not an arbitrary toy numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
