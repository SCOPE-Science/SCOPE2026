# Super coalition numbers of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with nonempty partite classes \(V_1,\ldots,V_r\), let \(N=\sum_i n_i\), and put
\[
p=\left|\{i:n_i\ge2\}\right|.
\]
Then
\[
C_s(G)=
\begin{cases}
0,&N=2,\\
4,&N\ge3\text{ and }\bigl(p\ge3\text{ or }G\cong K_{2,2}\bigr),\\
3,&N\ge3\text{ otherwise}.
\end{cases}
\]
In particular,
\[
C_s(K_{1,2,2,2})=4,
\]
although \(K_{1,2,2,2}\) has a universal vertex. Thus the universal-vertex assertion \(C_s(G)=3\) in Theorem 3.6 of Alikhani--Ghanbari, arXiv:2607.22686v1, is false as stated.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. A set \(D\subseteq V(G)\) is super dominating if every \(u\in V(G)\setminus D\) has a witness \(v\in D\) satisfying
\[
N_G(v)\cap (V(G)\setminus D)=\{u\}.
\]
A super coalition partition is a vertex partition in which no block is super dominating, while every block has another block whose union with it is super dominating. The super coalition number \(C_s(G)\) is the maximum number of blocks, with value \(0\) when no such partition exists.

A previously published all-set classification for complete multipartite graphs is used only as prior-work context; the proof below reconstructs the needed structural criterion directly.

## Proof
Write \(C=V(G)\setminus D\). First observe the following criterion. A set \(D\) is super dominating exactly in one of these cases:

1. \(C=\varnothing\);
2. \(|C|=1\);
3. \(C=\{x,y\}\), the vertices \(x,y\) lie in distinct partite classes, and both of those classes have size at least \(2\).

Indeed, if \(u\in C\cap V_i\) has a witness \(v\in D\cap V_j\), then \(j\ne i\), and every vertex of \(C\setminus\{u\}\) must lie in \(V_j\), since \(v\) is adjacent to every vertex outside \(V_j\). If \(|C|\ge3\), applying the same requirement to a second omitted vertex gives a contradiction. If \(|C|=2\), say \(x\in V_i\) and \(y\in V_j\), then the two vertices must lie in distinct classes and witnesses must remain in \(V_j\setminus\{y\}\) and \(V_i\setminus\{x\}\), respectively; this is possible exactly when \(n_i,n_j\ge2\). The cases \(|C|\le1\) are immediate because the graph is connected.

Now let \(\Pi\) be a super coalition partition. Whenever two blocks \(A,B\in\Pi\) are coalition partners, \(A\cup B\) is super dominating, so the complement \(V(G)\setminus(A\cup B)\) has at most two vertices. Therefore \(|\Pi|\le4\): five blocks would leave at least three nonempty blocks, hence at least three vertices, outside every partner union.

For every \(N\ge3\), a three-block partition always exists. If some part has at least two vertices, choose two vertices \(x,y\) from that same part. If all parts are singletons, choose any distinct \(x,y\). Put
\[
B=V(G)\setminus\{x,y\}.
\]
The set \(B\) is not super dominating: in the first case its two omitted vertices lie in one part, and in the second case the omitted vertices lie in singleton parts. The singleton blocks \(\{x\}\) and \(\{y\}\) are not super dominating because \(N\ge3\). However, \(B\cup\{x\}=V(G)\setminus\{y\}\) and \(B\cup\{y\}=V(G)\setminus\{x\}\) are super dominating. Hence \(C_s(G)\ge3\).

It remains to determine when four blocks are possible. Form the partner graph on the four blocks, joining two blocks when their union is super dominating. It has no isolated vertex. For every partner edge, the two opposite blocks together form the complement of a super dominating set; because both opposite blocks are nonempty, the structural criterion forces both to be singletons, and their vertices must lie in distinct non-singleton partite classes.

If the partner graph contains two disjoint edges, all four blocks are singletons. Hence \(N=4\), and validity requires at least two non-singleton partite classes. The only connected complete multipartite graph of order \(4\) with that property is \(K_{2,2}\). Conversely, the four singleton blocks of \(K_{2,2}\) form a super coalition partition by pairing each vertex with a vertex on the opposite shore.

Suppose instead that the partner graph has no two disjoint edges. A graph on four vertices with minimum degree at least one and matching number one is a star. Let its center be \(B_0\) and leaves be \(B_1,B_2,B_3\). The edge \(B_0B_1\) forces \(B_2,B_3\) to be singleton blocks in two distinct non-singleton partite classes; similarly the other two star edges force \(B_1,B_2,B_3\) to be singletons lying in three pairwise distinct non-singleton partite classes. Thus \(p\ge3\).

Conversely, if \(p\ge3\), choose vertices \(x_1,x_2,x_3\) from three distinct non-singleton partite classes and set
\[
B_0=V(G)\setminus\{x_1,x_2,x_3\},\qquad B_i=\{x_i\}\quad(1\le i\le3).
\]
The block \(B_0\) is not super dominating because it omits three vertices, and each singleton \(B_i\) is not super dominating. For each \(i\), the union \(B_0\cup B_i\) omits exactly the other two \(x_j\), which lie in distinct non-singleton classes, so this union is super dominating. Hence \(C_s(G)=4\).

Finally, when \(N=2\), the graph is \(K_2\). Each singleton is already super dominating, so no super coalition partition exists and \(C_s(K_2)=0\).

The counterexample to the universal-vertex assertion is now explicit. In \(K_{1,2,2,2}\), let \(u\) be the singleton-part vertex and choose \(a,b,c\) from the three two-vertex parts. Then
\[
\left\{V(G)\setminus\{a,b,c\},\{a\},\{b\},\{c\}\right\}
\]
is a four-block super coalition partition, even though \(u\) is universal.

## Verification
The standalone program `verify.py` implements the literal witness definition of super domination and the definition of super coalition partitions. It independently checks the structural criterion for every subset and exhaustively enumerates every set partition for every connected complete-multipartite part profile of order \(2\) through \(8\). It also verifies three explicit universal-vertex counterexamples.

Its replay output is recorded in `verification_output.txt` and ends with `ALL CHECKS PASSED`. The finite enumeration is corroborative only; the arbitrary-order theorem is established by the symbolic proof above.

## Relationship to prior work
Alikhani and Ghanbari introduced the super coalition number in arXiv:2607.22686v1. Their paper proves general bounds, exact values for paths, cycles, complete graphs, stars, wheels, and friendship graphs, and states in Theorem 3.6 that every graph with a universal vertex has super coalition number \(3\). The complete-multipartite classification above is not stated there. The explicit graph \(K_{1,2,2,2}\) disproves that universal-vertex theorem as stated.

A published result titled *All super dominating sets of complete multipartite graphs* already classifies every super dominating set in this graph family and gives the same complement criterion used above. That result concerns super domination itself, not coalition partitions. The present theorem takes the known all-set structure as the closest prior coverage and determines the additional global partition condition: four blocks occur exactly at \(K_{2,2}\) or once three non-singleton partite classes are available. The initiating paper's general upper bound together with previously known scalar super-domination numbers already implies some \(C_s(G)=3\) boundary cases, so novelty is claimed for the exact four-block criterion and the universal-vertex counterexample family, not for those covered boundary values.

## Limitations
The theorem is restricted to connected complete multipartite graphs. The finite verifier reaches order \(8\); arbitrary order is proved analytically. The checked literature cannot exclude every poorly indexed equivalent formulation. The initiating source is currently arXiv version 1; a later revision could correct or supersede its universal-vertex statement after the date of this analysis.

## References
1. S. Alikhani and N. Ghanbari, *Super Coalition Number in Graphs*, arXiv:2607.22686v1, first public 2026-07-15. The inspected version lists AMS classifications 05C69 and 05C70.
2. *All super dominating sets of complete multipartite graphs*, published-finding corpus record 315739371089, public 2026-10-04.
