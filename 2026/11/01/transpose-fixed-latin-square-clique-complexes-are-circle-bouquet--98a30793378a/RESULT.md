# Transpose-fixed Latin-square clique complexes are circle bouquets

## Finding
Let \(A=(\mathbb F_2)^d\) with \(d\ge3\), and put \(q=2^d\). Form the Latin-square graph \(G_A\) on \(A\times A\), with distinct \((a,b)\), \((c,e)\) adjacent exactly when \(a=c\), \(b=e\), or \(a+b=c+e\). Let \(X_A=\operatorname{Cl}(G_A)\) be its full flag/clique complex. Coordinate interchange \(\tau(a,b)=(b,a)\) acts simplicially.

**Theorem.** The *actual geometric fixed-point space*, not a quotient, is the following integral circle bouquet:
\[
|X_A|^{\langle\tau\rangle}\simeq\bigvee^{(q-1)(q/2-1)}S^1.
\]
Moreover, the fixed space admits a canonical PL triangulation as the flag complex of a graph with \(q(q+1)/2\) vertices. This graph consists of a central \(q\)-clique, one peripheral \((q/2)\)-clique for each \(h\in A\setminus\{0\}\), and \(q/2\) triangular interfaces per peripheral clique, described explicitly below. Thus
\[
\widetilde H_i(|X_A|^{\langle\tau\rangle};\mathbb Z)
\cong\begin{cases}\mathbb Z^{(q-1)(q/2-1)},&i=1,\\0,&i\ne1,\end{cases}
\]
and its fundamental group is free of rank \((q-1)(q/2-1)\). At \(q=8\) the fixed space is \(\bigvee^{21}S^1\), whereas the ambient complex has zero first homology by the cited Latin-square homology theorem.

## Assumptions and scope
All groups are elementary abelian of exponent two: addition is componentwise over \(\mathbb F_2\), so \(a+a=0\). The theorem is asserted for every integer \(d\ge3\) without an upper bound. The clique complex contains all complete subgraphs as simplices. Geometric fixed points mean points of the geometric realization invariant under the coordinate-interchange homeomorphism; they are not the simplex-wise fixed subcomplex on the original graph vertices. The PL triangulation described below uses barycenters of the original vertex orbits. No claim about an integral representation on ambient homology is made.

## Proof
**Step 1: The canonical fixed-point triangulation.** The orbits on \(V(G_A)\) are the \(q\) singletons \(D_a=\{(a,a)\}\) and the \(q(q-1)/2\) two-element sets \(O_{a,b}=\{(a,b),(b,a)\}\), with \(a\ne b\) and \(O_{a,b}=O_{b,a}\). Every orbit is a clique: the two vertices of \(O_{a,b}\) share the group-table sum \(a+b\). A fixed barycentric point of an original simplex has equal weights on the vertices of each present orbit, and conversely any simplex formed by a union of full orbits supports such points. The orbit barycenters therefore form a canonical PL triangulation of \(|X_A|^{\langle\tau\rangle}\). Because \(X_A\) is flag, two orbit vertices form an edge precisely when every cross pair of their original vertices is adjacent. A set of orbit vertices forms a simplex if and only if it is pairwise adjacent in this *orbit-complete graph*.

**Step 2: Determine all orbit-complete adjacencies.** Any two distinct \(D_a,D_b\) are adjacent, as their originals both have sum zero. For \(a\ne b\), \(D_c\) is adjacent to \(O_{a,b}\) if and only if \(c\in\{a,b\}\): when \(c\notin\{a,b\}\), neither row nor column agrees and the two sums are \(0\) and \(a+b\ne0\). For distinct off-diagonal orbits \(O_{a,b},O_{c,e}\), if \(a+b=c+e\) then every cross pair is adjacent by the sum rule. If the sums differ, no cross pair may use the sum rule, and complete cross adjacency would require simultaneously
\[
(a=c\ \text{or}\ b=e)\quad\text{and}\quad(a=e\ \text{or}\ b=c).
\]
Each of the four resulting conjunctions contradicts \(a\ne b\) or \(c\ne e\). Thus distinct off-diagonal orbits are completely adjacent exactly when their nonzero sums coincide.

**Step 3: Maximal simplices and a gluing decomposition.** Set \(D=\{D_a:a\in A\}\), a \(q\)-vertex simplex. For each \(h\ne0\) put \(P_h=\{O_{a,a+h}:a\in A\}\), identifying \(a\) and \(a+h\), so \(|P_h|=q/2\) and \(P_h\) spans a simplex. The involution \(a\mapsto a+h\) partitions \(A\) into \(q/2\) disjoint unordered pairs. For each such pair, the only mixed maximal face using its orbit vertex is
\[
T_{a,h}=\{D_a,D_{a+h},O_{a,a+h}\}.
\]
There are no further mixed faces: one off-diagonal orbit has exactly two adjacent diagonal vertices, and two distinct orbits in the same \(P_h\) have disjoint adjacent diagonal pairs, while orbits from distinct \(P_h\)'s are nonadjacent. For \(q\ge8\) these yield *all* maximal simplices: \(D\), the \(q-1\) simplices \(P_h\), and the \(q(q-1)/2\) triangles \(T_{a,h}\).

Let \(Y_h\) be the subcomplex consisting of \(P_h\) together with its \(q/2\) interface triangles and all their faces. Each triangle intersects \(P_h\) only at its own orbit vertex, and different interface triangles for this \(h\) are otherwise disjoint because the pairs partition \(A\). Hence \(Y_h\) is contractible. Its intersection with \(D\) is exactly the disjoint union of \(q/2\) diagonal edges \(\{D_a,D_{a+h}\}\). When the \(Y_h\)'s are attached in any order to a complex already containing \(D\), their intersection with the preceding union is still exactly that same disjoint union of \(q/2\) edges: different \(P_h\)'s do not intersect, and any common diagonal vertices or edges already lie in \(D\).

**Step 4: Homotopy type.** Each attaching intersection is a disjoint union of \(q/2\) contractible components. Both its inclusions, into the contractible \(Y_h\) and into the preceding union, are nullhomotopic: the latter factors through the simplex \(D\). All these inclusions are subcomplex inclusions and hence cofibrations. The homotopy pushout therefore wedges \(q/2-1\) circles onto the preceding connected complex. Starting from \(D\simeq *\) and attaching the \(q-1\) pieces \(Y_h\) gives \((q-1)(q/2-1)\) circles. This is a homotopy equivalence over the integers, rather than an inference from finite-dimensional homology ranks. Van Kampen and cellular homology give the stated fundamental group and integral homology.

## Verification
The standalone file `verify_transpose.py` independently constructs the original Latin-square graph and its coordinate-swap vertex orbits. For \(q=4,8,16,32\) it checks all orbit-pair complete adjacencies against the stated combinatorial classification. At \(q=4,8\) it additionally enumerates *every* orbit-graph clique, compares them with the independently constructed purported facets, and computes all reduced mod-two homology by exact binary boundary ranks. It also finds and verifies elementary free-face collapse sequences onto connected graphs: 10 collapse pairs at order four and 176 at order eight, retaining respective graph cycle ranks three and 21. Results: \(q=4\), 10 orbit vertices, 42 nonempty faces, three independent degree-one classes; \(q=8\), 36 orbit vertices, 444 nonempty faces, 21 independent degree-one classes. For \(q=16,32\) the orbit-graph adjacency checks pass on 136 and 528 orbit vertices respectively. The finite computations corroborate—but do not replace—the unrestricted argument in Steps 1–4.

## Relationship to prior work
Cioabă and Mim, *On the homology groups of clique complexes of strongly regular graphs* (arXiv:2606.27328, first public 2026-06-25), §§3.2–3.4, calculate the ordinary homology of Latin-square clique complexes and identify intercalate tetrahedra. They prove that the ambient first homology vanishes for orders at least five and determine the ambient second Betti number. Those facts do not specify the geometric fixed locus of coordinate interchange or its fundamental group. The prior structural classification of four-cliques includes intercalates but does not imply the orbit-complete adjacency criterion or the circle-bouquet count without additional arguments. Cioabă, Guo, Ji, and Mim, *Clique complexes of strongly regular graphs, their eigenvalues, and cohomology groups* (arXiv:2508.05871), study Laplacians and ordinary cohomology, not these fixed spaces. Published computations of symmetries on **rook-graph Čech complexes** concern a distinct complex and cannot imply this fixed-point classification. No logically covering result was found in the inspected literature; unindexed work remains a possible priority risk.

## Limitations
Only elementary abelian two-groups and the single coordinate-interchange involution are treated. The theorem does not classify all finite abelian group tables, equivariant homotopy types of the ambient complex, fixed spaces of other subgroups, or the action of residual automorphisms on the circle basis. The claim is a homotopy classification of the actual fixed polyhedron, not a PL classification of its homeomorphism type. Independent mathematical validation has not been performed.

## References
1. S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328v1 (first posted 2026-06-25), §3, especially the discussion of intercalates and the clique homology theorem. https://arxiv.org/abs/2606.27328
2. S. M. Cioabă, K. Guo, C. Ji, and M. Mim, *Clique complexes of strongly regular graphs, their eigenvalues, and cohomology groups*, arXiv:2508.05871v1 (first posted 2025-08-07), Sections 1, 4–5. https://arxiv.org/abs/2508.05871
