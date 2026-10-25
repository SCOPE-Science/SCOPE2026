# Three-coordinate translation fixed loci of scale-three hypercube Rips complexes

## Finding
For every integer \(n\ge3\), equip \(Q_n=\{0,1\}^n\) with Hamming distance, and let \(\tau\) flip exactly three specified coordinates. Write
\[
F_n=\bigl|\operatorname{VR}_{\le3}(Q_n)\bigr|^{\langle\tau\rangle},
\]
where the geometric fixed-point set is taken in the realization of the inclusive Vietoris--Rips complex. Put \(m=n-3\), \(v=2^m\), and for \(m\ge1\) put \(e=m2^{m-1}\). Then:

* \(F_3\) is contractible (in fact, a tetrahedron).
* For every \(n\ge4\), there is an integral homotopy equivalence
  \[
  F_n\simeq\bigvee^{e-v+1}S^1\ \vee\ \bigvee^{e}S^3.
  \]
  In particular, \(F_4\cong S^3\) piecewise-linearly; \(F_5\simeq S^1\vee\bigvee^4 S^3\); and \(F_6\simeq\bigvee^5 S^1\vee\bigvee^{12} S^3\).
* At every scale \(0\le r<3\), the geometric fixed set \(\bigl|\operatorname{VR}_{\le r}(Q_n)\bigr|^{\langle\tau\rangle}\) is empty.

More precisely, for \(m\ge1\), \(F_n\) has a canonical simplicial model assembled from \(e\) copies of the boundary of the four-dimensional cross-polytope. Two copies meet in one full tetrahedral facet precisely when their indexing edges of the \(m\)-cube share an endpoint; all copies incident to a common cube vertex share that same tetrahedron. Its simplicial face vector is
\[
(f_0,f_1,f_2,f_3)
=e(8,24,32,16)-(2e-v)(4,6,4,1).
\]
All reduced integral homology groups therefore vanish except degrees one and three, with respective free ranks \(e-v+1\) and \(e\). In particular the geometric fixed set is not, in general, homotopy equivalent to a single-dimensional wedge of spheres.

## Assumptions and scope
The vertex set \(Q_n\) is a finite metric space with Hamming distance. The complex \(\operatorname{VR}_{\le r}(Q_n)\) contains a finite nonempty vertex set exactly when its diameter is at most \(r\). The action of \(\tau\) is the literal geometric realization of the simplicial permutation induced by translating by the vector with exactly three unit coordinates. The symbol \(F_n\) refers to geometric fixed points, not the vertexwise fixed subcomplex (which has no vertices), not an orbit quotient, and not invariant homology. Throughout, spheres and wedges are based homotopy types; an empty wedge of circles is omitted. The result covers all \(n\ge3\) at inclusive scale three, plus the assertion of emptiness at smaller real scales.

## Proof
**1. Fixed simplices and orbit barycenters.** Because \(\tau\) acts freely on the vertices, every fixed point lies in a unique minimal face that is a union of complete two-element \(\tau\)-orbits. Conversely, the barycenters of the two vertices of each orbit span a simplex in the fixed locus exactly when the union of the corresponding orbits is a face. This constructs a canonical piecewise-linear homeomorphism from \(F_n\) onto the orbit-union complex. Any orbit by itself is admissible at scale three, because its two vertices are at Hamming distance three. At any smaller scale no such orbit is admissible, and hence no fixed point exists.

**2. Exact orbit compatibility.** Permute coordinates so the first three are flipped. Represent each orbit uniquely by \((c,u)\), where \(c\in\{00,01,10,11\}\) records the two unflipped choices among the first three bits after fixing the first bit to zero, and \(u\in Q_m\) records the remaining bits. The first-three-bit complements give the other member of the orbit. For distinct orbit labels \((c,u)\) and \((d,w)\), let \(a\in\{0,1,2\}\) be the Hamming distance between \(c\) and \(d\), and \(b=d_{Q_m}(u,w)\). Among the four cross distances between the two orbits, the largest equals \(b+\max(a,3-a)\). Thus the orbits are compatible precisely when either \(c\ne d\) and \(b\le1\), or \(c=d\) and \(b=0\). The latter case is equality of the orbits and is excluded here. Therefore distinct labels are adjacent in the orbit-union complex exactly when
\[
 c\ne d\quad\text{and}\quad d_{Q_m}(u,w)\le1.
\]
All higher simplices are determined by these pairwise conditions, since the starting Rips complex is flag.

**3. Cross-polytope edge blocks.** For \(m=0\), the four orbit labels form a full tetrahedron. Suppose \(m\ge1\). The orbit labels above each \(u\in Q_m\) form a tetrahedron \(\Delta_u\). The \(m\)-cube has no triangles, so the projection of every clique to \(Q_m\) is supported on one vertex or on the two endpoints \(u,w\) of one cube edge. For an edge \(uw\), the eight labels \((c,u),(c,w)\), with four possible colors \(c\), form the join of four two-point complexes \(S^0\), because exactly the four same-color cross pairs are forbidden. The resulting subcomplex \(B_{uw}\) is the boundary of a four-dimensional cross-polytope, hence a PL \(S^3\). Its opposite tetrahedral facets \(\Delta_u\) and \(\Delta_w\) are disjoint. All maximal faces are in these blocks, so
\[
 F_n=\bigcup_{uw\in E(Q_m)} B_{uw},
\]
with intersections along the stated \(\Delta_u\)'s. Every \(\Delta_u\) is present because \(Q_m\) has no isolated vertices.

**4. Exact integral homotopy type.** The tetrahedra \(\Delta_u\) have pairwise disjoint vertex sets, are contractible subcomplexes, and may be contracted individually to distinct points without changing the homotopy type of the entire finite CW complex. Within each block \(B_{uw}\cong S^3\), collapsing the two disjoint closed tetrahedral facets separately yields another PL three-sphere with two distinguished points (its suspension poles): removing their relative interiors leaves a PL spherical annulus, and collapsing its two boundary spheres gives the suspension of \(S^2\). After these contractions, the whole complex is a graph of \(e\) three-spheres indexed by the edges of \(Q_m\), each glued to the rest at just its two poles. Choose in each three-sphere an arc joining the poles. Their union is a copy of the one-dimensional cube graph \(Q_m\). Collapsing a spanning tree of these arcs, a contractible CW subcomplex, does not change homotopy type. Each tree edge leaves one three-sphere, while each of the other \(e-v+1\) edges leaves a three-sphere and an additional circle. Hence the quotient, and therefore \(F_n\), has homotopy type
\[
\bigvee^{e-v+1} S^1\vee\bigvee^e S^3.
\]
This is an ordinary integral homotopy equivalence, not merely a rational or mod-two homology calculation.

**5. Face counting.** Each edge block has face vector \((8,24,32,16)\), and each vertex tetrahedron has face vector \((4,6,4,1)\). Among the \(2e\) block incidences, the \(v\) distinct vertex tetrahedra should each be counted only once. Subtracting their \(2e-v\) redundant incidences gives the displayed face-vector formula. The Euler characteristic agrees with the wedge decomposition.

## Verification
The included standalone `verify.py` reconstructs all pairwise compatibilities directly from the original Hamming metric and compares them with the orbit adjacency law for \(m=1,2,3,4,5\) (that is, \(4\le n\le8\)). For \(m=1,2,3\) it also independently enumerates all maximal cliques of the raw compatibility graph, agreeing with the cross-polytope facets. For every \(m=1,\ldots,5\) it builds all simplicial faces, checks the formula for their number in each dimension, and computes boundary ranks over \(\mathbb F_2\). Observed unreduced Betti ranks \((\beta_0,\beta_1,\beta_2,\beta_3)\) are respectively \((1,0,0,1)\), \((1,1,0,4)\), \((1,5,0,12)\), \((1,17,0,32)\), and \((1,49,0,80)\). The executable reports `VERIFY_OK`. These bounded finite checks do not establish the all-parameter theorem or integral homotopy equivalence; those follow from the proof above.

## Relationship to prior work
Bendersky--Elia--Grbić study cohomological properties of ambient hypercube Rips complexes (first public preprint May 1, 2026). Galetto--Montaño--Wellner determine ambient hyperoctahedral-group homology representations at small Rips scales (first public preprint June 18, 2026). Their stated ambient homology and representation conclusions do not logically imply the homotopy type of the geometric fixed-point locus of a specified nontrivial translation. Earlier ambient scale-three homotopy computations by Feng and homology bounds by Shukla are likewise insufficient to recover this fixed-locus classification. The present result uses a different geometric object: a PL subspace of the ambient Rips realization defined by an involution. The relevant 2026 preprints were available here at the abstract and bibliographic level, not in complete text; whether their full proofs contain overlapping intermediate fixed-locus constructions remains a bibliographic priority risk.

## Limitations
No claim is made about the fixed locus at scales larger than three, about actions generated by more than one translation, or about the equivariant homotopy type of the ambient Rips complex. The integral homotopy splitting is proven for the exact three-coordinate translation only. Exact novelty relative to unindexed literature, or intermediate calculations inside incompletely accessible primary papers, has not been independently certified. The finite checker gives mod-two homology corroboration only; the general proof supplies the integral result.

## References
1. M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris--Rips Complex of a Hypercube Graph*, arXiv:2605.00705, version first publicly submitted 2026-05-01, https://arxiv.org/abs/2605.00705.
2. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, version first publicly submitted 2026-06-18, https://arxiv.org/abs/2606.20784.
3. Z. Feng, *Homotopy types of Vietoris--Rips complexes of Hypercube Graphs*, arXiv:2305.07084, version first publicly submitted 2023-05-11, https://arxiv.org/abs/2305.07084.
4. S. Shukla, *On Vietoris--Rips complexes (with scale 3) of hypercube graphs*, arXiv:2202.02756, first publicly submitted 2022-02-06, https://doi.org/10.1137/22M1481440.
5. M. Adamaszek and H. Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040, first publicly submitted 2021-03-01, https://arxiv.org/abs/2103.01040.
