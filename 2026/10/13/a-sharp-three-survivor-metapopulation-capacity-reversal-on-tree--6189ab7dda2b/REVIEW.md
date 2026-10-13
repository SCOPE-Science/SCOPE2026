# Scientific review

## Correctness — PASS

For any three-vertex induced subgraph of a tree, the only adjacency radii are \(0\), \(1\), and \(\sqrt2\). The number of two-link triples is the wedge statistic \(W(T)\); double-counting edges across triples gives the one-link count, and subtraction gives the zero-link count. The proof establishes the sharp integer-degree bounds \(n-2\le W(T)\le\binom{n-1}2\) with unique path and star extremizers, and consequently establishes the strict regime-dependent inequalities for every \(n\ge4\). The separate one- and two-patch argument proves that three survivors are the first informative sample size. The standalone exact combinatorial checker passed 18,247 labeled trees and 615,482 triple samples, with 2,701 symbolic determinant checks. No infinite statement is inferred solely from this enumeration.

## Originality — PASS, with identified limitations

The 2000 Hanski–Ovaskainen work supplies the eigenvalue-based ecological capacity concept, and the 2003 Ovaskainen paper addresses effects of individual patch removal. The fully inspected 2015 Grilli–Barabás–Allesina article handles random spatial landscape ensembles and spectral metapopulation persistence, not the full distribution conditioned on three surviving vertices in an arbitrary fixed tree or its sharp star/path reversal. Searches for induced-three-vertex spectral means, wedge counts, conditioned site percolation and equivalent tree extremal statements did not locate that joint theorem. Possible unindexed graph-spectral or landscape-reliability theorems remain an originality risk. The complete 2003 article was not accessible; its abstract was compared, but whole-document noncoverage is not asserted.

## Value — PASS

The theorem supplies an exact, all-order decision boundary for conservation comparisons under a fixed severe-habitat-loss budget. It shows that the most favorable connected tree shape can reverse with the species' extinction-to-colonization threshold even though all original landscapes have the same number of habitat links, and it establishes why one- and two-patch studies cannot detect topology dependence. This is a motivated ecological limit of comparing landscapes by a single spectral average: the mean favors paths whereas high-threshold reliability favors stars. The classification uses no arbitrary census cutoff other than the provably smallest informative sample.

## Closest literature and restrictions

The full 2015 PLOS Computational Biology article establishes the model-to-eigenvalue connection and analyzes random spatial patches and individual patch loss; it does not present the fixed-tree uniform three-survivor classification. The 2000 Nature article is available in abstract/preview form, and the 2003 Mathematical Biosciences paper in abstract form; neither inaccessible full text is characterized as absent coverage. The underlying spectral persistence threshold is a deterministic mean-field proxy and is not a theorem of infinite stochastic survival. Weighted networks, more survivors and correlated failures are outside scope.

Self-review: passed. Independent audit: not yet performed.
