# Dual-server total domination and total dual-server domination of complete multipartite graphs
## Finding
Let \(G=K_{{n_1,\ldots,n_r}}\) be a finite connected complete multipartite graph with \(r\ge2\). Put
\[
N=\sum_{{i=1}}^r n_i,\qquad s=\min_i n_i,\qquad t=\left|\left\{{i:n_i=1\right\}}\right|.
\]
For dual-server total domination,
\[
\gamma_{{\mathrm{{dst}}}}(G)=
\begin{{cases}}
N,&r=2\text{{ and }}s=1,\\
2,&G\text{{ is not a star and }}t\ge2,\\
3,&G\text{{ is not a star, }}t\le1\text{{ and }}s\le2,\\
4,&s\ge3.
\end{{cases}}
\]
For total dual-server domination, a TDS-dominating set exists if and only if \(N\ge4\) and \(G\) is not a star. In every such case,
\[
\gamma_{{\mathrm{{tds}}}}(G)=4.
\]
Thus the complete-multipartite family has a sharp DST trichotomy \(2,3,4\) away from stars, while every admissible TDS case collapses to the universal lower bound \(4\).

## Assumptions and scope
Graphs are finite and simple. A dual-server dominating set \(S\) has an associated partition \(S=R\mathbin{{\dot\cup}}B\) such that every vertex outside \(S\) has a neighbor in \(R\) and a neighbor in \(B\). It is DST-dominating when \(G[S]\) has no isolated vertex. It is TDS-dominating when both \(G[R]\) and \(G[B]\) have no isolated vertex. The theorem concerns connected complete multipartite graphs with at least two parts.

A star means \(K_{{1,m}}\) with \(m\ge1\). The statement does not assign a finite value to \(\gamma_{{\mathrm{{tds}}}}\) when no TDS-dominating set exists.

## Proof
Write the partite classes as \(V_1,\ldots,V_r\). For a red-blue-white labeling associated with \(S=R\mathbin{{\dot\cup}}B\), a white vertex in \(V_i\) is dual-server dominated exactly when there is at least one red vertex and at least one blue vertex outside \(V_i\), because its neighbors are precisely the vertices in the other parts.

First consider DST domination. If \(G\) is a star, every leaf has only the center as a neighbor. A white leaf therefore cannot have both a red and a blue neighbor, so every leaf belongs to \(S\); the center also belongs to every total dominating set. Hence \(S=V(G)\) and \(\gamma_{{\mathrm{{dst}}}}(G)=N\).

Suppose now that \(G\) is not a star. A DST set of size two must consist of one red vertex \(x\) and one blue vertex \(y\). Since \(G[S]\) is isolate-free, \(x\) and \(y\) lie in distinct parts. If the part containing \(x\) contained another vertex, that vertex would be white and would have no red neighbor outside its own part; therefore the part of \(x\) is a singleton. The same argument applies to \(y\). Thus a size-two DST set exists only if \(t\ge2\). Conversely, two singleton parts, with one selected vertex red and the other blue, form a DST set. This proves the second line of the formula.

Assume \(t\le1\) and \(s\le2\). If \(s=2\), take a part \(V_i=\{x,y\}\) of order two and a vertex \(z\) in another part; color \(x\) red and \(y,z\) blue. The selected subgraph has no isolates, and every white vertex sees a red and a blue vertex outside its own part. If \(s=1\), then \(t=1\); because the graph is not a star there are at least three parts. Let \(x\) be the singleton vertex and choose \(y,z\) from two other distinct parts; coloring \(x\) red and \(y,z\) blue again gives a DST set of size three. Size two is impossible by the preceding characterization, so \(\gamma_{{\mathrm{{dst}}}}(G)=3\).

Finally suppose \(s\ge3\). Every three-vertex red-blue set has one color occurring exactly once, say a unique red vertex \(x\in V_i\). Since \(n_i\ge3\), at least one vertex of \(V_i\) is white. It has no red neighbor outside \(V_i\), so no DST set has size three. On the other hand, choose two vertices from each of two distinct parts, say \(a_1,a_2\in V_i\) and \(b_1,b_2\in V_j\), and color \(a_1,b_1\) red and \(a_2,b_2\) blue. Every white vertex sees both colors outside its part and the selected subgraph is isolate-free. Hence \(\gamma_{{\mathrm{{dst}}}}(G)=4\).

For TDS domination, each of \(G[R]\) and \(G[B]\) must be isolate-free, so \( |R|\ge2\) and \( |B|\ge2\); consequently every TDS set has at least four vertices. No star has a TDS set, because its unique center would have to belong to both color classes in order for both induced color classes to contain an edge. The complete graph \(K_3\) also has no TDS set because it has fewer than four vertices.

It remains to give four-vertex constructions in every other complete multipartite graph. If \(r=2\), nonstar means that both parts have at least two vertices; choose one red and one blue vertex from each part. If \(r\ge3\) and some part contains at least two vertices, choose \(a_1,a_2\) from that part and vertices \(b,c\) from two other parts, with \(R=\{a_1,b\}\) and \(B=\{a_2,c\}\). If every part is a singleton, then \(N\ge4\) and four distinct vertices may be split into two adjacent red vertices and two adjacent blue vertices. In each construction both color classes induce edges, and every unselected vertex has a red and a blue neighbor. Thus \(\gamma_{{\mathrm{{tds}}}}(G)=4\).

## Verification
The proof above is valid for arbitrary positive part sizes. As an independent finite stress test of the boundary cases, the accompanying verifier enumerates every nondecreasing complete-multipartite part profile of total order from \(2\) through \(8\). It then exhaustively tests every red-blue-white labeling against the definitions of DST and TDS domination and compares the exact minima with the formulas above. The recorded run checked \(58\) part profiles and enumerated \(177{,}534\) labelings for each invariant, with no discrepancy.

The finite enumeration is not used as a proof of the infinite statement; it checks implementation-independent boundary behavior such as stars, \(K_3\), complete graphs, parts of order two, and the transition to minimum part size at least three.

## Relationship to prior work
Chellali, Haynes, and Hedetniemi introduced DST and TDS domination in 2026. Their paper proves general existence statements, including that every connected nonstar graph of order at least four has a TDS set, and the universal lower bound \(\gamma_{{\mathrm{{tds}}}}\ge4\). It also explicitly gives \(\gamma_{{\mathrm{{dst}}}}(K_{{2,m}})=3\) and \(\gamma_{{\mathrm{{tds}}}}(K_{{2,m}})=4\) for \(m\ge2\), and notes \(\gamma_{{\mathrm{{dst}}}}(K_n)=2\) and \(\gamma_{{\mathrm{{tds}}}}(K_n)=4\) for \(n\ge4\). Those cases are prior coverage and are not claimed as new here.

The new content is the complete classification for arbitrary complete multipartite part profiles: the exact DST value is determined by the star condition, the number of singleton parts, and whether the smallest part has order at most two; and every admissible TDS instance attains the general lower bound four. The inspected full text of the 2026 source contains no complete-multipartite theorem and uses a complete bipartite graph only for the displayed \(K_{{2,m}}\) example. Its concluding section asks for further bounds and graph classes for these parameters.

## Limitations
The proof uses the exact neighborhood structure of complete multipartite graphs and does not extend automatically to arbitrary diameter-two graphs or to graphs obtained by deleting cross-part edges. Several individual branches of the formula, including stars, complete graphs, and the \(K_{{2,m}}\) example, follow from results already present in the initiating paper; originality is claimed only for the unified arbitrary-part classification and its remaining cases. Literature searches cannot exclude an equivalent theorem that is unindexed or published under different terminology.

## References
1. M. Chellali, T. W. Haynes, S. T. Hedetniemi, “Dual-server total domination and total dual-server domination,” Discussiones Mathematicae Graph Theory, DOI: 10.7151/dmgt.2635. Available online 27 March 2026.
2. M. Chellali, T. W. Haynes, S. T. Hedetniemi, “Dual-server domination in graphs,” Discrete Applied Mathematics 387 (2026), 251–259, DOI: 10.1016/j.dam.2026.03.017.
