# Square-filling theorem for ordinary three-cut complexes of triangle-free graphs

## Finding
Let \(G\) be any connected finite simple triangle-free graph on \(n\ge8\) vertices in which every two vertices have at most two common neighbors (equivalently, \(G\) has no \(K_{2,3}\) subgraph). Define the *square filling* \(S(G)\) to be the two-dimensional CW complex obtained from the graph \(G\) by attaching one disk along **every** simple four-cycle. Distinct squares may share graph edges. Let \(L(G)\) be the number of unordered vertex pairs whose graph distance is at least three. Let \(\Delta_3(G)\) denote the ordinary three-cut complex, whose facets are complements of disconnected induced three-vertex subgraphs.

There is an explicit sequence of elementary simplicial collapses, after choosing a diagonal in each square, giving
\[
\boxed{\Delta_3(G)^\vee\searrow S(G)^\triangle\cup\{\text{one edge for each vertex pair at distance at least three}\}.}
\]
Here \(\vee\) denotes combinatorial Alexander dual, and \(S(G)^\triangle\) is a simplicial triangulation of the square filling using one diagonal for each square. Since \(S(G)\) is connected, it follows that
\[
\boxed{\Delta_3(G)^\vee\simeq S(G)\vee\bigvee^{L(G)}S^1.}
\]
Write \(b_i=\operatorname{rank}H_i(S(G);\mathbb Z)\) and \(T=\operatorname{Tor}H_1(S(G);\mathbb Z)\). Then the entire reduced integral homology of the ordinary cut complex is
\[
\boxed{\widetilde H_j(\Delta_3(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{b_2}\oplus T,&j=n-5,\\
\mathbb Z^{b_1+L(G)},&j=n-4,\\
0,&\text{otherwise}.
\end{cases}}
\]
The displayed direct sum with \(T\) need not be natural as a splitting. In particular, any nonzero \(H^2(S(G);\mathbb Z)\) obstructs shellability of the pure complex \(\Delta_3(G)\).

As a non-product illustration, let \(G\) be obtained from two copies of the ordinary cube graph by identifying exactly one square face, including its boundary. Its square filling is two sphere boundaries glued along a disk, and has \(b_2=2\), \(b_1=0\). This graph has twelve vertices, satisfies the codegree assumption, and has \(L(G)=20\). Thus
\[
\boxed{\widetilde H_7(\Delta_3(G);\mathbb Z)\cong\mathbb Z^2,\qquad
\widetilde H_8(\Delta_3(G);\mathbb Z)\cong\mathbb Z^{20}.}
\]

## Assumptions and scope
All graphs in the theorem are finite, connected, undirected, loopless and simple; they have no triangles and at least eight vertices. The codegree condition concerns *all* pairs of distinct vertices. In a triangle-free graph, adjacent vertices have zero common neighbors, so only nonadjacent pairs need checking. The square filling has one attached two-cell for each (unoriented) simple four-cycle, even when separate squares share edges. Every such four-cycle is induced. Graph distance counts edges in shortest paths. The Alexander dual is taken on the complete original vertex set, so its one-skeleton is the complete graph. The result is about the **ordinary** cut complex, not the total cut complex. It does not assert that the ordinary cut complex itself is homotopy equivalent to the indicated wedge.

## Proof
**1. Exhaustive face classification.** Write \(K=\Delta_3(G)^\vee\). A subset \(A\) is a face of \(K\) exactly when each three-element subset of \(A\) induces a connected graph. Every vertex and every unordered pair lies in \(K\). Since \(G\) is triangle-free, a connected triple induces a path of two edges; these are exactly the two-faces of \(K\). A four-set in \(K\) must have at least four graph edges: each of its four triples has two edges, while each edge is contained in two triples. Mantel's bound gives at most four edges in a triangle-free graph on four vertices. Equality forces the complete bipartite graph \(K_{2,2}\), hence a four-cycle. Conversely, all triples of an induced four-cycle are paths. For a five-set in \(K\), its ten triples would require at least twenty edge incidences; every graph edge contributes to only three triples, requiring at least seven edges. A triangle-free graph on five vertices has at most six edges. Thus there are no faces of cardinality five or greater. Consequently, the only tetrahedra of \(K\) are the four-cycles, and the complete classification has been proved without a computation.

**2. Unique two-path collapses.** Each connected triple \(\{a,b,c\}\) with edges \(ab,bc\) and nonedge \(ac\) corresponds to a common neighbor \(b\) of \(a,c\). If \(a,c\) have exactly one common neighbor, the edge \(ac\) belongs to precisely this one triangle of \(K\) and to no tetrahedron. Thus \(ac\) is a free face and its triangle can be collapsed along it. Perform all such collapses. These pairs are disjoint, since their removed edges are distinct nonedges with unique common neighbors.

**3. Two collapses per square.** Suppose \(a,b,c,d\) are cyclically ordered around a four-cycle. The opposite vertices \(a,c\) have exactly the two common neighbors \(b,d\) by the codegree assumption. In particular, their path triangle \(abc\) is a face of exactly one tetrahedron, namely \(abcd\). Collapse tetrahedron \(abcd\) along triangle \(abc\). The diagonal edge \(ac\) now belongs to exactly one remaining triangle, namely \(acd\), and no tetrahedron; collapse \(acd\) along \(ac\). The remaining two triangles are \(abd\) and \(bcd\), sharing the other diagonal \(bd\), and form a triangulated square disk. No collapse removes an original graph edge. Two distinct squares cannot share an opposite-vertex pair, since that would give at least three common neighbors or the same four-cycle. Hence the square collapses do not interfere with one another even when squares share graph edges.

**4. Identify the survivor.** After all collapses, the surviving two-faces are precisely the two triangular halves of every original four-cycle. The original graph edges remain. Every nonedge at distance two either had a unique common neighbor and was removed, or was the diagonal of exactly one square and has one surviving diagonal. Every nonedge at distance at least three belongs to no triangle and remains as a one-simplex. Thus the surviving complex is exactly the stated triangulation of \(S(G)\), together with \(L(G)\) further edges joining pairs of vertices of the connected square filling. Attaching an extra edge between vertices of a connected space is homotopy equivalent to wedging on a circle; applying this successively proves the displayed homotopy decomposition. Each preceding step is an elementary simplicial collapse, not merely a homology equivalence.

**5. Integral homology and shellability.** Integral combinatorial Alexander duality gives
\[
\widetilde H_j(\Delta_3(G);\mathbb Z)\cong
\widetilde H^{n-j-3}(K;\mathbb Z).
\]
The connected survivor is two-dimensional. Its first cohomology is free of rank \(b_1+L(G)\), and its second cohomology is \(\mathbb Z^{b_2}\oplus T\) by the universal coefficient theorem; the torsion term comes from \(\operatorname{Ext}(H_1(S(G)),\mathbb Z)\). Higher cohomology vanishes and reduced degree-zero cohomology is zero. This proves every displayed integral group. Finally, a triangle-free graph on at least six vertices contains an independent triple by \(R(3,3)=6\), so \(\Delta_3(G)\) is nonempty and pure of dimension \(n-4\). Nonzero homology in dimension \(n-5\) is incompatible with pure shellability, completing the obstruction.

**6. Glued-cube example.** The square filling of one cube graph is its boundary two-sphere. Identifying a face of two such boundaries identifies a closed disk in each, leaving the union homotopy equivalent to a wedge of two two-spheres. Directly, its cellular Euler characteristic and van Kampen argument give \(H_2\cong\mathbb Z^2\) and \(H_1=0\). The finite graph has twelve vertices, twenty graph edges and eleven distinct squares. Its common-neighbor bound and the twenty distance-at-least-three vertex pairs are verified by the accompanying independently executable checker. Substitution into the general theorem gives the claimed degrees seven and eight.

## Verification
Run `python verify.py` in the extracted package with Python 3.10 or newer and SymPy (versions specified in `requirements.txt`). The program independently enumerates every allowed face of the Alexander dual and every four-cycle. It executes the proposed elementary collapses one at a time, checking that the collapsed face has exactly one current coface. It reconstructs the proposed square-filled survivor, counts the long-distance edges, and calculates exact integer Smith forms for the square-complex boundaries. Seven graph tests include three squares sharing an edge, the three- and four-dimensional cubes, two cubes glued along a face, a rectangular grid, a toroidal grid, and a Klein-bottle grid. The checker confirms both integral two-torsion in the Klein-bottle example and two independent second-homology classes in the glued-cube example. The verification marker is `SQUARE_FILLING_THREE_CUT_COLLAPSE_AND_INTEGRAL_CHECK_OK`. Finite tests are only corroboration: the five-step collapse and duality proof above supplies the universal argument.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue [1] define ordinary cut complexes and establish general face-lattice and Euler-characteristic tools; their triangle-free theorem in Section 6 concerns the **two-cut** complex. Their sequel [2] proves shellability and sphere-wedge results for **rectangular** grids, among other cases. Its face-lattice enumeration for grid three-cut complexes is compatible with the present formula but does not supply the graph-wide square-filling collapse or torsion transfer. A separate published research result [3] handles triangle-free graphs whose distinct squares have **disjoint edge sets**. That result collapses the Alexander dual to a graph and yields top-degree homology. Its edge-disjointness fails for cube graphs, ordinary grids, the glued-cube example, toroidal grids, and Klein-bottle grids; those cases can possess nontrivial two-dimensional square filling and next-to-top homology. Earlier exact computations of hypercube and periodic-grid three-cut complexes are special consequences of the present criterion, not proofs for all qualifying graphs. A separate square-completion calculation [4] concerns **discrete cubical homology**, not the ordinary cut-complex Alexander dual. The theorem here covers arbitrarily overlapping square edges while controlling their entire integral contribution.

## Limitations
The no-\(K_{2,3}\) hypothesis is essential for the specified *local collapse*: if an opposite pair has three common neighbors, its nonedge is shared by three path triangles and the chosen free-face argument fails. No general conclusion is claimed for graphs containing triangles, for codegree at least three, for disconnected graphs, or for fewer than eight vertices. The square filling need not be a manifold, simply connected or torsion-free. Only the Alexander dual's homotopy type and the original cut complex's integral homology are classified; the original cut complex's homotopy type and its automorphism representations are not determined. The comparison with indexed literature does not exclude every equivalent unindexed formulation; broad square-completion and Stanley–Reisner terminology remain residual bibliographic risks.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public version 2023-04-26; especially introduction and Section 6. https://arxiv.org/abs/2304.13675

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public version 2024-07-11; especially introduction and Section 5. https://arxiv.org/abs/2407.08158

[3] *Three-cut complexes of triangle-free graphs with edge-disjoint squares*, published mathematical research record, identifier `8ca830284420`; the full public mathematical result was compared, including its hypotheses, construction and proof.

[4] *Aspherical square fillings control second discrete cubical homology*, published mathematical research record, identifier `c9ee617a65ec`; compared for the distinction between cubical and ordinary cut-complex homology.
