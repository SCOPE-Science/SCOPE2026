# Noncomplete complete multipartite graphs have infinite multiset partition dimension
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected noncomplete complete multipartite graph, where \(r\ge2\), every \(n_i\ge1\), and \(\max_i n_i\ge2\). Then
\[
\operatorname{mpd}(G)=\infty.
\]
That is, no partition of \(V(G)\) is a resolving multiset partition.

## Assumptions and scope
For a vertex partition \(\Pi=\{P_1,\ldots,P_k\}\), the multiset partition representation of \(v\) is
\[
r_{mp}(v\mid\Pi)=\{d(v,P_1),\ldots,d(v,P_k)\},
\]
where multiplicities are retained but the order of the distances is discarded. The graph has at least two partite classes, so vertices in different classes are adjacent and two distinct vertices in the same class have distance \(2\).

The complete-graph case, in which every partite class is a singleton, is not part of the new claim: the initiating paper already proves that complete graphs have infinite multiset partition dimension.

## Proof
Fix an arbitrary partition \(\Pi=\{P_1,\ldots,P_k\}\) of \(V(G)\). For a partite class \(A_i\), let \(c_i\) be the number of blocks of \(\Pi\) that are contained entirely in \(A_i\). For \(v\in A_i\), the distance from \(v\) to a block is \(0\) for the block containing \(v\), is \(2\) exactly for a block contained in \(A_i\) that does not contain \(v\), and is \(1\) for every remaining block. Hence
\[
r_{mp}(v\mid\Pi)=\{0,1^{k-1-q(v)},2^{q(v)}\},
\]
where
\[
q(v)=
\begin{cases}
c_i-1,&\text{if the block containing }v\text{ is contained in }A_i,\\
c_i,&\text{if that block also meets another partite class.}
\end{cases}
\]
Thus a fixed partite class can produce at most two representation types.

Suppose, for contradiction, that \(\Pi\) resolves all vertices. Then every partite class has size at most \(2\). If \(|A_i|=2\), its two vertices must realize the two different types above. Consequently one lies in a pure block and the other in a mixed block. The pure block must be a singleton, so \(c_i=1\); the pure vertex then has \(q(v)=0\), while the mixed vertex has \(q(v)=1\). If \(|A_i|=1\), its unique vertex also has \(q(v)=0\): either its singleton block is pure and \(c_i=1\), or its block is mixed and \(c_i=0\).

Therefore every partite class contains a vertex with representation
\[
\{0,1,\ldots,1\}.
\]
Because \(r\ge2\), vertices chosen from two distinct partite classes have identical representations, contradicting that \(\Pi\) resolves \(G\). Since \(\Pi\) was arbitrary, no resolving multiset partition exists.

## Verification
A standalone checker enumerates every complete multipartite part-size profile of total order \(2\) through \(7\), every set partition of its vertex set, and every vertex representation from the graph-distance definition. It independently verifies the closed representation formula above and confirms that no resolving multiset partition occurs. The replay summary is:

`ALL CHECKS PASSED; graph_profiles=37; set_partitions=14692; vertex_formula_checks=99960; order_range=2..7`

The finite enumeration is a stress test; the proof for arbitrary order is the analytic argument above.

## Relationship to prior work
Albejani, Lin, Ryan, and Sugeng introduced the multiset partition dimension in arXiv:2607.07407v1 (first public 2026-07-08; Mathematics Subject Classification 05C12). Their full text proves \(\operatorname{mpd}(K_n)=\infty\), as well as infinite values for wheel, friendship, fan, and multi-hub wheel families, and gives finite values or bounds for paths, cycles, grids, ladders, and prisms. A document-wide check found no occurrence of “complete bipartite” or “complete multipartite.” The present result extends the complete-graph obstruction in a different direction, covering every noncomplete complete multipartite graph, including all stars and complete bipartite graphs.

The later survey arXiv:2607.08128v1 places multiset partition dimension among newly emerging multiset metric parameters and motivates structural study of such variants. Targeted searches for complete-multipartite, complete-bipartite, and equivalent multiset-resolving-partition formulations found no covering statement.

## Limitations
The theorem is specific to complete multipartite graphs. It proves nonexistence of resolving multiset partitions, not bounds for graph classes that do admit them. The computational checker covers only order at most \(7\) and is not used as an infinite proof. A residual originality risk remains that an equivalent statement could exist in poorly indexed work using different terminology, although the initiating full text and targeted semantic searches were inspected.

## References
1. A. Albejani, Y. Lin, J. Ryan, and K. A. Sugeng, *Multiset Partition Dimension of Graphs*, arXiv:2607.07407v1, 2026.
2. A. Albejani, Y. Lin, J. Ryan, and K. A. Sugeng, *A Survey on Multiset Dimension and Its Variations*, arXiv:2607.08128v1, 2026.
