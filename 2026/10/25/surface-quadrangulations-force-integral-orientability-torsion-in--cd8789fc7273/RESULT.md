# Surface quadrangulations force integral orientability torsion in ordinary three-cut complexes

## Finding

**Theorem (surface transfer for ordinary three-cut complexes).** Let \(G=(V,E)\) be a finite simple connected triangle-free graph on \(N\ge8\) vertices, cellularly embedded as a **quadrangulation** of a closed connected surface \(\Sigma\): each face has four distinct boundary vertices and its attaching cycle is a simple four-cycle. Assume also:

1. Every simple four-cycle in \(G\) is the boundary of one of the prescribed square faces.
2. Every pair of nonadjacent graph vertices has at most two common neighbors (equivalently, \(G\) contains no \(K_{2,3}\) subgraph).

Let \(\Delta_3(G)\) be the *ordinary* three-cut complex whose facets are complements of vertex triples inducing disconnected subgraphs. Define
\[
T(G)=\sum_{v\in V}\binom{\deg_G(v)}2,\qquad q(G)=\binom N2-T(G).
\]
Its combinatorial Alexander dual has the exact integral homotopy type
\[
\boxed{\Delta_3(G)^\vee\simeq\Sigma\vee\bigvee^{q(G)}S^1.}
\]
More precisely, it simplicially collapses to a triangulation of \(\Sigma\) together with exactly \(q(G)\) additional one-dimensional edges. In particular \(q(G)\ge0\). The complete reduced **integral** homology of the original complex is:

If \(\Sigma\) is orientable of genus \(g\ge0\),
\[
\widetilde H_i(\Delta_3(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=N-5,\\
\mathbb Z^{q(G)+2g},&i=N-4,\\
0,&\text{otherwise}.
\end{cases}
\]
If \(\Sigma\) is nonorientable of genus \(h\ge1\),
\[
\boxed{\widetilde H_i(\Delta_3(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&i=N-5,\\
\mathbb Z^{q(G)+h-1},&i=N-4,\\
0,&\text{otherwise}.
\end{cases}}
\]
Every such ordinary three-cut complex is pure of dimension \(N-4\) and is **not shellable**.

**Infinite torsion family.** For every pair of integers \(m,n\ge7\), take the twisted square-grid graph \(G_{m,n}\) with vertices \(v_{x,y}\), where \(x\in\mathbb Z/m\mathbb Z\), \(0\le y<n\), edges \(v_{x,y}v_{x+1,y}\), edges \(v_{x,y}v_{x,y+1}\) for \(y<n-1\), and seam edges \(v_{x,n-1}v_{-x,0}\). The square faces form a Klein-bottle quadrangulation. Write \(N=mn\). Then
\[
\widetilde H_i(\Delta_3(G_{m,n});\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&i=N-5,\\
\mathbb Z^{N(N-13)/2+1},&i=N-4,\\
0,&\text{otherwise}.
\end{cases}
\]
Thus for the natural \(7\)-by-\(7\) twisted square grid, \(\widetilde H_{44}\cong\mathbb Z/2\mathbb Z\) and \(\widetilde H_{45}\cong\mathbb Z^{883}\).

## Assumptions and scope

All surfaces are connected compact two-manifolds without boundary. The embedding and its square-face structure are part of the input. A quadrilateral face has no repeated vertex; each graph edge borders two (possibly differently oriented) faces. The hypothesis that *all* simple four-cycles are prescribed facial boundaries is essential; it excludes additional nonfacial squares. The no-\(K_{2,3}\) hypothesis prevents distinct squares from sharing a diagonal. The graph is assumed simple, triangle-free, and to have at least eight vertices. Four-cycles are allowed (indeed required) to share **edges**, so this class does not fall under the edge-disjoint-square theorem.

The combinatorial Alexander dual is on the full vertex set \(V\): a subset \(A\) is a face of \(\Delta_3(G)^\vee\) precisely if its complement is **not** a face of \(\Delta_3(G)\). By the ordinary cut definition, this is equivalent to every three-element subset of \(A\) inducing a connected subgraph of \(G\). Reduced integral homology follows the standard augmentation convention. The homotopy equivalence is non-equivariant; no automorphism representation is claimed.

## Proof

**1. Exhaustive dual-face classification.** Write \(Y=\Delta_3(G)^\vee\). Every singleton and pair is in \(Y\). A triple belongs to \(Y\) exactly when its induced graph is connected. Since \(G\) is triangle-free, each such graph is a path of length two. Every choice of a center \(v\) and two distinct neighbors contributes exactly one path triple, so \(Y\) has exactly \(T(G)\) triangular faces.

A four-element subset lies in \(Y\) exactly when each of its four triples spans a path. Its induced triangle-free graph must have four edges (two edges per triple, each edge counted twice) and hence is a simple four-cycle. By the first assumption, tetrahedra of \(Y\) correspond bijectively to the faces of the prescribed quadrangulation. No five-element face exists: if all ten triples induced by five vertices were connected, at least twenty edge incidences across triples would be needed; each graph edge occurs in three triples, demanding at least seven edges, while a triangle-free graph on five vertices has at most six (Mantel's bound). Therefore \(Y\) has no faces of dimension four or more.

**2. Elementary collapses that retain the whole surface.** Fix a cyclic ordering \((a,b,c,d)\) of the four vertices of each prescribed square. First pair its tetrahedron \(abcd\) with the triangular free face \(abc\). That triangle can lie in no other tetrahedron: the two nonadjacent endpoints \(a,c\) have exactly the common neighbors \(b,d\), by the no-\(K_{2,3}\) hypothesis, and determine this unique four-cycle. After removing the pair, remove the triangle \(acd\) together with the now-free diagonal edge \(ac\). These are actual codimension-one elementary free-face collapses. The two surviving triangles \(abd\) and \(bcd\), sharing the other square diagonal \(bd\), triangulate the original face.

Perform these two collapses for every square. A remaining triangle not in a prescribed square is a path \(u-v-w\) whose endpoints \(u,w\) have exactly one common neighbor: two would give another (facial) four-cycle. Its endpoint edge \(uw\) is now a free face of the unique triangle \(uvw\), so collapse the pair. All of these operations commute up to their order: square diagonals belong to one square, and non-square endpoint pairs have a unique common neighbor. Precisely \(T(G)-2F\) pairs are collapsed, where \(F\) denotes the number of quadrilateral faces.

The remaining two-dimensional complex is exactly the standard simplicial subdivision of the prescribed quadrangulation with one diagonal per face. Its realization is \(\Sigma\). Every extra surviving edge of \(Y\) has no coface of dimension two. Since the original one-skeleton of \(Y\) was complete, and each collapse removed exactly one edge except the \(F\) tetrahedron–triangle collapses, the residual one-skeleton contains \(\binom N2-(T(G)-3F)\) edges. The triangulated surface uses \(E+F=3F\) edges, since each edge of the closed quadrangulation belongs to two faces and hence \(E=2F\). Thus the number of remaining extra edges is \(\binom N2-T(G)=q(G)\). Attaching a new edge with its two endpoints in a path-connected complex is, up to homotopy, wedging on one circle; repeating yields \(Y\simeq\Sigma\vee\bigvee^{q(G)}S^1\).

**3. Integral duality and orientation.** Combinatorial Alexander duality for a finite \(N\)-vertex complex gives
\[
\widetilde H_i(\Delta_3(G);\mathbb Z)\cong
\widetilde H^{N-i-3}(Y;\mathbb Z).
\]
For orientable genus \(g\), the positive-degree integral cohomology of \(Y\) is \(H^1\cong\mathbb Z^{2g+q(G)}\) and \(H^2\cong\mathbb Z\). For nonorientable genus \(h\), integral homology of the surface has \(H_1(\Sigma;\mathbb Z)\cong\mathbb Z^{h-1}\oplus\mathbb Z/2\mathbb Z\) and \(H_2(\Sigma;\mathbb Z)=0\), so the universal coefficient theorem gives \(H^1(Y;\mathbb Z)\cong\mathbb Z^{h-1+q(G)}\), \(H^2(Y;\mathbb Z)\cong\mathbb Z/2\mathbb Z\). No higher reduced cohomology exists. These yield exactly the asserted degrees and groups.

By definition \(\Delta_3(G)\) is generated by complements of disconnected triples; every facet has \(N-3\) vertices, hence its dimension is \(N-4\). It is nonempty: a triangle-free graph on \(N\ge8\) has a disconnected triple, for instance by the elementary Ramsey bound \(R(3,3)=6\). Its next-to-top reduced integral homology is nonzero (\(\mathbb Z\) or \(\mathbb Z/2\mathbb Z\)). A pure shellable simplicial complex has vanishing reduced homology below its top dimension, so the complex cannot be shellable.

**4. The nonorientable infinite family.** The specified twisted graph is the unit-step square lattice modulo the horizontal translation \((x,y)\mapsto(x+m,y)\) and vertical glide reflection \((x,y)\mapsto(-x,y+n)\). The compact quotient is a Klein bottle. A nonidentity deck transformation displaces every lattice vertex at least \(\min(m,n)\) in Manhattan distance. Since \(m,n\ge7\), every walk or simple cycle of length at most four lifts uniquely, and every four-cycle is an elementary lattice square. In the lattice every distance-two nonadjacent pair has at most two common neighbors, with equality only for square-opposite vertices; this descends to the quotient under the same distance bound. Therefore all theorem hypotheses hold. The grid has \(N=mn\) vertices of degree four, giving \(T(G)=6N\), \(q(G)=\binom N2-6N=N(N-13)/2\). The nonorientable genus is \(h=2\); substitution finishes the computation.

## Verification

The standalone Python 3 script `quadrangulation_threecut_checker.py` (standard library only) independently builds four cellulated graph cases: the cubical sphere, an ordinary \(7\)-by-\(7\) torus grid, a twisted \(7\)-by-\(7\) Klein-bottle grid, and a twisted \(7\)-by-\(8\) Klein-bottle grid. It enumerates **all** possible three-vertex and four-vertex dual faces by their defining induced-connectivity condition; compares every four-simplex candidate to the prescribed square set; checks the no-\(K_{2,3}\) property; performs each claimed elementary collapse with an explicit free-face/coface test; checks the entire residual triangle and edge sets; checks all vertex links are connected cycles and every retained surface edge has exactly two triangular cofaces; and computes finite-field boundary ranks for primes \(2,3,5\).

The four cases give respectively \(12,196,196,224\) verified elementary pairs and \(4,882,882,1204\) leftover free chords. In the two Klein-bottle cases, the oriented boundary rank drops by one in characteristic two compared with odd characteristic, exactly as predicted by integral order-two torsion. These are exhaustive checks *for those four finite graphs*, not an independent proof for all possible quadrangulations. The displayed all-parameter theorem follows from the structural collapse and surface cohomology argument above.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduce ordinary cut complexes and establish results for forests, cycles and other graph classes [1]. Their conditional torsion-free theorem assumes a fuller codimension-one skeleton than is present here; it does not imply this orientability-sensitive classification. Their sequel [2] studies rectangular path grids and other operations, not closed surface quadrangulations. Chandrakar, Hazra, Rout and Singh [3] likewise treat open grid products and distinct cut constructions.

A published three-cut theorem for triangle-free graphs with **edge-disjoint** four-cycles [4] collapses the dual all the way to a graph; it cannot be applied to these closed quadrangulations, since every quadrangulation edge belongs to two prescribed squares. A published Vietoris–Rips collapse for a **twisted Klein-bottle grid** [5] concerns a different simplicial functor and different distance-clique faces; its existence does not establish the ordinary three-cut homology or its integral two-torsion. The toroidal, orientable case is a known special computation, while the present surface-wide collapse mechanism and, critically, the nonorientable \(\mathbb Z/2\mathbb Z\) phenomenon are not consequences of that special case.

## Limitations

The facial-four-cycle and no-\(K_{2,3}\) hypotheses are essential to the given elementary collapse. The theorem makes no assertion for short-parameter twisted grids, quadrangulations containing additional nonfacial four-cycles, graphs with triangles, or noncellular embeddings. It determines integral homology of the original cut complex but only a homotopy type for its *Alexander dual*; it does not determine the original complex's homotopy type or any symmetry representation. Computed examples test the proof's construction and do not certify all infinite cases. Equivalent results absent from the inspected published literature may exist.

## References

[1] M. Bayer, M. Denker, J. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first posted 2023-04-26), https://arxiv.org/abs/2304.13675.

[2] M. Bayer, M. Denker, J. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first posted 2024-07-11), https://arxiv.org/abs/2407.08158.

[3] S. Chandrakar, K. Hazra, S. Rout, A. Singh, *Topology of Cut Complexes of Certain Graphs*, arXiv:2408.07646, https://arxiv.org/abs/2408.07646.

[4] *Three-cut complexes of triangle-free graphs with edge-disjoint squares*, published mathematical research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-cut-complexes-of-triangle-free-graphs-with-edge-disjoint-s--8ca830284420.

[5] *An explicit simplicial collapse of twisted grid Rips complexes to the Klein bottle*, published mathematical research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-explicit-simplicial-collapse-of-twisted-grid-rips-complexes-t--640f98d44d0b.
