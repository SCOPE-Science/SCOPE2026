# Self-review

## Correctness

PASS. For a complete multipartite graph, every vertex in one part has the same open neighborhood, namely the complement of that part. Therefore the neighborhood-sum condition is exactly \(W-s_i\ge1\). A \(-1\)-vertex in part \(i\) has a \(2\)-neighbor exactly when a \(2\) occurs outside that part. These conditions are necessary and sufficient.

Fixed part-count triples contribute the product of multinomial coefficients, so summing over the feasible count arrays gives the exact weight enumerator. Summing all neighborhood inequalities gives \(W\ge2\). Exhaustive adjacency-level checking through total order eight agrees coefficientwise.

## Originality

PASS, with a documented access risk. The fresh 2026 preprint on the identical invariant and graph family states that it determines the signed total Roman domination and domatic numbers. Targeted published-finding corpus and web searches found no all-function weight enumerator. The closest database theorem enumerates signed Roman functions, not signed total Roman functions; its closed-neighborhood condition is not implication-equivalent to the open-neighborhood condition here.

Direct full-text inspection of arXiv:2606.27175 was blocked by transport, and the institutional fallback required an interactive step unavailable in this execution. This leaves a residual risk that the paper contains a closely related intermediate part-count lemma. The accessible material does not expose the final enumerator.

## Value

PASS. The polynomial gives the full weight distribution of a newly active domination variant on a canonical graph family. It strictly refines the scalar minimum and supplies exact multiplicities of both optimal and nonoptimal functions.

Self-review: passed. Independent audit: not yet performed.
