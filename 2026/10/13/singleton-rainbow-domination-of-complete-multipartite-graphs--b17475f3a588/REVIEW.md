# Self-review

## Correctness

PASS. In a complete multipartite graph, every zero in part \(V_i\) sees exactly the labels outside \(V_i\), so the part-count implication is necessary and sufficient. The weight enumerator is then a direct multinomial sum.

For the minimum, colors represented in fully colored parts need one occurrence, while any color absent there must occur in two distinct partially colored parts. The exact feasibility of those double incidences is a capacitated Hall condition
\[
\sum_{i\notin F}\min\{n_i-1,q\}\ge2q.
\]
The lower bound and construction match. Exhaustive enumeration through order seven and four colors confirms the classification, enumerator, and minimum formula.

## Originality

PASS. The closest primary paper studies singleton three-rainbow domination on cylindrical graphs and contains no complete-multipartite theorem. Exact searches using singleton-rainbow, singleton \(k\)-rainbow, complete multipartite, and complete bipartite terminology found no covering result.

The closest published-result record treats ordinary \(2\)-rainbow domination on complete multipartite graphs. That invariant permits a vertex to carry several colors, unlike the singleton model, so it does not imply the present arbitrary-\(k\) feasible-set classification or Hall-capacity formula.

Residual risk remains from older abbreviated terminology such as SkRD and S3RD.

## Value

PASS. The result classifies all singleton rainbow functions, not only one minimum value, and gives an exact arbitrary-\(k\) optimization criterion with a clear structural interpretation. It therefore turns a currently active special-\(k\), special-product problem into a complete theorem on a canonical dense family.

Self-review: passed. Independent audit: not yet performed.
