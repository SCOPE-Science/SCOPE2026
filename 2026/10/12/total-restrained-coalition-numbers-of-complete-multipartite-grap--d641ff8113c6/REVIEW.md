# Review

## Correctness
**PASS.** In a complete multipartite graph, a set is total restrained dominating exactly when it meets at least two partite classes and its complement is empty or meets at least two partite classes. This equivalence follows directly from adjacency between different parts and nonadjacency inside each part. It implies that for at least three parts and order at least four, every vertex has a vertex in another part such that the two-vertex union is a TRD-set, so the singleton partition is valid. The exceptional cases \(K_3\) and \(K_{1,m}\) have the whole vertex set as their only TRD-set and therefore have coalition number \(2\). Exact exhaustive partition enumeration through order \(8\) independently matches the formula.

## Originality
**PASS.** The initiating paper states exact values for complete graphs, nonstar complete bipartite graphs, and stars, records the triangle case, and characterizes triangle-free graphs with maximum total restrained coalition number. Its full text contains no occurrence of “multipartite.” The new implication is the triangle-containing complete multipartite regime with at least three parts and at least four vertices; none of the inspected published-finding corpus records or owned-ledger claims states or implies this classification. The closest indexed published-finding corpus records concern restrained domination on chain or crown graphs and different domination variants, not total restrained coalition partitions.

## Value
**PASS.** Complete multipartite graphs are a canonical extension of the clique and biclique families already singled out in the initiating work. The theorem completes that family with a sharp two-exception classification and explains structurally why the parameter jumps to its maximum as soon as a third part is present outside the triangle boundary. This is an exact natural classification rather than an arbitrary finite slice.

## Closest literature and limitations
The closest source is Chellali et al., *Total restrained coalitions in graphs*, arXiv:2412.18623 and DOI 10.1007/s40314-025-03439-w. It supplies the invariant and the complete, biclique, star, and triangle boundary cases, plus a triangle-free maximum-value theorem. The present result does not claim those boundary statements anew. A residual originality risk is a poorly indexed equivalent complete-multipartite statement under different terminology.

Self-review: passed. Independent audit: not yet performed.
