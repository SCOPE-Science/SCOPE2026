# Scientific review: bipartite spanning-tree covariance geometry

## Correctness

PASS. The edge law is derived from the known determinantal transfer-current theorem, with the transfer kernel evaluated from the three nonconstant vertex-Laplacian eigenspaces. Its four edge-pair types determine the entire covariance operator. Orthogonal two-way ANOVA projectors then give exact eigenvalues, dimensions, and the arbitrary-weight quadratic form. The normalizations, including the constant direction and the \(a=b=2\) spectral degeneracy, were checked. A standalone exact-rational verifier exhausts 4657 small spanning trees, but the proof—not enumeration—covers every \(a,b\ge2\).

## Originality

PASS under the documented accessible comparisons, with residual priority risk. Burton–Pemantle gives all edge-set inclusion probabilities through a transfer-current determinant, so the entrywise law and negative pairwise covariance are established prior facts. The newly assessed claim is the all-size fully evaluated covariance eigenspace decomposition and sharp variance/prediction geometry, which does not appear as such in the inspected Burton–Pemantle text, Eğecioğlu–Remmel multipartite degree enumeration, Klee–Stamps vertex-product weighted enumeration, or the accessible Rapoport material. Those general tools may support an earlier implicit derivation; this risk remains. No uniqueness or independence of this review is claimed.

## Mathematical value

PASS. Edge-selection uncertainty is a natural property of randomly chosen spanning trees, and weighted total tree cost is its central linear statistic. The theorem simultaneously answers the variance of every possible deterministic edge-cost matrix, identifies the only deterministic linear combination, and sharply measures the loss in predicting costs from vertex degrees. The exact condition number separates balanced from increasingly unbalanced bipartite graphs and is not merely a single numerical covariance entry.

## Closest sources and limitations

Burton–Pemantle, https://arxiv.org/abs/math/0404048: general finite-graph transfer-current identity; it is used rather than claimed. Eğecioğlu–Remmel, https://sites.cs.ucsb.edu/~omer/DOWNLOADABLE/multipartite94.pdf: degree-weight generating functions on multipartite graphs. Klee–Stamps, https://arxiv.org/abs/1903.03575: vertex-factorized edge-weight enumeration. Rapoport, https://pmc.ncbi.nlm.nih.gov/articles/PMC12535553/: general UST edge and degree correlation framework. Exact evaluation of the covariance eigenvalue spectrum could conceivably be implicit elsewhere. The result is unweighted and restricted to \(K_{a,b}\) with \(a,b\ge2\); prediction optimality is only linear/affine.

Self-review: passed. Independent audit: not yet performed.
