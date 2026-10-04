# Mobile general position of \(L(K_{1,1,n})\)

## Finding

For every integer \(n\ge 2\), let \(H_n=L(K_{1,1,n})\). Then
\[
H_n\cong K_1\vee (K_n\square K_2),
\qquad
\operatorname{Mob}_{\mathrm{gp}}(H_n)=n,
\qquad
\operatorname{gp}(H_n)=n+1.
\]
Thus this infinite line-graph family has mobile general position number exactly one below its ordinary general position number.

## Assumptions and scope

Graphs are finite, simple, undirected, and connected. A set \(S\subseteq V(G)\) is in general position if no vertex of \(S\) lies on a shortest path between two other vertices of \(S\). A legal move sends one robot from its occupied vertex to an adjacent unoccupied vertex while leaving the occupied set in general position. A mobile general position set admits a finite sequence of legal moves during which every vertex of the graph is visited. The maximum size of such a set is \(\operatorname{Mob}_{\mathrm{gp}}(G)\).

Write the two singleton parts of \(K_{1,1,n}\) as \(\{a\}\) and \(\{b\}\), and its \(n\)-vertex part as \(\{c_1,\ldots,c_n\}\). In the line graph, let \(x\) denote the vertex corresponding to \(ab\), let \(a_i\) correspond to \(ac_i\), and let \(b_i\) correspond to \(bc_i\). Then \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\) are cliques, \(a_i b_i\) is an edge for every \(i\), there are no other edges between \(A\) and \(B\), and \(x\) is universal. Hence
\[
H_n\cong K_1\vee (K_n\square K_2).
\]

A useful elementary fact is that in a graph of diameter at most two, a vertex set is in general position if and only if every connected component of its induced subgraph is a clique. Indeed, a connected nonclique component contains an induced three-vertex path along a shortest path inside the component; its endpoints have graph distance two, so the middle vertex violates general position. Conversely, if the induced components are cliques, vertices in one component are at distance one, while vertices in different components are at distance two and cannot have an occupied common neighbor without joining the two components.

## Proof

First determine the ordinary general position number.

Consider a general position set \(S\subseteq A\cup B\), so \(x\notin S\). If \(S\) contains both \(a_i\) and \(b_i\) for some \(i\), then these two vertices are in one induced component. Any additional selected vertex of \(A\) is adjacent to \(a_i\) but not to \(b_i\), and any additional selected vertex of \(B\) is adjacent to \(b_i\) but not to \(a_i\). Either case would make that induced component connected but noncomplete. Hence then \(|S|=2\). If no matched pair \(a_i,b_i\) is simultaneously selected, then \(S\cap A\) and \(S\cap B\) are two disjoint cliques whose index sets are disjoint, so \(|S|\le n\).

Now suppose \(x\in S\). Since \(x\) is universal, \(H_n[S]\) is connected, so the diameter-two criterion forces \(S\) to be a clique. The clique number of \(H_n\) is \(n+1\): the sets \(\{x\}\cup A\) and \(\{x\}\cup B\) have that size, while a clique meeting both \(A\) and \(B\) contains at most one matched pair in addition to \(x\). Therefore
\[
\operatorname{gp}(H_n)=n+1.
\]

We next prove the mobile upper bound. For \(n\ge3\), the only cliques of size \(n+1\) are \(\{x\}\cup A\) and \(\{x\}\cup B\). Consider \(\{x\}\cup A\). The only unoccupied neighbor to which a robot at \(a_i\) can move is \(b_i\); after that move the occupied induced subgraph is connected through \(x\) but is not a clique, because \(b_i\) is nonadjacent to every \(a_j\) with \(j\ne i\). If the robot at \(x\) moves to an unoccupied \(b_i\), then the occupied set is \(A\cup\{b_i\}\), again connected and noncomplete. Thus no legal move exists. The same argument applies to \(\{x\}\cup B\).

When \(n=2\), every general position set of size three is a triangle. Besides \(\{x\}\cup A\) and \(\{x\}\cup B\), the other triangles are \(\{x,a_i,b_i\}\). Each is also frozen: moving \(x\) to either unoccupied vertex, or moving \(a_i\) or \(b_i\) to its only unoccupied neighbor, produces a connected nonclique three-vertex set. Hence no general position set of size \(n+1\) is mobile for any \(n\ge2\). Therefore
\[
\operatorname{Mob}_{\mathrm{gp}}(H_n)\le n.
\]

For the matching lower bound, start with
\[
S_0=\{x\}\cup\{b_1,\ldots,b_{n-1}\},
\]
which has \(n\) vertices and is a clique. The following legal excursions, always returning to \(S_0\), visit every vertex not initially occupied.

To visit \(b_n\), move \(b_1\) to \(b_n\) and then return. The occupied set remains a clique. To visit \(a_n\), move \(x\) to \(a_n\) and then return; while \(x\) is absent, \(a_n\) is isolated from the occupied clique \(\{b_1,\ldots,b_{n-1}\}\), so the occupied set is a disjoint union of cliques. Finally, for each \(i<n\), first move \(b_i\) to \(b_n\), then move \(x\) to \(a_i\). At that stage \(a_i\) is isolated from the occupied clique \(B\setminus\{b_i\}\). Reverse the two moves to return to \(S_0\). Every intermediate occupied set is therefore in general position.

These excursions visit all of \(A\cup B\cup\{x\}\), proving
\[
\operatorname{Mob}_{\mathrm{gp}}(H_n)\ge n.
\]
Together with the upper bound, this proves the finding.

## Verification

The proof is purely structural and does not rely on finite enumeration. Its critical points are:

1. the explicit line-graph identification \(L(K_{1,1,n})\cong K_1\vee(K_n\square K_2)\);
2. the diameter-two characterization of general position sets as induced disjoint unions of cliques;
3. the complete classification needed for sets of size \(n+1\), including the exceptional triangle forms when \(n=2\);
4. an explicit reversible move sequence from \(S_0\) that visits every vertex with exactly \(n\) robots.

The \(n=2\) case is treated separately in the upper-bound argument, so the proof does not silently assume that the only maximum cliques are the two \((n+1)\)-cliques coming from the prism layers.

## Relationship to prior work

Klavžar, Krishnakumar, Tuite, and Yero introduced mobile general position and determined \(\operatorname{Mob}_{\mathrm{gp}}(L(K_m))=m-2\) for complete-graph line graphs. Their concluding problems explicitly ask for the mobile general position number of arbitrary line graphs. The family here is a different infinite line-graph family, coming from complete tripartite graphs \(K_{1,1,n}\).

Klavžar, Krishnakumar, Kuziak, Shallcross, Tuite, and Yero later proved \(\operatorname{Mob}_{\mathrm{gp}}(K_n\square K_2)=n\) and general bounds for joins with a universal vertex. Since \(H_n\) is obtained by adding a universal vertex to \(K_n\square K_2\), those results locate the present family naturally but do not determine the exact value for \(H_n\). The present argument shows that adding this universal vertex leaves the mobile number at \(n\) while raising the ordinary general position number to \(n+1\).

## Limitations

The result concerns only the family \(L(K_{1,1,n})\) for \(n\ge2\); it does not classify mobile general position numbers for general complete-multipartite line graphs or arbitrary line graphs. The originality assessment used targeted exact-form, alias, implication, and nearby-family searches together with full-text inspection of the most relevant primary sources. Such searches cannot rule out every uncatalogued or unpublished equivalent statement.

## References

1. S. Klavžar, A. Krishnakumar, J. Tuite, and I. G. Yero, “Traversing a graph in general position,” arXiv:2209.12631v1, 26 September 2022; published version DOI: 10.1017/S0004972723000102.
2. S. Klavžar, A. Krishnakumar, D. Kuziak, E. Shallcross, J. Tuite, and I. G. Yero, “Moving through Cartesian products, coronas and joins in general position,” arXiv:2505.00535v1; Discrete Applied Mathematics 379 (2026), 768–780, DOI: 10.1016/j.dam.2025.10.041.
