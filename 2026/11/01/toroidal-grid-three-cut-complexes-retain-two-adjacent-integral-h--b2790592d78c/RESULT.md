# Toroidal-grid three-cut complexes retain two adjacent integral homology degrees

## Finding
For every pair of integers \(m,n\ge5\), let \(G=C_m\square C_n\), let \(N=mn\), and let \(\Delta_3(G)\) be the ordinary three-cut complex. Its facets are the complements of three-vertex sets inducing disconnected subgraphs. Its Alexander dual has the explicit homotopy type
\[
\Delta_3(G)^\vee\simeq (S^1\times S^1)\vee\bigvee^{\binom{N}{2}-6N}S^1.
\]
Consequently its reduced integral homology is
\[
\widetilde H_j(\Delta_3(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=N-5,\\
\mathbb Z^{\binom{N}{2}-6N+2},&j=N-4,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, all these homology groups are torsion-free and none of the ordinary three-cut complexes in this family is shellable. This is an integral homology classification and an Alexander-dual homotopy classification; no homotopy classification of \(\Delta_3(G)\) itself is asserted.

## Assumptions and scope
The cycles have distinct vertices indexed by \(\mathbb Z/m\mathbb Z\) and \(\mathbb Z/n\mathbb Z\). The graph has vertex set \(V=\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\), with edges between pairs differing by \(\pm1\) in exactly one coordinate. The lower bound five on both cycle lengths ensures that all four-cycles are elementary coordinate squares and that every graph-distance-two pair has the unique length-two path required below, except the pairs of opposite corners of one coordinate square, which have exactly two such paths. The claim includes every \(m,n\ge5\), without parity restrictions.

Write \(K=\Delta_3(G)^\vee\), with combinatorial Alexander duality taken relative to the full \(N\)-vertex ground set. By definition, a set \(F\subseteq V\) is a face of \(K\) exactly when it contains no disconnected three-subset. Thus \(K\) has all vertices and all two-subsets as faces, and a triple is a face precisely when the induced three-vertex graph is connected.

## Proof
**1. Complete face classification.** The graph is triangle-free. Hence its connected induced three-vertex sets are exactly the two-edge paths. Every vertex has degree four, so there are \(6N\) such triples: \(4N\) bent paths using one edge in each coordinate direction, and \(2N\) straight paths using two opposite edges in one coordinate direction. The four-subsets all of whose triples induce connected graphs are exactly the vertex sets of four-cycles. Indeed, counting incidences of edges with three-subsets inside a four-set yields exactly four edges; a triangle-free simple graph with four vertices and four edges is a four-cycle. These are precisely the \(N\) coordinate squares.

There are no faces containing five vertices. If every triple in a five-set had exactly two induced edges, the total number of edge–triple incidences would be \(2\binom53=20\), but each induced edge would belong to exactly three triples, a contradiction modulo three. Thus \(K\) has the face vector \((N,\binom N2,6N,N)\) in dimensions zero through three, with no larger faces.

**2. Explicit integral collapse.** Consider an elementary square with cyclically ordered vertices \(a=(i,j)\), \(b=(i+1,j)\), \(c=(i+1,j+1)\), \(d=(i,j+1)\). Its tetrahedron \(abcd\) has \(abc\) as a free triangular face because that bent three-vertex path lies in no other square. Remove the free pair \((abc,abcd)\). Now the edge \(ac\) has the triangle \(acd\) as its sole remaining coface: its endpoints differ in both coordinates, and the two other square corners \(b,d\) are their only common neighbors. Remove the free pair \((ac,acd)\). The surviving two triangles \(abd\) and \(bcd\) triangulate the original square using diagonal \(bd\). Perform these two elementary simplicial collapses independently on all \(N\) coordinate squares.

Every remaining straight-path triangle has as a free edge the chord joining the endpoints of its two-step path. That chord is contained in no other triangle: a same-coordinate distance-two pair has exactly one common neighbor when the coordinate cycle has length at least five. Collapse each of the \(2N\) straight-path triangles with its chord.

The result is an ordinary triangulation \(T\) of the square-tiled topological torus, together with edges whose endpoints are vertices of \(T\) but which lie in no higher-dimensional simplex. At the start there were \(\binom N2\) edges. The collapses remove \(N\) square diagonals and \(2N\) straight-path chords. The triangulated torus retains \(2N\) original graph edges and \(N\) chosen diagonals, for a total of \(3N\) edges. Thus the number of extra edges is
\[
L=\binom N2-(N+2N)-3N=\binom N2-6N.
\]
Each extra edge adds one free circle up to homotopy because \(T\) is connected. Elementary collapses preserve simple-homotopy type, so
\[
K\simeq T\vee\bigvee^{L}S^1\simeq(S^1\times S^1)\vee\bigvee^{L}S^1.
\]
The construction has no dependence on numerical experiments. In particular its integral reduced cohomology is \(\widetilde H^1(K;\mathbb Z)=\mathbb Z^{L+2}\), \(\widetilde H^2(K;\mathbb Z)=\mathbb Z\), and zero in all other degrees.

**3. Return to the cut complex.** Combinatorial Alexander duality gives
\[
\widetilde H_j(\Delta_3(G);\mathbb Z)\cong\widetilde H^{N-j-3}(K;\mathbb Z).
\]
Substituting the preceding integral cohomology proves exactly the displayed homology classification. Every facet of \(\Delta_3(G)\) has \(N-3\) vertices, so it is pure of dimension \(N-4\). Since \(\widetilde H_{N-5}\) is nonzero, the complex cannot be shellable: a pure shellable complex has reduced homology only, if anywhere, in its top dimension.

## Verification
The accompanying standalone Python program `toroidal_cut_checker.py` reconstructs the Alexander dual directly from the induced-connectivity criterion, exhaustively determines all faces through dimension three, validates that the tetrahedra are exactly the elementary squares, replays the two free-face collapses per square and the two straight-path collapses per vertex, and checks the torus triangulation remaining. It separately builds boundary matrices over \(\mathbb F_2\) and calculates ranks.

For \((m,n)=(5,5)\), the dual face vector is \((25,300,150,25)\) and boundary ranks are \((24,124,25)\), giving \((\beta_1,\beta_2)=(152,1)\). For \((5,6)\), the corresponding values are \((30,435,180,30)\), ranks \((29,149,30)\), and Betti numbers \((257,1)\). For \((6,6)\), they are \((36,630,216,36)\), ranks \((35,179,36)\), and Betti numbers \((416,1)\). These finite checks corroborate, but do not replace, the all-order integral proof above.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced and systematically investigated ordinary cut complexes, including cycles and several graph operations [1]. Their companion paper computes \(\Delta_3(P_m\square P_n)\) for rectangular, nonperiodic grid graphs and proves shellability in that setting [2, Section 5, especially Propositions 5.6 and 5.8]. Replacing two boundary paths with cycles gives the toroidal graph here; their rectangular result does not cover the toroidal case. Chauhan, Shukla and Vinayak classify three-cut complexes of single squared-cycle graphs, not Cartesian products of two ordinary cycles [3].

Related indexed research on toroidal grids determines discrete cubical homology, Lovász neighborhood complexes or total two-cut complexes. These use different complexes and do not supply this ordinary three-cut integral homology calculation or the explicit Alexander-dual torus collapse. Earlier calculations for hypercubes and Cartesian products of complete graphs do not imply this toroidal result: their square completions do not retain the two-dimensional fundamental class of a torus. All these comparisons concern mathematical implication, not just a title match.

## Limitations
The hypothesis \(m,n\ge5\) is essential for the stated elementary uniqueness arguments; the cases with a four-cycle factor are not covered. The theorem does not determine the homotopy type of \(\Delta_3(G)\) itself, its full equivariant homology representation, or the integral ring structure of the cut complex. Searches of indexed literature and inspected primary sources do not establish exhaustive priority; equivalent unindexed work remains possible.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first publicly submitted 2023-04-26, especially the introduction, Section 6 and concluding discussion. https://arxiv.org/abs/2304.13675

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first publicly submitted 2024-07-11, especially Section 5. https://arxiv.org/abs/2407.08158

[3] P. Chauhan, S. Shukla and K. Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979, first publicly submitted 2024-06-04, especially Theorem 1.4. https://arxiv.org/abs/2406.01979
