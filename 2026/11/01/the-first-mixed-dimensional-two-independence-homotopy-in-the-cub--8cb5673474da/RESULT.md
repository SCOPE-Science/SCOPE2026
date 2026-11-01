# The first mixed-dimensional two-independence homotopy in the cubical sequence

## Finding
For each integer \(1\le d\le4\), let \(Q_d\) be the graph on binary strings of length \(d\), adjacent precisely when they differ in one coordinate. Let \(X_d=\operatorname{Ind}_2(Q_d)\) be the simplicial complex of subsets inducing connected components of at most two vertices. Then the complete integral homotopy types through cubical dimension four are
\[
X_d\simeq\begin{cases}
*,&d=1,\\
\bigvee^{3}S^1,&d=2,\\
\bigvee^{3}S^2,&d=3,\\
\bigvee^{16}S^3\vee S^4,&d=4.
\end{cases}
\]
In particular, \(d=4\) is the first dimension in this sequence with nonzero reduced integral homology in more than one degree. The corresponding groups are \(\widetilde H_3(X_4;\mathbb Z)\cong\mathbb Z^{16}\) and \(\widetilde H_4(X_4;\mathbb Z)\cong\mathbb Z\), with all others zero. This is an integral homotopy statement, not just an agreement of Betti numbers.

## Assumptions and scope
The graph is finite, simple, undirected, and has exactly \(2^d\) distinct labeled vertices; \(d\) is restricted to \(1,2,3,4\). A face \(\sigma\) is permitted if every vertex of the induced subgraph \(Q_d[\sigma]\) has degree at most one. For a simple graph this is equivalent to every induced connected component having at most two vertices. The empty face is included abstractly and is not counted among nonempty faces in the enumeration.

Vertex labels are the binary integers \(0,\ldots,2^d-1\). A face is encoded by a bitmask with bit \(v\) set if vertex \(v\) is selected. Let \(N(v)\) be the neighbors of \(v\); forbidden triples are \(\{u,v,w\}\) with distinct \(u,w\in N(v)\). A subset is a face exactly when it contains none of these triples. This equivalence is used as a second, independent face-membership test.

## Proof
**Exhaustive finite face determination.** The standalone verification program examines every subset of the \(2^d\) vertices, both by the induced-degree predicate and by independent forbidden-triple exclusion. The predicates agree in every case. The numbers of nonempty faces in successive dimensions are, respectively, \((2,1)\), \((4,6)\), \((8,28,32,8)\), and
\[
(16,120,464,964,960,440,80,10)
\]
for \(d=1,2,3,4\). For \(d=4\), maximal simplices occur in dimensions \(3,5,7\), with multiplicities \(16,160,10\), so the complex is nonpure.

**Explicit acyclic Morse matchings.** Process the vertices in the prescribed order. At each vertex \(v\), pair every as-yet-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), provided both are currently unmatched faces. Use the natural order for \(d\le3\), and for \(d=4\) use the fixed order
\[
(0,3,4,8,10,1,15,7,11,5,9,2,6,13,12,14).
\]
Within each stage, pairs are disjoint because they differ only at the specified vertex. Reverse the matched covering relations in the face Hasse diagram and orient all other covering relations from upper to lower face. The supplied program reconstructs every oriented relation and executes an exhaustive topological sort, verifying that all faces are visited. The numbers of matched pairs are \(1,3,36,1518\), and the critical-cell dimension counts are respectively \(\{0:1\}\), \(\{0:1,1:3\}\), \(\{0:1,2:3\}\), and \(\{0:1,3:16,4:1\}\). Thus the finite acyclic matching gives a CW complex with exactly the listed cells in each case, by discrete Morse theory.

**Integral attaching-map calculation.** Only the fourth case has critical cells in consecutive positive dimensions. Fix the orientation of each face by ascending vertex labels, so that its signed boundary is \(\partial[v_0,\dots,v_q]=\sum_i(-1)^i[v_0,\dots,\widehat v_i,\dots,v_q]\). For any face \(a\) of fixed dimension, define an integer projection \(\rho(a)\) to critical faces of that same dimension as follows. If \(a\) is critical, its projection is the corresponding unit basis vector. If it is the upper member of a matched pair, its projection is zero. If \(a\) is paired upward with \(b\), with incidence sign \(\epsilon(a,b)\in\{\pm1\}\), then
\[
\rho(a)=-\epsilon(a,b)\sum_{f\in\partial b,\ f\ne a}\epsilon(f,b)\rho(f).
\]
The acyclic orientation makes this recursion finite and supplies the standard integral algebraic Morse differential. The unique critical four-cell has bitmask `0x4a30` and vertex set \(\{4,5,9,11,14\}\); the program computes its projected signed boundary on all sixteen critical three-cells. **Every one of these sixteen integer coefficients equals zero.** The complete sixteen-by-one Morse boundary matrix is therefore the zero matrix. There are no other possible nonzero positive-degree Morse differentials.

**Homotopy conclusion.** In dimensions \(1,2,3\), the Morse CW model has a point and cells only in one positive dimension, so it is the specified wedge of spheres (or a point). In dimension four, its three-skeleton is \(\bigvee^{16}S^3\) and it has exactly one four-cell. The three-skeleton is two-connected, so its Hurewicz homomorphism \(\pi_3\to H_3\) is an isomorphism. The zero integral attaching-degree vector computed above therefore means that the four-cell's attaching map is nullhomotopic. The resulting CW complex is \(\bigvee^{16}S^3\vee S^4\), as claimed.

## Verification
The complete source files for these computations are `scripts/verify.py` and `verification_output.txt`. Run `python3 scripts/verify.py` from the package root using Python 3.10 or later; only the standard library is required. The program reconstructs all faces (not a sample), checks the two independent membership predicates, validates every matching pair, checks all directed Hasse edges for acyclicity, evaluates the integral Morse boundary, and independently computes simplicial boundary ranks over \(\mathbb F_2\). Its recorded output ends with `ALL_CHECKS_PASS`.

For the crucial case, the full search checks \(65,536\) ambient subsets and identifies \(3,054\) nonempty faces, \(13,568\) directed Hasse incidences, \(1,518\) matched pairs, and the eighteen critical cells used in the proof. Independent mod-two computation gives reduced Betti ranks \(16\) in dimension three and \(1\) in dimension four. The integral Morse differential, rather than these mod-two checks alone, certifies the attaching map and integral homotopy type.

## Relationship to prior work
Taylan's 2015 treatment of path-devoid complexes introduces methods for complexes forbidding induced path triples and treats paths, cycles, and forests; its proved graph classes do not contain the four-cube. Deshpande and Singh (2020) classify higher independence for complete multipartite, fully whiskered, path, cycle, and perfect-tree families; none of those theorems covers the present graph. The 2021 work on chordal graphs likewise does not apply to the four-cube, which has induced squares.

The published literature on cubical graph Čech and Vietoris–Rips complexes studies different face predicates: one imposes nonempty intersections of metric balls and the other a pairwise distance bound. Neither supplies the induced-maximum-degree-at-most-one complex here. Previously recorded ordinary independence and cubical cut-complex calculations similarly concern different simplicial complexes and do not imply the mixed-dimensional classification. Equivalent formulations searched include *two-independence*, *dissociation*, and *induced three-vertex-path-devoid* complexes, including the four-by-four periodic square-grid realization \(Q_4\cong C_4\square C_4\).

## Limitations
The theorem covers only \(1\le d\le4\); it asserts nothing for larger hypercubes. It does not determine the automorphism representation on integral homology, the homotopy types of orbit spaces, or the attaching maps of complexes defined by other forbidden subgraphs. The finite algorithm is exhaustive only over the stated dimensions, not an induction for all \(d\). Literature searching cannot rule out every unindexed or inaccessible equivalent calculation. No independent mathematical audit has been performed.

## References
- D. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754, first submitted 2015-01-27.
- P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first submitted 2020-01-15.
- F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863.
- M. Adamaszek and H. Adams, *On Vietoris–Rips Complexes of Hypercube Graphs*, arXiv:2103.01040.
- H. Adams, S. Shukla, and A. Singh, *Čech Complexes of Hypercube Graphs*, arXiv:2212.05871.
- Previously published ordinary-independence classification of the four-cube, public research identifier `9947aaad144c` (different face predicate).
