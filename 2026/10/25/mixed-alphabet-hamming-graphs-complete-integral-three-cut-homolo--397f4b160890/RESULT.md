# Mixed-alphabet Hamming graphs: complete integral three-cut homology

## Finding

Let \(d\geq3\) and let \(q_1,\ldots,q_d\geq2\) be integers, with at least one \(q_i\geq3\). Let
\[
G=K_{q_1}\mathbin{\square}\cdots\mathbin{\square}K_{q_d},\qquad
N=\prod_{i=1}^d q_i,
\]
be the Cartesian product graph: its vertices are words, adjacent precisely when they differ in one coordinate. Write \(\Delta_3(G)\) for the **ordinary** three-cut complex whose facets are the complements of disconnected induced vertex triples. Define the nonnegative integers
\[
E=\sum_{i=1}^d\frac{N}{q_i}\binom{q_i}{2},\qquad
Q=\sum_{1\leq i<j\leq d}\frac{N}{q_iq_j}\binom{q_i}{2}\binom{q_j}{2},
\]
\[
a=\binom N2-E-2Q,\qquad
b=Q+N-1-\sum_{i=1}^d\frac{N(q_i-1)}{q_i}.
\]
Then the combinatorial Alexander dual \(K=\Delta_3(G)^\vee\), taken on all \(N\) vertices, has integral homotopy type
\[
\boxed{K\simeq\left(\bigvee^a S^1\right)\vee\left(\bigvee^b S^2\right).}
\]
Consequently the complete reduced **integral** homology is
\[
\boxed{\widetilde H_j(\Delta_3(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{\,b},&j=N-5,\\
\mathbb Z^{\,a},&j=N-4,\\
0,&\text{otherwise}.
\end{cases}}
\]
Both displayed ranks are positive in the stated domain. The original cut complex is pure of dimension \(N-4\), but has nonzero homology in degree \(N-5\), hence is nonshellable.

For the smallest mixed-alphabet three-coordinate example, \(G=K_2\square K_2\square K_3\), the formulas give \(N=12\), \(E=24\), \(Q=15\), \(a=12\), \(b=6\), and
\[
\widetilde H_7(\Delta_3(G);\mathbb Z)\cong\mathbb Z^6,
\qquad
\widetilde H_8(\Delta_3(G);\mathbb Z)\cong\mathbb Z^{12}.
\]

## Assumptions and scope

All graphs are finite, simple, and undirected. The factor orders may differ; no primality or prime-power condition is imposed. A triple is disconnected when its induced three-vertex graph is not connected. The symbol \(\square\) denotes **Cartesian**, not direct or tensor graph product. The Alexander dual is the complex of subsets containing no disconnected triple; in particular **every pair** of vertices lies in the dual, even if its two vertices are far apart in the graph. The theorem asserts the homotopy type of this dual, not that of the original three-cut complex. Only the integer homology of the original complex is classified.

## Proof

**1. Exact classification of dual faces.** A triple induces a connected graph if and only if it contains at least two graph edges. Suppose \(S\) is a dual face with at least three vertices and contains a nonadjacent pair \(u,v\). For every third vertex \(w\in S\), connectedness of \(\{u,v,w\}\) forces \(w\) to be adjacent to both \(u\) and \(v\). In a Cartesian product of complete graphs, a nonadjacent pair has common neighbors if and only if it differs in exactly two coordinates. In that case it has exactly **two** common neighbors, the two opposite corners of its unique axis-parallel rectangle. Thus \(S\) lies in this four-vertex rectangle. Conversely, every triple from such a rectangle induces a connected path of length two. If \(S\) contains no nonadjacent pair it is a clique, and every clique is contained in a single coordinate-line simplex. Therefore all dual faces of size at least three are exactly the faces contained in one of the coordinate-line simplices or in a four-vertex rectangle tetrahedron. The dual also contains all \(\binom N2\) pairs, by vacuity of the triple condition.

**2. The coordinate-line subcomplex.** Let \(B\) be the union of all coordinate-line simplices. There are \(N/q_i\) lines in direction \(i\), each on \(q_i\) vertices. Two distinct lines intersect in at most one vertex. Each line simplex can be collapsed to a tree on its vertices while fixing its vertex set: choose one root vertex, pair each higher face not containing the root with its cone face, and retain the root edges. These relative collapses work independently in \(B\), because different line simplices have no positive-dimensional common face. Hence \(B\) is homotopy equivalent to a **connected graph** on \(N\) vertices with
\[
L=\sum_{i=1}^d\frac{N(q_i-1)}{q_i}
\]
edges. Therefore \(H_1(B;\mathbb Z)\cong\mathbb Z^{L-N+1}\) and \(H_j(B;\mathbb Z)=0\) for \(j\geq2\).

**3. Attaching the rectangles.** Let \(K_0\) be the union of \(B\) and the tetrahedra on axis-parallel rectangles. There are precisely \(Q\) such rectangles. Each tetrahedron meets \(B\) exactly in its four-edge perimeter, and any two distinct rectangle tetrahedra intersect only in faces belonging to \(B\). In particular, each distance-two diagonal belongs to one rectangle. For a rectangle with cyclic corners \(0,1,2,3\), one may collapse its tetrahedron along triangle \(012\), then collapse the remaining triangle \(023\) along its now-free diagonal edge \(02\). The two remaining triangles \(013\) and \(123\) form a disk spanning the rectangle's four-edge perimeter. These operations preserve \(B\) and are independent for different rectangles. Therefore \(K_0\) has the homotopy type of \(B\) with one two-cell attached along the perimeter of each rectangle. The relative cellular homology is
\[
H_j(K_0,B;\mathbb Z)\cong
\begin{cases}\mathbb Z^Q,&j=2,\\0,&j\ne2.\end{cases}
\]

**4. Simply connectedness and integral rank.** Equip the contractible product of simplices
\[
P=\Delta^{q_1-1}\times\cdots\times\Delta^{q_d-1}
\]
with its standard product CW structure. Its two-skeleton consists of coordinate edges, coordinate triangles, and **one square cell per rectangle**. All those edges and triangles lie in \(B\), while the square cells are attached to \(B\) in step 3. Higher-dimensional cells of the individual coordinate-line simplices cannot change fundamental groups. Consequently \(K_0\) has the same fundamental group as the two-skeleton of \(P\), namely the trivial group. Equivalently, the rectangle loops normally generate \(\pi_1(B)\). The homology long exact sequence of \((K_0,B)\) therefore contains a surjective connecting homomorphism
\[
\mathbb Z^Q\longrightarrow H_1(B;\mathbb Z)
\cong\mathbb Z^{L-N+1},
\]
with kernel \(H_2(K_0;\mathbb Z)\). Hence \(H_2(K_0;\mathbb Z)\cong\mathbb Z^b\) where \(b=Q-(L-N+1)\), and every other reduced integral homology group of \(K_0\) vanishes. The kernel is free over \(\mathbb Z\), not merely rationally. Since \(K_0\) is simply connected, the Hurewicz theorem gives homotopy classes representing a basis of \(H_2\). The induced map \(\bigvee^b S^2\to K_0\) is an integral homology equivalence and therefore a homotopy equivalence by the simply connected homological Whitehead theorem.

**5. The remaining edges and duality.** A pair at Hamming distance at least three lies in no connected triple, hence is an edge of \(K\) attached only at its endpoints to \(K_0\). All distance-one pairs lie in a coordinate line, and every distance-two pair is the unique diagonal of one rectangle, giving exactly \(E+2Q\) edges in \(K_0\). Thus there are \(a=\binom N2-E-2Q\) new edges. Attaching an edge between points of the connected complex \(K_0\) adds one wedge summand \(S^1\). This establishes the claimed homotopy equivalence for \(K\). Combinatorial Alexander duality on the \(N\)-vertex ground set gives the degree relation
\[
\widetilde H_j(\Delta_3(G);\mathbb Z)
\cong\widetilde H^{N-j-3}(K;\mathbb Z).
\]
The integral cohomology of the established wedge is free, supported only in degrees one and two. This gives exactly the two stated homology groups, with neither torsion nor omitted degrees.

**6. Positivity and nonshellability.** Since \(d\geq3\), pairs differing in three coordinates exist, so \(a>0\). To see \(b>0\), choose two levels in any three distinct coordinates and fix all others. The six oriented rectangle two-cells bounding that three-dimensional cubical subproduct give a nonzero element of the kernel \(\mathbb Z^Q\to H_1(B;\mathbb Z)\): their oriented cellular boundary cancels, and the coefficient vector is not zero. Thus \(b\geq1\). Every facet of \(\Delta_3(G)\) is the complement of a disconnected triple, hence has size \(N-3\). Its dimension is \(N-4\). A pure shellable complex has no reduced homology below its top dimension, whereas the established degree \(N-5\) group is nonzero. Therefore \(\Delta_3(G)\) is nonshellable for all stated parameters.

## Verification

Run `python3 check_hamming_three_cut.py` with Python 3 and no third-party packages. The program constructs the dual from coordinate-line and rectangle faces, then independently tests the defining connected-triple criterion on **all** triples and quadruples for seven parameter tuples. For cases with a four-symbol coordinate it additionally excludes five-vertex faces by exhaustive enumeration. It computes all boundary ranks over three characteristics \(2\), \(3\), and \(5\), checking the entire Betti vector against \(a,b\). Tested tuples are `(2,2,2)`, `(2,3)`, `(2,3,3)`, `(3,3,3)`, `(2,2,2,2)`, `(2,3,4)`, and `(3,3,4)`. The checker outputs `ALL CHECKS PASSED (finite examples only).` The general integral conclusion does **not** rely on finite-field experiments: it follows from the preceding homotopy proof and integral exact sequence.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced the ordinary cut complex and studied, among other cases, the Cartesian prism \(K_n\square K_2\), complete multipartite graphs, and cycles. Their sequel treats **path-grid** products and disjoint unions. These theorems do not state the present arbitrary-length product-of-cliques classification. Previously published calculations handle the two-coordinate rook graphs and the all-binary cube, as well as the one specific ternary three-cube; those special cases are not claimed as new here. The new content is the **single integral and homotopy classification for all mixed alphabet tuples with at least three coordinates**, including previously uncomputed products such as \(K_2\square K_2\square K_3\). The relative rectangle-cell proof explains how the results for different alphabets fit into one theorem. A recent paper about **total two-cut** complexes of Cartesian graph products uses a different cut condition and cannot imply these ordinary three-cut groups.

## Limitations

The main domain excludes the two-factor and all-binary cases already treated separately elsewhere, although the same counting argument specializes to them. No homotopy classification of the **original** ordinary three-cut complex or automorphism-group representation is asserted. Literature comparisons establish no equivalent coverage among the inspected sources; independent priority verification and inspection of all uncatalogued results remain open. Finite computations verify examples, not the infinite family.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first publicly posted 2023-04-26, notably the introduction, cut-complex definition, and Section 7 (https://arxiv.org/abs/2304.13675).
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first publicly posted 2024-07-11, especially Section 5 (https://arxiv.org/abs/2407.08158).
3. *Integral and equivariant homology of three-cut complexes of rook graphs*, publicly indexed research result (2026), exact two-factor Cartesian-clique classification; not a claim about three or more factors.
4. P. Chauhan, S. Shukla and K. Vinayak, *Total two-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, arXiv:2512.04486, first posted 2025-12-05; its total two-cut condition differs from the ordinary three-cut condition.
