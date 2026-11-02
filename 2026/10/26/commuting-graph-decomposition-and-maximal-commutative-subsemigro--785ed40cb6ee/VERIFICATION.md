---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Nagy Theorem 3 gives the actual free semigroup normal forms: each injective word has plain and doubled-first-letter incarnations, n>=2. Multiplication is concatenation followed by removal of repeated letters with preserved initial double flag. Two distinct normal forms commute exactly when they lie in the same compatible initial-letter/initial-pair sector and underlying suffixes are prefix-comparable, with a plain singleton joined to its doubled sector. Thus the graph decomposes as n(K1∨T_(n−1))⊔n(n−1)T_(n−2). This yields n² components, 2n B_(n−1) elements, the stated ordered pair formula, cograph/perfectness, alpha=2n!, and exactly 2n! maximal commuting subsemigroups (n! of size n+1 and n! of size n−1). Closure under multiplication holds for every maximal chain, including n=2 singleton cases. The Laplacian recursion for T_m=K1∨(mT_(m−1)) follows from eigenvector decomposition of a graph join and gives integral spectra. Independently generated finite semigroups n=2,3,4,5 reproduced element counts 8,30,128,650, graph components 4,9,16,25, commuting ordered pair counts 20,108,664,4580 and maximal cliques 4,12,48,240. Full numerical spectrum matched predicted exact multiplicities for n<=4. No reliance on finite extrapolation for the all-n structural statement.

## originality

PASS

The free left legal semigroup algebra and its normal forms are explicitly Nagy 2023 Theorem 3; these are not original. Free left regular bands are idempotent, lacking the separate doubled-initial-letter sector and nontrivial plain singleton behavior, so their published prefix-tree structure cannot be transplanted without new analysis. The candidate novel finding is the complete ordinary commuting graph and exact all-n subsemigroup and Laplacian classification, not the elementary graph-join spectrum identity itself. Relevant primary semigroup paper and published Resultary semantic records were checked; priority risk remains other terminology for centralizers or commutative graphs of these bands.

## value

PASS

The commuting graph of a natural finitely generated free semigroup is a canonical algebraic graph; maximal commutative subsemigroups and Laplacian spectra are natural global invariants. The proof yields a full parameter family and sharp n-dependent counts, including an equal split of two different maximal-subsemigroup sizes, rather than merely a restatement of Nagy’s multiplication table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
