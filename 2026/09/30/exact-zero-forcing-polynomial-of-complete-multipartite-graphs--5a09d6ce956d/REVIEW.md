# Review of Exact zero forcing polynomial of complete multipartite graphs

## Correctness assessment
PASS. Writing \(W\) for the initially white vertices gives a complete case split. If \(|W|\ge3\), any first force can occur only when all but one white vertex lie in one part; after that force, at least two white vertices remain in that one part and no second force is possible. For \(|W|=2\), two whites in one part are stalled, while whites in distinct parts are forceable exactly when at least one of their parts contains another, blue vertex. The cases \(|W|\le1\) always succeed in a connected complete multipartite graph. Counting the admissible two-white pairs yields \(\sum_{i<j}n_i n_j-\binom{s}{2}\). Edge cases checked explicitly include complete graphs, stars, \(K_{2,2}\), and mixtures of singleton and non-singleton parts. `verify.py` exhaustively confirms all coefficients for all 58 unordered part-size types of orders 2 through 8.

## Originality assessment
PASS, best-of-knowledge. The 2018 zero-forcing-polynomial paper introduces the counting invariant and gives formulas for several families. Later complete-multipartite zero-forcing work located in the search addresses the minimum number, minimum-set density, or other forcing variants rather than the entire standard zero forcing polynomial. Targeted web searches used “zero forcing polynomial complete multipartite,” “complete bipartite zero forcing polynomial,” “zero forcing sets complete multipartite counting,” and complement-of-pairs formulations. Targeted published-finding corpus searches used “complete multipartite graph zero forcing polynomial exact coefficients,” “zero forcing sets complete multipartite complements of pairs different parts counting,” “zero forcing polynomial complete bipartite complete multipartite minimum sets,” and “complete multipartite zero forcing dense zero forcing set enumeration.” No equivalent or stronger result was returned. The closest published-finding hit was a zero-forcing-polynomial result for trees, followed by unrelated complete-multipartite work on phylogenetic rank and a different coloring polynomial.

## Value assessment
PASS. The result determines the full counting sequence of zero forcing sets for every connected complete multipartite graph, not merely the minimum size. It gives the exact number of minimum zero forcing sets, recovers the known minimum \(N-2\) outside the complete-graph case, and supplies a compact benchmark family for the zero forcing polynomial introduced specifically to study the distribution of all forcing sets.

## Closest literature
- arXiv:1801.08910 / DOI:10.1016/j.dam.2018.11.033: introduction and systematic study of the zero forcing polynomial; first public version 2018-01-26.
- DOI:10.7151/dmgt.2389: zero- and total-forcing density results including complete multipartite graphs, but not the closed standard zero forcing polynomial located here.
- published-finding corpus `2026/9/17/SCOPE002`: zero forcing polynomial order comparison for nonpath trees; different graph family and claim.
- published-finding corpus `2026/9/18/SCOPE-phylogenetic-rank-complete-multipartite-graphs--cea9c3369a96`: complete multipartite graphs, but a different invariant.

## Scientific limitations
The literature search cannot prove global novelty and may miss an unindexed or differently phrased equivalent. The theorem treats standard zero forcing only. The finite exhaustive replay is not an independent audit or formal verification.

Same-model review: passed. Independent audit: not yet performed.
