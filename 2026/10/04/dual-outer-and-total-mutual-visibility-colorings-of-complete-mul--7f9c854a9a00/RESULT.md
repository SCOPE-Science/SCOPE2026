# Dual, outer, and total mutual-visibility colorings of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph, where \(r\ge2\). Then the outer mutual-visibility chromatic number satisfies \(\chi_{\mu_o}(G)=1\) exactly when \(G\) is complete, and \(\chi_{\mu_o}(G)=2\) otherwise.

For the dual parameter,
\[
\chi_{\mu_d}(G)=
\begin{cases}
1,&G\text{ is complete},\\
\infty,&G\cong K_{1,n}\text{ with }n\ge3,\\
2,&\text{otherwise}.
\end{cases}
\]
For the total parameter,
\[
\chi_{\mu_t}(G)=
\begin{cases}
1,&G\text{ is complete},\\
\infty,&G\cong K_{1,n}\text{ with }n\ge2,\\
2,&\text{otherwise}.
\end{cases}
\]
Thus \(K_{1,2}\) is the sharp point at which dual and total mutual-visibility colorability separate inside the complete multipartite family.

## Assumptions and scope
A set \(M\subseteq V(G)\) makes two vertices \(x,y\) \(M\)-visible when some shortest \(x,y\)-path has no internal vertex in \(M\). An outer mutual-visibility set requires the ordinary mutual-visibility condition on pairs in \(M\) together with visibility for cross pairs; a dual set requires it on pairs in \(M\) and pairs in \(V(G)\setminus M\); a total set requires it for every vertex pair. The corresponding chromatic number is the minimum number of such sets partitioning \(V(G)\), with value \(\infty\) when no such partition exists.

The claim concerns finite connected complete multipartite graphs only. Write their independent parts as \(V_1,\ldots,V_r\), and put \(B=V(G)\setminus M\).

## Proof
Vertices in different parts are adjacent, so they are automatically \(M\)-visible. If \(x,y\in V_i\) are distinct, then every shortest \(x,y\)-path has length two and its internal vertex may be any vertex outside \(V_i\). Consequently,
\[
x,y\text{ are }M\text{-visible}\quad\Longleftrightarrow\quad B\setminus V_i\ne\varnothing.
\]
This one observation gives all three set criteria.

For a total set \(M\), every same-part pair must be visible. Hence \(M\) is total exactly when \(B\setminus V_i\ne\varnothing\) for every part \(V_i\) of size at least two.

For a dual set \(M\), the same condition is needed precisely for those parts \(V_i\) having either at least two vertices in \(M\) or at least two vertices in \(B\). In particular, if \(B\) meets at least two parts, then \(M\) is dual. If nonempty \(B\) is contained in a single part \(V_i\), then \(M\) is dual exactly when both \(|M\cap V_i|\le1\) and \(|B\cap V_i|\le1\). If \(B=\varnothing\), duality holds exactly when every part is a singleton.

For an outer set \(M\), the condition is needed precisely when a part contains either two vertices of \(M\), or one vertex of \(M\) and one of \(B\). Thus, if \(B\) meets at least two parts, then \(M\) is outer. If nonempty \(B\subseteq V_i\), then \(M\) is outer exactly when \(B=V_i\). If \(B=\varnothing\), the whole vertex set is outer exactly when \(G\) is complete.

The outer formula follows immediately. A noncomplete graph cannot use one color, while the two sets \(V_1\) and \(V(G)\setminus V_1\), for any part \(V_1\), are both outer.

For dual coloring, suppose first that \(G\) is not a star with at least three leaves. If two parts have size at least two, split each of those two parts nontrivially between two colors. If exactly one part has size at least two and \(r\ge3\), split that part and assign two singleton parts to opposite colors. In either construction, each color class and its complement meet at least two parts, so both color classes are dual. The remaining noncomplete exception \(K_{1,2}\) is dual-two-colorable by the partition \(\{c,\ell_1\}\), \(\{\ell_2\}\), where \(c\) is the center. On the other hand, in \(K_{1,n}\) with \(n\ge3\), no dual set can contain the center: if it contains at least two leaves, those two leaves are blocked by the center, while if it contains at most one leaf, at least two leaves lie outside and are again blocked by the center. Hence no dual coloring exists.

For total coloring, the same two-color constructions work whenever the graph is noncomplete and not a star: the complement of each color class meets at least two parts, so it contains a vertex outside every non-singleton part. In \(K_{1,n}\) with \(n\ge2\), no total set can contain the center, because any two leaves have the center as the unique internal vertex of their geodesic. Therefore no total coloring exists for these stars. Complete graphs have value one for all three parameters.

## Verification
A self-contained exact verifier reconstructs the graph from its part sizes, computes graph distances and shortest paths, tests the three visibility-set definitions directly, exhaustively searches colorings, and compares the computed values with the formulas above. It checks every nondecreasing part-size profile with between two and four parts, each part of size at most four, and total order at most eight. The recorded run reports:

`ALL CHECKS PASSED; profiles=34; parameter_cases=102; max_order=8`

This finite computation is a boundary and implementation check only; the infinite family statement is proved by the argument above.

## Relationship to prior work
Babu, Jakovac, Kuziak, Lakshmanan S., and Yero introduced the dual, outer, and total mutual-visibility chromatic numbers in 2026. Their paper gives general finiteness criteria, proves that total colorability is impossible exactly when a vertex is the center of a convex \(P_3\), gives sufficient obstructions for dual colorability, and determines the parameters on several graph classes. It also asks for further structural characterizations, including the infinite dual case. The complete multipartite family is not treated there.

The total-star obstruction above is therefore an instance of their general total-colorability theorem, and the one-color lower bound for noncomplete graphs in the outer case is also prior coverage. The new content is the exact complete-multipartite classification, especially the dual criterion and the sharp distinction between \(K_{1,2}\) and larger stars, together with uniform two-color constructions for every remaining noncomplete complete multipartite graph.

Earlier work on mutual-visibility sets in diameter-two graphs determines maximum set sizes for cographs and related families. Those results concern extremal cardinalities of individual visibility sets, not partitions of the vertex set into visibility classes, so they do not imply these chromatic formulas.

## Limitations
The proof is specific to complete multipartite graphs and relies on the fact that every nonedge lies inside a part and has every outside vertex as a common neighbor. It does not classify arbitrary diameter-two graphs, arbitrary cographs, or all graphs with finite dual or total mutual-visibility chromatic number. The literature search cannot exclude unpublished or newly posted equivalent results not yet indexed.

## References
1. S. Babu, M. Jakovac, D. Kuziak, A. Lakshmanan S., I. G. Yero, “A variety of the mutual-visibility coloring problem for graphs,” arXiv:2609.31427v1, 2026. https://arxiv.org/abs/2609.31427
2. S. Cicerone, G. Di Stefano, S. Klavžar, I. G. Yero, “Mutual-visibility problems on graphs of diameter two,” European Journal of Combinatorics 120 (2024), 103995. https://doi.org/10.1016/j.ejc.2024.103995
