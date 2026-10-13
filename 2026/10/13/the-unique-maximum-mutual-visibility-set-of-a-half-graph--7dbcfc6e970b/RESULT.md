# The unique maximum mutual-visibility set of a half graph
## Finding
For \(n\ge3\), let \(H_n\) have bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), with \(a_i b_j\in E(H_n)\) exactly when \(i\le j\). Then
\[
\mu(H_n)=2n-2,
\]
and the unique maximum mutual-visibility set is
\[
V(H_n)\setminus\{a_1,b_n\}.
\]
Thus \(H_n\) has the same mutual-visibility number as \(K_{n,n}\), but its maximum set is unique rather than one of \(n^2\) choices.

## Assumptions and scope
For \(X\subseteq V(G)\), two vertices of \(X\) are \(X\)-visible when some shortest path joining them has no internal vertex in \(X\). A mutual-visibility set is a set whose pairs are all visible in this sense; \(\mu(G)\) is the maximum cardinality. The uniqueness theorem starts at \(n=3\); \(H_2\cong P_4\) has scalar value \(2\) but several maximum sets.

## Proof
Distinct vertices on the same side of \(H_n\) have distance \(2\). For opposite sides,
\[
d(a_i,b_j)=1\quad(i\le j),\qquad d(a_i,b_j)=3\quad(i>j).
\]
In the latter case \(a_i,b_n,a_1,b_j\) is a geodesic.

Set \(M=V(H_n)\setminus\{a_1,b_n\}\). Two selected \(A\)-vertices see each other through omitted \(b_n\); two selected \(B\)-vertices see each other through omitted \(a_1\); adjacent cross pairs need no internal vertex; and a nonadjacent selected pair \(a_i,b_j\), \(i>j\), uses the geodesic \(a_i,b_n,a_1,b_j\). Hence \(|M|=2n-2\) is feasible.

A set of size \(2n-1\) is impossible. If the sole omitted vertex is in \(A\), all \(B\)-vertices are selected. Their distance-two pairs can only be witnessed through the omitted \(A\)-vertex; even when that vertex is the universal \(a_1\), at least two \(A\)-vertices remain selected and there is no omitted \(B\)-vertex through which they can see each other. The case with the omission in \(B\) is symmetric. Thus \(\mu(H_n)=2n-2\).

For uniqueness, let \(X\) have size \(2n-2\) and write \(T=V(H_n)\setminus X\). If \(n\ge4\) and \(T\) lies in one side, at least two selected vertices remain on that side and every internal vertex of their length-two geodesics lies in the fully selected opposite side, impossible. For \(n=3\), if \(T\subseteq A\), visibility of \(b_1,b_2\) forces \(a_1\in T\); the remaining selected \(A\)-vertex is then nonadjacent to \(b_1\), and every length-three geodesic to \(b_1\) has an internal selected \(B\)-vertex. The other side is symmetric. Hence \(T=\{a_p,b_q\}\).

Let \(a_r\) be the selected \(A\)-vertex of largest index. Since \(n-1\ge2\), a selected same-side pair containing \(a_r\) must use the only omitted \(B\)-vertex \(b_q\), so \(r\le q\). Thus if \(p\ne n\), then \(q=n\); if \(p=n\), then \(q\ge n-1\). Dually, if \(b_s\) is the selected \(B\)-vertex of smallest index, then the only omitted \(A\)-vertex must satisfy \(p\le s\). Thus if \(q\ne1\), then \(p=1\); if \(q=1\), then \(p\le2\). The alternatives \(p=n\) and \(q=1\) contradict these paired inequalities for \(n\ge3\). Therefore \(p=1\) and \(q=n\), proving uniqueness.

## Verification
The included checker constructs \(H_n\) for \(3\le n\le10\), computes graph distances, and tests mutual visibility directly by blocking every other selected vertex while searching for a shortest path. It checks every set of sizes \(2n-1\) and \(2n-2\): all former fail and exactly \(V(H_n)\setminus\{a_1,b_n\}\) succeeds at the latter size.

## Relationship to prior work
Mutual visibility was introduced in 2021. The introducing paper proves \(\mu(K_{m,n})=m+n-2\) for \(m,n\ge3\), so in particular \(\mu(K_{n,n})=2n-2\); its construction yields \(n^2\) maximum sets in the balanced case. Its full text has no half-graph or chain-graph specialization.

A 2023 paper gives a linear-time algorithm for maximum mutual visibility on distance-hereditary graphs. Half graphs are distance-hereditary, so this is genuine broader computational coverage of the scalar optimization problem, but the paper does not state the half-graph formula or classify all maximum sets. A 2025 visibility-polynomial paper gives a generic exhaustive enumeration algorithm, again without a half-graph or chain-graph formula. The new point here is the closed all-orders formula together with uniqueness: Ferrers nesting preserves the complete-bipartite optimum size while collapsing maximum-set multiplicity from \(n^2\) to \(1\).

## Limitations
The theorem concerns canonical half graphs, not arbitrary chain graphs with repeated neighborhood classes. The computation through \(n=10\) is corroborative only. Generic algorithms can compute individual instances; the contribution is the explicit formula and uniqueness classification.

## References
1. G. Di Stefano, “Mutual Visibility in Graphs,” arXiv:2105.02722v1, 6 May 2021; Applied Mathematics and Computation 419 (2022), 126850.
2. S. Cicerone and G. Di Stefano, “Mutual-visibility in distance-hereditary graphs: a linear-time algorithm,” arXiv:2307.10661v1, 20 July 2023.
3. Tonny K. B. and Shikhi M., “On the Visibility Polynomial of Graphs,” arXiv:2507.01851v1, 2 July 2025.
