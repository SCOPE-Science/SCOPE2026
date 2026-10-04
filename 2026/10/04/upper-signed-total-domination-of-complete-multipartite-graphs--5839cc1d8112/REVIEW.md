# Review: Upper signed total domination of complete multipartite graphs

## Correctness
PASS. The proof derives the exact parity threshold for every open-neighborhood sum, establishes the minimality criterion by analyzing the effect of a \(+1\)-to-\(-1\) flip, proves all three pairwise upper bounds, isolates the unique-tight case, and gives an explicit attainment argument. The standalone verifier checks the literal definitions and formula exhaustively through order \(10\), with a stronger all-lower-functions minimality check through order \(7\).

## Originality
PASS. The foundational upper-parameter paper gives general bounds; Liang's complete-multipartite paper computes the minimum signed total domination number; and the nearest own-ledger result is the closed-neighborhood upper signed domination number. Targeted published-finding corpus and literature searches found no statement implying the exact pairwise parity formula or the minimality classification. The principal residual risk is inaccessible older full text under alternate terminology.

## Value
PASS. This determines a natural established upper domination invariant on the full complete-multipartite family and explains minimality structurally. The parity-sensitive pair bottleneck is not obtained by substituting into the known minimum formula, and the result simultaneously covers cliques, complete bipartite graphs, and arbitrary multipartite profiles.

## Closest literature and limitations
Henning (2004) defines the same upper parameter and proves general bounds. Liang (2012) treats complete multipartite graphs but minimizes signed total domination weight. Shan and Cheng (2009) provide general upper bounds. Full text for the two upper-parameter journal papers was not available from the accessible open sources, so that comparison limitation is retained explicitly.

Same-model review: passed. Independent audit: not yet performed.
