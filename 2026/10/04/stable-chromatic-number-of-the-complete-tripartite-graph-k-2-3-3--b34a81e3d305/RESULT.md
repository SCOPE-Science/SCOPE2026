# Stable chromatic number of the complete tripartite graph \(K_{2,3,3}\)
## Finding
For the complete tripartite graph \(K_{2,3,3}\), the stable chromatic number introduced by Koana, Oh, and Yoneda is
\[
\chi_{\mathrm{stable}}(K_{2,3,3})=6.
\]
Here a preference profile assigns each vertex a strict ranking of the available colors, a proper coloring is stable when its envy digraph is acyclic, and \(\chi_{\mathrm{stable}}(G)\) is the least \(k\) such that every preference profile admits a stable coloring with colors in \([k]\).

## Assumptions and scope
All graphs are finite, simple, and undirected.  Write the partite sets as \(A=\{a_1,a_2\}\), \(B=\{b_1,b_2,b_3\}\), and \(C=\{c_1,c_2,c_3\}\).  For the lower bound it is enough to specify rankings on \([5]\); each ranking may be extended arbitrarily to a strict ranking of the positive integers after those five colors.

The witnessing restrictions, written best to worst, are
\[
egin{array}{c|c}
a_1&5\succ2\succ4\succ3\succ1\\
a_2&4\succ5\succ2\succ3\succ1\\
b_1&2\succ1\succ3\succ4\succ5\\
b_2&1\succ5\succ4\succ3\succ2\\
b_3&3\succ1\succ2\succ5\succ4\\
c_1&3\succ5\succ2\succ4\succ1\\
c_2&5\succ2\succ4\succ3\succ1\\
c_3&1\succ4\succ5\succ3\succ2
\end{array}
\]

## Proof
For the upper bound, orient every edge from \(C\) to \(B\), every edge from \(C\) to \(A\), and every edge from \(B\) to \(A\).  This orientation is acyclic.  A vertex in \(A\) reaches only itself, a vertex in \(B\) reaches itself and the two vertices of \(A\), and a vertex in \(C\) reaches itself together with all three vertices of \(B\) and both vertices of \(A\).  Thus no vertex reaches more than six vertices.  The reachability upper bound of Koana, Oh, and Yoneda therefore gives \(\chi_{\mathrm{stable}}(K_{2,3,3})\le6\).

For the lower bound, use the displayed preference profile on \([5]\).  There are exactly \(2940\) proper maps from the eight vertices to \([5]\), including maps that use fewer than five colors.  Exhaustive evaluation of the defining envy relation shows that every one of these \(2940\) proper colorings contains a directed blocking cycle.  The file `artifacts/certificate.json` records one such cycle for every proper coloring, and `artifacts/verify.py` independently enumerates all \(5^8=390625\) color maps, reconstructs properness and envy arcs from the definitions, checks all certificate cycles, and confirms that no proper coloring has an acyclic envy digraph.  Hence this single preference profile admits no stable \(5\)-coloring, so \(\chi_{\mathrm{stable}}(K_{2,3,3})\ge6\).

Combining the two bounds proves the claim.

## Verification
Running `python3 artifacts/verify.py` from the package directory prints exactly:

`ALL CHECKS PASSED; proper_5_colorings=2940; stable_5_colorings=0; blocking_cycles=2940; orientation_max_reach=6`

The computation is exhaustive over the finite lower-bound instance; it is not sampling and it is not used to infer any statement about other complete multipartite graphs.

## Relationship to prior work
Koana, Oh, and Yoneda introduced the stable chromatic number and proved the general reachability upper bound.  Their exact elementary families are paths, cycles, and complete bipartite graphs; in particular, for \(1\le m\le n\) they prove \(\chi_{\mathrm{stable}}(K_{m,n})=m+1\).  Their appendix also gives a six-vertex triangular-prism preference profile with no stable four-coloring.  By monotonicity that prism lower bound supplies only \(5\) for suitable supergraphs and therefore does not imply the present lower bound of \(6\).  The new ingredient here is the explicit five-color obstruction on \(K_{2,3,3}\).

Within complete tripartite graphs of order at most seven, ordering the partite sets from a largest part to the others gives a reachability upper bound of at most five.  Thus \(K_{2,3,3}\) is the first part-size profile by order for which this elementary complete-tripartite upper bound can reach six, and the obstruction above shows that six is genuinely necessary.

## Limitations
The result determines one canonical complete tripartite graph only.  It does not assert a formula for arbitrary complete multipartite graphs, and the finite certificate does not supply such a formula.  The literature comparison was performed against the initiating preprint, exact alias searches, the available published-result database; very recent or unindexed independent work remains a residual originality risk.

## References
1. Tomohiro Koana, Yeeseok Oh, and Hirotaka Yoneda, *Graph Coloring with Color Preferences*, arXiv:2609.00569v1, 1 September 2026.  See the definition of stable coloring and stable chromatic number, Theorem 3.1, Proposition 3.7, and Appendix A.
