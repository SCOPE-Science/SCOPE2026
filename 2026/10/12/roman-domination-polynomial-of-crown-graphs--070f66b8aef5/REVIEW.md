# Review

## Correctness
**PASS.** The proof reduces the Roman condition to an exact sidewise rule determined by the number and indices of vertices labeled \(2\). The seven regimes for \((p,q)\) are disjoint and exhaustive. Each polynomial term is derived from those rules, and the minimum-weight conclusion follows from the same partition. The packaged direct checker exhaustively verifies all labelings for \(3\le n\le6\) and matches every coefficient. The finite replay supports the proof but is not used to infer the theorem for arbitrary order.

## Originality
**PASS.** The closest same-invariant source introduces the Roman domination polynomial and gives a complete-bipartite formula, but a crown graph deletes a perfect matching and therefore has index-sensitive exceptional nonneighbors absent from \(K_{n,m}\). Full-text inspection found no crown treatment in that source. Searches using crown, deleted-perfect-matching, one-factor-deleted, and \(K_{n,n}-M_n\) formulations located no equivalent ordinary Roman-domination polynomial. The closest crown-graph record found concerns restrained domination, which neither states nor implies the all-weight Roman-function formula. Residual risk remains for poorly indexed literature under another graph-family name.

## Value
**PASS.** Crown graphs are a standard structured bipartite family, and the theorem gives the complete weight distribution rather than only a minimum parameter. The formula isolates exactly how one deleted perfect matching changes Roman feasibility from complete bipartite graphs: a unique opposite-side defender creates one exceptional matched vertex. The result supplies both a natural benchmark polynomial and the exact multiplicity of minimum functions.

## Closest literature and limitations
The foundational Roman-domination paper supplies the invariant. The Roman-domination-polynomial paper supplies the polynomial framework and the complete-bipartite comparison. The result here is limited to connected crown graphs and does not assert literature-wide uniqueness; synonym and indexing risk remains.

Self-review: passed. Independent audit: not yet performed.
