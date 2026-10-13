# Six vertices are the sharp unique-leader split for betweenness and eigenvector centrality
## Finding
Let \(G=(V,E)\) be a connected finite simple undirected graph. For a vertex \(v\), use Freeman's unnormalized betweenness
\[
B(v)=\sum_{\{s,t\}\subseteq V\setminus\{v\}}\frac{\sigma_{st}(v)}{\sigma_{st}},
\]
where \(\sigma_{st}\) is the number of shortest \(s\)-\(t\) paths and \(\sigma_{st}(v)\) is the number of those paths containing \(v\).

Let eigenvector centrality be given by the positive Perron vector \(x\) of the adjacency matrix \(A\):
\[
Ax=\lambda x,
\]
where \(\lambda\) is the spectral radius. Scaling \(x\) does not affect its maximizing vertex.

Assume that both \(B\) and \(x\) have unique maximizing vertices. If
\[
|V|\le 5,
\]
then the two maximizers are the same vertex.

The bound is sharp. At order \(6\), exactly seven connected unlabeled graph classes have distinct unique maximizers. Their labeled orbit sizes are
\[
720,\ 720,\ 720,\ 720,\ 180,\ 360,\ 360,
\]
so the complete first-conflict layer contains
\[
3780
\]
of the
\[
26704
\]
connected labeled six-vertex graphs. The labeled incidence is
\[
\frac{3780}{26704}=\frac{945}{6676}.
\]

The seven representatives, with betweenness leader \(b\), eigenvector leader \(e\), and orbit size, are:

\[
\begin{array}{c|l|c|c|c}
& E & b & e & \text{orbit}\\ \hline
1&\{01,04,05,12,13,14,23,34\}&0&1&720\\
2&\{01,03,04,12,15,23,34\}&1&0&720\\
3&\{01,03,04,05,12,15,23,34,35\}&3&0&720\\
4&\{01,04,12,13,14,23,34,45\}&4&1&720\\
5&\{01,02,03,34,35,45\}&0&3&180\\
6&\{01,04,12,15,23,34,35,45\}&1&5&360\\
7&\{02,12,13,14,23,25,34,35,45\}&2&3&360
\end{array}
\]

The fifth class is especially transparent. Its degree sequence is
\[
(3,1,1,3,2,2),
\]
so local degree does not choose between vertices \(0\) and \(3\). Its betweenness vector is
\[
(7,0,0,6,0,0),
\]
while eigenvector centrality uniquely maximizes at vertex \(3\). Vertex \(0\) is the stronger geodesic broker because every connection from leaves \(1,2\) to the rest of the graph passes through it. Vertex \(3\), however, is attached to the mutually adjacent pair \(4,5\), and recursive neighbor prestige makes \(3\) the eigenvector leader.

## Assumptions and scope
Graphs are finite, simple, undirected, unweighted, and connected.

Betweenness excludes path endpoints and is unnormalized. Any positive normalization common to all vertices preserves the maximizing set.

Eigenvector centrality is the Perron eigenvector of the ordinary adjacency matrix. Connectedness guarantees a unique positive Perron vector up to positive scaling.

The theorem requires both maximizing sets to be singletons. It concerns the first order of two different unambiguous choices, not merely the first set-valued discrepancy.

The exact classification stops at six vertices. No frequency statement is made for larger graphs.

## Proof
The proof is a complete finite classification over the connected Read--Wilson Graph Atlas representatives through six vertices. Their counts by order are
\[
1,\ 2,\ 6,\ 21,\ 112
\]
for orders \(2,3,4,5,6\).

Betweenness is computed exactly in rational arithmetic in two independent ways. The first is the Brandes dependency recurrence specialized to unweighted undirected graphs. The second reconstructs every unordered endpoint pair \(\{s,t\}\): if \(v\) lies on a shortest \(s\)-\(t\) path, then its contribution is
\[
\frac{\sigma_{sv}\sigma_{vt}}{\sigma_{st}},
\]
and otherwise it contributes zero. The two vectors agree for every Atlas graph through order six.

Eigenvector comparisons are also exact. Let
\[
p(t)=\det(tI-A)
\]
and let
\[
q_i(t)=\det(tI-A_{-i}),
\]
where \(A_{-i}\) deletes row and column \(i\). If \(\lambda\) is the simple Perron root and \(x\) is a Perron vector, the diagonal adjugate identity gives
\[
q_i(\lambda)=\frac{p'(\lambda)}{\lVert x\rVert^2}x_i^2.
\]
Because \(p'(\lambda)>0\), the ordering of the positive coordinates \(x_i\) is exactly the ordering of the numbers \(q_i(\lambda)\). The verifier computes characteristic polynomials over the integers, isolates \(\lambda\) by rational Sturm sequences, and compares the cofactors exactly, including equality cases.

No graph through order five has distinct unique leaders. Exactly seven order-six representatives do. Exhausting all \(6!\) relabelings gives automorphism-group orders
\[
1,1,1,1,4,2,2,
\]
hence the orbit sizes displayed above. Summing all connected six-vertex Atlas orbits independently reproduces \(26704\), and summing the seven conflict orbits gives \(3780\).

## Verification
The embedded `verify_betweenness_eigenvector_boundary.py` uses only the Python standard library and the embedded `graph_atlas_connected_2to6.json` table.

It verifies the connected unlabeled counts \(1,2,6,21,112\), computes betweenness by two exact algorithms, certifies eigenvector-coordinate order by characteristic cofactors and rational Sturm isolation, checks that the conflict-class counts are
\[
0,0,0,0,7,
\]
and replays every automorphism group and labeled orbit. It also sums all order-six orbits to \(26704\) connected labeled graphs and the conflict orbits to \(3780\).

Run:

`python3 verify_betweenness_eigenvector_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Campiteli and collaborators explicitly compare betweenness and eigenvector centralities as two nonlocal node-importance measures. Grando, Noble, and Lamb subsequently compare major centrality measures on complex and social networks, emphasizing that different measures capture distinct notions of importance. In their terminology, betweenness measures communication control through paths, whereas eigenvector centrality measures visibility through the importance of neighbors.

The classical literature therefore owns both centrality notions and the qualitative fact that different centralities can rank vertices differently. The contribution here is restricted to a sharp finite boundary: no distinct unique betweenness/eigenvector leaders through five vertices, followed by exactly seven isomorphism classes at six vertices and an exact labeled count.

Related small-graph results comparing degree with betweenness or degree with eigenvector centrality do not imply this theorem. Six of the seven first-conflict classes have no unique degree leader, so a degree-mediated comparison cannot decide the two nonlocal leaders there.

Targeted searches using betweenness/eigenvector aliases, unique-leader and unique-maximizer language, six-vertex restrictions, smallest-graph language, and exact-count terms did not locate this finite boundary or seven-class census.

## Limitations
The graph domain is unweighted, undirected, connected, and simple.

The result concerns ordinary shortest-path betweenness and ordinary adjacency eigenvector centrality. Weighted, directed, current-flow, Katz, PageRank, and walk-betweenness variants are not covered.

The Atlas table is an externally curated complete list of graph isomorphism types through seven vertices; only orders through six are embedded and used here.

An unindexed exercise, thesis appendix, graph-atlas annotation, or software corpus could contain one or more of the same six-vertex examples.

## References
1. M. G. Campiteli, A. J. Holanda, P. R. C. Soles, L. H. D. Soares, and O. Kinouchi, “Hirsch index as a network centrality measure,” arXiv:1005.4803, first submitted 26 May 2010.
2. F. Grando, D. Noble, and L. C. Lamb, “An Analysis of Centrality Measures for Complex and Social Networks,” *IEEE GLOBECOM 2016*, DOI: 10.1109/GLOCOM.2016.7841580.
3. L. C. Freeman, “Centrality in Social Networks: Conceptual Clarification,” *Social Networks* 1, 215–239, 1978/1979, DOI: 10.1016/0378-8733(78)90021-7.
4. P. Bonacich, “Some unique properties of eigenvector centrality,” *Social Networks* 29, 555–564, 2007, DOI: 10.1016/j.socnet.2007.04.002.
5. R. C. Read and R. J. Wilson, *An Atlas of Graphs*, Oxford University Press, 1998.
