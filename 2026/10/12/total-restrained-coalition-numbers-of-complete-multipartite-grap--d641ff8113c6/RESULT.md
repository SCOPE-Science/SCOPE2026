# Total restrained coalition numbers of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), with nonempty partite classes \(V_1,\ldots,V_r\), and put
\[
N=\sum_{i=1}^r n_i.
\]
Then
\[
C_{tr}(G)=
\begin{cases}
2,&G\cong K_{1,m}\text{ for some }m\ge2,\text{ or }G\cong K_3,\\
N,&\text{otherwise.}
\end{cases}
\]
In particular, every complete multipartite graph of order at least four with at least three partite classes has the maximum possible total restrained coalition number \(N\).

## Assumptions and scope
Graphs are finite, simple, and undirected. A total restrained dominating set, abbreviated TRD-set, is a set \(D\subseteq V(G)\) such that every vertex has a neighbor in \(D\), and every vertex of \(V(G)\setminus D\) has a neighbor in \(V(G)\setminus D\). Two disjoint non-TRD sets form a total restrained coalition when their union is a TRD-set. A total restrained coalition partition is a vertex partition in which every block is non-TRD and has another block with which it forms such a coalition. The parameter \(C_{tr}(G)\) is the largest number of blocks in such a partition.

The statement includes the already-established complete-graph, complete-bipartite, star, and triangle boundary cases so that the complete multipartite classification is self-contained. The new structural content is the multipartite regime with at least three partite classes and order at least four.

## Proof
First characterize TRD-sets in a complete multipartite graph. Let \(D\subseteq V(G)\). Since vertices in one partite class are pairwise nonadjacent and vertices in distinct classes are adjacent, every vertex has a neighbor in \(D\) exactly when \(D\) meets at least two partite classes. Likewise, the induced graph on \(V(G)\setminus D\) has no isolated vertex exactly when the complement is empty or meets at least two partite classes. Therefore
\[
D\text{ is a TRD-set}
\quad\Longleftrightarrow\quad
D\text{ meets at least two parts and }V(G)\setminus D\text{ is empty or meets at least two parts.}
\]

Suppose first that \(r\ge3\) and \(N\ge4\). We show that the singleton partition is a total restrained coalition partition. Fix a vertex \(u\in V_i\). If \(r\ge4\), choose any vertex \(v\) from a different part. The pair \(\{u,v\}\) meets two parts, and after deleting it at least two untouched nonempty parts remain. Hence \(\{u,v\}\) is a TRD-set.

It remains to treat \(r=3\). Since \(N\ge4\), at least one of the three parts has size at least two. If the part containing \(u\) has size at least two, choose \(v\) from either other part; the complement still meets the part of \(u\) and the third part. If the part containing \(u\) is a singleton, choose \(v\) in a part of size at least two; the complement still meets that part and the remaining third part. Thus every singleton has a singleton partner whose union is a TRD-set. No singleton is itself a TRD-set, so the partition into all \(N\) singleton blocks is valid. Consequently \(C_{tr}(G)=N\), which is maximal by definition.

For \(K_3\), every proper two-vertex set leaves a single outside vertex, so no proper set is a TRD-set. The whole vertex set is a TRD-set. Hence a two-block partition exists, while three blocks would require a pair of singleton blocks whose union were a TRD-set. Therefore \(C_{tr}(K_3)=2\).

Now let \(r=2\), so \(G=K_{s,t}\). If \(s,t\ge2\), any pair consisting of one vertex from each shore is a TRD-set: it meets both shores and its complement also meets both shores. Thus the singleton partition gives \(C_{tr}(G)=s+t=N\). If, say, \(s=1\) and \(t=m\ge2\), every set meeting both shores contains the unique vertex of the one-vertex shore. Any proper such set leaves outside vertices only in the other shore, so it is not restrained. Hence \(V(G)\) is the unique TRD-set. A two-block partition is therefore valid, and no partition with three blocks can work because the union of any two blocks is then proper. Thus \(C_{tr}(K_{1,m})=2\). Finally, \(K_{1,1}=K_2\) has \(C_{tr}=2=N\).

These cases exhaust all connected complete multipartite graphs.

## Verification
The proof is analytic and covers arbitrary part sizes. A standalone checker independently constructs complete multipartite graphs, tests the TRD definition directly from adjacency, enumerates all set partitions, and computes the exact total restrained coalition number for every complete multipartite part-size profile of orders \(2\) through \(8\). It then compares those exact values with the displayed classification. The finite computation is corroborative only; the all-orders conclusion follows from the structural proof above.

## Relationship to prior work
Chellali, Valenzuela-Tripodoro, Golmohammadi, Takhonov, and Matrokhin introduced total restrained coalitions. Their first public arXiv version appeared on 2024-12-17, and the current article lists MSC 05C60. The paper proves \(C_{tr}(K_n)=n\) for \(n\ge4\), \(C_{tr}(K_{p,q})=p+q\) when \(p,q\ge2\), and \(C_{tr}(K_{1,n-1})=2\); it also notes \(C_{tr}(C_3)=2\) and characterizes the triangle-free graphs attaining \(C_{tr}(G)=|V(G)|\).

The inspected arXiv and open-access journal texts contain no complete-multipartite theorem. In particular, the triangle-free characterization cannot cover complete multipartite graphs with three or more parts, which contain triangles. The theorem above supplies the missing multipartite regime and combines it with the established boundary cases into one exact classification.

## Limitations
The result is restricted to complete multipartite graphs and does not characterize arbitrary graphs of maximum total restrained coalition number. The complete, complete-bipartite, star, and \(K_3\) boundary values are prior results or immediate recorded cases in the initiating paper; novelty is claimed for the at-least-three-part multipartite classification and the resulting unified formula. Literature search cannot exclude a poorly indexed equivalent statement under different terminology.

## References
1. M. Chellali, J. C. Valenzuela-Tripodoro, H. Golmohammadi, I. I. Takhonov, and N. A. Matrokhin, *Total restrained coalitions in graphs*, arXiv:2412.18623, first version 2024-12-17; later published in *Computational and Applied Mathematics* 45 (2026), article 50, DOI 10.1007/s40314-025-03439-w.
2. J. H. Hattingh and E. J. Joubert, *Restrained and Total Restrained Domination in Graphs*, in *Topics in Domination in Graphs*, Developmental Mathematics 64, Springer, 2020, pp. 129--150.
