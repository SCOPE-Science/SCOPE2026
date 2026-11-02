# Review of the maximal-clique/subspace correspondence

## Correctness — PASS
The proof reduces commutation of nonzero rank-one square-zero matrices to two-sided annihilation. A clique's common kernel contains all its images, forcing containment in one canonical subspace-indexed clique. The images and common kernels of each canonical clique reconstruct the indexing subspace, yielding exact maximality and uniqueness. Tensor-scaling counts prove clique sizes and intersections, while a one-variable convexity argument proves the sharp maximum. Boundary cases \(n=2\) and \(q=2\) are included. The standalone program exhaustively checked eight finite configurations, including \(\mathbb F_4\), but the proof supplies the infinite result.

## Originality — PASS, subject to publication-priority risk
The closest earlier rank-one nilpotent commutator record (opaque identifier `c64b3bef-2714-42c6-aeaa-b9883604b3df`) determines commuting-pair numbers and graph degree; this finding **does not** relabel those numbers as new. The full text of Ou–Zhong (2016) concerns upper-triangular rank-one matrices and graph automorphisms, not the full nilpotent rank-one graph or its clique intersection geometry. The full public text of Britnell–Wildon (2010) establishes class-type commutation and nilpotent existence theorems, not an all-clique classification. The accessible Akbari–Raja (2006) abstract addresses connectedness for broader matrix subsets; its full text was not available in this review. Search failure does not establish novelty, and an older or unindexed precise maximal-clique result is a residual risk.

## Value — PASS
Maximal cliques classify *all* maximal pairwise commuting families of the smallest nonzero nilpotent similarity class, a natural structural object in matrix theory. The theorem identifies every extremal family with a Grassmannian subspace, describes all intersections through sums/intersections of linear spaces, and works uniformly in characteristic and matrix dimension. This is structural and extremal information not provided by pairwise degree counts alone; the complete intersection formula supports further work on clique complexes and graph reconstruction without claiming such applications are proved.

## Limits
No full classification of graph automorphisms, graph spectrum, or higher-rank nilpotents is proved. The proof is self-contained; software testing is finite. Independent validation and exhaustive literature priority review have not been performed.

Self-review: passed. Independent audit: not yet performed.
