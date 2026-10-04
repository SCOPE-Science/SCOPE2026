# Review

## Correctness

PASS. For each source length \(2\le n\le8\), the lower certificate is an explicit code whose exact-two descendant sets are pairwise disjoint. The upper certificate partitions the entire binary word space into exactly the same number of cliques in the exact-two confusability graph. Therefore no independent set, hence no correcting code, can be larger. The verifier reconstructs all descendant sets directly from the channel rule. The published exact/at-most equivalence and even-length PAL/RC conjugacy justify the two stated channel transfers.

## Originality

PASS. The closest 2026 paper defines this graph, determines the maximum two-error sphere, and derives a general maximum-degree coloring bound, but it does not give finite independence numbers. Exact-value, graph-equivalence, small-length, palindromic-duplication, and reverse-complement-duplication searches did not locate the table \(4,8,14,20,28,42,66\). Nearby earlier work treats different error-count or duplication-length regimes. Residual risk remains that an unindexed finite computation under different terminology contains overlapping values.

## Value

PASS. Binary two-error coding at even duplication length is explicitly left with a factor-two asymptotic gap in the recent literature, and the length-\(2\) channel is singled out as structurally special. Exact optima for the first five nontrivial source lengths are useful finite benchmarks for constructions and conjectures in that open problem. Matching clique-cover and code certificates make each benchmark independently reusable rather than a solver-only datum.

Same-model review: passed. Independent audit: not yet performed.
