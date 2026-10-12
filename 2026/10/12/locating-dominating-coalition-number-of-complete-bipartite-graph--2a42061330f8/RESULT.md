# Locating-dominating coalition number of complete bipartite graphs
## Finding
Let \(K_{m,n}\) have bipartition \(A\sqcup B\), where \(m=|A|\ge 1\) and \(n=|B|\ge 1\). The graph \(K_{1,1}\) admits no locating-dominating coalition partition. For every other complete bipartite graph,
\[
C_L(K_{m,n})=\begin{cases}
4,&(m,n)=(2,2),\\
3,&\text{otherwise}.
\end{cases}
\]
Thus, apart from the four-cycle, the entire nontrivial complete-bipartite family has the same locating-domination coalition number.

## Assumptions and scope
All graphs are finite, simple, and connected. A set \(D\subseteq V(G)\) is locating-dominating (LD) when it dominates every vertex outside \(D\) and the traces \(N(v)\cap D\), for \(v\notin D\), are pairwise distinct. Two disjoint non-LD sets form an LD-coalition when their union is LD. An LDC-partition is a vertex partition in which every block is non-LD and has another block with which it forms an LD-coalition. The number \(C_L(G)\) is the maximum number of blocks in such a partition, when one exists.

## Proof
First characterize LD-sets in \(K_{m,n}\). If \(D\) meets both \(A\) and \(B\), then domination is automatic. Any two vertices of \(A\setminus D\) have the same trace \(D\cap B\), and any two vertices of \(B\setminus D\) have the same trace \(D\cap A\). Conversely, an outside vertex in \(A\) and one in \(B\) have nonempty traces lying in disjoint sides of the bipartition, hence distinct. Therefore such a \(D\) is LD exactly when
\[
|A\setminus D|\le 1\qquad\text{and}\qquad |B\setminus D|\le 1.
\]
If \(D\) lies in one side, domination forces \(D=A\) or \(D=B\). The set \(A\) is LD exactly when \(n=1\), and \(B\) is LD exactly when \(m=1\).

Now suppose \(\max\{m,n\}\ge2\). Choose two distinct vertices \(x,y\) from a side of size at least two. The three blocks
\[
V(K_{m,n})\setminus\{x,y\},\qquad \{x\},\qquad \{y\}
\]
form an LDC-partition: the large block is not LD because \(x\) and \(y\) have identical traces into it, neither singleton is LD, and adjoining either singleton to the large block leaves only one outside vertex and hence gives an LD-set. Thus \(C_L(K_{m,n})\ge3\).

If \(\min\{m,n\}=1\), every LD-set has complement of size at most one by the characterization above. In any LDC-partition, the union of a coalition pair is LD, while every other block lies in its complement. Hence there can be at most one further block, and \(C_L=3\).

Assume next that \(m,n\ge2\). Every LD-set has complement of size at most two, so the same coalition-pair argument gives \(C_L\le4\). Suppose an LDC-partition has four blocks. For any coalition pair, the other two nonempty blocks must together be exactly the two vertices omitted by their LD union. Those two omitted vertices must lie in opposite bipartition classes, and the two remaining blocks are therefore singletons \(\{a\}\) and \(\{b\}\) with \(a\in A\), \(b\in B\).

If \(\{a\}\cup\{b\}\) is LD, then its complement omits at most one vertex from each side, forcing \(m=n=2\). Otherwise \(\{a\}\) must partner one of the two original coalition blocks, say \(X\). Since \(\{a\}\cup X\) is LD, its complement consists of \(\{b\}\) together with the fourth block \(Y\), and can contain at most one vertex from each side. Hence \(Y\) is a singleton in \(A\). The singleton \(\{b\}\) cannot then partner \(X\), because the complement would contain two vertices of \(A\); and partnering \(\{a\}\) or \(Y\) would make a two-vertex transversal LD, which again forces \(m=n=2\). Thus four blocks are possible only for \(K_{2,2}\).

Finally, in \(K_{2,2}\) the partition into four singleton vertices is an LDC-partition: every singleton is non-LD and every singleton has either vertex in the opposite side as a coalition partner. Hence \(C_L(K_{2,2})=4\). The graph \(K_{1,1}=K_2\) has no LDC-partition because each singleton is already an LD-set.

## Verification
The proof is analytic. The accompanying `verify.py` independently reconstructs the LD definition on complete bipartite graphs, checks the stated LD-set characterization for every subset when \(1\le m,n\le8\), and exhaustively enumerates all vertex partitions for \(1\le m\le n\le7\) with \(m+n\le9\). Its replay output is:

`ALL CHECKS PASSED; subset_checks=260100; partition_parameter_cases=19; partition_candidates=83382; subset_range=1<=m,n<=8; partition_range=1<=m<=n<=7,m+n<=9`

The finite computation is a stress test only; it is not used to infer the infinite theorem.

## Relationship to prior work
Chellali, Dobrynin, Foucaud, Golmohammadi, and Valenzuela-Tripodoro introduced locating-dominating coalitions and \(C_L\) in arXiv:2602.18760v1. Their paper gives general existence and upper bounds, exact values for paths and cycles, a characterization of connected graphs with \(C_L(G)=|V(G)|\), and a characterization of trees with \(C_L(T)=|V(T)|-1\). The inspected full text does not state a complete-bipartite or biclique classification. Some boundary cases of the theorem above are therefore already consequences of their results: \(K_{1,2}\cong P_3\) and \(K_{2,2}\cong C_4\) occur in their path/cycle formulas, and small stars intersect their tree extremal classification. The uniform theorem for all \(K_{m,n}\), especially the collapse to the constant value \(3\) away from \(K_{2,2}\), is not supplied by those special cases.

Nearby literature on self-, solid-, and locating-total domination in complete multipartite graphs concerns different code conditions and does not impose the coalition-partition requirement, so those formulas do not imply this result.

## Limitations
The theorem is restricted to complete bipartite graphs. It does not classify all maximizing LDC-partitions, and it does not yet extend the coalition number to arbitrary complete multipartite graphs. The originality search covered the initiating full text, exact biclique terminology, coalition aliases, and nearby locating-domination variants, but an unindexed result under different terminology remains a residual risk.

## References
1. M. Chellali, A. A. Dobrynin, F. Foucaud, H. Golmohammadi, J. C. Valenzuela-Tripodoro, “Locating-dominating coalitions in graphs,” arXiv:2602.18760v1, first public 2026-02-21.
