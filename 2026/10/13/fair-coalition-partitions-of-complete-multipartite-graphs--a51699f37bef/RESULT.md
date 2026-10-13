# Fair coalition partitions of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), \(n_i\ge1\), and \(N=\sum_i n_i\). A \(1\)-fair dominating set is a dominating set \(S\) such that every vertex outside \(S\) has exactly one neighbor in \(S\). As in the defining formulation, \(V(G)\) itself satisfies the condition vacuously.

Then \(G\) admits a fair-coalition partition if and only if it is not a nontrivial star \(K_{1,m}\) with \(m\ge2\). Whenever a fair-coalition partition exists,
\[
\mathcal C_f(G)=
\begin{cases}
N,&\text{if every }n_i=1,\\
N,&\text{if }r=2\text{ and }n_1,n_2\ge2,\\
2,&\text{if }r\ge3\text{ and at least one }n_i\ge2.
\end{cases}
\]

Thus complete graphs and non-star complete bipartite graphs attain the largest possible value, every genuinely multipartite noncomplete graph with at least three parts collapses to two blocks, and nontrivial stars are exactly the complete multipartite graphs for which the defining partition does not exist.

## Assumptions and scope
Graphs are finite, simple, and connected. The multipartite presentation has at least two nonempty parts. The definition of fair coalition is the \(1\)-fair version introduced in arXiv:2507.15080: coalition partners are both required not to be \(1\)-fair dominating, whereas a block that is itself \(1\)-fair dominating is permitted only when it is a singleton. The whole vertex set is a dominating set and satisfies the outside-vertex condition vacuously.

The statement is only about complete multipartite graphs. It does not assert a general existence criterion for fair-coalition partitions outside this class.

## Proof
Write the partite classes as \(V_1,\ldots,V_r\). For a set \(S\subseteq V(G)\), put \(t=|S|\) and \(s_i=|S\cap V_i|\). If \(V_i\setminus S\ne\varnothing\), every vertex there has exactly
\[
t-s_i
\]
neighbors in \(S\). Hence \(S\) is \(1\)-fair dominating exactly when
\[
t-s_i=1
\]
for every incomplete part \(V_i\), together with domination; the displayed equality already gives domination for every outside vertex.

Suppose first that \(S\ne V(G)\). If at least two parts, say \(V_i,V_j\), are incomplete, then \(s_i=s_j=t-1\), so
\[
2(t-1)=s_i+s_j\le t.
\]
Thus \(t\le2\). If \(t=1\), every incomplete part contains zero selected vertices, so the unique selected vertex must occupy a singleton part and is universal. If \(t=2\), every incomplete part contains one selected vertex. There can therefore be exactly two incomplete parts and no full part, so \(r=2\) and \(S\) consists of one vertex from each shore.

If exactly one part \(V_i\) is incomplete, then \(s_i=t-1\). Since all other parts are full,
\[
t=(N-n_i)+s_i=(N-n_i)+(t-1),
\]
so \(N-n_i=1\). Therefore \(r=2\) and the other part is a singleton. In other words, in a nontrivial star every proper \(1\)-fair dominating set is precisely a set containing the center. This also subsumes the two-vertex cross-shore sets. If no part is incomplete, then \(S=V(G)\).

Consequently, when \(r\ge3\), the only proper \(1\)-fair dominating sets are singleton universal vertices. When \(r=2\) and both shores have size at least two, the only proper \(1\)-fair dominating sets are cross-shore pairs. For a nontrivial star, the proper \(1\)-fair dominating sets are exactly the sets containing its center.

Now classify fair-coalition partitions. If every part is a singleton, \(G\) is complete and the partition into \(N\) singletons is valid, because each singleton is \(1\)-fair dominating. If \(r=2\) with both part sizes at least two, the partition into all \(N\) singletons is valid: no singleton is \(1\)-fair dominating, but every singleton has any singleton on the opposite shore as a coalition partner, since their union is a cross-shore \(1\)-fair dominating pair. Hence \(\mathcal C_f(G)=N\) in both cases.

Let \(r\ge3\) and assume that some part has size at least two. At least one block of any fair-coalition partition is therefore not a singleton universal vertex. Such a block must have a non-\(1\)-fair partner, and the union of those two blocks must be \(1\)-fair dominating. By the preceding classification, this union cannot be a proper \(1\)-fair set, so it must equal \(V(G)\). Since the blocks form a partition, no third block can occur. Thus every fair-coalition partition has two blocks. Such a partition exists: choose a vertex \(x\) in a non-singleton part and take \(\{x}\}\) and \(V(G)\setminus\{x\}\). The first block is not dominating, while the second is not \(1\)-fair because the omitted vertex has at least two neighbors in it; their union is \(V(G)\). Hence \(\mathcal C_f(G)=2\).

Finally let \(G=K_{1,m}\) with \(m\ge2\), with center \(c\). Every set containing \(c\) is \(1\)-fair dominating. In any fair-coalition partition, the block containing \(c\) therefore must be the singleton \(\{c\}\), because only singleton \(1\)-fair blocks are allowed. Every remaining block lies wholly among the leaves, and the union of any two such blocks still omits \(c\), so it is not dominating and cannot be \(1\)-fair dominating. Hence the leaf blocks have no possible coalition partners, and no fair-coalition partition exists.

## Verification
The proof above is symbolic and covers all part sizes. A separate exhaustive checker enumerates every integer multipartite profile of order at most \(7\), every set partition of its vertex set, and tests the defining conditions directly. It confirms the existence classification and every stated value. This finite computation is corroborative; the theorem does not depend on extrapolation from it.

Run `verify.py` with a standard Python 3 interpreter. The expected final line is `ALL CHECKS PASSED`.

## Relationship to prior work
Alikhani, Jafari, and Safazadeh introduced fair coalitions and the fair coalition number in 2025. Their paper defines the parameter, proves general bounds, determines paths and cycles, and studies cubic graphs of orders at most ten. It explicitly notes \(\mathcal C_f(K_{3,3})=6\) as an example arising from one of the cubic graphs, but it does not give a complete-bipartite or complete-multipartite classification.

A separate result on fair domination of complete multipartite graphs classifies fair dominating sets by part occupancies. That result concerns domination sets themselves rather than coalition partitions. The theorem here uses the sharper \(1\)-fair specialization to classify which unions of partition blocks can serve as coalitions, and then determines the partition parameter and its existence boundary.

## Limitations
The result is specific to \(1\)-fair coalitions. It does not determine \(k\)-fair coalition numbers for \(k\ge2\). The convention that \(V(G)\) is \(1\)-fair dominating is the ordinary vacuous reading of the defining condition; adopting a nonstandard convention that forbids the whole vertex set would change the two-block construction for graphs with at least three parts. The result also does not address uniqueness or counting of maximum partitions.

## References
1. S. Alikhani, A. Jafari, M. Safazadeh, “Fair coalition in graphs,” arXiv:2507.15080, first public 2025-07-20. The current preprint lists AMS classifications 05C25 and 05C60.
2. S. Alikhani, M. Safazadeh, work on enumerative aspects of \(1\)-fair dominating sets, cited in the initiating paper.
