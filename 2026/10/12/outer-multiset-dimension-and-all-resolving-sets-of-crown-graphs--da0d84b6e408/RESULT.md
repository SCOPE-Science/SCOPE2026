# Outer multiset dimension and all resolving sets of crown graphs
## Finding
For every integer \(n\ge 3\), let
\[
\operatorname{Cr}_n=K_{n,n}-M_n
\]
be the crown graph with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), where the deleted perfect matching is \(M_n=\{a_i b_i:1\le i\le n\}\). A set \(S\subseteq V(\operatorname{Cr}_n)\) is outer multiset resolving exactly in the following cases. Put \(X=A\setminus S\) and \(Y=B\setminus S\). Then either
\[
(|X|,|Y|)\in\{(0,0),(1,0),(0,1)\},
\]
or
\[
(|X|,|Y|)=(2,1)\text{ and }|X\cap Y|=1,
\]
or
\[
(|X|,|Y|)=(1,2)\text{ and }|X\cap Y|=1.
\]
Here the intersection is taken on the common matching-index set \(\{1,\ldots,n\}\).

Consequently,
\[
\operatorname{odim}(\operatorname{Cr}_n)=2n-3.
\]
Moreover, there are exactly \(2n(n-1)\) outer multiset bases. If
\[
R_n(z)=\sum_{S	ext{ outer multiset resolving}} z^{|S|},
\]
then the complete size distribution is
\[
R_n(z)=z^{2n}+2n z^{2n-1}+2n(n-1)z^{2n-3}.
\]
In particular, no outer multiset resolving set has size \(2n-2\).

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. For a connected graph \(G\), a set \(S\subseteq V(G)\) is outer multiset resolving when the multisets
\[
m_G(v\mid S)=\!\!\left\{\!\!\left\{d_G(v,s):s\in S\right\}\!\!\right\}
\]
are pairwise distinct for vertices \(v\in V(G)\setminus S\). The outer multiset dimension \(\operatorname{odim}(G)\) is the minimum size of such a set.

The theorem concerns \(n\ge3\). At this range \(\operatorname{Cr}_n\) is connected, \((n-1)\)-regular, and has diameter \(3\). The statement classifies every resolving set, not only minimum ones.

## Proof
Fix \(S\), write \(X=A\setminus S\), \(Y=B\setminus S\), and put \(x=|X|\), \(y=|Y|\). For an omitted vertex \(a_i\), all selected vertices of \(A\) are at distance \(2\). Among the \(n-y\) selected vertices of \(B\), every one is at distance \(1\) except \(b_i\), when it is selected, which is at distance \(3\). Hence
\[
m(a_i\mid S)=
\begin{cases}
\left\{\!\left\{1^{n-y},2^{n-x}\right\}\!\right\},&i\in Y,\\
\left\{\!\left\{1^{n-y-1},2^{n-x},3\right\}\!\right\},&i\notin Y.
\end{cases}
\]
Symmetrically, for an omitted \(b_j\),
\[
m(b_j\mid S)=
\begin{cases}
\left\{\!\left\{1^{n-x},2^{n-y}\right\}\!\right\},&j\in X,\\
\left\{\!\left\{1^{n-x-1},2^{n-y},3\right\}\!\right\},&j\notin X.
\end{cases}
\]

There are only two possible representations among omitted vertices of \(A\), according to whether the matching mate is omitted. Therefore \(x\le2\); if \(x=2\), the two omitted \(A\)-vertices are distinguished exactly when one and only one of their indices lies in \(Y\), equivalently \(|X\cap Y|=1\). The symmetric argument gives \(y\le2\), with the same intersection condition when \(y=2\).

If \(x\ne y\), every omitted \(A\)-vertex has exactly \(n-x\) entries equal to \(2\), while every omitted \(B\)-vertex has exactly \(n-y\) such entries. Thus no cross-shore collision is possible. If \(x=y=1\), the unique two omitted vertices always have equal representations: either both matching mates are omitted or both matching mates are selected. Hence \((1,1)\) is impossible. If \(x=y=2\), the within-shore conditions force \(|X\cap Y|=1\); the omitted pair indexed by \(X\cap Y\) then has the same representation on the two shores, so this case is also impossible.

Combining these facts leaves exactly the five patterns stated in the finding. For a minimum set, the complement has three vertices. In the \((2,1)\) pattern one first chooses the two omitted \(A\)-indices and then chooses the single omitted \(B\)-index from those two, giving \(2\binom{n}{2}=n(n-1)\) sets. The symmetric pattern contributes another \(n(n-1)\). The other allowed patterns give the full set and the \(2n\) sets omitting one vertex. This proves both the minimum and the enumerator.

## Verification
The standalone script `verify.py` constructs each crown graph directly, computes all-pairs graph distances by breadth-first search, enumerates every vertex subset, and compares the defining outer-multiset-resolving test with the closed structural criterion above. It checks every \(n\) from \(3\) through \(8\), including all \(87360\) subsets in aggregate, and verifies the claimed size distribution and basis count.

The computation is a finite stress test. The universal statement is established by the analytic proof, not by the finite enumeration.

## Relationship to prior work
Gil-Pons, Ramírez-Cruz, Trujillo-Rasua, and Yero introduced the outer multiset dimension. Klavžar, Kuziak, and Yero later proved that a graph of order \(N\) has outer multiset dimension \(N-1\) exactly when it is regular with diameter at most \(2\), and recorded complete multipartite examples. Their full text does not contain a crown-graph or matching-deletion treatment.

For \(K_{n,n}\), the regular diameter-two characterization gives outer multiset dimension \(2n-1\). The crown graph is obtained by deleting one perfect matching, which increases the diameter to \(3\). The theorem therefore shows that this sparse deletion lowers the outer multiset dimension by exactly two, to \(2n-3\), and it identifies every resolving set after the deletion.

Peng's recent work on toroidal grids determines the same invariant on \(C_s\square C_t\) and lists primary MSC \(05C12\). It provides the literature-led context for the present direction but does not state a crown-graph result in the accessible metadata and abstract. Exact searches under the aliases “crown graph,” “complete bipartite minus a perfect matching,” “bipartite Kneser \(H(n,1)\),” and “bipartite complement of a perfect matching” found no covering statement.

## Limitations
The theorem is specific to crown graphs with \(n\ge3\). It does not determine outer multiset dimension for arbitrary matching-deleted bicliques or for general bipartite Kneser graphs. The recent toroidal-grid paper's full text was not retrievable in this review, so its accessible abstract and metadata were used only to establish scope, date, and MSC; the same-invariant foundational and follow-up literature was inspected in full where available. An older or poorly indexed equivalent crown-graph result remains a residual originality risk.

## References
1. B. Peng, *The Outer Multiset Dimension of Toroidal Grids*, arXiv:2609.20073v1, 2026.
2. S. Klavžar, D. Kuziak, and I. G. Yero, *Further contributions on the outer multiset dimension of graphs*, arXiv:2207.06834v1; Results in Mathematics 78 (2023), 50.
3. R. Gil-Pons, Y. Ramírez-Cruz, R. Trujillo-Rasua, and I. G. Yero, *Distance-based vertex identification in graphs: the outer multiset dimension*, arXiv:1902.03017v1; Applied Mathematics and Computation 363 (2019), 124612.
