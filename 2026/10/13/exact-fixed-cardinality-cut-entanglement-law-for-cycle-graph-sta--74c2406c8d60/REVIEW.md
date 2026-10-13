# Scientific review: exact fixed-cardinality cut-entanglement law for cycle graph states

## Correctness — PASS

The claim concerns the full bivariate polynomial counting cuts by both cardinality and binary cut-matrix rank for every unweighted cycle of length at least three. The proof reduces graph-state entanglement to that rank, decomposes every cut with a noncrossing edge into alternating paths, and proves each path's half-rank is the ceiling of half its edge-run length. The four-state transfer counts such cuts exactly. The only exceptional binary configurations are the two even-cycle alternating cuts; their cut matrices have rank one below maximum, and their doubled transfer traces are explicitly corrected. The characteristic polynomial and analytic dominant eigenvalue give the mean, variance, and unrestricted-cut Gaussian limit. Boundaries at odd/even sizes and at empty/full subsets are addressed. The included independently implemented exact binary-matrix verifier checks every size and entanglement value for \(3\le n\le15\). A finite check is not an infinite proof.

## Originality — PASS with residual literature risk

The closest 2025 source defines the fixed-subsystem-size cut-rank distribution and evaluates cycle examples only up to 12 vertices. Its finite tables cannot imply the all-size bivariate polynomial or Gaussian limit without further argument. The general average-cut-rank literature gives different, weaker statistics. Standard graph-state Schmidt-rank equivalence is credited. A closely related published cycle *rank* enumerator deals instead with varying antisymmetric adjacency weights and counts graphical-group characters; its rank variables cannot recover conditional vertex-subset cut ranks, despite a similar run-counting idea. The 2026 circuit-block paper treats particular graph-state cuts rather than uniformly ranging over every fixed-size subset. No equivalent theorem was located after searches for graph-state cycle cut-rank histograms, aliases and generating polynomials. This does not prove global novelty; implicit transfer-matrix specializations in unindexed graph-polynomial literature remain a priority risk.

## Value — PASS

All fixed-cardinality entanglement histograms, including the balanced-cut heterogeneity statistic explicitly studied in recent literature, follow from one fixed-size matrix and an essential even-cycle correction. This replaces separate exponentially sized cut enumerations with an exact polynomial-time-in-size computation for an infinite family of graph-state resources. The formula also quantifies unrestricted random-cut fluctuations by an explicit variance constant and Gaussian limit, without asserting any operational speedup or arbitrary-graph generalization. It answers a motivated classification question rather than producing an arbitrary finite case or merely recomputing the 2025 tables.

## Scope and residual risks

The statement is for simple unweighted cycle graph states and exact bipartite entanglement; noisy preparations, other graphs, and balanced-cut central limit behavior are outside scope. Existing equivalent formulas may be expressed through another graph-polynomial convention. The scientific review is not an independent validation.

Self-review: passed. Independent audit: not yet performed.
