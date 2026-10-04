# Edge metric bases of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n\) be the crown graph obtained from \(K_{n,n}\) with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\) by deleting the perfect matching \(\{a_i b_i:1\le i\le n\}\). Then
\[
\operatorname{edim}(\operatorname{Cr}_n)=n-1.
\]
Moreover, the edge metric bases are exactly the sets obtained by choosing one index \(r\), taking neither \(a_r\) nor \(b_r\), and taking exactly one of \(a_i,b_i\) for every \(i\ne r\). Consequently the number of edge metric bases is
\[
n2^{n-1}.
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. For an edge \(e=uv\) and vertex \(x\), the vertex-edge distance is \(d(x,e)=\min\{d(x,u),d(x,v)\}\). An edge metric generator is a vertex set whose distance vectors distinguish all edges; an edge metric basis is a minimum such set. The restriction \(n\ge3\) is necessary for connectedness: \(\operatorname{Cr}_2\) is two disjoint edges.

## Proof
Write every edge as \(e_{ij}=a_i b_j\) with \(i\ne j\). Since \(n\ge3\), two vertices in the same bipartition class are at distance two, each deleted pair \(a_k,b_k\) is at distance three, and every nondeleted cross-pair is adjacent. Therefore, for every \(k\),
\[
d(a_k,e_{ij})=
\begin{cases}
0,&k=i,\\
2,&k=j,\\
1,&k\notin\{i,j\},
\end{cases}
\qquad
d(b_k,e_{ij})=
\begin{cases}
2,&k=i,\\
0,&k=j,\\
1,&k\notin\{i,j\}.
\end{cases}
\]

Let \(S\) be an edge metric generator. If two matched index-pairs, say \(r\) and \(s\), are both disjoint from \(S\), choose \(t\notin\{r,s\}\). The two distinct edges \(e_{rt}\) and \(e_{st}\) have the same distance to every vertex of \(S\): a landmark with index \(t\) sees both at distance zero or two according to its side, while every landmark with any other available index sees both at distance one. Hence at most one matched pair can be disjoint from \(S\). Thus \(S\) meets at least \(n-1\) matched pairs and \(|S|\ge n-1\).

Conversely, fix an index \(r\), omit both \(a_r,b_r\), and choose exactly one of \(a_i,b_i\) for each \(i\ne r\). At a chosen index \(k\), the coordinate of \(e_{ij}\) is one of \(0,2,1\), and these three values tell whether \(k=i\), \(k=j\), or \(k\notin\{i,j\}\); choosing \(b_k\) merely exchanges the roles of zero and two. Thus two edges with the same representation must have the same tail/head status at every index other than \(r\). If neither edge uses \(r\), they are identical. If exactly one uses \(r\), its representation has only one non-unit endpoint coordinate whereas the other has two. If both use \(r\), their other endpoint index and its tail/head role must coincide, again giving the same edge. Hence the chosen set resolves every edge and has size \(n-1\).

Finally, any basis has size \(n-1\) and meets at least \(n-1\) of the \(n\) matched pairs. Therefore it must omit exactly one pair and contain exactly one vertex from each remaining pair. There are \(n\) choices for the omitted pair and \(2^{n-1}\) choices of sides, proving the count.

## Verification
The accompanying `artifacts/verify.py` constructs \(\operatorname{Cr}_n\), computes graph distances by breadth-first search, and exhaustively checks \(3\le n\le8\). It independently verifies the closed vertex-edge distance formula, tests every subset of size below \(n-1\) to confirm that none resolves all edges, and tests every subset of size \(n-1\) against the claimed matched-pair classification. Its replay output is:

`VERIFY_OK n_range=3..8 subset_checks=34896 basis_checks=1788 distance_formula_checks=2176 max_order=16`

The finite computation is corroborative only; the proof above establishes the theorem for every \(n\ge3\).

## Relationship to prior work
Kelenc, Tratnik, and Yero introduced edge metric dimension and proved \(\operatorname{edim}(K_{r,t})=r+t-2\) for complete bipartite graphs. Their full preprint does not contain the terms “crown” or “matching.” The crown result is not a specialization of their complete-bipartite theorem: removing one perfect matching changes both the edge set and the relevant distances. In the balanced case the contrast is sharp: \(K_{n,n}\) has edge metric dimension \(2n-2\), whereas \(\operatorname{Cr}_n\) has edge metric dimension \(n-1\).

Zhu, Taranenko, Shao, and Xu characterize graphs attaining the maximum possible edge metric dimension \(|V|-1\). Crowns lie far outside that regime, since the present value is \(n-1\) on \(2n\) vertices. Work on \(k\)-size edge metric dimension imposes an additional induced-subgraph-size condition and does not imply the ordinary crown-graph basis classification here. Targeted searches under “crown graph,” “complete bipartite minus perfect matching,” and “edge resolving set/basis” did not locate a statement that implies the theorem; this absence is treated only as supporting evidence, not by itself as a novelty proof.

## Limitations
The theorem concerns ordinary edge metric dimension only and does not address fault-tolerant, mixed, local, or \(k\)-size edge-resolving variants. No claim is made for disconnected \(\operatorname{Cr}_2\). The literature comparison is necessarily bounded by the sources retrievable under the inspected names and aliases; an unindexed source using different terminology remains a residual originality risk.

## References
1. A. Kelenc, N. Tratnik, I. G. Yero, “Uniquely identifying the edges of a graph: the edge metric dimension,” arXiv:1602.00291v1, 31 January 2016; later Discrete Applied Mathematics 251 (2018), 204–220.
2. E. Zhu, A. Taranenko, Z. Shao, J. Xu, “On graphs with the maximum edge metric dimension,” Discrete Applied Mathematics 257 (2019), 317–324, DOI:10.1016/j.dam.2018.08.031.
3. T. Iqbal, M. N. Azhar, S. A. U. H. Bokhary, “The K-Size Edge Metric Dimension of Graphs,” Journal of Mathematics (2020), 1023175, DOI:10.1155/2020/1023175.
