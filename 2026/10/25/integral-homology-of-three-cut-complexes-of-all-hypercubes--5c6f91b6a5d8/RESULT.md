# Integral homology of three-cut complexes of all hypercubes

## Finding
For each integer \(d\ge3\), let \(Q_d\) be the graph on binary strings \(\{0,1\}^d\), with two strings joined when their Hamming distance is one. Let \(\Delta_3(Q_d)\) denote the **ordinary** three-cut complex: its facets are the complements of three-vertex subsets inducing a disconnected graph. Define
\[
 n=2^d,\qquad
 a_d=2^{d-2}\left(4-2d+\binom{d}{2}\right)-1,\qquad
 b_d=2^{d-1}\left(2^d-1-d-\binom{d}{2}\right).
\]
Then the combinatorial Alexander dual \(L_d=\Delta_3(Q_d)^\vee\) admits a complete integral homotopy decomposition
\[
 L_d\simeq\bigvee^{b_d}S^1\vee\bigvee^{a_d}S^2.
\]
Consequently the **complete reduced integral homology** of the original cut complex is
\[
\widetilde H_i(\Delta_3(Q_d);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{a_d},&i=n-5,\\
\mathbb Z^{b_d},&i=n-4,\\
0,&\text{otherwise}.
\end{cases}
\]
Both ranks are strictly positive for \(d\ge3\), so no \(\Delta_3(Q_d)\) in this family is shellable. For the first three dimensions of the family, the ordered pairs \((a_d,b_d)\) are \((1,4)\), \((7,40)\), and \((31,256)\) at \(d=3,4,5\), respectively. Thus \(\Delta_3(Q_4)\) has \(\mathbb Z^7\) in reduced degree eleven and \(\mathbb Z^{40}\) in reduced degree twelve, with no other reduced integral homology.

## Assumptions and scope
All graph vertices and edges are unweighted, and all homology groups have coefficients in \(\mathbb Z\). The cut convention is the complement-of-disconnected-induced-triples convention, **not** the total three-cut complex defined using independent triples. The equality \(L_d=\Delta_3(Q_d)^\vee\) uses the combinatorial Alexander dual within the full \(n\)-element ground set; a face of \(L_d\) contains no disconnected three-element subset. The displayed wedge is a homotopy classification of \(L_d\), not an asserted homotopy classification of \(\Delta_3(Q_d)\).

## Proof
**1. The Alexander-dual faces.** All singleton and two-element sets are faces of \(L_d\). A three-vertex subset belongs to \(L_d\) precisely when its induced graph is connected. The cube is bipartite and has no triangles, so this means that the three vertices form a two-edge path. A four-vertex subset of \(L_d\) must have every induced triple connected; counting at least two induced edges per triple forces at least four edges on the four vertices. Any induced four-vertex bipartite graph has at most four edges, so equality forces a complete \(K_{2,2}\), namely one square face of the cube. Conversely all four subsets of each cubical square belong to \(L_d\). No five-vertex set lies in \(L_d\): any two four-element subsets sharing a connected triple would have to be the same square, since a two-edge path lies in a unique cubical square. Thus the only simplices above dimension one are the four triangles and one tetrahedron on each cubical square.

**2. A simply connected square core.** Let \(C_d\subset L_d\) consist of all vertices, those edges joining cube vertices at Hamming distance one or two, and all the triangles and tetrahedra belonging to cubical squares. Each distance-two edge \(uv\) is homotopic within the triangle of a square to the two-step edge path through a common neighbor of \(u,v\). Therefore every loop of \(C_d\) is homotopic to a loop using only edges of the original graph \(Q_d\). The square boundary of every two-face of the standard Euclidean \(d\)-cube bounds a disk of triangles within its tetrahedron in \(C_d\). The one-skeleton of the \(d\)-cube with these square disks attached is simply connected: it is the two-skeleton of the contractible cubical cell complex \([0,1]^d\), and cells of dimension at least three do not affect its fundamental group. Hence \(C_d\) is simply connected.

**3. Dimension reduction and the sphere count.** The number of square faces is \(q_d=2^{d-2}\binom d2\). Each path triangle lies in exactly one such square tetrahedron, and each tetrahedron has a triangular face not shared with another tetrahedron. Elementary collapse along one private triangle of each tetrahedron leaves a simply connected two-dimensional finite CW complex. Its second integral homology is free, and its homotopy type is a wedge of two-spheres: by the Hurewicz theorem, sphere maps represent a basis of second homology, and the induced homology equivalence from a wedge of spheres is a homotopy equivalence by the simply connected Whitehead theorem.

The face vector of \(C_d\) (vertices, edges, triangles, tetrahedra) is exactly
\[
\left(2^d,\ 2^{d-1}\left(d+\binom d2\right),\ 2^d\binom d2,\ 2^{d-2}\binom d2\right).
\]
The edge count follows from Hamming distances one and two; each square supplies four unique path triangles. Connectedness, simple connectivity, and the collapse to dimension two imply \(\chi(C_d)=1+\operatorname{rank}H_2(C_d;\mathbb Z)\). The alternating face count yields
\[
\operatorname{rank}H_2(C_d;\mathbb Z)
=2^{d-2}\left(4-2d+\binom d2\right)-1=a_d.
\]

**4. The long edges and the dual homotopy type.** Every pair of distinct cube vertices is an edge of the one-skeleton of \(L_d\); however, if the pair has Hamming distance at least three, that edge lies in no triangle. Thus \(L_d\) is obtained from the connected complex \(C_d\) by freely attaching one one-cell between existing vertices for each pair at Hamming distance at least three. After choosing paths inside \(C_d\), each such addition wedges on a circle. The number of these long edges is
\[
 b_d=\frac{2^d}{2}\sum_{j=3}^d\binom dj
 =2^{d-1}\left(2^d-1-d-\binom d2\right).
\]
Consequently \(L_d\simeq\bigvee^{b_d}S^1\vee\bigvee^{a_d}S^2\). In particular there is no torsion in the integral homology or cohomology of \(L_d\).

**5. Integral duality and non-shellability.** Combinatorial Alexander duality on \(n\) vertices gives natural group isomorphisms
\[
\widetilde H_i(\Delta_3(Q_d);\mathbb Z)
\cong\widetilde H^{\,n-i-3}(L_d;\mathbb Z).
\]
The dual's only nonzero reduced integral cohomology groups are \(\mathbb Z^{b_d}\) in degree one and \(\mathbb Z^{a_d}\) in degree two. Substituting those two degrees proves the asserted complete integral homology, with no undetected torsion. Since every facet of \(\Delta_3(Q_d)\) has \(n-3\) vertices, its dimension is \(n-4\). A pure shellable complex has reduced homology only in its top dimension, whereas \(a_d>0\) for every \(d\ge3\). Thus every member of the family is nonshellable.

## Verification
The standalone file `VERIFY.py` reconstructs the Alexander-dual faces for the cubes in dimensions three, four, and five. For dimensions three and four it forms exact signed integral boundary matrices, checks their chain identities, and computes integer Smith normal forms; every nonzero invariant factor is one. It obtains the ranks \((7,17,6)\) for \((\partial_1,\partial_2,\partial_3)\) at \(d=3\) and \((15,65,24)\) at \(d=4\). For \(d=5\) it independently checks the dimensions and verifies that the second-boundary rank modulo two is \(209\), consistent with \((a_5,b_5)=(31,256)\). These checks support, but do not replace, the dimension-independent proof above. Execute `python VERIFY.py` with Python and SymPy.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced ordinary cut complexes and investigated their topology, shellability, and face lattices [1]. Their Theorem 6.1 gives an at-most-two-degrees conclusion when the full codimension-one skeleton is present; that hypothesis **fails** here because complements of cubical squares are missing codimension-one faces. Their sequel [2] studies disjoint unions, squared paths, and rectangular grids, not the hypercube family. A later work on rectangular grids [3] likewise does not cover Cartesian powers of an edge.

The ordinary three-cut complex of the three-dimensional cube was previously shown to have homotopy type \(S^3\vee\bigvee^4 S^4\) [4], matching the \(d=3\) instance here; that individual calculation is not claimed as new. An existing theorem for triangle-free graphs with edge-disjoint squares [5] does not apply to \(Q_d\): every graph edge belongs to \(d-1\ge2\) distinct squares. The total three-cut complex of \(Q_4\) was previously classified [6], but it uses only independent triples and is a different complex. The present uniform ordinary-cut computation is neither a special case of those statements nor a change of notation for their parameters.

## Limitations
This is a theorem about the ordinary three-cut complex for integer dimensions \(d\ge3\), plus the homotopy type of its **Alexander dual**. No homotopy decomposition or automorphism representation of the cut complex itself is claimed. The finite checker only covers dimensions three through five; the infinite assertion is proved geometrically and combinatorially. A literature search, even one examining the closest full documents and published records, cannot exclude an equivalent result absent from the sources indexed or retrieved.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first posted 2023-04-26, especially Sections 5–7.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first posted 2024-07-11, especially Introduction and Sections 4–6.
3. H. Chandrakar, N. R. Hazra, D. Rout, A. Singh, *Topology of Total Cut Complexes and Cut Complexes of Grid Graphs*, arXiv:2408.07646, first posted 2024-08-14, especially Introduction.
4. *The cube is a minimal forbidden graph for three-cut-complex shellability*, publicly available research record, identifier `4ccdf01d9eec` (case \(d=3\)).
5. *Three-cut complexes of triangle-free graphs with edge-disjoint squares*, publicly available research record, identifier `8ca830284420` (different hypotheses).
6. *The total three-cut complex of the four-cube: a 129-sphere wedge and its hyperoctahedral character*, publicly available research record, identifier `ccb644c2e2a2` (different functor).
