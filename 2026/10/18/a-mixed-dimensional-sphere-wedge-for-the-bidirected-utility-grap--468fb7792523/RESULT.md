# A mixed-dimensional sphere wedge for the bidirected utility graph

## Finding
Let \(D=\overleftrightarrow{K}_{3,3}\) be the simple digraph obtained by replacing each of the nine edges of the complete bipartite graph on two triples by **both** possible directed arcs. Let \(X(D)\) be the multipath complex: its vertices are the directed arcs of \(D\), and its simplices are exactly the subsets of arcs whose connected components are isolated vertices or directed simple paths. Then
\[
\boxed{|X(D)|\simeq \bigvee^{19}S^3\vee\bigvee^{12}S^4.}
\]
In particular, the only nonzero reduced integral homology groups occur in degrees three and four and are free of ranks \(19\) and \(12\), respectively. This is a statement about the *bidirected* graph, not the one-way oriented complete bipartite graph or its ordinary chessboard/matching complex.

## Assumptions and scope
The vertex set is \(\{0,1,2,3,4,5\}\), with parts \(U=\{0,1,2\}\), \(W=\{3,4,5\}\). The arc set comprises \(u\to w\) and \(w\to u\) for every \(u\in U\), \(w\in W\), with no loops. A subset of arcs is a multipath precisely when all vertices have indegree and outdegree at most one in the selected arcs and the selected digraph has no directed cycle. The simplex with no arcs is included as the empty face. We use the standard geometric realization, ordinary integral homology, and unreduced simplicial chains except where reduced groups are explicitly stated.

There are \(18\) simplicial vertices. Since an acyclic collection of directed paths on six vertices has at most five arcs, \(X(D)\) has dimension four. A complete enumeration, retaining the empty face, gives face counts by cardinality \(0,1,2,3,4,5\):
\[
(1,18,108,264,252,72).
\]
Thus its ordinary Euler characteristic is \(-6\), agreeing with the wedge displayed above.

## Proof
**1. Explicit finite complex.** Order the nine arcs from \(U\) to \(W\) lexicographically by their endpoints, followed by the nine reverse arcs ordered by their source in \(W\) and target in \(U\). Represent an arc subset by its eighteen-bit mask. The face predicate is exactly the indegree/outdegree/cycle criterion given above, so testing every possible arc subset of size at most five produces all faces with no sampling. The independent implementation uses a different arc order and tests all eighteen-bit masks. Both yield the stated face numbers.

**2. Integral chain reduction.** Let \(C_k\) be the free integral group on \(k\)-arc faces, so that the ordinary simplicial boundary from \(C_k\) to \(C_{k-1}\) is \(\partial_k\); the corresponding topological dimension is \(k-1\). With increasing arc-index orientation,
\[
\partial_k(e_{i_1}\wedge\cdots\wedge e_{i_k})=
\sum_{j=1}^{k}(-1)^{j-1}
(e_{i_1}\wedge\cdots\wedge\widehat{e_{i_j}}\wedge\cdots\wedge e_{i_k}).
\]
The initial integer matrices satisfy \(\partial_{k-1}\partial_k=0\), as does every reduced stage. Whenever the coefficient at row \(r\) and column \(c\) of a boundary matrix is \(\varepsilon\in\{1,-1\}\), split off the elementary contractible two-term complex supported by these generators. The new middle boundary is its exact integral Schur complement:
\[
D'_{ij}=D_{ij}-D_{ic}D_{rj}/\varepsilon,
\qquad i\ne r,\ j\ne c.
\]
Delete the corresponding generator from each adjacent boundary. This is a genuine integral chain-homotopy equivalence, not a rank calculation over a field.

The supplied `certificates/unit_pivots.csv` records *every* pivot as its boundary degree, lower-face mask, upper-face mask and signed coefficient. The standalone `verify_integral.py` reconstructs all original matrices, verifies their chain property, recomputes the deterministic sparse unit-pivot selection, and compares all \(341\) pivots with the certificate. The numbers of pivots in boundary degrees \(2,3,4,5\) are \(17,91,173,60\), respectively. All remaining boundary entries vanish; the only remaining chain groups, indexed by face cardinality, have ranks
\[
\operatorname{rank}C_1=1,\quad
\operatorname{rank}C_2=\operatorname{rank}C_3=0,\quad
\operatorname{rank}C_4=19,\quad
\operatorname{rank}C_5=12.
\]
The singleton is the sole generator of the connected degree-zero part, so the reduced integral homology groups are precisely the claimed free groups. No unexamined prime torsion can remain, since all canceled entries were integral units and the final integral matrices are zero.

**3. Simply connectedness.** Use the one-skeleton of the complex, whose vertices are arcs of \(D\), edges are compatible pairs of arcs, and triangular two-cells arise from compatible triples. The standalone checker chooses a spanning tree of its \(108\) edges; the tree has \(17\) edges. Set tree-edge generators to the identity in the standard edge-path presentation of the fundamental group. Every triangular face supplies a relation among its three boundary edge generators. Repeatedly, if two of those generators have already been shown trivial, its third generator is trivial too. The certificate-reproducible successive numbers of newly trivial edge generators are
\[
46,\quad 7,\quad 12,\quad 19,\quad 7.
\]
Their sum is \(91\), accounting for *all* non-tree edges. Consequently \(\pi_1(|X(D)|)=1\). Since the integral calculation gives \(H_2(|X(D)|;\mathbb Z)=0\), the degree-two Hurewicz theorem also yields \(\pi_2(|X(D)|)=0\).

**4. Upgrade from homology to homotopy.** The three-skeleton \(Y=|X(D)|^{(3)}\) is two-connected because attaching four-cells cannot alter \(\pi_1\) or \(\pi_2\). A two-connected finite three-dimensional CW complex is homotopy equivalent to a wedge of three-spheres: choose maps representing a basis of its free \(H_3\), use Hurewicz, and apply the simply-connected homological Whitehead theorem. The attaching maps of the four-cells to this wedge lie in \(\pi_3(Y)\cong H_3(Y;\mathbb Z)\), so their homotopy classes are exactly their integer cellular boundary columns. Integral changes of basis of the three-spheres and four-cell attaching maps reduce that matrix to Smith normal form; these operations are realized by homotopy equivalences and cell slides. Since Step 2 gives torsion-free \(H_3\), every nonzero Smith invariant is a unit. Each degree-one three-/four-cell pair is contractible, and the remaining zero columns are freely attached four-spheres. The free ranks from Step 2 are \(19\) and \(12\), proving the asserted wedge homotopy type.

## Verification
Run `python3 verify_integral.py` and `python3 verify_independent.py` from a directory containing the delivered relative paths. The first checks all integer boundaries, the explicit \(341\)-pivot certificate and the full fundamental-group triangle elimination. The second independently enumerates the simplices using a different arc order and obtains boundary ranks over the primes \(2,3,5,101\). Its field checks support—but do not replace—the integral unit-pivot proof. Exact recorded standard outputs appear in `checks/integral.txt` and `checks/independent.txt`. No external mathematical packages, random seeds or network resources are required.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith, *On the homotopy type of multipath complexes* (2022 preprint, later published), define this complex and compute the Euler generating function of a **one-way** oriented complete bipartite graph: its arc set has nine elements for the \((3,3)\) case and its multipath complex is the chessboard matching complex. Their homogeneous families with explicit homotopy classifications are linear graphs, oriented polygons, small grids and transitive tournaments. Those results do not give the homotopy type of the **eighteen-arc bidirected** graph here.

Vrećica and Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, develop the full complete-digraph complex and connectivity bounds, and introduce the general directed-graph formulation. The present complex is a restricted-arc subcomplex of the six-vertex complete-digraph construction; parent-complex connectivity does not determine its homotopy type. Caputi, Collari and Smith, *Multipath complexes of bidirectional polygonal digraphs* (2026), treat bidirected paths and cycles, not the three-regular, six-vertex utility graph. These distinctions concern the actual hypotheses and object, not merely the titles.

## Limitations
The result is specific to the six-vertex bidirected \(K_{3,3}\). It does not classify bidirected \(K_{m,n}\) for other parameters or the automorphism action on its homology. The finite enumeration is exhaustive only because all eighteen arc choices and all relevant chain generators are explicitly checked. The homotopy conclusion additionally uses the proved vanishing of the first two homotopy groups; integral Betti numbers alone would not suffice in general. The literature comparison cannot rule out an unindexed equivalent computation.

## References
1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first public version 9 August 2022. See Definitions 2.1–2.2, Theorem 3.7, and Sections 4–5. https://arxiv.org/abs/2208.04656
2. S. T. Vrećica and R. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252, 2007; European Journal of Combinatorics 30 (2009), 542–554. See Sections 2–3. https://arxiv.org/abs/0710.5252
3. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, first public version 9 January 2026. See Introduction, Definitions 1.1–1.5 and Section 2. https://arxiv.org/abs/2601.05670
