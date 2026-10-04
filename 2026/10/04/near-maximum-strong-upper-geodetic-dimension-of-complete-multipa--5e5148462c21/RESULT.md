# Near-maximum strong upper geodetic dimension of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph of order \(N\). Its strong upper geodetic number satisfies \(\operatorname{sg}^+(G)=N\) exactly when \(G\) is complete. If \(G\) is not complete, then \(\operatorname{sg}^+(G)=N-1\) exactly for the following four, mutually nonredundant families of part-size multisets: \(\{1,m\}\) with \(m\ge2\); \(\{2,m\}\) with \(m\ge2\); \(\{2,1^t\}\) with \(t\ge2\); and \(\{2,2,1^t\}\) with \(t\ge1\). For every other connected complete multipartite graph, \(\operatorname{sg}^+(G)\le N-2\). Moreover the number of minimal strong geodetic sets of size \(N-1\) is respectively: \(1\) for \(K_{1,m}\); \(m\) for \(K_{2,m}\) when \(m\ge3\) and \(4\) for \(K_{2,2}\); \(t\) for \(K_{2,1^t}\) with \(t\ge2\); and \(5\) for \(K_{2,2,1}\) while it is \(4\) for \(K_{2,2,1^t}\) with \(t\ge2\).

## Assumptions and scope
All graphs are finite and simple. Let \(G=K_{n_1,\ldots,n_r}\) be connected, so \(r\ge2\), with partite classes \(X_1,\ldots,X_r\) and order \(N=\sum_i n_i\). A strong geodetic set \(S\) is a vertex set for which one shortest path can be fixed for every pair of vertices of \(S\) so that the union of the selected paths covers all vertices. A strong geodetic set is minimal when no proper subset is strong geodetic. The strong upper geodetic number \(\operatorname{sg}^+(G)\) is the maximum size of a minimal strong geodetic set.

## Proof
In a complete multipartite graph, a shortest path between selected vertices from different parts is their edge and has no internal vertex. A selected pair from the same part has distance two, and its fixed geodesic can have any one vertex outside that part as its internal vertex. Therefore omitted vertices can be covered exactly by assigning each omitted vertex to a distinct selected same-part pair lying in a different part.

The full vertex set \(V(G)\) is always strong geodetic. It is minimal exactly when deleting any vertex destroys strong geodeticity. If every part is a singleton, this is the complete graph and deleting one vertex leaves no selected same-part pair, so \(V(G)\) is minimal and \(\operatorname{sg}^+(G)=N\). Conversely, if some part has at least two vertices, deleting a vertex from another part leaves a selected same-part pair that covers the deletion; if there is only one non-singleton part, connectedness supplies such another part. Hence the full set is not minimal. Thus noncomplete complete multipartite graphs satisfy \(\operatorname{sg}^+(G)\le N-1\).

Now suppose \(S=V(G)\setminus\{x\}\) is a minimal strong geodetic set, with \(x\in X_i\). Since \(S\) is strong geodetic, some other part contains a selected pair.

First assume \(n_i\ge2\). Removing a second vertex from \(X_i\) creates two omitted vertices in the same part. They can be covered exactly when there are at least two selected same-part pairs outside \(X_i\). Minimality therefore forces the number of such outside pairs to be exactly one. Hence exactly one other part has size two and every remaining outside part is a singleton. If no singleton part exists, this gives \(K_{2,m}\) with \(m=n_i\ge2\). If a singleton part exists, deleting such a singleton from \(S\) would still be coverable whenever \(n_i\ge3\), because the size-two part supplies one pair and the selected vertices remaining in \(X_i\) supply another. Thus minimality forces \(n_i=2\), giving \(K_{2,2,1^t}\) with \(t\ge1\).

Next assume \(n_i=1\). If another singleton vertex \(y\) exists, then after deleting \(y\) the two omitted singleton vertices are coverable exactly when at least two selected same-part pairs remain. Minimality therefore forces exactly one selected pair in total, which means the only non-singleton part has size two. This gives \(K_{2,1^t}\) with \(t\ge2\).

It remains to consider the case in which \(x\) is the unique singleton part. If there is exactly one non-singleton part, deleting any vertex from that part leaves the omitted vertex in that same part with no pair outside it, so every \(K_{1,m}\), \(m\ge2\), occurs. If there are at least two non-singleton parts, let their sizes be \(a,b,\ldots\). After deleting a vertex from a non-singleton part \(X_j\), the two omitted vertices lie in different parts. For the new set to fail strong geodeticity for every such deletion, the available selected-pair count after each deletion must be at most one outside the relevant obstruction. With two non-singleton parts this forces
\[
\binom{a-1}2+\binom b2\le1
\quad\text{and}\quad
\binom a2+\binom{b-1}2\le1,
\]
hence \(a=b=2\). Three or more non-singleton parts already leave at least two selected pairs after any one deletion, contradicting minimality. Thus the only remaining family is \(K_{2,2,1}\), already contained in \(K_{2,2,1^t}\).

This proves the four-family classification of size-\(N-1\) minimal strong geodetic sets. Every strong geodetic set contains a minimal strong geodetic subset, so when neither \(N\) nor \(N-1\) is attained by a minimal set, the strong upper geodetic number is at most \(N-2\).

The counts follow directly from which vertex may be omitted. In \(K_{1,m}\), only the singleton may be omitted. In \(K_{2,m}\) with \(m\ge3\), exactly one of the \(m\) vertices in the larger part may be omitted; in \(K_{2,2}\), any one of the four vertices may be omitted. In \(K_{2,1^t}\), exactly one singleton may be omitted, giving \(t\) choices. In \(K_{2,2,1}\), either the singleton or one of the four vertices in the size-two parts may be omitted, giving five choices. When \(t\ge2\) in \(K_{2,2,1^t}\), omitting a singleton is not minimal because a second singleton can also be deleted while two selected same-part pairs remain, so only the four vertices in the two size-two parts can be omitted.

## Verification
The included checker uses the strong-geodetic definition specialized only through the actual shortest paths of a complete multipartite graph. For each candidate set it forms every selected same-part pair, treats that pair as a one-use length-two geodesic resource, and computes a bipartite matching from omitted vertices to resources in different parts. It then tests minimality by deleting each selected vertex in turn.

All connected complete multipartite isomorphism types through order ten are checked exhaustively, including every vertex subset. The checker compares the computed strong upper geodetic number against the complete-graph case, the four \(N-1\) families, and the asserted \(N-2\) upper bound elsewhere; it also checks every stated count of maximum size-\(N-1\) minimal sets.

## Relationship to prior work
The 2021 paper introducing the strong upper geodetic number defines it as the maximum size of a minimal strong geodetic set, proves general complexity and structural results, and records the general equivalence \(\operatorname{sg}(G)=N\) if and only if \(\operatorname{sg}^+(G)=N\). Its full text contains no complete-multipartite treatment.

The 2018 work on the strong geodetic problem gives the optimization framework for complete bipartite graphs and studies minimum strong geodetic sets on complete multipartite graphs. Those results explain the shortest-path resource structure used here but optimize the minimum size, not the maximum cardinality of a minimal strong geodetic set.

A separate exact result for complete bipartite graphs gives \(\operatorname{sg}^+(K_{a,b})=b\) for nontrivial stars and \(b+1\) for \(2\le a\le b\). Accordingly, the present theorem does not claim the bipartite subfamilies \(K_{1,m}\) and \(K_{2,m}\) as new in isolation. The new statement is the exact near-maximum classification across all complete multipartite graphs, including the additional multipartite families and the proof that every other multipartite type drops to at most \(N-2\).

## Limitations
The theorem classifies only the top two possible values \(N\) and \(N-1\); it does not give \(\operatorname{sg}^+(G)\) exactly for every remaining multipartite graph. The finite computation through order ten is corroborative only; the all-orders threshold theorem follows from the proof. Search coverage cannot exclude a differently phrased or non-indexed prior classification of the same near-maximum multipartite boundary.

## References
1. L. G. Bino Infanta, D. Antony Xavier, “Strong Upper Geodetic Number of Graphs,” Communications in Mathematics and Applications 12 (2021), 737–748, DOI 10.26713/cma.v12i3.1597.
2. V. Iršič, M. Konvalinka, “Strong geodetic problem on complete multipartite graphs,” Ars Mathematica Contemporanea 17 (2019), 481–491, arXiv:1806.00302v1, DOI 10.26493/1855-3974.1725.2e5.
