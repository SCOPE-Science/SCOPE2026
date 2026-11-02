# First failures of vertex-deletion monotonicity for orientable total domination

## Finding

Let \(G\) be a finite simple connected graph for which both \(G\) and \(G-v\) admit valid orientations. Write \(\mathrm{DOM}_t(G)\) for the largest directed total-domination number across the valid orientations of \(G\). The conjectured deletion inequality \(\mathrm{DOM}_t(G)\le \mathrm{DOM}_t(G-v)+1\), proposed by Anderson, Dravec, Johnston and Kuenzel, fails already at order six.

More precisely, for every integer \(m\ge5\), let \(G_m\) have vertices \(c_0,\ldots,c_{m-1},\ell\), the edges of the cycle \(c_0c_1\cdots c_{m-1}c_0\), the chord \(c_0c_2\), and the pendant edge \(c_1\ell\). Then

\[
\mathrm{DOM}_t(G_m)=m,
\qquad
\mathrm{DOM}_t(G_m-c_3)=m-2.
\]

Thus the deletion gap is exactly two in an infinite family, and order six is the least possible order of a connected counterexample.

There is also an exhaustive first-failure census. Among all simple graphs on six fixed labeled vertices and all choices of a distinguished deleted vertex, **exactly 9000** labeled pairs \((G,v)\) satisfy that both orientations are admissible and \(\mathrm{DOM}_t(G)>\mathrm{DOM}_t(G-v)+1\). These form **exactly 18** marked-graph isomorphism classes and arise from **5850** distinct labeled underlying graphs. A marked isomorphism must carry the distinguished deleted vertex to the distinguished deleted vertex.

## Assumptions and scope

A valid orientation \(D\) of an undirected graph is an orientation in which every vertex has at least one incoming arc. A directed total dominating set is a subset \(S\) such that each vertex, including vertices in \(S\), has an in-neighbor belonging to \(S\). Denote the least size of such a set by \(\gamma_t(D)\), and define \(\mathrm{DOM}_t(G)=\max_D\gamma_t(D)\), with \(D\) ranging over valid orientations. An undirected graph admits a valid orientation exactly when every connected component contains a cycle. The deletion problem is considered only when both \(G\) and \(G-v\) admit valid orientations.

The infinite family is indexed by all integers \(m\ge5\); no assertion is made here about the maximum possible deletion gap across arbitrary orders. The finite census concerns every one of the \(2^{15}\) undirected simple labeled graphs on six vertices, every distinguished vertex, and every valid orientation, without graph-shape restrictions.

## Proof

**Infinite family.** Orient the main cycle cyclically \(c_i\to c_{i+1}\), with subscripts modulo \(m\); orient the extra edges \(c_0\to c_2\) and \(c_1\to\ell\). This is valid. The vertices \(c_0,c_1,\ldots,c_{m-1}\) are individually indispensable in any directed total dominating set: the respective vertices \(c_1,\ell,c_3,c_4,\ldots,c_{m-1},c_0\) each have exactly one in-neighbor, namely the indicated cycle vertex in the same order. In particular, the chord does not change the unique in-neighbor of \(c_3\). Hence this orientation has \(\gamma_t=m\).

In *every* valid orientation, the pendant edge must point from \(c_1\) to \(\ell\), because \(\ell\) requires positive indegree. Thus no cycle vertex can have \(\ell\) as an in-neighbor. All cycle vertices together total dominate every vertex in every valid orientation, giving \(\mathrm{DOM}_t(G_m)\le m\). Equality follows.

Deleting \(c_3\) leaves the triangle on \(c_0,c_1,c_2\), a pendant path from \(c_0\) ending at \(c_4\), and the leaf \(\ell\) attached to \(c_1\). This graph has \(m\) vertices, exactly one cycle, and exactly two leaves. Every valid orientation of a connected unicyclic graph is obtained by orienting its sole cycle consistently and orienting all remaining edges away from that cycle. Its nonleaf vertices are precisely the forced directed total dominating set: each is the unique in-neighbor of its successor along the oriented cycle or along an outward path. Therefore its directed total-domination number is the number of nonleaves, \(m-2\), for every valid orientation. This proves the displayed gap.

**Least order.** If a connected graph \(H\) has a valid orientation with \(\gamma_t(D)=|V(H)|\), each vertex is indispensable to the full vertex set. Therefore each vertex is the sole in-neighbor of some vertex. These sole-in-neighbor witnesses are distinct and exhaust all vertices, so every vertex has indegree exactly one. Consequently the underlying graph is unicyclic, and validity forces its cycle to be directed cyclically and all other edges outward. A vertex off that cycle is a leaf or lies on an outward path, so deleting a terminal leaf from the full selected set still totally dominates; hence \(H\) must itself be a cycle. Thus a connected noncycle satisfies \(\mathrm{DOM}_t(H)\le |V(H)|-1\).

If \(G-v\) admits a valid orientation, \(G\) cannot be a cycle. Also every directed total dominating set induces a subdigraph of minimum indegree at least one, and hence contains a directed cycle of length at least three. Therefore \(\mathrm{DOM}_t(G-v)\ge3\). For \(|V(G)|\le5\), these observations give

\[
\mathrm{DOM}_t(G)-\mathrm{DOM}_t(G-v)
\le (|V(G)|-1)-3\le1.
\]

The graph \(G_5\) has six vertices and attains gap two, establishing minimum order.

**Exhaustive six-vertex census.** The included C++17 verifier implements the definitions directly, not an inference from a conjectured formula. An undirected graph is represented by one bit for each of the 15 potential edges in lexicographic vertex-pair order. The verifier visits all \(2^{15}\) such masks. By the preceding bounds, any six-vertex counterexample necessarily satisfies \(\mathrm{DOM}_t(G)=5\) and \(\mathrm{DOM}_t(G-v)=3\), so the verifier computes the parent invariant only when a deleted graph has the latter value. For every graph whose orientation invariant is needed, it visits all \(2^e\) directions, where \(e\) is the edge count, discarding orientations with any vertex of indegree zero. For each remaining orientation and each selected-vertex bitmask, it forms the union of selected vertices' out-neighborhoods. Equality with the full vertex set characterizes directed total domination; the least cardinality is computed, then maximized over orientations. Every deletion is represented by the induced five-vertex graph. For graph/vertex pairs satisfying the strict gap inequality, the verifier takes the least encoding under all \(6!\) vertex permutations, remembering the distinguished vertex, so equality of canonical encodings is equivalent to marked-graph isomorphism.

The complete output is 9000 labeled marked pairs, 5850 underlying labeled graphs, and 18 canonical marked classes. Below is the entire canonical class list. Graph masks use lexicographic edge order \((01,02,03,04,05,12,13,14,15,23,24,25,34,35,45)\) with the first edge as the least-significant bit. The second column identifies the deleted vertex. Class sizes sum to 9000.

| Graph mask | Deleted vertex | Labeled marked pairs |
| ---: | ---: | ---: |
| 926 | 1 | 180 |
| 958 | 1 | 360 |
| 1749 | 2 | 720 |
| 1751 | 1 | 720 |
| 1751 | 4 | 360 |
| 1759 | 1 | 360 |
| 1781 | 2 | 720 |
| 1881 | 2 | 360 |
| 1883 | 1 | 720 |
| 1885 | 2 | 720 |
| 1887 | 1 | 720 |
| 1916 | 0 | 360 |
| 1917 | 0 | 720 |
| 1917 | 2 | 720 |
| 2013 | 2 | 180 |
| 2014 | 1 | 360 |
| 2015 | 1 | 360 |
| 2015 | 2 | 360 |

## Verification

Compile the supplied `verify_census.cpp` using `c++ -O3 -std=c++17 verify_census.cpp -o verify_census`, then run `./verify_census`. It exhaustively checks the bound through five vertices and performs the complete six-vertex marked census, including canonical isomorphism representatives. Its output terminates in `VERIFY_OK`. The second supplied program, `verify_family.py`, independently enumerates valid orientations of the family and all selected sets for \(5\le m\le8\); its output also terminates in `VERIFY_OK`. As a separate cross-check of the finite orbit count, `verify_atlas.py` independently inspects the NetworkX six-vertex graph atlas using direct in-neighborhood enumeration and a marked-graph isomorphism test; it confirms 18 isomorphism classes. The stated infinite-family equations and least-order obstruction have human-readable proofs above; no finite experiment is offered as a substitute.

## Relationship to prior work

Anderson, Dravec, Johnston and Kuenzel's 2023 paper formulates the upper orientable total-domination vertex-deletion bound as Conjecture 2.7 and proves the connected-unicyclic formula used here. Blázsik and Nagy's 2024 paper classifies *individual graphs* with upper orientable total-domination number one below their order. That classification provides stronger prior coverage of the first displayed equality and, together with the unicyclic formula, could also be used to deduce the gap-two family. These prior contributions are explicitly acknowledged. Neither inspected work supplies the complete six-vertex marked deletion census or explicitly resolves the vertex-deletion conjecture by the present obstruction. The primary independently assessable additional information here is the smallest-counterexample classification, including its full 18-orbit census, in the context of a concrete refutation.

## Limitations

The theorem does not establish a universal replacement bound of two: gaps larger than two at greater orders are neither proved nor excluded. The order-six census rests on exhaustive finite search with openly specified loops and independent computational cross-checks; it does not assert a purely hand-classified list of graph forms. The 2024 extremal classification makes part of the infinite-family parameter calculation a consequence of existing stronger work, so no novelty is claimed for the isolated value \(\mathrm{DOM}_t(G_m)=m\). An unindexed first-failure census or unpublished refutation may exist. Mathematical priority has not been independently established.

## References

1. S. E. Anderson, T. Dravec, D. Johnston, K. Kuenzel, *Orientable total domination in graphs*, arXiv:2311.16307v1, first publicly submitted 2023-11-27. Section 2, Proposition 2.3 and Conjecture 2.7. https://arxiv.org/abs/2311.16307
2. Z. L. Blázsik, L. V. Nagy, *Characterization of graphs with orientable total domination number equal to \(|V|-1\)*, arXiv:2411.04560v1, first publicly submitted 2024-11-07. Theorem 1.3 and structural families. https://arxiv.org/abs/2411.04560
