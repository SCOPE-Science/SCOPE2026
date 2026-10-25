# The ordinary three-cut complex of the Paley graph on thirteen vertices

## Finding
Let \(P_{13}\) be the Paley graph with vertex set \(\mathbb Z/13\mathbb Z\), joining distinct vertices precisely when their difference is a nonzero square. The ordinary three-cut complex \(\Delta_3(P_{13})\) has complete reduced integral homology
\[
\widetilde H_i(\Delta_3(P_{13});\mathbb Z)\cong
\begin{cases}
\mathbb Z^2,&i=7,\\
\mathbb Z,&i=8,\\
0,&\text{otherwise}.
\end{cases}
\]
More strongly, its combinatorial Alexander dual \(K=\Delta_3(P_{13})^\vee\) has the exact homotopy type
\[
K\simeq S^2\vee S^3\vee S^3.
\]
The original three-cut complex is pure of dimension \(9\). Its lower-dimensional nonzero reduced homology therefore obstructs shellability.

## Assumptions and scope
All graphs are finite, undirected, and loopless. Write \(V=\{0,1,\ldots,12\}\) and let \(Q=\{1,3,4,9,10,12\}\) be the nonzero quadratic residues modulo \(13\). Two vertices \(u\ne v\) are adjacent in \(P_{13}\) exactly when \(u-v\pmod {13}\in Q\). This graph is strongly regular with parameters \((13,6,2,3)\), and each induced vertex neighborhood is a six-cycle.

For a three-element subset \(T\), the induced graph \(P_{13}[T]\) is disconnected exactly when it has at most one edge. The **ordinary** three-cut complex has as facets the ten-vertex sets \(V\setminus T\) for disconnected triples \(T\); this differs from the *total* three-cut complex, for which \(T\) must be independent. The Alexander dual is
\[
K=\{U\subseteq V: \text{every three-element subset of }U\text{ induces a connected graph}\}.
\]
All subsets of cardinality below three belong to \(K\). Homology is reduced and has integer coefficients unless a different coefficient ring is displayed.

## Proof
**1. Face classification.** The elementary Paley adjacency rule yields the strongly regular common-neighbor counts: every adjacent pair has two common neighbors and every nonadjacent pair has three. It also gives a six-cycle for each neighborhood. Thus \(P_{13}\) has \(39\) edges and \(26\) triangles. There are
\[
13\binom 62-3\cdot26=117
\]
induced three-vertex paths, together with \(26\) induced triangles. Consequently the number of connected induced triples, and hence the number of two-faces of \(K\), is \(143\). The full one-skeleton has \(\binom{13}{2}=78\) edges.

A four-set belongs to \(K\) if and only if every vertex has at least two neighbors within that four-set. The only possible induced forms are a four-cycle, a diamond, or a complete four-graph. A complete four-graph is impossible because a graph neighborhood induces a six-cycle. Each of the \(39\) graph edges belongs to a unique diamond: its two common neighbors are nonadjacent. There are \(39\) induced four-cycles, found by counting pairs of common neighbors of nonadjacent vertices, with each four-cycle counted twice by its two diagonals. Hence \(K\) has exactly \(78\) tetrahedra.

There is no five-vertex face. Indeed, if every triple in a five-set \(W\) were connected, every vertex of \(P_{13}[W]\) would have degree at least three, and the complement of \(P_{13}[W]\) would be a matching. There is a vertex in \(W\) adjacent to the other four. Those four vertices induce a complete four-graph minus a matching, which contains a four-cycle. This contradicts the fact that every vertex neighborhood in \(P_{13}\) is a six-cycle. The same hereditary argument rules out larger faces. The complete nonempty face vector of \(K\), in dimensions zero through three, is therefore
\[
(f_0,f_1,f_2,f_3)=(13,78,143,78).
\]

**2. Trivial fundamental group.** The complete one-skeleton of \(K\) admits the star at vertex \(0\) as a spanning tree. Its \(66\) remaining edges \(\{i,j\}\) with \(1\le i<j\le12\) freely generate the fundamental group of the graph. Every connected triple \(\{0,i,j\}\) gives a two-simplex killing its edge generator \(\{i,j\}\). Exactly \(33\) generators die this way.

For a direct finite presentation, put \(A=Q\) and \(B=V\setminus(A\cup\{0\})=\{2,5,6,7,8,11\}\). The \(33\) generators already killed are the \(15\) edges between pairs in \(A\) together with the \(18\) edges between adjacent \(A\)- and \(B\)-vertices. The other \(18\) pairs between \(A\) and \(B\) are killed by connected-triple relators \(\{i,k,b\}\) where \(i,k\in A\) are adjacent and \(k,b\) are adjacent. The remaining \(15\) pairs within \(B\) are killed by connected triples \(\{a,b,b'\}\) with a common neighbor \(a\in A\). Such neighbors exist for every pair because the sets of \(A\)-neighbors of the six elements of \(B\), in increasing order, are
\[
\{1,3,12\},\ \{1,4,9\},\ \{3,9,10\},\ \{3,4,10\},\ \{4,9,12\},\ \{1,10,12\},
\]
which intersect pairwise. The first eighteen assertions are explicitly enumerated by the accompanying checker. Consequently every fundamental-group generator dies in the two-skeleton, so \(\pi_1(K)=1\).

**3. Integral homology.** Orient every face by the increasing vertex order, and construct the signed integral simplicial boundary matrices \(\partial_1\), \(\partial_2\), \(\partial_3\). Exact integer row/column elimination gives
\[
\operatorname{rank}\partial_1=12,\qquad
\operatorname{rank}\partial_2=66,\qquad
\operatorname{rank}\partial_3=76.
\]
Moreover, a sequence of unimodular elementary operations diagonalizes each matrix with only unit nonzero diagonal entries. Thus their integer Smith factors are all \(1\), not merely nonzero modulo a prime. Their compositions vanish. The resulting reduced groups are
\[
\widetilde H_1(K;\mathbb Z)=0,\qquad
\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^{143-66-76}=\mathbb Z,
\qquad \widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{78-76}=\mathbb Z^2,
\]
with all other reduced groups zero. The complete integer reduction is carried out in `verify_paley13.py`, which reconstructs the matrices from the residue definition; the resulting equalities constitute exhaustive finite calculations.

**4. Homotopy type and duality.** Since \(K\) is simply connected and three-dimensional, its two-skeleton is homotopy equivalent to a wedge of two-spheres. The attaching maps of the three-cells are determined by the integers in \(\pi_2\), by Hurewicz. The free integral \(H_2(K)\) and \(H_3(K)\), together with Smith normal form, permit elementary changes of two- and three-cell bases that cancel all unit-degree cell pairs, leaving one two-sphere and two three-spheres. Equivalently, a cellular homotopy equivalence from \(S^2\vee S^3\vee S^3\) induces an integral homology isomorphism and hence a homotopy equivalence by the simply connected Whitehead theorem. This proves the claimed homotopy equivalence for the **dual**, without asserting one for the original cut complex.

Combinatorial Alexander duality on thirteen vertices supplies
\[
\widetilde H_i(\Delta_3(P_{13});\mathbb Z)\cong
\widetilde H^{10-i}(K;\mathbb Z).
\]
The integral cohomology of \(K\) is free and concentrated in degrees two and three, so the original reduced homology is \(\mathbb Z^2\) in degree seven, \(\mathbb Z\) in degree eight, and zero otherwise. Every facet is a ten-vertex complement of a disconnected triple, so the original complex is pure of dimension nine. A pure shellable nine-complex has reduced homology only in dimension nine; thus this complex is not shellable.

## Verification
Run `python3 verify_paley13.py` using the Python standard library. It computes the adjacency matrix from quadratic residues; checks all common-neighbor counts and six-cycle links; enumerates every face of the dual up to cardinality five; checks every one of the \(2^{13}=8192\) vertex subsets against the defining Alexander-dual criterion; verifies all relevant triangle relators kill the \(66\) fundamental-group generators; builds the signed integral boundary matrices and verifies consecutive differentials compose to zero; and proves the integer diagonalizations using only unit pivots and unimodular row and column operations. It rejects a nonzero residual block and prints `VERIFY_OK` only if all tests pass. This is finite, complete enumeration for the specified thirteen-vertex graph, not extrapolation to other Paley graphs.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue [1] introduced ordinary cut complexes and treated selected families and general structural results. Their hypotheses and conclusions do not determine the thirteen-vertex Paley example: in particular, the complete-skeleton condition in their general homology criterion does not hold because the dual has tetrahedra. Their sequel [2] treats other graph operations and grid-related examples. The total-cut complex [3] is a different construction.

Published exact calculations for the order-thirteen Paley **Lovász neighborhood complex** concern the simplicial complex of subsets of an open graph neighborhood, not the dual of its ordinary cut complex. Published ordinary three-cut computations for the cuboctahedral and icosahedral graphs have different defining graph vertex sets and do not imply these groups. A four-cycle-free graph theorem does not apply because this Paley graph has \(39\) four-cycles. Targeted comparisons found no covering mathematical statement; this is evidence of noncoverage among checked sources, not proof that no equivalent unindexed result exists.

## Limitations
The classification is for exactly the thirteen-vertex undirected Paley graph. It does not claim a homotopy-type classification of the original cut complex, equivariant homology representations, or an infinite Paley-family theorem. Finite calculations are fully reproducible in the standalone checker. Novelty is assessed against inspected sources rather than certified universally; no independent validation of the new finding is claimed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public 2023-04-26, https://arxiv.org/abs/2304.13675.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public 2024-07-11, https://arxiv.org/abs/2407.08158.
3. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, https://arxiv.org/abs/2209.13503.
4. Published comparative record, *The neighborhood complex of the order-thirteen Paley graph is a wedge of twenty-five two-spheres*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-neighborhood-complex-of-the-order-13-paley-graph-is-a-wedge--3f8cbbf12bfc.
5. Published comparative record, *The cuboctahedral three-cut complex is a mixed-dimensional sphere wedge*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-cuboctahedral-three-cut-complex-is-a-mixed-dimensional-spher--64f6ee0f1faa.
6. Published comparative record, *Three-cut complexes of four-cycle-free graphs with triangles*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-cut-complexes-of-four-cycle-free-graphs-with-triangles--06da2f0ef7ce.
