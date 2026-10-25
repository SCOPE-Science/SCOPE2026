# Weight-three translation fixed spaces in hypercube Vietoris–Rips complexes

## Finding
For every integer \(n\ge4\), let \(K_n=\operatorname{VR}_{\le3}((\mathbb F_2)^n)\), where Hamming distance is used and a simplex is a set of diameter at most three. If \(t\) translates by any vector of Hamming weight exactly three, write \(m=n-3\), \(v=2^m\), and \(e=m2^{m-1}\). Then the **geometric** fixed-point space, not the combinatorial subcomplex on individually fixed vertices, has homotopy type
\[
|K_n|^{\langle t\rangle}\simeq\bigvee^{e-v+1}S^1\vee\bigvee^{e}S^3.
\]
The reduced integral homology is free of rank \(e-v+1\) in degree one and rank \(e\) in degree three; all other reduced integral homology groups vanish. Its fundamental group is free of rank \(e-v+1\). For \(n=4,5,6,7\), respectively, the wedge ranks (circles, three-spheres) are \((0,1),(1,4),(5,12),(17,32)\).

## Assumptions and scope
The domain is exactly the full Boolean cube of dimension \(n\ge4\), inclusive Rips scale three, and the order-two translation induced by a weight-three vector. Coordinate permutations conjugate all such translations, so the conclusion is independent of which three coordinates are flipped. The statement is about topological fixed points inside the geometric realization. The rank formulas refer to the cube graph with \(v\) vertices and \(e\) edges in dimension \(m=n-3\), which is connected for \(m\ge1\).

## Proof
**1. Orbit-complex identification.** For a simplicial complex acted on by a vertex permutation of order two with no fixed vertices, construct its orbit complex \(L\) whose vertices are the two-element vertex orbits and whose faces are sets of orbits whose union is a simplex of the original complex. The fixed points of a geometric simplex have equal barycentric weights on each pair. Sending a barycentric weight on an orbit in \(|L|\) to half that weight on each of its two vertices gives a simplexwise affine bijection \(|L|\to|K_n|^{\langle t\rangle}\). Its inverse adds the equal weights in each orbit. The finite simplicial constructions make this a piecewise-linear homeomorphism.

**2. Four colors over the smaller cube.** Permute coordinates to write \(t(a,u)=(a+(1,1,1),u)\), with \(a\in\mathbb F_2^3\) and \(u\in\mathbb F_2^m\). The orbits are indexed by \((u,c)\), where the color \(c\) is one of the four antipodal pairs \(\mathbb F_2^3/\langle(1,1,1)\rangle\). The union of two orbits indexed \((u,c)\) and \((w,d)\) has Hamming diameter
\[
d_H(u,w)+\begin{cases}3,&c=d,\\2,&c\ne d.\end{cases}
\]
For distinct orbit vertices, the union is admissible at scale three precisely when either \(u=w\) (all distinct colors compatible), or \(u,w\) are adjacent in the cube graph and \(c\ne d\). An individual orbit always has diameter three. The orbit complex is flag because the original Rips complex is flag: admissibility of any collection of vertex orbits is equivalent to pairwise admissibility of their unions. Thus each cube vertex \(u\) supports a tetrahedral simplex \(\Delta_u\) on all four colors; a mixed face occurs only over endpoints of one cube edge, since the cube graph contains no triangle.

**3. A sphere for each cube edge.** For an edge \(uw\) of the smaller cube, let \(S_{uw}\) be the subcomplex on its eight orbit vertices. The only four missing edges connect equal colors at its two endpoints, hence
\[
S_{uw}=(S^0)^{*4}\cong S^3,
\]
where the displayed homeomorphism is that of the standard four-dimensional cross-polytope boundary. The tetrahedra \(\Delta_u\) and \(\Delta_w\) are opposite, vertex-disjoint facets of this sphere. All faces of \(L\) belong to some \(S_{uw}\), because every vertex of the connected cube graph belongs to an edge. For distinct cube edges \(uw\) and \(ab\), their corresponding spheres intersect in exactly \(\Delta_z\) if the cube edges share endpoint \(z\), and are disjoint otherwise; for an attaching edge \(uw\), its intersection with the union of preceding edge spheres is therefore the union of \(\Delta_u\) and/or \(\Delta_w\), according to which endpoints have previously appeared. No previously added edge sphere contains a face mixed across both endpoints of the new edge.

**4. Homotopy pushouts and the cycle rank.** Select a spanning tree of the smaller cube and add the corresponding cross-polytope spheres in rooted tree order. The first edge sphere is \(S^3\); each successive tree edge attaches along exactly one contractible tetrahedral facet and therefore wedges on another \(S^3\). After all \(v-1\) tree edges the space is a wedge of \(v-1\) three-spheres and is connected.

Each of the other \(e-v+1\) cube edges attaches a further \(S^3\) along the union of its two **disjoint** tetrahedral facets, already contained in the previous connected union. These inclusions are cofibrations. In their homotopy-pushout diagram, replace each facet by one point; the maps from the two points into each connected side can be homotoped to the same chosen basepoint. The homotopy pushout is consequently the wedge of the prior union, the newly attached \(S^3\), and a circle corresponding to the second component of the attaching intersection. This adds one sphere and one circle for each non-tree edge. The total is \(e\) three-spheres and \(e-v+1\) circles, proving the claimed homotopy equivalence and its integral homology and fundamental-group consequences.

## Verification
A standalone exact finite checker, `verify_weight3.py`, constructs the orbit graph directly from Hamming distances, computes its maximal cliques, and independently compares these to the four-fold cross-polytope facets over each edge of the smaller hypercube. It also computes all mod-two simplicial boundary ranks in dimensions up to three, for every \(n=4,5,6,7\). These values agree with the wedge formula; the checker reports the maximal tetrahedron counts \(16,60,176,464\), and the reduced Betti tuples \((0,0,0,1),(0,1,0,4),(0,5,0,12),(0,17,0,32)\). The parameter-uniform homotopy equivalence comes from the preceding proof, not from extrapolating finite cases.

## Relationship to prior work
Feng established the nonequivariant scale-three hypercube Rips homotopy-sphere classification. Adams and Virk investigated its homology and cross-polytopal generators. Galetto, Montaño and Wellner subsequently classified the **rational homology representations** under the full hyperoctahedral group at scale three. Those representation results describe induced actions on homology of the original complex, rather than the actual geometric fixed-point spaces; they do not imply, for example, the free fundamental groups proved here. The cross-polytope building blocks in this result are related to the cross-polytopal constructions appearing in that literature, but their specific orbit-space arrangement and geometric fixed-space homotopy types are separate statements.

## Limitations
Only involutions translating by Hamming weight exactly three, not arbitrary subgroups or all translation weights, are classified. The result makes no claim to an equivariant homotopy-equivalence of the entire original complex, nor to new nonequivariant Betti numbers or new representation characters. It establishes no persistence claim. As with any originality assessment, the existence of an unindexed equivalent fixed-point construction cannot be categorically excluded.

## References
1. Z. Feng, *Homotopy types of Vietoris–Rips complexes of Hypercube Graphs*, arXiv:2305.07084 (initial public preprint May 11, 2023), Theorem 24. https://arxiv.org/abs/2305.07084
2. H. Adams and Ž. Virk, *Lower bounds on the homology of Vietoris–Rips complexes of hypercube graphs*, arXiv:2309.06222 (2023), sections 2 and 4. https://arxiv.org/abs/2309.06222
3. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (2026), introduction and sections on the homology representations at scales two and three. https://arxiv.org/abs/2606.20784
