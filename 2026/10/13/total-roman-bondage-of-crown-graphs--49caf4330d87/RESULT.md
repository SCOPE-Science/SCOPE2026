# Total Roman bondage of crown graphs
## Finding
For every integer \(n\ge4\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph with deleted matched pairs \((a_i,b_i)\). Then \(\gamma_{tR}(\operatorname{Cr}_n)=6\) and \[b_{tR}(\operatorname{Cr}_n)=n-1.\] Moreover, every minimum total Roman dominating function has exactly two vertices labeled \(2\), one on each shore. If these are \(a_i\) and \(b_j\) with \(i\ne j\), the two vertices labeled \(1\) are forced to be \(a_j\) and \(b_i\); if \(i=j\), the two vertices labeled \(1\) are an arbitrary \(a_p\) and \(b_q\) with \(p,q\ne i\). Hence \(\operatorname{Cr}_n\) has exactly \(n^2(n-1)\) minimum total Roman dominating functions.

## Assumptions and scope
A total Roman dominating function on a finite simple graph with no isolated vertices is a map \(f:V(G)\to\{0,1,2\}\) such that every vertex labeled \(0\) has a neighbor labeled \(2\), and the subgraph induced by the positive-labeled vertices has no isolated vertex. Its weight is \(\sum_{v\in V(G)}f(v)\), and \(\gamma_{tR}(G)\) is the minimum weight. The total Roman bondage number \(b_{tR}(G)\) is the least number of edges whose deletion leaves no isolated vertices and strictly increases \(\gamma_{tR}\).

Write the crown graph as a bipartite graph with shores \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_i\) is the unique missing cross-edge incident with the matched pair indexed by \(i\). The theorem concerns \(n\ge4\). The smaller crown \(\operatorname{Cr}_3\cong C_6\) is excluded because cycles belong to a boundary regime already covered by the initiating total-Roman-bondage literature.

## Proof
First determine \(\gamma_{tR}(\operatorname{Cr}_n)\). The positive support of every total Roman dominating function is a total dominating set. In a crown graph, any total dominating set contains at least two vertices of each shore: if only \(a_i\) were selected from \(A\), then \(b_i\) would have no selected neighbor, and symmetrically for \(B\). Thus every positive support has size at least \(4\).

Suppose a total Roman dominating function had weight at most \(5\). Since \(2n\ge8\), some vertex is labeled \(0\), so at least one vertex is labeled \(2\). The support-size bound forces exactly four positive vertices and exactly one label \(2\). If that unique \(2\) lies in \(A\), then every zero vertex of \(A\) would lack a label-
\(2\) neighbor, so all vertices of \(A\) must be positive. For \(n\ge5\) this already exceeds four positive vertices. For \(n=4\), it makes the entire positive support equal to \(A\), which is independent and violates the totality condition. The case with the unique \(2\) in \(B\) is symmetric. Hence the weight is at least \(6\).

For distinct indices \(i\ne j\), label \(a_i,b_j\) by \(2\), label \(a_j,b_i\) by \(1\), and label every other vertex by \(0\). The positive support consists of the two edges \(a_i b_j\) and \(a_j b_i\), and every zero is adjacent to the label-
\(2\) vertex on the opposite shore. Hence the weight is \(6\), proving \(\gamma_{tR}(\operatorname{Cr}_n)=6\).

The same argument classifies all weight-
\(6\) functions. Since the support has size at least \(4\), the only possible support/defender counts are \((5,1)\) or \((4,2)\), where the second coordinate is the number of label-
\(2\) vertices. The first case is impossible by the preceding unique-defender argument, including the \(n=4\) boundary. Thus there are four positive vertices and two defenders. The defenders must lie on opposite shores. If they are \(a_i\) and \(b_j\) with \(i\ne j\), then the exceptional nonneighbors \(a_j\) and \(b_i\) are forced to be the two label-
\(1\) vertices. If \(i=j\), totality forces one label-
\(1\) vertex on each shore, and any \(a_p,b_q\) with \(p,q\ne i\) works. Counting gives \(n(n-1)+n(n-1)^2=n^2(n-1)\) minimum functions.

Now let \(F\) be a set of deleted crown edges. Encode it by a loopless directed graph \(D_F\) on \(\{1,\ldots,n\}\): put an arc \(p\to q\) exactly when \(a_p b_q\in F\). Let \(O\) be the indices of outdegree zero and \(I\) the indices of indegree zero in \(D_F\).

A minimum function whose two defenders are the matched pair \(a_i,b_i\) survives precisely when \(i\in O\cap I\). A minimum function with defenders \(a_i,b_j\), where \(i\ne j\), survives precisely when \(i\in O\), \(j\in I\), and the reverse arc \(j\to i\) is absent: the untouched defender stars and the cross-support edge \(a_jb_i\) are exactly the edges needed by that minimum function.

Consequently, if \(F\) destroys every minimum function, then \(O\cap I=\varnothing\) and every arc from \(I\) to \(O\) must be present. Put \(a=|O|\), \(b=|I|\), and \(k=n-a-b\). If \(|F|\le n-2\), then both \(a\) and \(b\) are positive because at most \(|F|\) indices can occur as arc tails or heads. The complete set of arcs from \(I\) to \(O\) contributes \(ab\) deletions. Each of the remaining \(k\) indices is not in \(O\), so it contributes at least one further outgoing arc, distinct from those \(ab\) arcs. Therefore
\[
|F|\ge ab+k=ab+n-a-b=n-1+(a-1)(b-1)\ge n-1,
\]
a contradiction. Thus fewer than \(n-1\) deletions cannot increase \(\gamma_{tR}\).

For the matching upper bound, delete the edge corresponding to the arc \(1\to2\), and on the indices \(3,\ldots,n\) delete the edges corresponding to one directed cycle. There are exactly \(n-1\) deleted edges. In the resulting directed graph, \(O=\{2\}\), \(I=\{1\}\), and the arc \(1\to2\) is present, so the survival characterization shows that every weight-
\(6\) function is destroyed. Each crown vertex loses at most one incident edge, so the remaining graph has minimum degree \(n-2\ge2\). Finally, deleting edges cannot create a new total Roman dominating function of smaller weight: every such function on a spanning subgraph is also valid on the original graph. Hence the new total Roman domination number is strictly larger than \(6\), proving \(b_{tR}(\operatorname{Cr}_n)=n-1\).

## Verification
The accompanying checker reconstructs crowns from their definition, tests the total Roman conditions directly, and exhaustively enumerates all labelings of weight at most \(6\) for \(n=4,5\). It verifies both the minimum value and the complete optimizer classification, then checks every edge-deletion set smaller than \(n-1\) for those two orders and the explicit \(n-1\)-edge witness. It separately checks the lower-bound inequality for all admissible \((a,b,k)\) through \(n=60\) and the witness degree pattern through \(n=100\). These finite checks corroborate, but do not replace, the arbitrary-
\(n\) proof above.

## Relationship to prior work
Khosh-Ahang Ghasr and Nazari-Moghaddam introduced total Roman bondage in the cited 2026 preprint and proved exact values for several standard families. Their Corollary 9 gives \(b_{tR}(K_{m,n})=m\) for \(2\le m\le n\), so in particular the undeleted balanced biclique has value \(n\). Their full text does not state a crown, perfect-matching-deletion, or one-factor-complement theorem. The present result therefore identifies the exact effect of deleting one perfect matching from the balanced complete bipartite graph: for every \(n\ge4\), the value becomes \(n-1\).

A previously published exact total-bondage result for the same crown family gives \(b_t(\operatorname{Cr}_n)=2n-3\). The general comparison theorem in the 2026 total-Roman-bondage paper can only yield an upper bound from ordinary total bondage in applicable cases; it does not imply the sharper exact value \(n-1\) or the optimizer-survival characterization proved here.

## Limitations
The theorem is specific to the balanced crown family and \(n\ge4\). It does not classify total Roman bondage for arbitrary \(K_{r,s}-M_t\), nor does it claim that the directed-deletion argument extends unchanged to unequal shores or partial matchings. Literature and database searches reduce but cannot eliminate the possibility of an older poorly indexed equivalent statement under an uncommon alias. The proof is self-contained for the claimed range; the finite checker is only a stress test.

## References
1. F. Khosh-Ahang Ghasr and S. Nazari-Moghaddam, “Total Roman bondage number of a graph,” arXiv:2602.08758v1, first public 2026-02-09, MSC 2020 05C69.
