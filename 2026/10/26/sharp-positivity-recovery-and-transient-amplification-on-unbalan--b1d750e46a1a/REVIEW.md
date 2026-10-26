# Self-review

## Correctness — PASS
The proof reconstructs \(e^{-tL^2}\) from all four spectral projectors for the unnormalized complete-bipartite Laplacian. Critical derivatives prove unique within-part recovery times. A monotone parameter lemma orders the two recoveries; a separate exponential-difference sign argument establishes dominance of the larger vertex part for the sharp \(\ell^\infty\) row norm. The exact peak time and amplitude then follow from a single exponential derivative, and controlled limits give the three asymmetric time scales and vanishing amplification. The standalone checker verifies the spectral identities and independent numerical matrix powers (41930 assertions). These finite checks do not establish the infinite-family statements on their own.

## Originality — PASS within examined evidence
The initial 2015 Daners–Glück–Kennedy work supplies eventual positivity theory rather than these graph-specific sharp formulas. The public three-spectral-value theorem on positivity-time sets was inspected in full: it does not determine the biclique norm or threshold, and the generic unbalanced biclique has four spectral levels. Earlier local calculations on rook-graph squared heat and ordinary biclique heat have different matrix kernels and are not mathematically covering. An exact prior derivation under alternate graph-filter terminology remains possible; the priority assessment is provisional.

## Value — PASS
For fourth-order network smoothing the largest possible bounded-coordinate output error and the time of recovery of nonnegative data are natural stability quantities. The result gives exact values and an unexpected strict two-stage spatial recovery, with the larger part governing every worst-case row. As asymmetry grows, its within-small-part recovery is on a \(b^{-2}\) scale, the transient peak on a \(b^{-2}\log b\) scale, and final recovery on a \(b^{-1}\) scale, yet its worst amplification approaches one. This is structural rather than a routine particular numerical example.

## Closest literature and limits
See arXiv:1511.05294 (2015), the public three-spectral-value positivity-time theorem (2026), and Gazzola–Grunau (2008). The 2008 continuum article was reviewed only at abstract level. No generalization is claimed beyond unweighted bicliques, \(L^2\), and the vertex maximum norm. Independent scientific and historical-priority examinations have not occurred.

Self-review: passed. Independent audit: not yet performed.
