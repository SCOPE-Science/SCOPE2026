# Exact \(3,2\)-domination of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge2\), and let \(t_j=|\{i:n_i=j\}|\). For the Cody--Detore \(3,2\)-domination number, \[\gamma^3_2(G)=\begin{cases}N,&\text{if every }n_i=1,\\2,&\text{if }r=2\text{ or }t_2>0,\\3,&\text{otherwise,}\end{cases}\] where \(N=\sum_i n_i\). The minimum sets are completely classified: in the complete-graph case the unique minimum set is \(V(G)\); when \(r=2\), the minimum two-sets are exactly the cross-part pairs together with any whole part of order two; when \(r\ge3\) and \(t_2>0\), they are exactly the whole parts of order two; and in the remaining case the minimum three-sets are exactly a whole part of order three, a \(2+1\) selection across two parts, or, only when \(r=3\), a transversal meeting all three parts. Consequently the number of minimum sets is respectively \(1\), \(n_1n_2+t_2\), \(t_2\), or \[t_3+\sum_i\binom{n_i}{2}(N-n_i)+\mathbf 1_{r=3}\prod_i n_i.\]

## Assumptions and scope
The graph is finite, simple, connected, and complete multipartite with at least two nonempty parts. The invariant is the \(k,d\)-domination number introduced by Cody and Detore: a set \(D\) is \(k,d\)-dominating if every vertex outside \(D\) lies on a shortest path of length at most \(d\) that contains at least \(k-1\) vertices of \(D\). Here only \((k,d)=(3,2)\) is asserted. No statement about other parameter pairs is claimed.

## Proof
Write the partite sets as \(V_1,\ldots,V_r\), put \(d_i=|D\cap V_i|\), and fix \(v\in V_i\setminus D\). In a complete multipartite graph every geodesic of length two has its two endpoints in one part and its middle vertex in a different part. Since \(v\notin D\), a shortest path of length at most two containing \(v\) and two vertices of \(D\) must therefore have length exactly two. There are precisely two possibilities:

* \(v\) is an endpoint. Then the other endpoint belongs to \(D\cap V_i\) and the middle vertex belongs to \(D\setminus V_i\). This is possible exactly when \(d_i\ge1\) and \(|D|-d_i\ge1\).
* \(v\) is the middle vertex. Then both endpoints are vertices of \(D\) lying in a common part \(V_j\) with \(j\ne i\). This is possible exactly when \(d_j\ge2\) for some \(j\ne i\).

Thus a vertex \(v\in V_i\setminus D\) is \(3,2\)-dominated if and only if
\[
(d_i\ge1\text{ and }|D|-d_i\ge1)\quad\text{or}\quad(\exists j\ne i:\ d_j\ge2).
\]
This local criterion yields the formula and the classification.

If every part is a singleton, then the graph is complete and has no geodesic of length two. Hence no vertex outside \(D\) can be covered together with two vertices of \(D\), so \(D=V(G)\) is forced.

Assume next that \(|D|=2\). If \(r=2\), one vertex from each part satisfies the first alternative for every outside vertex; additionally, the whole of a part of order two satisfies the second alternative for every vertex in the other part. No other same-part pair works because it leaves an undominated vertex in its own part. If \(r\ge3\), a cross-part pair fails on every vertex in a third part, while a same-part pair works exactly when it is the whole of a part of order two. This proves the two-valued cases and their counts.

Finally suppose \(r\ge3\), no part has order two, and not every part is a singleton. A set consisting of two vertices from any part of order at least three and one vertex from another part is \(3,2\)-dominating, so the minimum is at most three; the preceding paragraph rules out two. A three-set has one of the profiles \(3\), \(2+1\), or \(1+1+1\). A profile \(3\) works exactly when it is the whole of a part of order three. Every profile \(2+1\) across two parts works. A profile \(1+1+1\) has no doubled part, so it works exactly when there is no fourth part, that is, when \(r=3\). Counting these disjoint types gives the displayed formula.

## Verification
A standalone verifier constructs each complete multipartite graph from its adjacency relation, explicitly enumerates every simple length-two path, retains exactly those whose endpoints are at graph distance two, and checks the original \(3,2\)-domination definition for every candidate set. It exhaustively compares the resulting minimum size and number of minimum sets with the theorem for all complete-multipartite isomorphism types of orders two through nine. The finalized replay reports:

`ALL CHECKS PASSED; multipartite_types=87; candidate_subsets=5109; max_order=9`

This finite enumeration is a stress test only. The universal statement follows from the structural proof above.

## Relationship to prior work
Cody and Detore introduced the \(k,d\)-domination number and, in Question 6.1 of their 2026 preprint, explicitly ask for \(k,d\)-invariants of classical families including complete multipartite graphs. Their paper gives general inequalities and structural properties but does not state a complete-multipartite domination formula; its full text has no occurrence of “multipartite” outside the open-question list in the rendered version inspected for this result.

Several older shortest-path invariants have close terminology but different quantifiers. Geodetic domination requires a set to be both an ordinary dominating set and a geodetic set. Strong geodetic sets fix shortest paths between selected pairs so that their union covers all vertices; the complete multipartite strong-geodetic problem has been studied extensively. These conditions neither equal nor imply the Cody--Detore requirement used here, which permits the outside vertex to be an endpoint of the witnessing bounded geodesic. General-position coloring of complete multipartite graphs has also been determined, but that is a coloring invariant rather than a domination invariant.

Targeted semantic-index and literature searches under “\(3,2\)-dominating”, “\(k,d\)-dominating”, metric-geodesic domination, complete bipartite, and complete multipartite aliases did not locate this statement or a stronger theorem implying it.

## Limitations
Only the parameter pair \((k,d)=(3,2)\) is determined. The argument uses the diameter-two geodesic structure of complete multipartite graphs and does not by itself extend to larger \(d\) or \(k\). The literature comparison is necessarily subject to terminology drift: an older equivalent statement under unrelated notation could have escaped the searches, and the initiating invariant is recent. Independent audit has not been performed.

## References
1. B. Cody and R. Detore, *Metric general position extensions of classical graph invariants and perfection*, arXiv:2601.04351, first public version 7 January 2026; Definition 1.1 and Question 6.1.
2. H. M. Nuenay and F. P. Jamil, *On Minimal Geodetic Domination in Graphs*, Discussiones Mathematicae Graph Theory 35 (2015), 403–418, DOI 10.7151/dmgt.1803.
3. V. Iršič and M. Konvalinka, *Strong geodetic problem on complete multipartite graphs*, arXiv:1806.00302.
4. U. Chandran S. V., G. Di Stefano, H. S., E. J. Thomas, and J. Tuite, *Colouring a graph with position sets*, arXiv:2408.13494.
