# Three-cut complexes of triangle-free graphs with edge-disjoint squares

## Finding
Let \(G=(V,E)\) be any finite simple triangle-free graph on \(n\ge8\) vertices. Assume distinct (not necessarily induced) cycles of length four have disjoint edge sets; they may share vertices. Write \(q(G)\) for the number of four-cycles and \(d(v)\) for the degree of a vertex. The ordinary three-cut complex, with facets the complements of three-vertex sets inducing disconnected subgraphs, has the homotopy type
\[
\Delta_3(G)\simeq\bigvee^{B(G)}S^{n-4},\qquad
B(G)=\binom{n-1}{2}-\sum_{v\in V}\binom{d(v)}2+q(G).
\]
In particular, all reduced integral homology vanishes away from degree \(n-4\), where it is free of rank \(B(G)\). A wedge of zero spheres is interpreted as a contractible space. No connectivity hypothesis on \(G\) is required.

## Assumptions and scope
Graphs are finite, simple, and triangle-free. A four-cycle is counted by its four edges, independently of orientation or starting vertex; its four vertices necessarily induce a square. Edge-disjointness means that no edge occurs in two distinct four-cycles. The claimed homotopy equivalence is for every such graph with at least eight vertices, including disconnected graphs and graphs with isolated vertices. This is the ordinary cut complex, not the total cut complex.

## Proof
Write \(\Delta=\Delta_3(G)\) and let \(K=\Delta^\vee\) be the combinatorial Alexander dual on the entire \(n\)-element vertex set. A vertex subset belongs to \(K\) precisely when none of its three-subsets induces a disconnected graph. Thus \(K\) has all vertices and all edges, and its two-simplices are exactly the connected triples of \(G\). Since \(G\) is triangle-free, each connected triple is an induced path of length two. The number of these triangles is
\[T=\sum_{v\in V}\binom{d(v)}2.\]

There are no simplices of \(K\) with five or more vertices. Indeed, if every triple in a five-vertex triangle-free induced graph were connected, then every triple would contain at least two graph edges. Counting edge occurrences over the ten triples gives at least twenty occurrences, whereas each edge occurs in exactly three triples. This would force at least seven edges on five vertices, contradicting the triangle-free bound of six. A four-subset lies in \(K\) exactly when all its induced triples are connected. Such a triangle-free induced graph is necessarily a four-cycle. Consequently the three-simplices of \(K\) are precisely the \(q(G)\) square tetrahedra.

We now collapse \(K\) to a connected graph. If two nonadjacent vertices had at least three common neighbors, two different four-cycles would share an edge. Therefore the endpoints of any induced two-edge path have either one or two common neighbors, and they have two precisely when their path belongs to a square. First collapse every path triangle not contained in a square along the edge joining its nonadjacent endpoints. That edge is a free face: its unique common neighbor supplies the only triangle containing it, and it lies in no tetrahedron. None of these collapses interferes with another.

For each square with cyclically ordered vertices \(a,b,c,d\), collapse its tetrahedron along the triangle \(abd\). Then collapse triangle \(bcd\) along the now-free diagonal \(bd\), triangle \(abc\) along the now-free graph edge \(bc\), and triangle \(acd\) along the now-free diagonal \(ac\). The edge \(bc\) cannot occur in any other surviving square triangle, since four-cycles are edge-disjoint; all nonsquare path triangles have already been removed. The diagonals occur only in the two path triangles of this square. Thus all indicated faces are free at the moment of removal. Distinct squares can share vertices, but no edges, so these collapses can be performed separately.

Each elementary collapse removes exactly one edge and one higher-dimensional simplex except the tetrahedron-triangle collapses, which remove no edge. A square removes exactly three edges together with its four triangles and its tetrahedron, while every nonsquare path triangle removes one edge. Hence the final graph has all \(n\) vertices and precisely \(\binom n2-(T-q(G))\) edges. It is connected, because elementary collapse preserves homotopy type and \(K\) originally has the complete one-skeleton. It follows that
\[
K\simeq\bigvee^{B(G)}S^1,
\qquad B(G)=\binom n2-(T-q(G))-n+1.
\]
This also proves that the integer homology of \(K\) is torsion-free.

Combinatorial Alexander duality now gives
\[\widetilde H_i(\Delta;\mathbb Z)\cong
\widetilde H^{\,n-i-3}(K;\mathbb Z),\]
so the only possible nonzero reduced group of \(\Delta\) is \(\mathbb Z^{B(G)}\) in degree \(n-4\).

Finally, every five-vertex subset of a triangle-free graph contains a disconnected triple by the same edge-count argument. Therefore every vertex set of cardinality at most \(n-5\) is a face of \(\Delta\); in other words \(\Delta\) contains the full \((n-6)\)-skeleton of the simplex on \(V\). As \(n\ge8\), this includes the entire two-skeleton, so \(\Delta\) is simply connected. The vanishing of lower integral homology, together with Hurewicz and the cellular Whitehead theorem, shows that this \((n-4)\)-dimensional simplicial complex is homotopy equivalent to the indicated wedge of \((n-4)\)-spheres.

## Verification
The standalone `verify.py` constructs four sample graphs on eight or nine vertices with one or two edge-disjoint squares. It enumerates every disconnected triple, constructs all simplices of the ordinary three-cut complex, computes every boundary rank over \(\mathbb F_2\), and compares its complete reduced Betti vector to the formula. It also independently recounts the connected triples and squares. Its recorded output is `VERIFY_OK`. These finite computations confirm representative boundary cases; the preceding collapse and duality argument is the proof for all graphs in the stated class.

## Relationship to prior work
The original treatment of ordinary cut complexes by Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue [1] includes shellability and homology results for forests, cycles, complete multipartite graphs, and specific graph operations. In particular, its forest and cycle statements cover special members of the present class, but not the universal edge-disjoint-square theorem. Its general face-lattice hypothesis requiring a complete codimension-one skeleton is not satisfied by graphs containing a square. The sequel [2] treats disjoint unions, squared paths, and grid graphs, not this graph-wide homotopy statement. When \(q(G)=0\), the result specializes to the square-free formula; novelty is claimed only for the genuinely larger edge-disjoint-square domain, where each square contributes a homological correction with an explicit elementary-collapse mechanism.

## Limitations
No assertion is made for graphs containing triangles, for graphs with intersecting square edge sets, or for fewer than eight vertices. The proof determines homotopy type and integral Betti numbers, not automorphism representations or shellability. A finite source search cannot establish universal absence of equivalent results; the most significant residual risk is an uncatalogued characterization using hypergraph or Stanley–Reisner terminology.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first publicly posted 2023-04-26), especially Sections 5–7.

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first publicly posted 2024-07-11), especially introduction and Sections 3–6.
