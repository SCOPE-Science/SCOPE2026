# Induced-matching polynomials and optimal-exchange geometry of the Shrikhande–rook pair

## Finding
Let \(R=K_4\square K_4\) be the four-by-four rook graph and \(S\) the Shrikhande graph. Both have the strongly regular parameters \((16,6,2,2)\). If
\[
F_G(z)=\sum_{M\text{ an induced matching of }G}z^{|M|}
\]
counts each edge set once, including the empty matching, then
\[
\boxed{F_R(z)=1+48z+216z^2},\qquad
\boxed{F_S(z)=1+48z+192z^2+32z^3}.
\]
For \(k=\nu_s(G)\), let \(\mathcal J_k(G)\) join two maximum induced matchings when their edge sets differ by replacing exactly one selected edge with one previously unselected edge, maintaining the induced-matching property. Then
\[
\boxed{\mathcal J_2(R)\text{ is connected and }16\text{-regular, with }216\text{ vertices, }1728\text{ edges, and diameter }3};
\]
\[
\boxed{\mathcal J_3(S)\cong32K_1}.
\]
Thus the two cospectral graphs have different optimum induced-matching sizes, and their optimum-exchange spaces have opposite mobility behavior.

## Assumptions and scope
Graphs are simple and have labelled vertex set \(V=(\mathbb Z/4\mathbb Z)^2\), using representatives \(0,1,2,3\). Distinct vertices \((a,b),(c,d)\) are adjacent in \(R\) exactly when \(a=c\) or \(b=d\). In \(S\), they are adjacent when their coordinate difference belongs to
\[
D=\{\pm(1,0),\pm(0,1),\pm(1,1)\}\pmod4.
\]
Two distinct edges are *compatible* when their four endpoints are distinct and no endpoint of one is adjacent to an endpoint of the other. An induced matching is a set of pairwise compatible edges. The token-jumping exchange used here replaces a whole edge of an induced matching, not a vertex, and does not require the two edges to share an endpoint. The assertions concern precisely these two fixed sixteen-vertex graphs, not arbitrary graphs with the same strongly regular parameters.

## Proof
**1. Edge compatibility.** Define the compatibility graph \(C_G\) on the \(48\) edges of \(G\), with adjacency exactly when the corresponding edges are compatible. An induced matching of cardinality \(r\) is precisely an \(r\)-clique in \(C_G\). Both graphs are edge-transitive: for \(R\), permutations of the rows and columns together with coordinate interchange suffice. For \(S\), translations of \((\mathbb Z/4\mathbb Z)^2\), inversion, coordinate interchange \((a,b)\mapsto(b,a)\), and the linear transformation \((a,b)\mapsto(a,a-b)\) preserve \(D\) and act transitively on the six directed generator differences. It therefore suffices to compute the neighborhood inside \(C_G\) of the graph edge \(e=\{(0,0),(0,1)\}\).

**2. The rook graph.** Its compatible edges are of precisely two forms. There are three horizontal edges, namely the edge joining columns \(2,3\) in any of rows \(1,2,3\). There are also six vertical edges, namely an edge joining any two of rows \(1,2,3\) in either column \(2\) or column \(3\). No two of these nine edges are compatible: pairs of horizontals share occupied columns, pairs of verticals share at least one occupied row, and each horizontal and vertical pair shares an occupied column. Thus \(C_R\) is \(9\)-regular and triangle-free. It has \(48\cdot9/2=216\) edges, giving the polynomial claimed for \(R\) and \(\nu_s(R)=2\).

To prove connectivity of \(C_R\), write a horizontal edge as \(h_{r,A}\), where \(r\) is its row and \(A\subseteq\{0,1,2,3\}\) is its two-element set of columns. The horizontal–horizontal compatibility graph has three components, indexed by the unordered partitions \(\{A,A^c\}\); each component is \(K_{4,4}\) with one perfect matching removed, and is connected. By exchanging rows and columns, the vertical–vertical compatibility graph has the same structure. A horizontal \(h_{r,A}\) and a vertical \(v_{c,T}\) are compatible exactly when \(c\notin A\) and \(r\notin T\). For every horizontal component and every vertical component such a choice exists; hence \(C_R\) is connected.

Every maximum induced matching of \(R\) consists of two compatible edges, so \(\mathcal J_2(R)\cong L(C_R)\), the ordinary line graph. Connectedness and regular degree \(2(9-1)=16\) follow, with \(216\cdot16/2=1728\) exchange edges. The diameter is exactly \(3\) by complete breadth-first search from each of its \(216\) vertices as implemented in `check_local.py`. One pair attaining distance three is
\[
\{\{(0,0),(1,0)\},\{(2,3),(3,3)\}\}
\quad\text{and}\quad
\{\{(0,1),(0,3)\},\{(1,2),(2,2)\}\}.
\]
The algorithm checks all adjacency relations and all shortest paths, not merely a sample.

**3. The Shrikhande graph.** For \(e=\{(0,0),(0,1)\}\), the compatible edges are the following eight edges (letters are only labels for this local calculation):
\[
\begin{aligned}
A&=\{(1,3),(2,0)\},&B&=\{(1,3),(2,3)\},\\
C&=\{(2,0),(2,1)\},&D&=\{(2,0),(2,3)\},\\
E&=\{(2,1),(2,2)\},&F&=\{(2,1),(3,2)\},\\
G&=\{(2,2),(2,3)\},&H&=\{(2,2),(3,2)\}.
\end{aligned}
\]
Checking endpoint differences against \(D\) shows that the **only** compatibility adjacencies among these eight are \(AH\) and \(BF\). In particular, the subgraph \(C_S[N_{C_S}(e)]\) is \(2K_2\sqcup4K_1\). Edge-transitivity proves the same local description for all \(48\) vertices of \(C_S\).

Consequently \(C_S\) is \(8\)-regular, with \(48\cdot8/2=192\) edges. Each vertex belongs to exactly two triangles, which gives \(48\cdot2/3=32\) distinct triangles. No four-clique exists, since the neighborhood of any vertex has no triangle. This yields \(F_S\) and \(\nu_s(S)=3\). Finally, every edge of \(C_S\) lies in at most one triangle: in each local neighborhood, every vertex has internal degree at most one. Two distinct triangles therefore cannot share an edge. Since maximum induced matchings correspond to those triangles, no two differ by a single edge exchange, so \(\mathcal J_3(S)\) consists of exactly \(32\) isolated vertices.

## Verification
Both graphs' \(48\) original edges were reconstructed from the displayed adjacency rules. `check_local.py` enumerates all compatibility pairs and local neighborhoods, verifies the rook neighborhood has nine isolated vertices and the Shrikhande neighborhood has \(2K_2\sqcup4K_1\), enumerates larger cliques, builds the full optimal-exchange graphs, and exhaustively computes all shortest-path distances in the rook exchange graph. `check_direct.py` independently enumerates every one-, two-, three- and four-edge subset of the original graph, tests its induced endpoint subgraph, and builds the optimal-exchange relations without using the local-neighborhood routine. Both run using Python 3's standard library only. Their complete outputs are in `check_local.out` and `check_direct.out` and the executed scripts are embedded alongside this document. The calculations are finite exhaustive certificates; the accompanying symmetry and compatibility arguments explain why they suffice.

## Relationship to prior work
The pair \(R,S\) and its identical strongly regular parameters were established long before this calculation. In particular, the original Shrikhande uniqueness phenomenon is discussed in Cameron's dated account and Sane's 2015 full-length exposition. Beezer and Farrell (2000) explicitly computed the **ordinary matching polynomials** of these graphs; those enumerate disjoint-edge sets without the induced condition and are *not* the polynomials here. Their matching-polynomial distinction is credited, not represented as new. The published independence-complex comparison for the same two graphs concerns independent **vertex** subsets \(\operatorname{Ind}(G)\), not the cliques of \(\overline{L(G)^2}\) corresponding to induced **edge** matchings; its stated results do not give the present induced-matching counts or edge-exchange geometry. The new claim is the induced-matching and optimal-edge-exchange classification above, not the first-ever way to distinguish the two graphs.

## Limitations
This is an exact finite classification for two specific graphs; it asserts no extension to larger Hamming/Doob graphs and does not claim a general theorem about all strongly regular graphs. The diameter assertion uses full finite exhaustive enumeration in addition to the structural proof of connectivity. The available source comparison cannot exclude equivalent assertions in unindexed works or inaccessible portions of the 2026 monograph *The Shrikhande Graph*. No independent external validation is represented by the present computations.

## References
1. R. A. Beezer and E. J. Farrell, *The matching polynomial of a distance-regular graph*, International Journal of Mathematics and Mathematical Sciences 23 (2000), 89–97. DOI: 10.1155/S0161171200000740. Publisher records first publication on 2000-01-15. Its Section 4 gives **ordinary** matching polynomials for the Shrikhande and rook graphs.
2. P. J. Cameron, *The Shrikhande graph*, 2010-08-26, https://cameroncounts.wordpress.com/2010/08/26/the-shrikhande-graph/. Gives the exact two strongly regular examples and their common parameters.
3. S. S. Sane, *The Shrikhande Graph*, Resonance 20 (2015), 903–918, DOI: 10.1007/s12045-015-0255-7. Full-text copy: https://people.math.binghamton.edu/zaslav/Oldcourses/510.S18/sane.shrikhande-graph.resonance2015.pdf.
4. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187. This concerns vertex independence complexes, not induced matchings.
5. P. J. Cameron, A. Lakshmanan S., and A. Vijayakumar, *The Shrikhande Graph: A Window on Discrete Mathematics*, Cambridge University Press (2026), DOI: 10.1017/9781009709118. A potentially relevant broad monograph; complete accessible text was not obtained.
