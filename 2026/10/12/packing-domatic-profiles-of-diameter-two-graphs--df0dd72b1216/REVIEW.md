# Self-review

## Correctness

PASS. The proof uses only the definitions and the diameter-two metric. Colors at least \(2\) cannot repeat because \(s_2\ge2\), while color \(1\) is independent. Every higher-colored vertex alone dominates the graph. A color-\(1\)-only block can dominate only when it is the entire color-\(1\) class and that class is maximal independent, so at most one such block exists. These observations force the lower bound and the exact equality criterion. The \(k+1\) construction uses an independent color-\(1\) set of size \(n-k\) and \(k\) distinct higher-colored vertices.

The direct finite checker agrees on every labeled diameter-two graph of orders \(3\) through \(5\).

## Originality

PASS. The closest source is Proposition 2.6 of Brešar, Ferme, and Hu, which gives only the optimal-color packing domatic number \(n-\alpha+1\) for diameter-two graphs. It therefore proves the initial plateau of the new formula but not the values for any larger \(k\). The inspected full text contains no all-\(k\) tail criterion and no complete-multipartite treatment. Targeted database and web searches for maximal-independent-set, independent-dominating-set, diameter-two, \(k\)-versus-\(k+1\), and complete-multipartite formulations found no covering result.

Residual risk: the invariant is very recent, so concurrent or poorly indexed follow-up work could contain an equivalent observation.

## Value

PASS. The result completely determines the newly introduced invariant on a broad canonical metric class. More importantly, it identifies the full chromatic profile with the cardinality spectrum of maximal independent sets, showing that the profile contains structural information not visible in the previously known threshold. The complete-multipartite specialization is immediate and explicit.

Self-review: passed. Independent audit: not yet performed.
