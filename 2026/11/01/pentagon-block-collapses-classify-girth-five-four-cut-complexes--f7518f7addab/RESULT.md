# Pentagon-block collapses classify girth-five four-cut complexes

## Finding
Let \(G\) be **any finite simple undirected graph** with \(n=|V(G)|\ge9\), girth exactly five, and degrees \(d_v\). Let \(\Delta_4(G)\) denote the **ordinary four-cut complex**: its facets are the complements of four-element vertex sets inducing disconnected subgraphs. Let \(p_5(G)\) be the number of unoriented simple five-cycles (not rooted or directed), and put
\[
 c_4(G)=\sum_{v\in V(G)}\binom{d_v}{3}+\sum_{uv\in E(G)}(d_u-1)(d_v-1),\qquad
 \mu(G)=\binom{n-1}{3}-c_4(G)+p_5(G).
\]
Then \(\mu(G)\) is a nonnegative integer and
\[
 \boxed{\Delta_4(G)\simeq\bigvee^{\mu(G)}S^{n-5}.}
\]
The empty wedge means a point. In particular, reduced integral homology is torsion-free, equals \(\mathbb Z^{\mu(G)}\) in dimension \(n-5\), and vanishes in every other dimension. No connectedness, regularity, or planarity assumption is needed.

The new structural statement is the **sphere-wedge homotopy classification at girth five**, not the Euler-characteristic expression alone. The latter follows already from the face-lattice formula in Bayer et al., *Topology of Cut Complexes II*, Proposition 2.18. The present proof shows why every five-cycle contributes one cancellation block rather than causing lower-dimensional homology. A previous Petersen-specific computation is a covered special case, not a separate contribution of this theorem.

## Assumptions and scope
All graph cycles are simple; girth exactly five means the graph has at least one five-cycle and has no triangles or four-cycles. The cut complex is ordinary (disconnected induced four-sets), not the **total** cut complex (independent four-sets). For a finite simplicial complex \(K\) on \(V\), write \(K^*=\{U\subseteq V:V\setminus U\notin K\}\) for its combinatorial Alexander dual. Reduced homology is taken with integer coefficients unless otherwise stated.

The bound \(n\ge9\) ensures that the four-cut complex contains its complete two-skeleton; nothing is claimed here about smaller graphs. The top dimension of \(\Delta_4(G)\) is \(n-5\). We classify neither equivariant homotopy types nor shellability.

## Proof
**1. The Alexander dual has a controlled four-dimensional structure.** Put \(L=\Delta_4(G)^*\). All vertex sets of size at most three are faces of \(L\), since their complements are too large to belong to \(\Delta_4(G)\). A four-set \(U\) is a face of \(L\) precisely when \(G[U]\) is connected. Every connected four-vertex induced subgraph is a tree, hence is a four-vertex path or a three-leaf star.

A five-set \(W\) belongs to \(L\) if and only if all its four-subsets induce connected graphs. This happens exactly when \(G[W]\) is a five-cycle: if connected and acyclic, the five-vertex tree has a nonleaf whose deletion disconnects it; if cyclic, girth five forces an induced five-cycle. There are no faces on six vertices. Indeed, if all six five-subsets of a six-set induced five-cycles, counting edges across those six induced subgraphs would give \(6\cdot5=4e\), impossible for an integer \(e\). Larger faces are then also impossible. Thus \(L\) consists exactly of the complete two-skeleton of the \((n-1)\)-simplex, one tetrahedron for every connected four-set, and one four-simplex for every induced five-cycle.

**2. Private triangles away from five-cycles.** If a connected four-set is a star centered at \(b\) with leaves \(a,c,d\), its leaf triangle \(\{a,c,d\}\) belongs to no other connected-four-set tetrahedron. Any further completion would require a second common neighbor of the leaves, creating a four-cycle together with \(b\).

For a path \(a-b-c-d\), consider the triangle \(T=\{a,c,d\}\), with its unique induced edge \(cd\) and isolated vertex \(a\). A different vertex \(z\ne b\) can make \(G[T\cup\{z\}]\) connected only by joining \(a\) to at least one of \(c,d\) through \(z\). If \(z\) joins \(a,c\), the edges \(a-b-c-z-a\) form a forbidden square. If it joins \(a,d\), the edges \(a-b-c-d-z-a\) form a five-cycle (no chords are possible at girth five). Consequently, when the original path is **not** contained in a five-cycle, \(T\) is a private triangle for its tetrahedron. Distinct private triangles cannot coincide because they each lie in a unique tetrahedron.

**3. Each five-cycle is one independent collapsible block.** Fix a five-cycle \(Q=(v_0,v_1,v_2,v_3,v_4)\), indices cyclic. Its five four-vertex subsets are five path tetrahedra. A path tetrahedron can belong to at most one five-cycle: two distinct vertices completing the same four-vertex path would make a square between its endpoints. The five *disconnected* three-subsets of \(Q\) are the common triangular faces of the pairs of these tetrahedra indexed by nonadjacent omitted vertices; their adjacency graph on the five tetrahedra is again a five-cycle. Each such triangle belongs to **exactly two tetrahedra globally**. To see this, express either associated path as \(a-b-c-d\) and take \(T=\{a,c,d\}\). The only possible completions are \(b\) and the fifth vertex of \(Q\): a third completion joined to \(a,c\) creates a square with \(b\), while one joined to \(a,d\) creates a square with the existing fifth vertex.

First remove the four-simplex \(Q\) together with any one of its tetrahedral facets; this is an elementary simplicial collapse because that tetrahedron is contained in no other four-simplex. The remaining four tetrahedra of \(Q\) have a *path* of shared disconnected triangular faces, with free triangles at its endpoints. Remove the four tetrahedra successively along these free triangles, starting at an endpoint. This leaves no tetrahedron in the block. Blocks associated with different five-cycles have no common tetrahedra or selected disconnected triangles, by the uniqueness arguments above. Finally remove every noncycle path tetrahedron along its private triangle and every star tetrahedron along its leaf triangle. All removals are genuine elementary simplicial collapses. They remove every simplex of dimension at least three from \(L\), producing a two-dimensional complex \(Y\).

**4. Exact integral homotopy of the dual.** Before the collapses, \(L\) contained the complete two-skeleton, so it was simply connected; elementary collapse preserves this property. Its reduced Euler characteristic, calculated from its actual face numbers, is
\[
 \widetilde\chi(L)=\left(-1+n-\binom n2+\binom n3\right)-c_4(G)+p_5(G)
 =\binom{n-1}{3}-c_4(G)+p_5(G)=\mu(G).
\]
The collapsed \(Y\) is a simply connected two-dimensional CW complex, hence its only nonzero reduced integral homology is \(H_2(Y;\mathbb Z)\), a free abelian subgroup of its cellular two-chain group. Euler characteristic forces its rank to be \(\mu(G)\). Hurewicz and the homological Whitehead theorem imply
\[
 L\simeq Y\simeq\bigvee^{\mu(G)}S^2.
\]
This is an **integral homotopy proof**, not an extrapolation from field-valued boundary ranks.

**5. Transfer to the cut complex.** Every six-vertex set contains a disconnected induced four-set. Otherwise each of its five-subsets would have all four-subsets connected and would therefore be a five-cycle, contradicted by the edge-counting identity \(6\cdot5=4e\) from Step 1. For every three-set \(A\subseteq V(G)\), its complement has \(n-3\ge6\) vertices and therefore contains a disconnected four-set. Thus \(A\) lies in a facet of \(\Delta_4(G)\). The complete two-skeleton ensures \(\pi_1(\Delta_4(G))=0\). By integral combinatorial Alexander duality,
\[
 \widetilde H_i(\Delta_4(G);\mathbb Z)\cong
 \widetilde H^{n-i-3}(L;\mathbb Z).
\]
Step 4 implies that the only nonzero group occurs at \(i=n-5\), where it is free of rank \(\mu(G)\). Because \(\Delta_4(G)\) is simply connected and has dimension \(n-5\ge4\), Hurewicz and Whitehead promote this integral homology classification to the claimed wedge-of-spheres homotopy equivalence.

**6. The explicit connected-set count.** Every connected induced four-set is either a star, uniquely counted by selecting three neighbors of its center, or a path, uniquely counted by selecting a middle edge \(uv\) and one other neighbor of each endpoint. Triangles and squares are excluded, so the four selected vertices are distinct, induce a chordless path, and cannot be counted twice. The two contributions sum to the formula for \(c_4(G)\).

## Verification
A self-contained Python 3 standard-library checker `verify.py` reconstructs graph adjacency, rejects cycles shorter than five, enumerates *every* connected four-set and five-cycle in each tested finite graph, independently checks the degree formula and absence of dual six-faces, and constructs a complete explicit sequence of free-face elementary collapses from \(L\) to a two-complex. It also computes full mod-two boundary ranks of the dual for ten named examples, and separately constructs the **primal cut complex** and computes its mod-two boundary ranks for examples on at most ten vertices.

The tests cover ten named graphs and 300 deterministically generated additional simple graphs of girth at least five. For the Petersen graph, \((n,c_4,p_5,\mu)=(10,70,12,26)\); for the dodecahedral graph, \((20,140,12,841)\). Both are illustrative special cases, not separate new claims. Exact output and reproduction instructions appear in `verification_output.txt` and `VERIFICATION.md`. Finite tests are corroboration; Steps 1–6 prove the universal claim.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue, *Topology of Cut Complexes of Graphs* (arXiv:2304.13675, first posted April 26, 2023), established the basic cut-complex framework, full-skeleton and Euler/homology restrictions in Section 6, and specific graph families. Its results do not assert a uniform girth-five four-cut homotopy classification.

Bayer, Denker, Jelić Milutinović, Sundaram and Xue, *Topology of Cut Complexes II* (arXiv:2407.08158, first posted July 11, 2024), **already proves in Proposition 2.18 the face-lattice description and Euler characteristic with the five-cycle correction**, for the more general girth-\(k+1\) setting. This theorem does **not** take priority for that enumeration. The added content is the pentagon-block collapse and deduction of a uniform integral sphere-wedge homotopy type, which does not follow from the Euler characteristic alone.

The publicly available *High-girth cut complexes are wedges of top-dimensional spheres* (2026) gives the corresponding homotopy classification for graphs of girth at least \(k+2\), hence girth at least **six** when \(k=4\). Its private-free-face proof cannot directly remove the cyclic five-cell blocks present here. The earlier four-cut computation of the Petersen graph is an included known instance, not independently new. A separate four-cut theorem for \(J(5,2)\) concerns a graph with triangles, outside these hypotheses. The theorem does not claim priority over possible equivalent unindexed homotopy classifications.

## Limitations
This establishes homotopy type but not shellability, equivariant homology representations, or a simple-homotopy equivalence directly on the **primal** cut complex. The result is for ordinary four-cut complexes with girth exactly five and at least nine vertices; it does not classify the four-cut complexes of graphs containing triangles or squares, or cases on at most eight vertices. The displayed formula for \(c_4(G)\) and the five-cycle Euler correction are not individually novel. Independently audited originality and mathematical correctness remain open.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public April 26, 2023), Section 6 and Sections 7–8. https://arxiv.org/abs/2304.13675
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first public July 11, 2024), Propositions 2.17–2.18. https://arxiv.org/abs/2407.08158
3. *High-girth cut complexes are wedges of top-dimensional spheres* (2026), publicly available full scientific result at https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-high-girth-cut-complexes-are-wedges-of-top-dimensional-spheres--ec8bbe3d352b .
4. A. Hatcher, *Algebraic Topology* (2002), for the Hurewicz and Whitehead theorems and integral Alexander duality.
