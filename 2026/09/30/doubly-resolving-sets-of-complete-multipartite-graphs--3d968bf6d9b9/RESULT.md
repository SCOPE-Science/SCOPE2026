# Doubly resolving sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), with partite sets \(A_1,\ldots,A_r\), where \(|A_i|=n_i\), and let \(N=\sum_i n_i\). A set \(W\subseteq V(G)\) is doubly resolving when for every distinct \(u,v\in V(G)\) there are \(x,y\in W\) such that
\[
d(u,x)-d(v,x)\ne d(u,y)-d(v,y).
\]
Put \(m_i=|W\cap A_i|\) and \(t=|\{i:m_i>0\}|\). Then \(W\) is doubly resolving if and only if \(|W|\ge2\), every part with \(n_i\ge2\) satisfies \(m_i\ge n_i-1\), and one of the following mutually exclusive support conditions holds.

If \(t\ge3\), at most one part is disjoint from \(W\). If \(t=2\), with support \(\{i,j\}\), at most one other part exists; moreover, \(m_i<n_i\) implies \(m_j\ge2\), and \(m_j<n_j\) implies \(m_i\ge2\). If \(t=1\), then \(r=2\), the disjoint part is a singleton, and \(W\) is the entire other part, whose size is at least two.

Write \(p=|\{i:n_i\ge2\}|\) and \(s=|\{i:n_i=1\}|\). When \(p=2\), denote the two non-singleton part sizes by \(a,b\). The doubly resolving number is
\[
\psi(G)=
\begin{cases}
\max\{N-1,2\}, & p=0,\\
N-1, & p=1,\ s\in\{1,2\},\\
N-2, & p=1,\ s\ge3,\\
N-1, & p=2,\ s=0,\ \min\{a,b\}=2,\\
N-2, & p=2,\ s=0,\ \min\{a,b\}\ge3,\\
N-2, & p=2,\ s=1,\ \min\{a,b\}=2,\\
N-3, & p=2,\ s=1,\ \min\{a,b\}\ge3,\\
N-3, & p=2,\ s\ge2,\\
N-p-1, & p\ge3,\ s\ge1,\\
N-p, & p\ge3,\ s=0.
\end{cases}
\]
The number \(B(G)\) of doubly bases is also explicit:
\[
B(G)=
\begin{cases}
1, & p=0,\ N=2,\\
N, & p=0,\ N\ge3,\\
1, & p=1,\ s=1,\\
N, & p=1,\ s=2,\\
as, & p=1,\ s\ge3,\\
N, & p=2,\ s=0,\ \min\{a,b\}=2,\\
ab, & p=2,\ s=0,\ \min\{a,b\}\ge3,\\
ab+a+b, & p=2,\ s=1,\ \min\{a,b\}=2,\\
ab, & p=2,\ s=1,\ \min\{a,b\}\ge3,\\
abs, & p=2,\ s\ge2,\\
\left(\prod_{n_i\ge2}n_i\right)s, & p\ge3,\ s\ge1,\\
\prod_{n_i\ge2}n_i, & p\ge3,\ s=0.
\end{cases}
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. Thus a complete multipartite graph has at least two nonempty parts. The result concerns the ordinary vertex version of doubly resolving sets, not edge-doubly-resolving variants. The classification is for all vertex subsets, not only minimum ones.

## Proof
For vertices in the same part, all vertices outside the pair have equal distance to the two vertices. Hence, if two vertices of a non-singleton part were both omitted from \(W\), they would have identical distance differences to every member of \(W\). Therefore every doubly resolving set satisfies \(m_i\ge n_i-1\) whenever \(n_i\ge2\). Conversely, once at most one vertex is omitted from a part, a selected vertex and the unique omitted vertex of that same part are doubly resolved by the selected vertex itself and any second member of \(W\).

Now let \(u\in A_i\) and \(v\in A_j\) with \(i\ne j\). For every \(w\in W\), the value \(d(u,w)-d(v,w)\) is
\[
\begin{cases}
+1, & w\in (A_i\setminus\{u\})\cup\{v\},\\
-1, & w\in \{u\}\cup(A_j\setminus\{v\}),\\
0, & w\notin A_i\cup A_j.
\end{cases}
\]
Thus \(u,v\) are doubly resolved by \(W\) exactly when \(W\) meets at least two of these three cells.

Suppose first that \(t\ge3\). If one of \(u,v\) belongs to \(W\), then the cell containing that selected vertex and a cell from a third supported part are both met. If both are omitted, failure can occur only when both of their parts are disjoint from \(W\), because otherwise one of the \(\pm1\) cells is met and a third supported part supplies the \(0\) cell. The twin condition already forces every disjoint part to be a singleton, so the only obstruction is having two disjoint singleton parts. This is exactly the condition that at most one part be disjoint from \(W\).

Suppose next that \(t=2\), with support \(\{i,j\}\). Two parts outside the support would be singleton parts and their two vertices would see the constant difference \(0\) on all of \(W\), so at most one outside part is allowed. Consider an omitted vertex of \(A_j\) and a selected vertex \(u\in A_i\). Because no third supported part exists, the difference values are nonconstant precisely when \(A_i\) contributes another selected vertex; equivalently, \(m_i\ge2\). Interchanging \(i,j\) gives the other implication. Pairs of two omitted vertices in the two supported parts are resolved because the two supported parts contribute the two signs \(+1\) and \(-1\), while a pair involving a possible outside singleton and an omitted vertex in a supported part is resolved by the supported part and the other supported part. These observations prove the stated \(t=2\) criterion.

Finally suppose \(t=1\), with support \(A_i\). The twin condition forces every other part to be a singleton. Two such disjoint singleton parts would be unresolved, so there can be only one other part. If \(A_i\) itself had an omitted vertex, that vertex together with the omitted singleton would have constant distance difference on \(W\). Hence \(W=A_i\); and \(|W|\ge2\) is necessary and sufficient. This proves the all-set characterization.

The formulas for \(\psi(G)\) follow by maximizing the number of omitted vertices under the characterization. When \(p\ge3\), one vertex may be omitted from every non-singleton part and, if present, from exactly one singleton part. When \(p=2\), the only extra obstruction is that a supported part reduced to one selected vertex cannot face an omission in the other supported part; this produces the threshold at part size two and the displayed \(s=0,1,\ge2\) cases. When \(p=1\), two singleton parts force one additional selected vertex unless there are at least three singleton parts, in which case three supported parts are available after one singleton omission. The case \(p=0\) is the known complete-graph case. Counting which vertices are omitted in each extremal profile gives the displayed formula for \(B(G)\).

## Verification
A standalone exhaustive checker independently evaluates the definition of a doubly resolving set and compares it with the characterization above on every complete multipartite isomorphism type of orders \(2\) through \(8\). It checks all \(8{,}084\) vertex subsets of the \(58\) types, and for every type separately checks both the minimum cardinality and the number of minimum sets. The recorded run ends with `VERIFY_OK`. This finite computation corroborates the proof but is not a substitute for it.

## Relationship to prior work
Jannesari's 2021 paper studies ordinary doubly resolving sets, gives MSC2020 \(05C12\), and explicitly computes the complete-bipartite values. In particular, for \(K_{r,s}\) with \(r\le s\), it obtains the star case \(\psi(K_{1,s})=s\), the case \(\psi(K_{2,s})=r+s-1\), and \(\psi(K_{r,s})=r+s-2\) for \(r\ge3\). Those bipartite values are prior work and are recovered by the formula above. A later paper on lexicographic products can cover product-structured subclasses, so no novelty is claimed merely for any balanced instance that follows from such a product theorem. The best-of-knowledge contribution here is the arbitrary complete-multipartite all-set characterization, the resulting full piecewise formula across arbitrary part sizes and singleton counts, and the exact count of minimum doubly resolving sets.

## Limitations
The originality assessment is best-of-knowledge rather than an exhaustive proof of absence from all literature. A later lexicographic-product result may overlap balanced product-structured subclasses, so those subclasses are conservatively excluded from the novelty emphasis. The result does not address edge versions, weighted variants, directed graphs, disconnected graphs, or inclusion-minimal nonminimum families beyond the all-set characterization itself. Independent audit, proof-assistant verification, and expert attestation have not been performed.

## References
1. M. Jannesari, *On minimal doubly resolving sets in graphs*, arXiv:2106.03080v1, 6 June 2021. The source lists AMS/MSC2020 \(05C12\) and contains the complete-bipartite theorem.
2. J. Cáceres, C. Hernando, M. Mora, I. M. Pelayo, M. L. Puertas, C. Seara, and D. R. Wood, *On the metric dimension of Cartesian products of graphs*, SIAM Journal on Discrete Mathematics 21 (2007), 423–441. This work introduced doubly resolving sets in the Cartesian-product context.
3. M. Jannesari, *The doubly resolving number of the lexicographic product of graphs*, Discrete Mathematics, Algorithms and Applications, DOI 10.1142/S1793830925500892 (2025). This later product result was checked for stronger or equivalent coverage.
