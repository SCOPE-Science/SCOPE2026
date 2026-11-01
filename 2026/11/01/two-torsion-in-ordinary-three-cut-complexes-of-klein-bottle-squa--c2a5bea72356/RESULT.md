# Two-torsion in ordinary three-cut complexes of Klein-bottle square grids

## Finding

**Theorem.** For integers \(m,n\ge5\), let \(G_{m,n}\) be the square-grid graph with vertex set \(\{(i,j):0\le i<m,\ j\in\mathbb Z/n\mathbb Z\}\). Join \((i,j)\) to \((i,j+1)\), join \((i,j)\) to \((i+1,j)\) for \(i<m-1\), and join \((m-1,j)\) to \((0,n-1-j)\). Put \(N=mn\) and \(h=\binom N2-6N\). Write \(\Delta_3(G_{m,n})\) for the **ordinary three-cut complex**, whose facets are the complements of disconnected induced triples.

For the combinatorial Alexander dual \(X=\Delta_3(G_{m,n})^\vee\), there is a sequence of exactly \(4N\) elementary simplicial collapses leaving a triangulated Klein bottle and \(h\) isolated-in-dimension-one long edges between its vertices. Consequently,
\[
X\simeq K\vee\bigvee^h S^1,
\qquad
\widetilde H_j(\Delta_3(G_{m,n});\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&j=N-5,\\
\mathbb Z^{h+1},&j=N-4,\\
0,&\text{otherwise}.
\end{cases}
\]
Here \(K\) denotes the Klein bottle. In particular the three-cut complex is pure of dimension \(N-4\) and is **not shellable**. At \((m,n)=(5,5)\), its nonzero reduced homology is \(\mathbb Z/2\mathbb Z\) in degree \(20\) and \(\mathbb Z^{151}\) in degree \(21\).

## Assumptions and scope

All graphs are finite simple graphs. The graph \(G_{m,n}\) is the quotient of the nearest-neighbor square lattice by the freely acting transformations \((x,y)\mapsto(x,y+n)\) and \((x,y)\mapsto(x+m,n-1-y)\). The latter reverses vertical orientation, so the square-cell quotient is a Klein bottle. The bound \(m,n\ge5\) ensures that no nontrivial deck transformation takes a lattice point within Manhattan distance four of itself. In particular the graph is four-regular and triangle-free; its induced four-cycles are exactly the \(N\) images of unit squares.

For a complex \(\Delta\) on the full vertex ground set \(V\), the combinatorial Alexander dual is \(\Delta^\vee=\{\sigma\subseteq V:V\setminus\sigma\notin\Delta\}\). We use reduced homology with integral coefficients, and no assertion about the homotopy type of the original cut complex is made.

## Proof

**1. Exact dual-face criterion.** A set \(\sigma\subseteq V\) belongs to \(X\) precisely when \(\sigma\) contains no disconnected induced triple. Indeed, the complement \(V\setminus\sigma\) belongs to the three-cut complex exactly if it lies in the complement of some disconnected triple, equivalently such a triple lies inside \(\sigma\). Every vertex and every pair therefore occurs in \(X\); each three-face is an induced three-vertex path (the graph is triangle-free). Four vertices form a face of \(X\) if and only if all their three-subsets induce connected graphs. Every edge of a four-set belongs to two triples, so it must span at least four graph edges. Mantel's bound for a triangle-free graph on four vertices is four edges; equality forces \(K_{2,2}\), i.e., an induced four-cycle. Thus the four-faces of \(X\) are exactly the \(N\) unit-square tetrahedra. There are no five-faces: for five vertices with every triple connected, counting each edge in three triples requires \(3|E|\ge 2\binom53=20\), hence \(|E|\ge7\), whereas Mantel's bound allows at most six. All larger faces are likewise excluded.

**2. Pair types and counts.** The distance-two sphere about any vertex contains four straight endpoints and four turn endpoints. Thus the graph has \(2N\) edges, \(2N\) unordered straight distance-two pairs (one common neighbor), and \(2N\) unordered square-diagonal distance-two pairs (two common neighbors). Hence exactly
\[
h=\binom N2-(2N+4N)=\binom N2-6N
\]
unordered pairs are at graph distance at least three. Every path of length two has a unique central vertex, giving \(6N\) three-faces of \(X\) and the complete dual face vector \((N,\binom N2,6N,N)\). The local classifications follow by lifting paths of length at most four to the square lattice: distinct translates of a lifted vertex are at \(\ell^1\)-distance at least \(\min(m,n)\ge5\), hence there is no identification along paths or cycles of length at most four.

**3. Explicit elementary collapses.** For every oriented unit square with cyclic vertices \(a,b,c,d\), first collapse its tetrahedron \(\{a,b,c,d\}\) along the free triangle \(\{a,b,c\}\). That triangle is in exactly one tetrahedron because a corner path lies in a unique unit square. After all \(N\) such pairs, collapse the diagonal edge \(\{a,c\}\) together with its sole surviving coface \(\{a,c,d\}\). The only other three-face containing \(\{a,c\}\), namely \(\{a,b,c\}\), was removed in the first phase. Different squares have disjoint diagonals and the local-distance argument rules out additional cofaces. Finally, for each of the \(2N\) straight induced paths \(u-v-w\), collapse the edge \(\{u,w\}\) with the triangle \(\{u,v,w\}\). The endpoints \(u,w\) have exactly the one common neighbor \(v\), so each is a free face. In total these are \(N+N+2N=4N\) valid elementary pairs.

The surviving two-faces on each square are \(\{a,b,d\}\) and \(\{b,c,d\}\), which triangulate that square along its retained diagonal \(\{b,d\}\). The surviving one-skeleton includes the \(2N\) original graph edges, one retained diagonal per square, and the \(h\) long edges; no long edge occurs in a two-face. The first two kinds form the connected triangulated Klein-bottle surface \(K\). Attaching each of the \(h\) remaining one-cells between points of a connected space adds a wedge summand \(S^1\) up to homotopy. This proves the claimed homotopy type of \(X\).

**4. Integral duality and shellability.** The Klein bottle has \(H_1(K;\mathbb Z)=\mathbb Z\oplus\mathbb Z/2\mathbb Z\) and \(H_2(K;\mathbb Z)=0\). Therefore \(H_1(X;\mathbb Z)=\mathbb Z^{h+1}\oplus\mathbb Z/2\mathbb Z\), and \(H_2(X;\mathbb Z)=0\). The universal coefficient theorem gives \(H^1(X;\mathbb Z)=\mathbb Z^{h+1}\) and \(H^2(X;\mathbb Z)=\mathbb Z/2\mathbb Z\), with other reduced cohomology zero. Combinatorial Alexander duality on the \(N\)-vertex ground set gives \(\widetilde H_j(\Delta_3(G_{m,n});\mathbb Z)\cong\widetilde H^{N-j-3}(X;\mathbb Z)\). This yields the displayed groups. Every facet of the cut complex has cardinality \(N-3\), so its dimension is \(N-4\). A pure shellable complex has reduced integral homology concentrated in top dimension and torsion-free; the nonzero \(\mathbb Z/2\mathbb Z\) one degree below the top excludes shellability.

## Verification

The standalone `verify_klein_cut.py` constructs the reflected-seam graphs, enumerates **all** dual faces through four vertices and proves no others can occur using the five-vertex argument above. For \((m,n)=(5,5),(5,6),(6,6)\), it verifies the exact face counts, checks each of the prescribed elementary collapses as a unique-coface free-face pair, and checks that the surviving face sets agree with the claimed triangulated surface plus long edges. It also computes the integral Smith normal form of the square-cell Klein surface after contracting an independently constructed spanning tree, obtaining one invariant factor \(2\) and \(N-1\) unit factors in each case. The sample results are \((N,h)=(25,150),(30,255),(36,414)\). The program uses Python 3 and SymPy. Its finite tests corroborate the separate all-parameter mathematical argument; no finite test proves the theorem for all parameters.

## Relationship to prior work

Bayer–Denker–Jelić Milutinović–Rowlands–Sundaram–Xue, *Topology of Cut Complexes of Graphs* (arXiv:2304.13675, first posted 2023-04-26), introduces the ordinary cut-complex definition and studies several families, but not reflected square-lattice Klein quotients. Their subsequent *Topology of Cut Complexes II* (arXiv:2407.08158) treats rectangular path-product grid graphs and gives shellable ordinary three-cut complexes in that different setting; it does not imply nonorientable torsion. An openly accessible mathematical note entitled *An explicit simplicial collapse of twisted grid Rips complexes to the Klein bottle* (2026-10-11) studies the **same reflected-seam graphs** for parameters at least seven, but analyzes their **scale-two Rips complexes**, not ordinary three-cut complexes. Its Klein-bottle core is relevant geometrically, whereas the dual-face identification, long edges, Alexander-dual integral torsion and all-order statement here are additional. The earlier untwisted toroidal-grid three-cut calculation concerns a different graph family with orientable surface core, free next-to-top homology and no two-torsion; the specialization does not contain the reflected seam case. High-girth cut-complex statements do not apply because these graphs contain four-cycles.

## Limitations

The theorem concerns the ordinary \(3\)-cut complex, not the total cut complex or the scale-two Rips complex. It does not give the homotopy type of the original cut complex, nor a classification of all graph families carrying such torsion. Although closely related published statements and indexed mathematical records were inspected, an unindexed equivalent theorem cannot be conclusively ruled out. The finite checker relies on SymPy for Smith normal forms; the universal proof is independent of software.

## References

- Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, Lei Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public version 2023-04-26, https://arxiv.org/abs/2304.13675.
- Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Sheila Sundaram, Lei Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public version 2024-07-11, https://arxiv.org/abs/2407.08158.
- *An explicit simplicial collapse of twisted grid Rips complexes to the Klein bottle*, publicly indexed 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-an-explicit-simplicial-collapse-of-twisted-grid-rips-complexes-t--640f98d44d0b.
