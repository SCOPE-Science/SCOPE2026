# Local outer multiset dimension of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge 2\), with partite sets \(V_1,\ldots,V_r\). Relabel the positive part sizes so that
\[
1\le n_1\le n_2\le\cdots\le n_r,
\qquad
N=\sum_{i=1}^r n_i.
\]
For \(W\subseteq V(G)\), put \(a_i=|W\cap V_i|\) and call part \(i\) active when \(a_i<n_i\), equivalently when \(V_i\setminus W\neq\varnothing\).

Then \(W\) is a local outer multiset resolving set if and only if the occupancies \(a_i\) are pairwise distinct over the active parts.

Define
\[
\mathcal K=\left\{k\in\{1,\ldots,r\}: n_{r-k+j}\ge j\text{ for every }j=1,\ldots,k}\right\}.
\]
Then
\[
\operatorname{lodim}(G)
=
\min_{k\in\mathcal K}
\left(
N-\sum_{i=r-k+1}^r n_i+\binom{k}{2}
\right)
=
N-\max_{k\in\mathcal K}
\left(
\sum_{i=r-k+1}^r n_i-\binom{k}{2}
\right).
\]
The set \(\mathcal K\) is nonempty because \(1\in\mathcal K\).

## Assumptions and scope
Graphs are finite, connected, simple, and undirected. A representation multiset of a vertex \(x\) with respect to \(W\) is the multiset of distances from \(x\) to the vertices of \(W\). A set \(W\) is local outer multiset resolving when every adjacent pair of vertices in \(V(G)\setminus W\) has distinct representation multisets. The parameter \(\operatorname{lodim}(G)\) is the minimum cardinality of such a set.

All part sizes are positive and \(r\ge2\), so the complete multipartite graph is connected. The theorem covers complete graphs, complete bipartite graphs, Turán graphs, and arbitrary unequal complete multipartite graphs.

## Proof
Fix \(W\subseteq V(G)\), and write \(a_i=|W\cap V_i|\). If \(x\in V_i\setminus W\), then every vertex of \(W\cap V_i\) is at distance \(2\) from \(x\), while every vertex of \(W\setminus V_i\) is at distance \(1\). Hence the representation multiset of \(x\) is
\[
m(x\mid W)=\left\{1^{|W|-a_i},2^{a_i}\right\}.
\]
Thus all vertices outside \(W\) in the same part have the same representation, and for two distinct parts \(i\neq j\) containing outside vertices, the representations agree exactly when \(a_i=a_j\). Vertices in distinct parts are adjacent. Therefore \(W\) is local outer multiset resolving exactly when the occupancies of the active parts are pairwise distinct.

Now fix an active set \(A\) of \(k\) parts. For \(i\in A\), activity means \(0\le a_i\le n_i-1\), and the \(k\) values \(a_i\) must be distinct. Consequently
\[
\sum_{i\in A}a_i\ge0+1+\cdots+(k-1)=\binom{k}{2}.
\]
Let the sizes of the active parts, in nondecreasing order, be \(m_1\le\cdots\le m_k\). Equality is attainable exactly when
\[
m_j\ge j\qquad(j=1,\ldots,k).
\]
Indeed, if this condition holds, assign occupancies \(0,1,\ldots,k-1\) in the same order. Conversely, among the first \(j\) active parts every occupancy must lie in \(\{0,1,\ldots,m_j-1\}\); \(j\) distinct values cannot fit there unless \(m_j\ge j\).

Every inactive part is entirely contained in \(W\). Therefore, for a feasible active set \(A\) of size \(k\), the least possible size of \(W\) is
\[
N-\sum_{i\in A}n_i+\binom{k}{2}.
\]
For fixed \(k\), if any active set is feasible, then the \(k\) largest parts are feasible: their ordered sizes dominate the ordered sizes of any other \(k\)-subset. They also maximize the removed total \(\sum_{i\in A}n_i\). Hence the optimum for that \(k\) uses the \(k\) largest parts. Feasibility is precisely
\[
n_{r-k+j}\ge j\qquad(j=1,\ldots,k),
\]
which gives the stated minimization and maximization formulas.

For \(r=2\), taking one active part with occupancy \(0\) gives \(\operatorname{lodim}(G)=1\), in agreement with the general bipartite boundary. If every part has size \(1\), only \(k=1\) is feasible and the formula gives \(\operatorname{lodim}(K_r)=r-1\).

## Verification
A standalone verifier reconstructs every complete multipartite graph from its part sizes, computes all-pairs shortest-path distances, enumerates every subset \(W\), checks the local outer multiset condition directly from the defining distance multisets, and compares the direct optimum with the closed formula. The exhaustive test covers all complete multipartite isomorphism types through order \(11\): \(183\) graph types and \(177556\) subsets. It returns

`ALL CHECKS PASSED; multipartite_types=183; subsets=177556; max_order=11`

This finite computation is a stress test only; the universal result follows from the proof above.

## Relationship to prior work
Simanjuntak, Hasan, and Anggarawan introduced the local outer multiset dimension and established, among other basic cases, that it equals \(1\) exactly on bipartite graphs. Their paper emphasizes that determining local outer multiset dimensions for diameter-two graphs and graph joins remains broadly open. Complete multipartite graphs are iterated joins of independent sets and have diameter at most \(2\), so the present theorem gives an exact solution on a standard dense join family.

A 2026 survey records a complete-multipartite theorem for the different local multiset dimension and records local outer exact values for cycles and wheels, but does not give an arbitrary complete-multipartite local outer formula. Earlier outer multiset work concerns the stronger global requirement of distinguishing all outside vertices, not merely adjacent outside vertices; for balanced complete multipartite graphs that global parameter is \(N-1\), so it does not imply the local formula here. For example, the present result gives \(\operatorname{lodim}(K_{2,2,2})=3\), whereas the global outer multiset dimension is \(5\).

## Limitations
The theorem is specific to complete multipartite graphs. It does not determine local outer multiset dimension for arbitrary graph joins, nor does it settle the corresponding local multiset dimension beyond previously known regimes. The literature search may miss an equivalent theorem under terminology not indexed by the sources inspected; the closest same-family results found concern either the non-outer local invariant or the global outer invariant.

## References
1. R. Simanjuntak, M. A. Hasan, and M. Anggarawan, *Local (Outer) Multiset Dimensions of Graphs*, arXiv:2507.15071v1, 2025.
2. M. A. Farhan, S. Klavžar, D. Kuziak, and I. G. Yero, *Multiset resolvability parameters in graphs: A survey with new results and open problems*, arXiv:2607.10311v1, 2026.
3. R. Gil-Pons, Y. Ramírez-Cruz, R. Trujillo-Rasua, and I. G. Yero, *Distance-based vertex identification in graphs: The outer multiset dimension*, Applied Mathematics and Computation 363 (2019), 124612; arXiv:1902.03017v1.
