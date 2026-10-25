---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

In any connected proper-interval ordering v_1,…,v_n with umbrella property, closed neighborhoods are contiguous integer intervals [ℓ_i,r_i] and both endpoint sequences are nondecreasing. Starting at extreme v1, distance layers L_k are contiguous cliques indexed by successive b_{k+1}=r_{b_k}; stability of rooted 1-WL separates each distance layer. For each nonroot vertex in layer k, predecessor-layer neighbor count is b_{k−1}−ℓ_i+1, successor count is r_i−b_k (final layer has r_i=n), uniquely determining its full closed neighborhood. Thus equal colors iff true twins except the distinguished root, and refinement needs at most D+1 rounds. True-twin clique cells have uniform full/empty bipartite interactions, so C²-equivalent arbitrary rooted graphs must realize exactly the same cell sizes and quotients; hence rooted identification. Root-fixing automorphisms are independent permutations on nonroot twin cells. Any doubly stochastic root-fixing matrix commuting with adjacency preserves 1-WL cells (strict convexity level-set argument), hence decomposes into those Birkhoff blocks; conversely every such block commutes. Independently enumerated all 6,918 connected proper-interval right-endpoint encodings at n≤10, checked actual individualization refinement versus nonroot true-twin equality and stabilization bound, and the three-path center root counterexample. Finite checks corroborate all-size layer proof.

## originality

PASS

Interval umbrella ordering and general 1-WL/C² correspondence, identification and compact/fractional automorphisms were already known. The assessed distinct theorem is that ONE canonical geometrical endpoint root forces stable WL classes to exactly the true-twin partition for every connected proper interval graph; consequences then specialize established general machinery. Inspected Arvind–Köbler–Rattan–Verbitsky (2015) and Kiefer–Schweitzer–Selman (2015) full primary PDFs: they develop general color refinement, graph identification and fractional symmetry theory without stating this endpoint-specific nonroot true-twin collapse. A specialized interval-graph canonization paper or unstated broad amenable-class criterion might imply it, retained as residual risk.

## value

PASS

The exact endpoint-to-true-twin stabilization mechanism is a structural rigidity result for a natural graph class and canonical unary geometric anchor, with explicit logical identification and compact fractional automorphism polytope consequences. Arbitrary rooting provably fails already on 3-vertex path, marking a genuine sharp geometric boundary. This is not the routine reformulation of global 1-WL equivalence; the adjacent-layer reconstruction lemma is the new mathematical ingredient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
