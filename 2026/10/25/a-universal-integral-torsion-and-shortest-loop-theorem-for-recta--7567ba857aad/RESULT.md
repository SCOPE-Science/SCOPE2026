# A universal integral torsion and shortest-loop theorem for rectangular rook neighborhood complexes

## Finding
For all integers \(m,n\ge4\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\) be the rook graph on \([m]\times[n]\), and let \(K_{m,n}=\mathcal N(R_{m,n})\) be its **open** Lovász neighborhood simplicial complex. Distinct cells are rook-adjacent precisely when they share a row or column; a simplex has a common rook-neighbor distinct from all its vertices.

**Theorem.** For every such rectangle,
\[
\boxed{H_1(K_{m,n};\mathbb Z)\cong\mathbb Z/2\mathbb Z.}
\]
The one-skeleton is complete. A three-cell set \(T\) is a missing triangle precisely when its three cells, treated as edges of the bipartite row–column incidence graph, form either a three-edge matching or a simple three-edge path. Every missing-triangle boundary represents the **same nonzero integral homology class** (hence the generator), and every other triangle boundary is null. There are exactly
\[
\boxed{6\binom m3\binom n3+4\binom m2\binom n2}
\]
missing triangles, all minimum-length representatives of that order-two generator.

More precisely, for every vertex subset \(W\subseteq[m]\times[n]\),
\[
\boxed{\operatorname{im}\bigl(H_1(K_{m,n}[W];\mathbb Z)\to H_1(K_{m,n};\mathbb Z)\bigr)\ne0
\iff W\text{ contains a missing triangle.}}
\]
Such a subset has no missing triangle exactly when the associated bipartite incidence graph is a disjoint union of **at most two stars** (isolated row or column nodes are ignored). In particular, the largest subsets failing to carry the order-two class have size \(m+n-2\); the only subsets of this maximum size are the \(mn\) full open neighborhoods. Thus **every** \((m+n-1)\)-vertex induced subcomplex carries the nonzero ambient first-homology class, and the threshold is sharp.

## Assumptions and scope
All homology is ordinary simplicial homology with integer coefficients unless \(\mathbb F_2\) is displayed. The open neighborhood of cell \((i,j)\) consists of all other cells in its row together with all other cells in its column. The induced subcomplex \(K_{m,n}[W]\) retains exactly those simplices of \(K_{m,n}\) whose vertices lie in \(W\). A missing triangle is a three-cell set whose three edges occur in the one-skeleton but which is not a two-simplex. A star in a bipartite row–column graph is a connected graph with at least one edge and a vertex incident to every edge.

## Proof
**1. Complete edges and the triple dichotomy.** Since both parameters are at least four, two cells in a common row have a third cell of that row as common neighbor, and similarly for a common column. Cells in different rows and columns share their two opposite rectangle corners as common neighbors. Thus every pair is an edge in \(K_{m,n}\).

For three distinct cells, there are exactly two ways to have *no* common rook neighbor. They may have three distinct rows and three distinct columns (a three-edge matching of the incidence graph). Or two share a row, two share a column, and the three form three corners of a rectangle (a length-three path in the incidence graph). In the other cases, a common neighbor exists: three cells in one row or column can be witnessed by a fourth cell there, while a pair on one row and an additional cell outside both occupied columns are witnessed at the intersection of that row and the third cell's column. The column cases are symmetric. This exhausts equality patterns. Counting matchings gives \(6\binom m3\binom n3\), and counting three-corner rectangles gives \(4\binom m2\binom n2\).

**2. A universal detecting cocycle.** On each oriented one-simplex with cell endpoints \(a,b\), define the \(\mathbb F_2\)-valued cochain \(\zeta(a,b)\) to be one if the cells have **distinct rows and columns**, and zero otherwise. Its evaluation on the boundary of a three-cell triangle is zero if the triangle is a simplex: in a row or column all three pair values are zero, and with exactly two cells sharing a row or column the pair values are \((0,1,1)\). On the two missing-triangle patterns those values are respectively \((1,1,1)\) and \((0,0,1)\), hence the sum is one. Since all two-simplices have one of the facial patterns, \(\zeta\) is a cocycle. Every missing-triangle boundary is therefore nontrivial after reduction mod two and in integral homology.

**3. Exact integral order from the finite four-by-four relation certificate.** For an increasing four-vertex tuple \(Q=(q_0,q_1,q_2,q_3)\), write \(\gamma_i\) for the oriented boundary of the face \(Q\setminus\{q_i\}\). The simplicial identity \(\partial^2[Q]=0\) gives
\[
\gamma_0-\gamma_1+\gamma_2-\gamma_3=0.
\]
If exactly two triples of \(Q\) are missing, the other two boundaries vanish in homology, and the two missing boundaries differ by an explicit sign. Form a signed graph whose vertices are the missing triples and whose edges are precisely these two-missing-triple relations, labeled by the corresponding sign \((-1)^{i+j+1}\).

On the four-by-four board, there are exactly \(240\) missing triples: \(144\) three-edge paths and \(96\) matchings. Of the \(\binom{16}{4}=1820\) four-cell subsets, exactly \(1440\) have two missing triples, \(320\) have none, and \(60\) have four. The signed relation graph has **one connected component of 240 vertices**, and it contains an **inconsistent signed cycle**, meaning the product of its edge signs around the cycle is \(-1\). These finite claims are certified by the exhaustive, input-free standalone program `verify_rook_rect.py`: its deterministic breadth-first search reaches every vertex and finds an edge with the opposite sign to that forced by the search tree. The verifier checks the face criterion directly from open-neighborhood incidence, tests every one of the \(1820\) four-cell subsets, and checks the actual sign formula. Connectivity says all missing-triangle classes are \(\pm u\), while the negative signed cycle implies \(u=-u\), or \(2u=0\).

This local certificate applies to **every** four-row, four-column subgrid of a larger rectangle: the triple face criterion in Step 1 depends only on the at-most-three rows and columns actually used, so it is unchanged by enlarging the board. Every missing triple lies in some such subgrid. Any two four-by-four subgrids can be joined by a chain changing one selected row or column at a time. Consecutive subgrids overlap in a three-by-four or four-by-three subgrid and therefore contain a **common missing three-corner rectangle**. Their locally generated classes agree up to sign. Hence the global missing-triangle relation graph is connected and contains a negative signed cycle. All missing triangles generate a cyclic group of order at most two; Step 2 shows their common class survives mod two. As the complete one-skeleton's cycle lattice is integrally generated by oriented triangle boundaries, there can be no other first-homology class. This proves \(H_1\cong\mathbb Z/2\mathbb Z\) for all parameters, and shows **each** missing triangle gives its generator.

**4. Exact induced supports and the sharp threshold.** For any \(W\), a missing triangle inside \(W\) is an induced three-edge circle whose class is the ambient generator, so the inclusion map is onto. Conversely, if \(W\) contains no missing triangle, its induced subcomplex contains every triangle on \(W\). Together with the complete one-skeleton this makes its first homology zero, proving the equivalence.

Regard \(W\) as the edge set of a bipartite graph on the \(m\) row nodes and \(n\) column nodes. By Step 1, absence of missing triangles means it contains neither a simple three-edge path nor three pairwise disjoint edges. A bipartite graph with no three-edge path is a disjoint union of stars: a connected nonstar component necessarily contains a simple path of three edges (a shortest path between vertices at distance at least three, or a four-cycle). Three edge-containing components give a three-edge matching; thus there are at most two star components. Conversely at most two disjoint stars contain neither forbidden pattern.

A single star has at most \(\max\{m,n\}\) edges. For two disjoint stars with centers on the same bipartition side, the total is at most \(n\) or \(m\), since their leaf sets on the opposite side must be disjoint. For two disjoint stars with opposite-side centers, row \(i\) and column \(j\), the edge \((i,j)\) is excluded, so their total is at most \((n-1)+(m-1)=m+n-2\). Equality holds **only** for the complete two stars, whose edge set is exactly the open neighborhood of cell \((i,j)\). Since \(m,n\ge4\), this bound strictly exceeds \(\max\{m,n\}\), and the full neighborhoods are the unique extremizers. Consequently every subset of size at least \(m+n-1\) contains a missing triangle, while full neighborhoods provide sharp \((m+n-2)\)-vertex counterexamples.

## Verification
Run `python3 verify_rook_rect.py` using Python 3 with its standard library. It independently reconstructs the four-by-four open-neighborhood three-faces; verifies the complete classification and \(\mathbb F_2\) cocycle on every triple; enumerates all \(1820\) four-sets and the \(1440\) signed relations; checks connectedness and an inconsistent signed cycle; checks the triple types and class counts on rectangles \((4,4),(4,5),(5,4),(5,5),(4,6)\); and exhaustively verifies the sharp induced-support threshold for \((4,4)\) and \((4,5)\). The proof for arbitrary parameters is the symbolic reduction in Steps 1–4, not extrapolation from finite tests. The same computation is recorded in `verification_output.txt`.

## Relationship to prior work
Matsushita's paper on fundamental groups of open neighborhood complexes [1] gives a general graph-theoretic presentation but does not state this rectangular rook family calculation or its primitive shortest-loop and induced-support classification. The archived four-by-four rook calculation [2] already establishes its isolated integral \(\mathbb Z/2\) and is a **special case** of the first assertion here, not a new base case. The archived Kummer-biplane calculation [3] strengthens that isolated case to a projective-plane wedge and identifies its missing triangles. A separate all-parameter study [4] determines the *higher* integral homology of rook neighborhood complexes and explicitly leaves degrees one and two unresolved. Its cofiber wedge construction does not determine the attaching map into degree-one homology and therefore does not imply the present group or support theorem. The two-row rook calculation [5] concerns a different parameter regime. The **closed** neighborhood complex studied by Matsushita [6] includes the center vertex and is different from the open complex used here.

## Limitations
Only first integral homology, its shortest triangular representatives and all induced-support images are classified. No claim is made about the full fundamental group, the second homology or the homotopy type for general rectangles. The four-by-four signed-relation certificate is a finite exhaustive lemma and must be checked using the supplied code; it is not replaced by floating-point or random evidence. Published and database searches cannot exclude obscure equivalent work, particularly under line-graph or box-complex terminology.

## References
[1] T. Matsushita, *Fundamental Groups of Neighborhood Complexes*, arXiv:1210.2803v1 (first public 2012-10-10); *J. Math. Sci. Univ. Tokyo* **24** (2017), 321–353. https://arxiv.org/abs/1210.2803 ; https://www.ms.u-tokyo.ac.jp/journal/jms240302.pdf .

[2] *Integral homology of the rook-graph neighborhood complex*, 2026 public published-finding corpus record `2026/10/11/SCOPE-integral-homology-of-the-rook-graph-neighborhood-complex--00c7d8853dcb`.

[3] *The Kummer biplane block complex has an integral projective-plane summand*, 2026 public published-finding corpus record `2026/10/11/SCOPE-the-kummer-biplane-block-complex-has-an-integral-projective-plan--6184c6679525`.

[4] *Row–column boundary spheres control higher neighborhood homology of rook graphs*, 2026 public published-finding corpus record `2026/10/11/SCOPE-row-column-boundary-spheres-control-higher-neighborhood-homology--f09a20a3ee45`.

[5] *Neighborhood complexes of two-row rook graphs split into two spheres and a crown suspension*, 2026 public published-finding corpus record `2026/10/11/SCOPE-neighborhood-complexes-of-two-row-rook-graphs-split-into-two-sph--9b16e10ce620`.

[6] T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608 (2025), Example 3.5 (closed-neighborhood version).
