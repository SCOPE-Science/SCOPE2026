# All Steiner sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), nonempty partite classes \(V_1,\ldots,V_r\), and \(N=\sum_i n_i\). A nonempty set \(W\subseteq V(G)\) is a Steiner set exactly in the following cases:

\[
W=V(G),
\]

or

\[
W=V_i\quad\text{for some }i\text{ with }n_i\ge2.
\]

Therefore, if \(F_G(x)\) counts Steiner sets by cardinality, then

\[
F_G(x)=x^N+\sum_{i:n_i\ge2}x^{n_i}.
\]

Equal-sized non-singleton parts contribute separately to the corresponding coefficient. In particular, if at least one part is non-singleton, then

\[
\operatorname{st}(G)=\min\{n_i:n_i\ge2\}.
\]

The inclusion-minimal Steiner sets are exactly the non-singleton partite classes, so the upper Steiner number, defined as the maximum cardinality of an inclusion-minimal Steiner set, is

\[
\operatorname{st}^{+}(G)=\max\{n_i:n_i\ge2\}.
\]

If every part is a singleton, then \(G\) is complete, \(V(G)\) is the unique Steiner set, and both quantities equal \(N\).

## Assumptions and scope
Graphs are finite, simple, and connected. For a nonempty set \(W\), a Steiner \(W\)-tree is a tree of minimum order among trees containing every vertex of \(W\). The Steiner interval of \(W\) is the union of the vertex sets of all Steiner \(W\)-trees. A Steiner set is a set whose Steiner interval is all of \(V(G)\).

The statement concerns ordinary vertex Steiner sets. It does not concern edge-Steiner sets, strong geodetic sets, Steiner domination, or the number of distinct Steiner trees.

## Proof
Suppose first that \(W\) meets at least two partite classes. The subgraph induced by \(W\) is connected: vertices in different parts are adjacent, while two vertices in the same part can be joined through any selected vertex in a different part. Hence the induced subgraph on \(W\) has a spanning tree whose vertex set is exactly \(W\). No tree containing \(W\) can have fewer than \(|W|\) vertices, so every minimum-order Steiner \(W\)-tree has vertex set exactly \(W\). Its Steiner interval is therefore \(W\). Such a set is Steiner if and only if \(W=V(G)\).

Now suppose that \(W\subseteq V_i\) for a single part. If \(|W|=1\), the one-vertex tree is already a minimum Steiner tree, so the Steiner interval is \(W\), which is not all of \(V(G)\) because \(r\ge2\).

Assume instead that \(|W|\ge2\). Since vertices in \(V_i\) are pairwise nonadjacent, any connected subgraph containing \(W\) needs at least one vertex outside \(V_i\). Conversely, every vertex \(z\in V(G)\setminus V_i\) is adjacent to all vertices of \(W\), so the star with center \(z\) and leaf set \(W\) is a Steiner \(W\)-tree of order \(|W|+1\). Thus the minimum order is exactly \(|W|+1\), and allowing the center \(z\) to range over \(V(G)\setminus V_i\) shows that the Steiner interval is

\[
W\cup\bigl(V(G)\setminus V_i\bigr).
\]

No vertex of \(V_i\setminus W\) can occur in a minimum Steiner \(W\)-tree, because adding such a vertex would require more than \(|W|+1\) vertices. Therefore the Steiner interval equals \(V(G)\) exactly when \(W=V_i\). This requires \(n_i\ge2\).

These two cases exhaust all nonempty sets \(W\), proving the classification. The generating function follows by listing the unique full-vertex set and one Steiner set for every non-singleton part. The formulas for the minimum and upper Steiner numbers follow immediately from the inclusion-minimal members of this list.

## Verification
The accompanying `verify.py` constructs every complete multipartite graph up to order \(9\), using one nondecreasing part-size profile per isomorphism type. For every nonempty vertex subset \(W\), it independently computes the minimum size of a connected vertex superset containing \(W\), unions all minimum supersets, and thereby evaluates the literal Steiner-set definition without using the theorem's case split. It then compares every subset with the classification, compares every coefficient of \(F_G(x)\), and independently derives the lower and upper Steiner numbers from the inclusion-minimal literal Steiner sets.

This finite computation is a stress test, not a proof of the infinite statement. The proof above supplies the general argument.

## Relationship to prior work
Chartrand and Zhang introduced the Steiner number and Steiner sets in the present sense and characterized several extremal values. Tong later studied the relationship between geodetic and Steiner sets; that 2009 paper supplies the archive-age literature anchor and is classified under MSC 05C12. Hernando, Jiang, Mora, Pelayo, and Seara studied implications among Steiner, geodetic, hull, and monophonic notions; their full text proves that every Steiner set is monophonic and, for distance-hereditary graphs, geodetic, but it does not state a complete-multipartite Steiner-set classification.

A later paper of Gnanasekar gives the Steiner number of a complete bipartite graph. Its inspected proof also analyzes the one-side and two-side cases underlying that special family. Accordingly, the complete-bipartite scalar formula is prior-covered and is not claimed as new here. The retained contribution is the exact all-set classification for arbitrary complete multipartite graphs, together with its cardinality generating function and the simultaneous lower/upper consequences.

## Limitations
The result is restricted to connected complete multipartite graphs. It does not assert a new result for the complete-bipartite scalar Steiner number, and it does not count the multiplicity of Steiner trees for a fixed terminal set. The searches and source inspections recorded with this result reduce, but cannot eliminate, the possibility that an older source states the same arbitrary-multipartite all-set classification under different terminology.

## References
G. Chartrand and P. Zhang, “The Steiner number of a graph,” Discrete Mathematics 242 (2002), 41–54. DOI: 10.1016/S0012-365X(00)00456-8.

C. Hernando, T. Jiang, M. Mora, I. M. Pelayo, and C. Seara, “On the Steiner, geodetic and hull numbers of graphs,” Discrete Mathematics 293 (2005), 139–154. DOI: 10.1016/j.disc.2004.08.039.

L.-D. Tong, “Geodetic sets and Steiner sets in graphs,” Discrete Mathematics 309 (2009), 4205–4207. DOI: 10.1016/j.disc.2008.10.010.

M. Gnanasekar, “The Sharpe Bound Steiner Number in Some Classes of Graphs,” International Journal of Advanced Research in Engineering and Technology 8(5) (2017), 62–72.
