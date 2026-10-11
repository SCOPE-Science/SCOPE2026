# Exact inradius and contact-facet rigidity of the Petersen symmetric edge polytope

## Finding
Let \(G=KG(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of \([5]\), and two vertices are adjacent precisely when the subsets are disjoint. Put
\[
H=\{x\in\mathbb R^{V(G)}:\sum_{u\in V(G)}x_u=0\},\qquad
P=\operatorname{conv}\{\pm(e_u-e_v):uv\in E(G)\}\subset H.
\]
With the Euclidean metric inherited from \(\mathbb R^{10}\), the radius of a largest ball contained in \(P\) is exactly
\[
\boxed{r(P)=\sqrt{5/28}}.
\]
The origin-centered largest ball touches exactly \(30\) facets, and **the origin is the unique center of any ball of this maximum radius**. The contacting outward facet normals, normalized to support value one, form one antipodal orbit \(\{\pm f_e:e\in E(G)\}\) of size \(30\). For \(e=\{A,B\}\), where \(A,B\) are disjoint two-element subsets of \([5]\), the normal \(f_e\in H\) has coordinates
\[
(f_e)_U=\begin{cases}
6/5,&U=A\text{ or }U=B,\\
-4/5,&U\cap A\ne\varnothing\text{ and }U\cap B\ne\varnothing,\\
1/5,&\text{otherwise}.
\end{cases}
\]
Thus \(f_e\cdot x\le1\) and \(-f_e\cdot x\le1\) are precisely the thirty closest facet inequalities.

## Assumptions and scope
All graph edges are unweighted and all Euclidean distances are measured in the intrinsic nine-dimensional subspace \(H\) using its inherited inner product, **not** in an arbitrary projected coordinate realization. The inscribed ball may have any center in \(H\); its radius is not assumed to be attained uniquely at the origin. The claims concern this specific canonical graph and polytope, not arbitrary Kneser graphs or other metrics. Every vertex index \(U\) in the formulas is a two-element subset, not an element of \([5]\).

## Proof
**1. Polar and integral potentials.** Since \(G\) is connected, its edge differences span \(H\), and the origin lies in the interior of \(P\). Its polar in \(H\) is the bounded Lipschitz polytope
\[
Q=P^\circ=\{h\in H:|h_U-h_W|\le1\text{ for every }UW\in E(G)\}.
\]
The origin-centered inradius is \(\bigl(\max_{h\in Q}\|h\|_2\bigr)^{-1}\): indeed, the hyperplane \(h\cdot x=1\) has distance \(1/\|h\|_2\), and it suffices to test vertices of \(Q\), which are the facet normals. Because \(P\) is centrally symmetric, this is also its unrestricted inradius: if radius-\(R\) balls centered at \(z\) and \(-z\) lie in \(P\), convexity places the radius-\(R\) ball centered at their midpoint, the origin, inside \(P\). Every \(h\in Q\) has a tight-edge subgraph formed by the edges with \(|h_U-h_W|=1\). A vertex of \(Q\) must have connected tight-edge graph: if it is disconnected, a small nonconstant component-wise perturbation inside \(H\) keeps all inequalities valid, contradicting extremality. Conversely, if it is connected, the tight equations have rank nine and isolate \(h\), so it is a vertex. On a connected tight graph, choosing a base vertex shows that all coordinate differences are integers. The Petersen graph has graph diameter two: two disjoint two-sets are adjacent, and two intersecting two-sets have a common neighbor equal to the complement of their three-element union. Thus every such vertex, after adding a constant, is represented by an integer-valued \(1\)-Lipschitz labeling taking values in \(\{0,1,2\}\). These arguments do not assume that the labeling reaches both extremes.

**2. Cross-intersection bound.** For any such labeling \(p\), let \(a,b,c\) denote the numbers of labels \(0,2,1\), respectively, so \(a+b+c=10\). If either \(a=0\) or \(b=0\), the range of \(p\) is at most one. Hence
\[
\sum_U(p_U-\overline p)^2\le10/4=5/2.
\]
Now assume \(a,b\ge1\), and write \(\mathcal A\) for the two-element subsets labeled zero and \(\mathcal B\) for those labeled two. They are disjoint families, and they are *cross-intersecting*: every member of \(\mathcal A\) intersects every member of \(\mathcal B\). Indeed, disjoint members would be adjacent in \(G\), contradicting the Lipschitz condition.

Here are the needed sharp finite cross-intersection bounds on \(\binom{[5]}2\). If \(a=1\), then \(b\le6\): exactly six other pairs intersect a fixed two-set. If \(a=2\), then \(b\le4\), with equality only when the two zero-labeled pairs are disjoint; two disjoint pairs have exactly four common-intersecting pairs (the four crosses), whereas two intersecting pairs have only three such pairs outside themselves. The same statements hold with \(a,b\) interchanged. Finally, **\(a\ge3\) and \(b\ge3\) cannot both occur**. To prove this, take any three members of \(\mathcal A\). If two are disjoint, relabel them \(12\) and \(34\). Every member of \(\mathcal B\) must lie among \(13,14,23,24\); a third distinct member of \(\mathcal A\) meets at most two of these four, once the disjointness of the color families is respected, so \(b\le2\). If no two members of \(\mathcal A\) are disjoint, any three are either a three-edge star or a triangle. A two-subset meeting all three star edges must contain the common vertex, leaving at most one permissible member of \(\mathcal B\) outside the star. A two-subset meeting all three edges of a triangle must itself be a triangle edge, leaving none. This proves the bounds.

**3. Exact norm maximum and equality.** Translating all labels by a common constant leaves their centered norm unchanged, and a direct expansion gives
\[
\|p-\overline p\mathbf1\|_2^2=a+b-\frac{(a-b)^2}{10}.
\]
By the preceding bounds, either \(\min\{a,b\}=1\) and the right side is at most \(9/2\), or \(\min\{a,b\}=2\) and it is at most \(28/5\); the case \(\min\{a,b\}\ge3\) is impossible. Equality \(28/5\) occurs exactly for \(\{a,b\}=\{2,4\}\) when the size-two extreme family consists of two disjoint pairs and the size-four extreme family consists of their four crosses. No range-one function attains this value.

Take, for example, the two disjoint pairs \(12,34\) at level two, the four crosses \(13,14,23,24\) at level zero, and the four remaining pairs \(15,25,35,45\) at level one. Its tight edges form a connected spanning graph: \(12\) meets \(35,45\) by Petersen adjacency; \(34\) meets \(15,25\); each of the four crosses is Petersen-adjacent to two of these middle pairs, connecting both groups. Hence the centered equality labeling is a **vertex** of \(Q\). The labels have mean \(4/5\), giving the displayed \(f_e\) coordinates \(6/5,-4/5,1/5\). Every choice of the unordered disjoint-pair edge \(e\) gives one normal, and switching levels zero and two gives its negative. There are \(15\) such edges, and the resulting \(30\) vectors are distinct. Their common squared norm is \(28/5\). Thus these, and only these, maximize norm among the polar vertices. A strictly convex squared norm on the bounded polytope \(Q\) cannot be maximized at a nonvertex, so there are no additional farthest points. Polar duality now yields \(r(P)=\sqrt{5/28}\) and precisely thirty nearest facets.

**4. Uniqueness of the optimal center.** The normals \(\{f_e\}\) span \(H\). To verify this directly, let \(A_J\) be the \(10\times10\) adjacency matrix of the Johnson graph on the two-subsets of \([5]\), where adjacency means nonempty intersection. Let \(J_{10}\) be the all-ones matrix. Counting the three coordinate levels in the fifteen explicit normals gives the Gram identity
\[
\sum_{e\in E(G)} f_e f_e^{\mathsf T}=6I_{10}-5A_J+\frac{12}{5}J_{10}.
\]
For clarity, its diagonal entries are \(42/5\), the entries for two intersecting pairs are \(-13/5\), and the entries for two disjoint pairs are \(12/5\); these follow by summing the products of the explicit three-level labels over all fifteen choices of \(e\). Let \(D\) be the \(10\times5\) unsigned incidence matrix of the ten two-subsets of \([5]\). Then \(A_J=DD^{\mathsf T}-2I_{10}\) and \(D^{\mathsf T}D=3I_5+J_5\). Consequently \(A_J\) has eigenvalues \(6\) once, \(1\) four times, and \(-2\) five times. On \(H\), the Gram sum therefore has eigenvalues \(1\) four times and \(16\) five times: it is positive definite and all fifteen normals span \(H\).

Suppose a ball of radius \(r(P)\) centered at \(z\in H\) lies in \(P\). For every facet pair \(\pm f_e\cdot x\le1\), both inequalities force
\[
\pm f_e\cdot z+r(P)\|f_e\|_2\le1.
\]
Because \(r(P)\|f_e\|_2=1\), this means \(f_e\cdot z=0\) for every edge \(e\). Their span is \(H\), hence \(z=0\), proving the asserted rigidity.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. Run `python verify.py` from the directory containing the file. It constructs the Petersen graph from all two-element subsets of a five-set and exhaustively enumerates all \(3^9\) assignments of signed tight-edge differences along a fixed spanning tree. It checks every graph Lipschitz inequality and connectedness of the tight-edge subgraph. It obtains \(2613\) feasible integer labelings, \(1410\) polar vertices (equivalently facets), maximum exact centered squared norm \(28/5\), and exactly \(30\) maximizers. Independently generating the thirty explicit normals reproduces the entire maximizer set. An exact integer Gram calculation and rational row reduction verify rank nine and the claimed reciprocal squared radius. The proof above establishes the identities without relying on floating-point experiments.

## Relationship to prior work
D’Alì, Delucchi and Michałek introduced a broad framework for symmetric edge polytopes and their metric-space duals [1]. Higashitani, Jochemko and Michałek's integral Lipschitz facet criterion is recorded explicitly as Theorem 2.3 in Braun and Bruegge [3]. Chen, Davis and Korchevskaia [2] characterize facet subgraphs via maximal bipartite subgraphs. The present calculation uses that general framework but directly evaluates a separate metric invariant for the Petersen graph: the maximum Euclidean norm of a polar potential, its entire equality orbit, and the uniqueness of largest-ball centers. General facet descriptions and unrelated graph-embedding distortion invariants do not themselves yield the value \(28/5\), the thirty contacts, or the span certificate. There is a mathematical alias with the maximum variance of unit-Lipschitz functions on the Petersen graph: this variance is exactly \(14/25\) by the theorem, using uniform vertex weights.

## Limitations
The theorem is specific to \(KG(5,2)\) and the Euclidean metric inherited from the ten coordinate directions. The polar facet count \(1410\) is supported by the complete finite enumeration in `verify.py`; it is not required for the proof of the exact inradius and thirty contact facets. Literature on graph spread (maximum variance of Lipschitz functions), particularly Yancey's work [4], may use an equivalent vocabulary; full-text comparison with [4] was unavailable, and the existence of an alternative published evaluation cannot be excluded solely by unsuccessful text searches. No result is claimed for larger Kneser graphs.

## References
1. A. D’Alì, E. Delucchi and M. Michałek, “Many faces of symmetric edge polytopes,” arXiv:1910.05193 (first publicly posted 2019-10-11). https://arxiv.org/abs/1910.05193
2. T. Chen, R. Davis and E. Korchevskaia, “Facets and facet subgraphs of symmetric edge polytopes,” arXiv:2107.12315 (first publicly posted 2021-07-26). https://arxiv.org/abs/2107.12315
3. B. Braun and K. Bruegge, “Facets of Symmetric Edge Polytopes for Graphs with Few Edges,” arXiv:2201.13303 (first publicly posted 2022-01-31), especially Theorem 2.3. https://arxiv.org/abs/2201.13303
4. M. P. Yancey, “Positively curved graphs,” *Journal of Graph Theory* **94** (2020), 539–578, DOI:10.1002/jgt.22545 (abstract inspected; complete text unavailable).
