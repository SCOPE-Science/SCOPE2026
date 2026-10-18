# Review: Full star-isolation spectra and parity-rigid minimum sets on rook graphs

## Correctness — PASS
The selected row/column supports uniquely determine the residual induced rook graph. Its regular degree, or its emptiness if a factor is zero, gives the exact threshold. Row/column inclusion–exclusion enumerates each supported cell set once. The minimum is sharp because any set smaller than the smaller factor must satisfy the support-sum bound, while nonattacking-rook witnesses attain the bound. Equality forces only three support patterns in the interior, and the saturated-row case has one precisely delimited extra pattern. Boundary cases (empty optimum, \(2\times2\), rectangular disparity, large stars) are included. The standalone verifier compares exact graph-based subset tests with every enumerator coefficient on 30 small parameter triples and checks larger cases.

## Originality — PASS (best-knowledge, residual source-access risk)
Zhang and Wu (SSRN 4634672; posted 16 November 2023) develop general star-isolation bounds; their public abstract was read, but the full text could not be examined. Brešar et al. (arXiv:2508.16338) explicitly record the scalar ordinary isolation number of square rook graphs and study graph-product bounds. Brešar and Rall (arXiv:2608.25752) extend general forbidden-subgraph isolation inequalities to Cartesian products, with a cycle–clique exact example. The available relevant sections do not state the complete rook-graph star-isolation size distribution, all minimum configurations, or the parity/independent-optimum structure. Published mathematical-record searches and accessible earlier claim comparisons revealed no implication covering the combined result. This is not a uniqueness certificate; the unavailable 2023 primary full text and unindexed enumerations remain risks.

## Value — PASS
Star isolation measures how many selected closed neighborhoods are needed to eliminate stars of prescribed size; an entire counting polynomial is a natural refinement of its scalar minimum. The theorem solves every cardinality across three unbounded discrete parameters. It also identifies a sharp transition between nonattacking-rook optima and configurations with a single doubled coordinate, proves that independent optima always exist, and recovers both factor orders from the full star-threshold spectrum. These features distinguish it from a one-off small calculation or a mere restatement of a known scalar bound.

## Limits and validation
The result is for exactly two complete-graph factors and forbidden non-induced stars. Exhaustive checks do not substitute for proof. A full-text comparison with Zhang–Wu remains outstanding, and no independent scientific validation has occurred.

Self-review: passed. Independent audit: not yet performed.
