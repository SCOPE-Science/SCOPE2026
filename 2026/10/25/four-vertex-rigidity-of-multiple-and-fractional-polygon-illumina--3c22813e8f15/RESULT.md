# Four-vertex rigidity of multiple and fractional polygon illumination

## Finding
Let \(Q\subset\mathbb R^2\) be a convex quadrilateral with four distinct genuine vertices, and let \(m\ge1\) be an integer. A direction \(u\in S^1\) illuminates \(x\in\partial Q\) when \(x+t u\in\operatorname{int}Q\) for some \(t>0\). Repeated directions are counted with multiplicity. Write \(I^m(Q)\) for the least multiset cardinality that illuminates every boundary point at least \(m\) times. Then
\[
I^m(Q)=\begin{cases}
4m,&Q\text{ is a parallelogram},\\
3m,&Q\text{ is not a parallelogram}.
\end{cases}
\tag{1}
\]
The **fractional illumination number** \(I^*(Q)\), defined as the least total nonnegative weight on a finite collection of illuminating directions such that each boundary point receives weight at least \(1\), satisfies
\[
I^*(Q)=\begin{cases}4,&Q\text{ is a parallelogram},\\3,&\text{otherwise}.\end{cases}
\tag{2}
\]
These values remain valid under arbitrary nonsingular affine changes of coordinates.

There is a rigid optimality criterion. If \(Q\) is not a parallelogram, one can choose a vertex \(v_*\) belonging to **every** pair of distinct vertices simultaneously illuminable by a single direction. Consequently, every optimal multiset of \(3m\) directions illuminates each of the other three vertices exactly \(m\) times, and every direction in that multiset illuminates precisely one of these three vertices (possibly also \(v_*\)).

## Assumptions and scope
Vertices are listed counterclockwise as \(v_1,\ldots,v_4\), with no straight interior angle. Write \(n_j\) for the outward normal to the edge from \(v_j\) to \(v_{j+1}\), indices modulo \(4\). The positive counterclockwise turn from \(n_{i-1}\) to \(n_i\) is \(\alpha_i\), so
\[
0<\alpha_i<\pi,\qquad\sum_{i=1}^4\alpha_i=2\pi.
\tag{3}
\]
For the fractional variant, it is enough to consider finite weighted sets; the lower bounds apply just as well to arbitrary finite nonnegative measures. Neither point-source illumination nor a fixed-angle illumination margin is asserted. Ordinary infinite-dimensional convex bodies and polygons with more than four genuine vertices are outside the theorem.

## Proof
**Vertex illumination and normal semicircles.** For a direction \(u\), the vertex \(v_i\) is illuminated if and only if
\[
\langle u,n_{i-1}\rangle<0
\quad\text{and}\quad
\langle u,n_i\rangle<0.
\tag{4}
\]
Necessity follows from the two incident supporting halfplanes. For sufficiency, all other supporting inequalities are strictly slack at the vertex, hence a sufficiently short positive displacement in direction \(u\) enters the interior. Equation (4) says that the two adjacent outward normals lie in an open semicircle centered at \(-u\). More generally, a direction illuminates a vertex set exactly when all incident outward normals are contained in one common open semicircle.

No direction can illuminate nonadjacent vertices. Such a pair has all four edge normals in its union of incident normals. But the four normals cannot fit into any open semicircle: if they did, the complementary circular gap between two consecutive normals would be strictly greater than \(\pi\), contradicting every \(\alpha_i<\pi\). The same argument excludes illumination of three or more vertices.

For adjacent vertices \(v_i,v_{i+1}\), their three incident normals are \(n_{i-1},n_i,n_{i+1}\). Those normals fit in an open semicircle **exactly when**
\[
\alpha_i+\alpha_{i+1}<\pi.
\tag{5}
\]
Indeed, the forward arc containing the middle normal has that length. When its length is at least \(\pi\), none of the three circular gaps among these normals exceeds \(\pi\) (the two individual gaps are below \(\pi\), and the remaining gap is at most \(\pi\)); consequently no open semicircle contains the three. Equality fails because vertex illumination is strict.

**The angular-star lemma.** Define the admissible-pair graph on the four vertices: the edge \(v_iv_{i+1}\) is present just when (5) holds. The two opposite edges of this graph cannot both be present, since the respective exterior-angle sums add to \(2\pi\). Therefore the graph has no matching of size \(2\); if it contains any edges, they all share a vertex \(v_*\). It is empty precisely when all four neighboring two-angle sums are \(\pi\). These equalities imply \(\alpha_1=\alpha_3\) and \(\alpha_2=\alpha_4\), hence opposite edge normals are antipodal and \(Q\) is a parallelogram. Conversely, for a parallelogram all neighboring sums equal \(\pi\). Thus every non-parallelogram has a nonempty admissible-pair star.

**Integral lower bound.** For a non-parallelogram, fix its star vertex \(v_*\). Every direction illuminates at most one of the other three vertices. Any \(m\)-fold illumination therefore uses at least \(3m\) directions, because those three vertices require at least \(3m\) total incidences. For a parallelogram the admissible-pair graph is empty, so every direction illuminates at most one of its four vertices and the lower bound is \(4m\).

**Integral upper bound.** In the non-parallelogram case choose any admissible pair and a direction illuminating its two vertices, guaranteed by (5). Choose one direction illuminating each remaining vertex; (4) ensures each inward cone is nonempty. These three directions illuminate all four vertices, hence every edge as well: if a direction illuminates an endpoint of an edge, it points strictly inward across that edge's supporting line, so it illuminates every point in the relative interior of that edge. Repeating these three directions \(m\) times gives an \(m\)-fold illumination of the entire boundary. In the parallelogram case, use one inward direction at each vertex and repeat each \(m\) times. The lower bounds are attained, proving (1).

**Fractional lower and upper bounds.** Replace counts by nonnegative direction weights. The same star argument says that total incident weight at the three vertices other than \(v_*\) is at most total weight. Since each of those vertices requires weight \(1\), total weight is at least \(3\). A parallelogram similarly requires total weight at least \(4\). The just-constructed three- or four-direction covers with weights \(1\) attain both bounds, proving (2).

**Rigidity of optimal multisets.** With \(3m\) directions and three non-star vertices each demanding \(m\) incidences, equality in the incidence-count lower bound forces all three vertex coverage counts to equal \(m\), and forces every selected direction to hit exactly one of these three vertices. This is also a sufficient characterization once the star vertex receives at least \(m\) incidences. The parallelogram analogue forces exactly \(m\) vertex incidences at each of its four vertices, one per direction.

## Verification
The proof is symbolic and covers every genuine convex quadrilateral and every positive integer multiplicity; its validity does not rely on finite computation. The embedded `verify.py` independently constructs the normal-fan sign cells for every four-positive-turn fan with denominator \(N\in\{10,12,14\}\), subject to each turn being strictly less than \(\pi\). For each fan it enumerates the realizable illumination masks and solves the exact capped multicover problem by breadth-first search for \(m=1,2,3,4\). It also checks that every feasible two-vertex mask belongs to a single star. The finite tests cover \(275\) fans with four multiplicities each; they corroborate, but do not establish, the unrestricted theorem.

## Relationship to prior work
Sriamorn's 2023 paper introduced the \(m\)-fold illumination formulation, established the general planar lower bound \(2m+1\), computed the regular \(n\)-gon value \(\lceil mn/\lfloor(n-1)/2\rfloor\rceil\), and stated the algorithmic determination for arbitrary convex polygons as Problem 2. It explicitly gives \(3m\) for triangles and \(4m\) for parallelograms. Those statements do not settle **non-parallelogram quadrilaterals**: the general lower bound is smaller than \(3m\) once \(m\ge2\), and a generic quadrilateral is neither regular nor a parallelogram.

A published result on polygons with antipodally paired normal fans has the regular-style formula; for four sides that fan assumption forces a parallelogram, which is already the covered branch here. Published equiangular-polygon fractional illumination results similarly cover a four-sided parallelogram but not an arbitrary non-parallelogram normal fan. The present distinction comes from the no-disjoint-illuminable-pairs structure and also determines the fractional optimum, not just a particular ordinary cover.

This is a complete smallest-side-count nonsymmetric benchmark in the arbitrary-polygon problem. For comparison, regular pentagons **do** obtain a multiple-cover saving: the cited regular-polygon formula gives \(I^2(P_5)=5<6=2I^1(P_5)\), whereas (1) gives no such saving at four vertices.

## Limitations
The result is confined to four-vertex convex polygons; the star lemma is false as stated for larger polygons. Its immediate extension to triangles and parallelograms is already recorded in the source, and novelty is asserted only for the non-parallelogram branch and its joint fractional/optimality classification. The comparison is based on the primary 2023 full text, targeted literature queries, and published-result summaries; it is not a comprehensive priority search or independent validation. A stronger unlocated treatment of circular-arc multicover may subsume this small polygon case, even without using the same terminology.

## References
1. Kirati Sriamorn, *On the multiple illumination numbers of convex bodies*, arXiv:2306.13517v1 (first public 2023-06-23), especially Section 3.3, Theorem 1.8, and Conclusion Problem 2. https://arxiv.org/html/2306.13517v1
2. *Exact multiple illumination and parity rigidity for polygons with antipodal edge-normal fans*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-multiple-illumination-and-parity-rigidity-for-polygons-wit--f4e6962728dc (consulted as record summary; no full-text exclusion asserted).
3. *Exact fractional illumination of every equiangular polygon*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fractional-illumination-of-every-equiangular-polygon--035cb636082a (record summary only).
