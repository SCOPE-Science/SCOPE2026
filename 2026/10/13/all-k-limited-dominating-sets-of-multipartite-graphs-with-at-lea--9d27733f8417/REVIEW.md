# Self-review

## Correctness

PASS. The proof begins from the exact domination criterion for complete multipartite graphs. For an occupied part \(V_i\), every selected vertex has precisely the omitted vertices outside \(V_i\) as outside neighbors, so the \(k\)-limited condition is exactly one linear inequality per occupied part. This yields the all-set classification and coefficient formula directly.

For a fixed support, the maximum omitted total is bounded by total per-part capacity, the smallest capacity, and the summed pairwise inequalities. The proof shows these three bounds are jointly sufficient by constructing an integer allocation above the common lower bound. Exhaustive direct checking through total order nine agrees with the classification, every polynomial coefficient, and the support minimum.

## Originality

PASS. The initiating paper gives the complete-bipartite minimum explicitly; that case is treated as prior work and excluded from the novelty scope. Its accessible full text contains no complete-multipartite theorem. Searches included \(k\)-limited domination, limited domination, complete multipartite aliases, exact/all-set/polynomial formulations, and the equivalent \((0,k)\)-pitchfork terminology.

The closest exact database result is for \(k\)-limited packing of complete multipartite graphs, which imposes a different neighborhood condition. Recent follow-up work on \(k\)-limited domination treats complexity and Sierpiński graphs rather than this family.

Residual risk remains from older pitchfork terminology and concurrent work.

## Value

PASS. The result classifies every feasible set rather than only the minimum. The exact enumerator and the support-by-support omission maximum expose the full capacity geometry on a canonical dense graph class and strictly extend the known two-part scalar calculation.

Self-review: passed. Independent audit: not yet performed.
