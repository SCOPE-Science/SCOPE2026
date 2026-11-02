# Research review: subdivided complete bipartite mixing

## Correctness

**PASS.** The graph, all feasible probabilities, and the unrestricted symmetric-stochastic objective are defined explicitly. Averaging under independent permutations of the two original parts preserves feasibility and cannot increase the spectral norm objective. The complete spectrum decomposes into one three-dimensional block, two families of two-dimensional blocks, and a scalar interaction block, with multiplicities totaling the graph order. At original-row saturation the largest nonstationary eigenvalue is \(F\), the possible dominating negative eigenvalue is \(-s\), and the sign of \(2s^2-s-1/p\) gives exactly two exceptional parameter pairs. The Laplacian Fiedler test-vector argument establishes strict optimality of the saturated weights inside the invariant rectangle in the main range. Nonnegative original holding probabilities then yield the conclusion for **every** unrestricted optimum. Strict improvement by small identity mixing proves both exceptions. The fixed-\(p\) asymptotic is an implicit-root calculation. Numerical verification checks implementation and does not replace the argument.

## Originality

**PASS, subject to residual historical-coverage risk.** The foundational convex SDP problem and automorphism averaging are prior results; so are the unsubdivided complete bipartite case and the eight-cycle special case. The inspected open primary work does not give the pair-specific edge-incidence subdivision spectrum or its two-exception holding classification. The original complete bipartite graph has only \(p+q\) vertices, while the present graph has \(p+q+pq\), different edge orbits, and a different extremal spectrum. K-partite pseudo-distance-regular layer networks use all-to-all connections between neighboring layers, not private intermediate vertices for each original edge. The general symmetrization method alone does not imply that both original vertex classes saturate the stochastic row budget except at two exact pairs. Published-record searches and accessible deduplication records found no statement-level coverage. An unindexed source could nevertheless cover it.

## Mathematical value

**PASS.** Subdivisions model pair-specific intermediaries in communication and incidence networks. Holding is a genuine design variable, and its optimal vanishing or persistence changes the support of a Markov transition matrix. The theorem gives a complete natural parameter classification of this support question over all \(p,q\ge2\), and an explicit globally optimal rate and allocation for every nonexceptional pair. The two exceptions and the fixed-side asymptotic reveal finite-size and imbalance effects. The result is not merely another numerical optimum for one graph.

## Closest literature and limitations

Boyd–Diaconis–Xiao (2004) provides general convexity and the ordinary complete-bipartite example. Boyd–Diaconis–Parrilo–Xiao (2007/2009) supplies orbit and representation reductions and the known cycle and unsubdivided biclique formulas. Jafarizadeh (2010) studies structurally distinct complete interlayer multipartite networks. None of the inspected results implies the stated support phase classification as written. The theorem does not determine the exact FMMC weights/SLEM in the two exceptional graphs and does not claim unrestricted optimizer uniqueness. Additional unpublished or specialized sources could present equivalent results. The mathematical proof has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
