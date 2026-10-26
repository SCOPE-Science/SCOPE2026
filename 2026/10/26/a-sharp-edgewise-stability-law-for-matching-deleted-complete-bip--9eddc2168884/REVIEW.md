# Review of the matching-deletion edge-gradient projection theorem

## Correctness

**PASS.** The theorem is an induced maximum-coordinate norm identity for finite orthogonal projectors. Its proof first derives the full biclique row–column averaging projection, then applies an exact Schur-complement identity to remove the observations indexed by a matching. The resulting two-index kernel is specified for every retained edge pair. A realizable-incidence sign classification, rather than an assumption that all nonsharing transfer currents are negative, yields all three absolute row sums. The strict comparison follows from a nonnegative quadratic bound; the final matching-edge jump is rational subtraction. The graph is connected for every specified parameter and the standard orientation is immaterial to the norm.

The standalone exact-rational incidence calculation independently reconstructs the projector and reproduces its entries, all row classes, and the sharp norm for every tested \(3\le n\le9\), including the crown-graph boundary. The checker reports 123,977 passed assertions. Finite checks are not used as a proof for all sizes. The analytical proof covers every integer \(n\ge3\) and \(0\le t\le n\); disconnected \(n=2\) perfect deletion is excluded explicitly.

## Originality

**PASS within inspected evidence; historical priority not independently certified.** The literature provides the graph-Hodge least-squares framework and transfer-current kernels, but the inspected primary material does not supply the matching-deletion family’s exact sharp maximum-coordinate norm or the final-step ratio. The rank-update mechanism is classical and is credited as such; the specific sign pattern, row-type domination, strict progression and terminal jump are the new mathematical conclusions asserted.

The closest accessible comparison for this exact operator is the unweighted complete-multipartite projection norm. A complete bipartite graph belongs to that family, but a biclique with any nonempty proper deleted matching is not a complete multipartite graph. Thus the complete-multipartite formula gives the \(t=0\) endpoint only. Other nearby records concern transportation-space basis projections on cactus graphs, Kirchhoff indices, or graph metric invariants rather than the row-sum norm of this specific Euclidean edge-gradient projector. None of those record statements implies the asserted matching-deletion classification. Older network papers using equivalent terminology remain a legitimate residual priority risk.

## Value

**PASS.** The object is the canonical least-squares operator for partial pairwise-comparison edge data. The computed invariant answers a natural robustness question: if every observed comparison has error bounded by one, how large can a single fitted comparison error become? The deleted edges are disjoint, a common and combinatorially canonical failure pattern. The result does more than give a small numerical improvement: it classifies every deletion count, finds norming edge orbits and finite sign witnesses, and exposes an exact terminal-edge phase in which the last deletion has \((n-2)(n+1)\) times the preceding effect. This distinguishes a change of the extremizing orbit from mere first-order sensitivity of an old norm formula.

## Limits and sources

The proof does not treat unequal bipartition sizes, arbitrary missing-edge patterns, weighted least squares or errors in recovered vertex potentials. The originality judgment is relative to specifically inspected material. Principal primary literature: Jiang–Lim–Yao–Ye, arXiv:0811.1067, especially the graph-gradient least-squares model and matrix-theoretic Hodge discussion; Kassel–Wu, arXiv:1312.2946, especially its definition of transfer current and spectral representation. Additional searches examined names and formulas for crown graphs, matching-deleted bicliques, generalized Laplacian inverses and maximum-coordinate projection constants. Details of exact comparisons and unexcluded priority risks are in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
