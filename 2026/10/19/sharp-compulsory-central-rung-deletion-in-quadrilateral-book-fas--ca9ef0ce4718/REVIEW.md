# Self-review

## Correctness — PASS
The proof uses group averaging for the convex spectral-norm objective, followed by a complete orthogonal spectral decomposition. The bounds \(\mu\ge1-b\) and \(\mu\ge\sqrt m\,b\) give the exact two-page optimizer; saturation at \(m\ge3\) forces \(b=1/m\) and \(a=0\). The remaining explicit \(2\times2\) norm inequality gives the full invariant-optimum interval, and the central rung's fixed-edge orbit transfers its value to all global optima. Exact symbolic matrix characteristic polynomials and numerical full-matrix computations were replayed from the bundled script. The infinite quantifier is supported by the proof, not by experiments.

## Originality — PASS
Boyd–Diaconis–Xiao (2004) gives the general convex problem, and Boyd–Diaconis–Parrilo–Xiao (arXiv:0709.0955, 2007; published 2009) gives symmetry and product-spectrum methods, but not this non-product-homogeneous star-book minimax formula. The closest complete-bipartite, wheel, K-partite, and friendship worked examples have different adjacency or constraints. Relevant public records on quadrilateral-book matching complexes and book edge polytopes treat different invariants. Searches and comparisons do not prove global novelty; differently indexed literature could coincide.

## Value — PASS
The result identifies a sharp structural cutoff: the common edge of a quadrilateral book is unavoidable for two pages but is exactly unused in every best-mixing stochastic chain from three pages onward. The full infinite-family optimum, the non-factorization from homogeneous Cartesian-product steps, the sharp all-optimum edge statement, and the complete interval of invariant optima are natural graph-mixing design facts rather than isolated computed constants.

## Closest literature and limitations
The full-text analyses checked Boyd et al. (2004, Sections 1 and 7), Boyd et al. (2009, Sections 3 and 5), Jafarizadeh (2010, Section III), and the later friendship-graph paper (Section 2); all were compared by graph definition and statement implication. The finding is limited to symmetric stochastic chains and has no asserted full non-invariant optimizer classification. Unindexed equivalent coverage remains a residual risk.

Self-review: passed. Independent audit: not yet performed.
