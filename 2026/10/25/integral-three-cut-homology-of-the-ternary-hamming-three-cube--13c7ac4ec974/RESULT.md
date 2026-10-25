# Integral three-cut homology of the ternary Hamming three-cube

## Finding
Let \(G=H(3,3)=K_3\mathbin{\square}K_3\mathbin{\square}K_3\), the graph on the \(27\) triples from \(\{0,1,2\}^3\) in which two vertices are adjacent when they differ in exactly one coordinate. Its **ordinary three-cut complex** \(\Delta_3(G)\) has complete reduced integral homology
\[
\widetilde H_i(\Delta_3(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{53},&i=22,\\
\mathbb Z^{108},&i=23,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular its homology is torsion-free, and the pure \(23\)-dimensional complex is not shellable.

## Assumptions and scope
This is the ordinary cut complex, **not** the total cut complex: its facets are precisely the complements, in the \(27\)-vertex set, of three-element sets inducing disconnected graphs. All simplicial chain groups use oriented faces with increasing lexicographic vertex order, integral coefficients, and the ordinary alternating boundary. The result concerns the single canonical graph \(H(3,3)\), with no claim for other alphabet sizes or dimensions and no homotopy-type assertion for the original cut complex.

## Proof
**1. The Alexander dual is small.** Write \(K=\Delta_3(G)^\vee\) for the combinatorial Alexander dual in the full \(27\)-vertex set. By the definition of the ordinary cut complex, a subset \(T\) is a face of \(K\) if and only if **every three-subset of \(T\) induces a connected subgraph** of \(G\). Thus \(K\) has all vertices and edges; its triangles are the connected triples of \(G\). Each of the \(27\) coordinate lines contributes one triangle, and each of the \(27\) vertices is the center of \(12\) induced two-edge paths, giving \(27+27\cdot12=351\) triangles. The \(351\) edges are simply all pairs of \(27\) vertices.

Every four-face must induce a four-cycle: the condition on all its triples forces its induced minimum degree to be at least two; four-cliques and triangles extended by a further vertex adjacent to two triangle vertices do not occur in this Hamming graph, and the only remaining possibility is a four-cycle. These are exactly the coordinate rectangles, counted by
\[
\binom32\,3\,\binom32^2=81.
\]
No fifth vertex can extend a rectangle: for a diagonal pair of a coordinate rectangle, the two common neighbors are exactly its other two corners. Therefore \(K\) has no five-faces or higher faces, and its exact face vector is \((27,351,351,81)\).

**2. Integral first and second boundary ranks.** The one-skeleton of \(K\) is the complete graph on \(27\) vertices. Its integral cycle lattice is free on the \(\binom{26}{2}=325\) edges not incident with a fixed root vertex, after eliminating the root-star tree edges. Express the \(351\) signed triangle boundaries in these integral coordinates, obtaining a \(325\)-by-\(351\) matrix. The complete, deterministic algorithm in `CHECK.py` performs integer column operations using only pivots \(+1\) or \(-1\); exactly \(217\) such pivots eliminate every nonzero column. Consequently, the image of the triangle boundary is a primitive rank-\(217\) sublattice of the cycle lattice, and
\[
H_1(K;\mathbb Z)\cong\mathbb Z^{325-217}=\mathbb Z^{108}.
\]

After those column operations, the \(134\) unpivoted triangle basis vectors span the integral kernel of the triangle boundary. The coefficients of an original chain along the unpivoted triangle labels are unchanged by the elimination, since each operation adds a selected pivot column to another column. The signed tetrahedral boundaries, expressed in these \(134\) kernel coordinates, form a \(134\)-by-\(81\) matrix. Its complete exact unit-pivot reduction makes \(81\) pivots and has no nonzero residual column. The fourth boundary is therefore injective, and its image is primitive in the integral triangle-cycle lattice. Thus
\[
H_2(K;\mathbb Z)\cong\mathbb Z^{134-81}=\mathbb Z^{53},\qquad H_3(K;\mathbb Z)=0.
\]
Connectivity and the absence of simplices above dimension three imply that these are the only positive-degree integral homology groups of \(K\). In particular there is no torsion. The reduced Euler characteristic check is \(27-351+351-81-1=-55=-108+53\).

**3. Pass back to the cut complex.** Integral combinatorial Alexander duality on \(27\) vertices identifies
\[
\widetilde H_i(\Delta_3(G);\mathbb Z)\cong
\widetilde H^{24-i}(K;\mathbb Z).
\]
The computed homology of \(K\) is free, so the universal coefficient theorem gives cohomology ranks \(108\) in degree one and \(53\) in degree two, with all other reduced cohomology zero. This proves the displayed classification. The cut complex is pure of dimension \(27-3-1=23\), but has nonzero degree-\(22\) reduced homology. Since a nonempty pure shellable simplicial complex has reduced homology only in its top degree, it cannot be shellable.

## Verification
Run `python3 CHECK.py` in the directory containing this report. The checker uses only the Python standard library. It independently constructs the complete graph and its dual faces from coordinate adjacency; confirms the complete face vector and absence of higher faces; checks the integral chain condition \(\partial_2\partial_3=0\); performs the two exhaustive unimodular \(\pm1\)-pivot eliminations; verifies ranks, freeness, and Euler characteristic; and checks the Alexander-duality degree conversion. This exact finite calculation supplies the critical integral lattice certificate; merely checking ranks over a finite field would not rule out torsion.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced and analyzed ordinary cut complexes in the 2023 preprint *Topology of Cut Complexes of Graphs*; their published results for complete multipartite graphs, clique prisms, and related operations do not calculate this three-coordinate Hamming product. Their later *Topology of Cut Complexes II* studies path-product grid graphs, defined using adjacent integer coordinates, not the product of three complete triangles. Other existing calculations cover ordinary three-cut complexes of binary cubes and two-coordinate rook graphs; these are different graphs with different associated dual chain complexes. Hamming-graph Rips, neighborhood and Čech complexes likewise do not imply this cut-complex homology. No general theorem for the specific \(27\)-vertex three-coordinate case was identified in the inspected material; unindexed equivalent work remains possible.

## Limitations
This is an exact finite-graph result, not a theorem for an infinite Hamming-graph family. It does not establish the homotopy type, cup products, symmetry representations, or shellability properties of other cut-complex parameters. Originality rests on the inspected literature and available database records and is not a claim of an exhaustive world-wide literature census. The integral proof depends on the explicit finite combinatorial enumeration and unit-pivot algorithm packaged as `CHECK.py`.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first posted 2023-04-26), SIAM Journal on Discrete Mathematics 38 (2024), 1630–1675. https://arxiv.org/abs/2304.13675
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first posted 2024-07-11). https://arxiv.org/abs/2407.08158
