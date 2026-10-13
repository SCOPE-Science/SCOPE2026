# Six vertices are the sharp split between a unique hub and a unique graph center
## Finding
Let \(G=(V,E)\) be a connected finite simple undirected graph. Define
\[
D(G)=\{v\in V:\deg(v)=\Delta(G)\}
\]
and let the graph center be
\[
C(G)=\{v\in V:\operatorname{ecc}(v)=\operatorname{rad}(G)\},
\qquad
\operatorname{ecc}(v)=\max_{u\in V} d(u,v).
\]

Whenever both \(D(G)\) and \(C(G)\) are singletons and \(|V|\le 5\), they contain the same vertex.

This is sharp. Among the
\[
26704
\]
labeled connected simple graphs on \(6\) vertices, exactly
\[
720
\]
have distinct unique vertices in \(D(G)\) and \(C(G)\). The exact incidence is
\[
\frac{720}{26704}=\frac{45}{1669}.
\]

Those \(720\) graphs form exactly two isomorphism classes. Each class has orbit size
\[
360=\frac{6!}{2},
\]
so each representative has automorphism group of order \(2\).

A tree representative has edge set
\[
E_1=\{02,04,05,12,13\}.
\]
Its degree and eccentricity vectors, in vertex order \(0,1,2,3,4,5\), are
\[
(3,2,2,1,1,1)
\]
and
\[
(3,3,2,4,4,4).
\]
Hence vertex \(0\) is the unique maximum-degree vertex while vertex \(2\) is the unique center.

A unicyclic representative has edge set
\[
E_2=\{04,05,12,13,14,23\}.
\]
Its degree and eccentricity vectors are
\[
(2,3,2,2,2,1)
\]
and
\[
(3,3,4,4,2,4).
\]
Hence vertex \(1\) is the unique maximum-degree vertex while vertex \(4\) is the unique center.

There is also a useful three-way refinement. Let
\[
F(v)=\sum_{u\in V} d(u,v)
\]
be farness, so classic closeness maximizes \(1/F(v)\). In the tree representative,
\[
(F(0),\ldots,F(5))=(8,10,8,14,12,12),
\]
and in the unicyclic representative,
\[
(F(0),\ldots,F(5))=(10,8,11,11,8,14).
\]
Thus, in both first-conflict classes, the unique hub and the unique minimax center tie for best closeness.

A weaker threshold occurs one order earlier. Exactly
\[
400
\]
of the \(728\) labeled connected five-vertex graphs have \(D(G)\ne C(G)\), but none has both sets singleton. Thus five vertices suffice for set-level disagreement through ties, whereas six vertices are necessary and sufficient for two unambiguous but different choices.

## Assumptions and scope
Graphs are finite, simple, undirected, connected, and labeled when counts are stated.

The graph center uses minimum eccentricity, equivalently the vertex \(1\)-center objective that minimizes the worst-case graph distance. Degree centrality uses raw degree; multiplying degrees by any positive graph-order-dependent normalization does not change \(D(G)\).

The claim concerns the identity of unique maximizers, not complete rankings of all vertices.

The exhaustive classification covers orders at most \(6\). No frequency or structural claim is made for larger graphs.

## Proof
Every labeled simple graph on \(n\) vertices is encoded by a bit vector on the \(\binom n2\) possible edges. The verifier exhausts all such vectors for \(1\le n\le 6\) and retains exactly the connected graphs.

The resulting connected labeled counts are
\[
1,\ 1,\ 4,\ 38,\ 728,\ 26704.
\]
Connectivity is checked independently by breadth-first search and union--find, and both tests agree for every graph.

For each connected graph, all-pairs shortest-path distances are computed independently by breadth-first search from every source and by Floyd--Warshall. The two distance matrices agree entrywise.

Degree is read directly from the adjacency relation. Eccentricity is computed as the row maximum of each independently reconstructed distance matrix; the two eccentricity vectors therefore provide an exact cross-check. The degree-maximizer set \(D(G)\) and center \(C(G)\) are then obtained directly.

The numbers of connected labeled graphs with \(D(G)\ne C(G)\) are
\[
0,\ 0,\ 0,\ 0,\ 400,\ 18480
\]
for orders \(1\) through \(6\).

After restricting to graphs for which both \(D(G)\) and \(C(G)\) are singletons, the numbers with distinct selected vertices are
\[
0,\ 0,\ 0,\ 0,\ 0,\ 720.
\]
Thus the unique-choice split first occurs at order \(6\).

Canonicalization of the \(720\) six-vertex conflicts under every permutation in \(S_6\) yields exactly two canonical edge masks. Their relabeling orbits each contain \(360\) distinct graphs, are disjoint, and together exhaust all \(720\) conflicts. Direct edge counts show that the first class is a tree and the second is unicyclic.

For each representative, direct exact evaluation gives the displayed degree, eccentricity, and farness vectors. In particular, the maximum-degree vertex and center are distinct and unique, while those two vertices tie for minimum farness.

## Verification
The embedded `verify_degree_center_boundary.py` uses only the Python standard library and exact integer arithmetic.

It verifies:
- every connected labeled simple graph through six vertices;
- the connected-graph counts \(1,1,4,38,728,26704\);
- connectivity by both breadth-first search and union--find;
- all-pairs distances by both repeated breadth-first search and Floyd--Warshall;
- exact degree and eccentricity maximizing sets;
- exactly \(400\) five-vertex set-level disagreements and no distinct unique leaders there;
- exactly \(720\) six-vertex distinct-unique conflicts;
- exactly two conflict isomorphism classes, each of orbit size \(360\);
- the tree and unicyclic representative edge sets;
- the displayed degree, eccentricity, and farness vectors;
- the closeness tie between the competing vertices in both representatives.

Run:

`python3 verify_degree_center_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Graph centers are a classical minimax-distance notion. Ram Kumar, Balakrishnan, Changat, Sreekumar, and Narasimha-Shenoi review the graph-center literature, define the center as the minimum-eccentricity vertices, connect it to facility-location problems, and separately recall degree as a basic vertex quantity. Their paper studies center sets in several graph classes, not the smallest order at which a unique maximum-degree vertex and unique graph center disagree.

Batool and Niazi compare degree, eccentricity, closeness, betweenness, and eigenvector centralities on empirical networks. Their study emphasizes that different centrality measures capture different notions of importance and explicitly treats degree and eccentricity centrality together. It does not provide a complete small-graph extremal classification.

Targeted searches using graph-center, eccentricity-centrality, maximum-degree, unique-center, smallest-graph, six-vertex, and exact-count formulations did not locate the \(720\)-graph two-class boundary or the \(400\)-graph five-vertex tie layer.

## Limitations
The theorem is restricted to connected simple undirected graphs.

The six-vertex threshold applies to distinct unique choices. Maximizing sets can differ already on five vertices because of ties.

The exhaustive census stops at six vertices and does not predict densities for larger graph orders.

The exact finite classification could conceivably have appeared in an unindexed graph atlas, software corpus, thesis appendix, or teaching enumeration; this residual bibliographic risk is not treated as evidence of absence.

## References
1. R. Ram Kumar, K. Balakrishnan, M. Changat, A. Sreekumar, and P. G. Narasimha-Shenoi, “On The Center Sets and Center Numbers of Some Graph Classes,” arXiv:1312.3182, first submitted 11 December 2013.
2. K. Batool and M. A. Niazi, “Towards a Methodology for Validation of Centrality Measures in Complex Networks,” *PLoS ONE* 9(4):e90283, 2014. DOI: 10.1371/journal.pone.0090283.
