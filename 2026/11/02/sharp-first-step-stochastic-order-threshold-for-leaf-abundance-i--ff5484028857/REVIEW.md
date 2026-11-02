# Scientific review

## Correctness

**PASS.** The coefficient identity for fixed-root forests is the established forest-volume formula. The root-plus-nonroot occupancy decomposition is reconstructed directly by coefficient comparison, with positive conditioning events. The first-step coupling preserves each conditional marginal and works precisely when the minimum possible empty-box count meets the required probability bound. The converse uses an exact minimum-atom ratio, and mean monotonicity and the saturation case use strict, explicit inequalities. The standalone verifier passes 2,975 exact assertions; exhaustive finite checks corroborate, but do not replace, the symbolic arguments.

## Originality

**PASS, with residual historical risk.** The foundation in Pitman's 2001 full-text forest-volume identity and fixed-root conditioning is expressly treated as prior work. The comparison is not a new enumeration formula: it is a sharp, all-size comparison of two conditional undirected-leaf laws, plus a distinct saturation obstruction and strict conditional-mean behavior. Searches for fixed-root leaf regression, degree-one counts, empty/singleton occupancy, and stochastic ordering did not reveal direct prior coverage. Potential implicit coverage by an older occupancy inequality remains possible. Related results for random recursive trees or component sizes under changing numbers of roots are not stronger statements about the present fixed-root, fixed-size conditioning.

## Value

**PASS.** The object is a standard Cayley-forest model, and its undirected leaf statistic is a natural boundary-size invariant. Two competing leaf mechanisms make mean comparisons misleading. The exact threshold \(m=2k\) distinguishes stochastic domination from incomparable conditional laws, not merely an arbitrarily chosen small-parameter example; the separate high-leaf saturation obstruction shows another structural failure mechanism. This clarifies when root branching predicts an entire leaf law, rather than only its first moment.

## Literature and limitations

The closest primary source is Pitman's full-text 2001 paper, equations (5) and (6) and Section 3.2, which supplies the classical fixed-root forest enumerator but not the asserted stochastic-order boundary. The earlier 1996 forest paper supplies foundational context. Published research on random recursive tree leaf covariances concerns a different growing-tree law. The proof does not classify all adjacent conditional distributions; implicit earlier coverage remains a research priority risk, and independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
