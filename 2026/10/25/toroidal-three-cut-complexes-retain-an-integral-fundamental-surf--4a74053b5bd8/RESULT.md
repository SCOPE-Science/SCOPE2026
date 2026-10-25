# Toroidal three-cut complexes retain an integral fundamental-surface class

## Finding
Let \(m,n\geq5\) be integers, put \(N=mn\), and let \(G=C_m\mathbin{\square} C_n\) be the Cartesian product of simple cycle graphs. Write \(\Delta=\Delta_3(G)\) for its **ordinary** three-cut complex: the facets of \(\Delta\) are the complements of three-vertex subsets inducing disconnected subgraphs of \(G\). Its combinatorial Alexander dual \(K=\Delta^\vee\), taken on all \(N\) graph vertices, has the integral homotopy type
\[
K\simeq (S^1\times S^1)\ \vee\ \bigvee^{\,N(N-13)/2} S^1.
\]
In particular, the complete reduced integral homology of the cut complex is
\[
\widetilde H_j(\Delta;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=N-5,\\
\mathbb Z^{\,N(N-13)/2+2},&j=N-4,\\
0,&\text{otherwise}.
\end{cases}
\]
The positive cup product of two degree-one generators of the torus summand is nonzero in \(H^2(K;\mathbb Z)\). Every \(\Delta\) in the family is pure of dimension \(N-4\) and **not shellable**. The first case, \(m=n=5\), has \(\widetilde H_{20}(\Delta;\mathbb Z)=\mathbb Z\) and \(\widetilde H_{21}(\Delta;\mathbb Z)=\mathbb Z^{152}\).

## Assumptions and scope
The two factors are cycle graphs with edges between consecutive residues, indices interpreted modulo \(m\) or \(n\). The product graph has vertex set \(\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\), and two vertices are adjacent when they differ by one along exactly one factor. The bounds \(m,n\geq5\) exclude the additional four-cycles and multiple two-step paths arising from shorter factors. An ordinary three-cut facet is the complement of a **disconnected induced triple**, not necessarily the complement of an independent triple; the latter defines a different, total cut complex.

An elementary collapse here always means deleting a free face together with its unique maximal coface. The wedge point in the stated homotopy equivalence may be chosen at any graph vertex. A wedge of circles is a one-dimensional CW bouquet. All homology groups use integral coefficients.

## Proof
**1. An exact description of the dual.** By the definitions of the ordinary cut complex and Alexander duality, a subset \(S\subseteq V(G)\) belongs to \(K\) if and only if **every three-element subset of \(S\) induces a connected graph**. Therefore every vertex and every pair is a face of \(K\). The graph \(G\) is triangle-free, so an admissible triple is exactly the vertex set of an induced two-edge path.

For any set of at least five vertices whose every triple is connected, each vertex would have at most one nonneighbor among the other vertices (otherwise a triple would have an isolated vertex). Choosing any five such vertices would thus yield a triangle-free graph of minimum degree at least three, impossible: the neighbors of a degree-three vertex are mutually nonadjacent and cannot themselves all have degree at least three on five vertices. Similarly, a four-element set satisfies the triple condition exactly when its induced subgraph is a four-cycle: minimum degree at least two, with triangle-freeness, forces the induced square. It follows that \(K\) has no simplices above dimension three; its triangles are precisely induced two-edge paths, and its tetrahedra are precisely the four-cycles of \(G\).

**2. The two-step geometry of the torus grid.** The graph is 4-regular with \(N\) vertices and \(2N\) edges. Since both factors have at least five vertices, its only four-cycles are the \(N\) coordinate unit squares. Each two-edge path whose edges follow different coordinate directions is a corner of exactly one such square, and the pair of its endpoints has exactly two common neighbors. Each straight two-edge path, with both edges in one factor, has endpoints with exactly one common neighbor. There are \(2N\) unordered straight endpoint pairs and \(2N\) unordered opposite-corner pairs, in total \(4N\) pairs at graph distance two. Every other nonedge has no common neighbor. Thus the number of pairs at graph distance at least three is
\[
L=\binom N2-2N-4N=\frac{N(N-13)}2.
\]
All these claims follow directly from the residues defining the Cartesian product; they hold equally for odd and even factors. Each square diagonal is associated with a **unique** square, although distinct squares share original graph edges.

**3. Exact collapses to a filled torus and long edges.** Cyclically label an arbitrary square \(a,b,c,d\), with \(a,b\) along the first coordinate and \(a,d\) along the second. First, for every square collapse its tetrahedron \(abcd\) across the face \(abc\). This face belongs to no other tetrahedron because the corner path \(a-b-c\) determines that square uniquely. Once all square tetrahedra are removed, collapse the triangle \(acd\) along its now-free diagonal edge \(ac\). The only two triangles that ever contained that diagonal were \(abc\) and \(acd\), both from this square. These moves are independent over all squares.

Every remaining straight two-edge path \(u-w-v\) supplies a triangle \(uwv\) with a free edge \(uv\): the endpoints have a unique common neighbor, and such a triangle belongs to no square tetrahedron. Collapse that triangle and its free edge. No other higher-dimensional simplices survive. Exactly two triangles per square remain, namely \(abd\) and \(bcd\), meeting along diagonal \(bd\). They triangulate the corresponding square disk and meet neighboring square disks along the original graph edges. All original graph edges remain. The only additional surviving edges join pairs of graph distance at least three, and no two-simplex uses such an edge.

Consequently these \(4N\) elementary collapses leave precisely the standard simplicial square subdivision of the \(m\)-by-\(n\) periodic torus, together with \(L\) independent extra one-cells joining pairs of vertices already in the connected torus. Attaching a new one-cell between two points of a path-connected CW complex adds one wedged circle up to homotopy. Thus
\[
K\simeq (S^1\times S^1)\vee\bigvee^{L}S^1.
\]
The two-torus is the rectangle \([0,m]\times[0,n]\) with opposite sides identified; its fundamental two-cycle comes from the consistently oriented \(N\) square disks. In particular, \(\widetilde H^1(K;\mathbb Z)\cong\mathbb Z^{L+2}\), \(\widetilde H^2(K;\mathbb Z)\cong\mathbb Z\), and every other reduced integral cohomology group is zero. The torus cup product remains nonzero after the circle attachments.

**4. Return to the ordinary cut complex.** Integral combinatorial Alexander duality for the full \(N\)-element ground set gives
\[
\widetilde H_j(\Delta;\mathbb Z)\cong
\widetilde H^{N-j-3}(K;\mathbb Z).
\]
Substituting the preceding cohomology groups gives the two stated ranks in degrees \(N-5\) and \(N-4\), with no torsion. Every facet of \(\Delta\) has \(N-3\) vertices, so \(\Delta\) is pure of dimension \(N-4\). Its nonzero homology in the strictly lower degree \(N-5\) excludes pure shellability.

## Verification
The self-contained standard-library Python program `verify.py` rebuilds the entire graph and all simplices of \(K\) from the exact triple-connectivity criterion; determines all four-simplices from that criterion, rather than assuming the square list; and checks every proposed free-face/coface collapse in its actual current simplicial complex. It then compares the residual complex with an independently generated triangulation of the torus plus exactly the predicted long edges. It verifies the closed orientable square incidence and cancels the complete signed two-cycle boundary. It checks \((m,n)=(5,5),(5,6),(6,6),(5,7)\); the first two cases additionally exhaust all five-element subsets for the absence of higher faces. Run `python3 verify.py`; successful completion prints `VERIFY_OK`. Representative outputs are `PASS 5 5 ... long_edges 150 ... cut_homology_ranks (1, 152)` and `PASS 5 6 ... long_edges 255 ... cut_homology_ranks (1, 257)`. The infinite two-parameter theorem is established by the structural proof above, not by extrapolating finite tests.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue [1] introduced ordinary cut complexes and integral combinatorial Alexander duality in this setting, treating graph classes including cycles, trees, and complete multipartite graphs. Their successor paper [2], Section 5, determines the **shellable**, top-dimensional three-cut homology of **rectangular path grids** \(P_m\square P_n\); its square filling is a disk, not a torus. Chandrakar, Hazra, Rout, and Singh [3] also focus on rectangular \(2\times n\) and \(3\times n\) path grids. These hypotheses and conclusions do not yield the two nonzero homology degrees of the periodic product of cycles.

The published edge-disjoint-square theorem [4] collapses ordinary three-cut Alexander duals to graphs when every pair of four-cycles is edge-disjoint. Here **every original graph edge belongs to two squares**, and the surviving full square cellulation carries an essential two-dimensional fundamental class; hence [4] does not cover the result. The square-completion theorem for intrinsic graph Čech nerves [5] identifies the same torus cellulation but applies to a distinct nerve with additional two-spheres; it does not determine this ordinary cut complex. A separate result [6] studies integral equivariant extensions for the **total two-cut** complex of toroidal grids, a different simplicial criterion and homological degree. The terminology **three-robust clique complex** [7] is also not interchangeable with this Alexander dual: that object forbids only independent triples, whereas the dual here forbids every disconnected triple (including triples spanning exactly one edge). Its general bipartite homotopy theorem therefore does not imply the present result. These are relevant analogies, not sources of the claimed ordinary three-cut classification.

## Limitations
The statement assumes \(m,n\ge5\); it makes no assertion for shorter cycles, twisted periodic boundary conditions, total cut complexes, higher cut parameters, or the complete homotopy type of the original \(\Delta_3(G)\). While the dual's torus summand has nonzero cup product, no cup-product claim is made for the original cut complex. The attached program verifies concrete sample values and explicit elementary collapses; it is not an independent proof of all integer parameters. An uncatalogued equivalent theorem expressed as a three-wise-connected hypergraph complex or as Stanley–Reisner duality remains a bibliographic possibility. Independent mathematical validation has not been performed.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public version 2023-04-26), https://arxiv.org/abs/2304.13675; particularly the definition and Sections 6–7.

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first public version 2024-07-11), https://arxiv.org/abs/2407.08158; particularly Section 5.

[3] H. Chandrakar, N. R. Hazra, D. Rout, and A. Singh, *Topology of total cut complexes and cut complexes of grid graphs*, arXiv:2408.07646 (first public version 2024-08-14), https://arxiv.org/abs/2408.07646.

[4] *Three-cut complexes of triangle-free graphs with edge-disjoint squares*, publicly indexed research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-cut-complexes-of-triangle-free-graphs-with-edge-disjoint-s--8ca830284420.

[5] *Square-completion decomposition of scale-two graph Čech nerves*, publicly indexed research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-square-completion-decomposition-of-scale-two-graph-ech-nerves--98a5c720a71e.

[6] *The integral face–winding obstruction in toroidal total two-cut complexes*, publicly indexed research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-integral-face-winding-obstruction-in-toroidal-total-two-cut--a66192a534f8.

[7] *A three-sphere wedge theorem for robust clique complexes of all connected bipartite graphs*, publicly indexed research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-three-sphere-wedge-theorem-for-robust-clique-complexes-of-all--8d06720b1a2b.
