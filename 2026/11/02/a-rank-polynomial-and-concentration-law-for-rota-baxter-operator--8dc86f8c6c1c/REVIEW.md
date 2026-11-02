# Review: rank distribution of nonzero-weight Rota–Baxter operators on sums of fields

## Correctness
**PASS.** The proof uses the exact established operator/tree correspondence, supplies the explicit matrix-row rule, proves that the subtree sums form a basis, and identifies every independent black or white row modulo black pivots. The marked labeled-tree species derivation establishes the complete polynomial. Prüfer degree moments give the exact mean; disjoint color supports away from adjacent tree vertices and the multinomial Prüfer distribution give variance \(O(n)\), sufficient for \(L^2\) convergence. The accompanying verifier tests all candidate coefficient matrices over two characteristics through dimension four and reproduces the tree/EGF counts through dimension five. Exhaustive checks at finite dimensions are independent evidence, not the general proof.

## Originality
**PASS within the inspected sources, with priority risk.** Gubarev (2018, arXiv:1811.08219) gives the tree bijection, unrefined counts, splitting classification and conjugacy totals, but not the tree nullity statistic or rank polynomial. Gubarev (2020, arXiv:2006.02654) gives spectral and minimal-polynomial restrictions, including sums of fields, not the rank multiplicity profile. Searches for aliases involving nullity, kernel dimension, weighted colored-tree counts, ordinary matrix rank and asymptotic typical rank found no stronger result in the retrieved literature and research index. A broad unlocated refinement theorem or combinatorial tree-statistic result could nevertheless subsume the counting part; uniqueness is not certified by failed searches.

## Mathematical value
**PASS.** Matrix rank is a central invariant of linear Rota–Baxter operators. The complete rank distribution across a natural infinite family refines the known total operator count, while the universal rank proportion \(1-\frac12e^{-1/2}\) expresses typical behavior not contained in the prior total-count or eigenvalue results. The reduction to a sharply defined colored-tree statistic makes both exact finite counts and asymptotic questions accessible. No general central limit theorem or optimal variance is claimed.

## References and limitations
The two relevant primary papers are arXiv:1811.08219 (November 20, 2018) and arXiv:2006.02654 (June 4, 2020). The classification of Rota–Baxter operators and all unrefined total counts belong to prior work. Finite experiments are not infinite proofs; publication priority is provisional. The limit is for all distinct weight-nonzero operators on labeled coordinate factors, not conjugacy classes. Independent mathematical review is outstanding.

Self-review: passed. Independent audit: not yet performed.
