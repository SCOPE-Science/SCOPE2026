# Fixed-point homotopy for triple flips of scale-three hypercube Vietoris–Rips complexes

## Finding

For every integer \(n\ge4\), let \(Q_n=\{0,1\}^n\) have the Hamming metric, and let \(K_n=\operatorname{VR}_{\le3}(Q_n)\) denote the flag simplicial complex whose simplices have pairwise Hamming distance at most three. Let \(\tau(x)=x+v\) over \(\mathbb F_2\), where \(v\) has Hamming weight precisely three. The **geometric fixed-point space** of the induced simplicial involution satisfies

\[
|K_n|^{\langle\tau\rangle}\simeq
\bigvee^{\,d2^{d-1}}S^3\ \vee\
\bigvee^{\,d2^{d-1}-2^d+1}S^1,
\qquad d=n-3.
\]

Thus the fixed locus has reduced integral homology \(\mathbb Z^{d2^{d-1}}\) in degree three and \(\mathbb Z^{d2^{d-1}-2^d+1}\) in degree one, and no other reduced homology. Its fundamental group is free of rank \(d2^{d-1}-2^d+1\). The exponent of \(S^1\) is zero when \(n=4\), and is positive for all \(n\ge5\).

## Assumptions and scope

All distances are integer Hamming distances, with the **inclusive** scale bound three. A fixed point means a point in the geometric realization, not necessarily a fixed original vertex (there are no fixed original vertices). Each translated pair \(\{x,\tau x\}\) has distance three and is an edge. Coordinate permutations conjugate all weight-three translations, so one may suppose that \(v\) flips coordinates one, two, three. The dimension \(n\) is any integer at least four; no finite-dimensional truncation is assumed.

## Proof

**Orbit model.** Since \(\tau\) has no fixed original vertex and permutes the vertices simplicially, a barycentric point of \(|K_n|\) is fixed exactly when its coefficients are equal on every \(\tau\)-orbit. Accordingly the fixed locus is homeomorphic to the realization of a simplicial complex \(L_n\) whose vertices are the two-element orbits, and a set of orbits is a simplex if their union is a simplex of \(K_n\). The linear homeomorphism sends each orbit vertex to the midpoint of its original edge.

**The orbit adjacency condition.** Represent an orbit by the vector with third coordinate zero. Write its label \((s,c)\), where \(s\in\mathbb F_2^d\) comprises the other \(d=n-3\) coordinates and \(c\in\mathbb F_2^2\) comprises the first two. For two different labels, write \(k\) for the Hamming distance between their \(s\)-values and \(a\in\{0,1,2\}\) for the distance between their \(c\)-values. All cross-distances between the two original orbits are at most three precisely when

\[
\max(a+k,3-a+k)\le3.
\]

For distinct orbits this is equivalent to \(a\in\{1,2\}\) and \(k\le1\), or simply

\[
(s,c)\sim(t,e)\quad\Longleftrightarrow\quad
c\ne e\ \text{and}\ d_H(s,t)\le1.
\]

The complex \(L_n\) is the flag complex of this graph. Since the lower-dimensional cube graph \(Q_d\) has no triangles, every clique of \(L_n\) projects either to one vertex \(s\) or to the two endpoints of a single cube edge.

**Sphere blocks.** For every \(s\in Q_d\), let \(A_s\) be the simplex on its four differently colored vertices. Hence \(A_s\cong\Delta^3\). For each edge \(e=st\) of \(Q_d\), let \(B_e\) be the full subcomplex of \(L_n\) on the eight vertices over its endpoints. Its only four missing edges join identically colored vertices over opposite endpoints. Consequently

\[
B_e\cong(S^0)^{*4}\cong S^3,
\]

the boundary of the four-dimensional cross-polytope. The two disjoint tetrahedral facets \(A_s,A_t\subset B_e\) are contractible. Every simplex of \(L_n\) lies in some \(B_e\), because \(d\ge1\) and the lower cube has no isolated vertices. Different blocks intersect exactly in the fiber tetrahedra corresponding to their common endpoints; otherwise they are disjoint.

**Gluing.** Let \(T\) be a spanning tree of \(Q_d\), which has \(V=2^d\) vertices and \(E=d2^{d-1}\) edges. Attach the blocks along the edges of \(T\) successively. Each new sphere \(B_e\simeq S^3\) meets the previous connected union in exactly one contractible tetrahedral facet. The homotopy pushout therefore wedges on one three-sphere for every tree edge. For every remaining edge \(e=st\), both endpoint fibers have already been included, and \(B_e\) meets the connected previous union in two **disjoint** contractible tetrahedra \(A_s\sqcup A_t\). The homotopy pushout along this two-component intersection adds one three-sphere and one one-sphere. This is seen by replacing the two cofibration inclusions of contractible components with their homotopy-equivalent two-point inclusions: joining two previously connected points through the new connected sphere creates exactly one independent loop, while retaining the sphere. Induction yields \(E\) three-sphere summands and \(E-(V-1)\) one-sphere summands, as stated. All the gluing steps are genuine homotopy equivalences of CW complexes, so the integral and fundamental-group conclusions follow.

## Verification

The companion standalone `check_fixed.py` constructs every two-point orbit and its adjacency directly from the original Hamming metric, independently of the sphere-block proof. It exhaustively enumerates all simplices and computes mod-two boundary ranks for dimensions \(n=4,5,6,7\). The respective nonzero reduced Betti pairs \((\widetilde\beta_1,\widetilde\beta_3)\) are \((0,1),(1,4),(5,12),(17,32)\), as predicted. It also checks the quotient adjacency formula for every orbit pair in those dimensions. Finite checks are supporting tests; the arbitrary-dimensional theorem is proved by the combinatorial decomposition and homotopy pushouts above.

Run with Python 3: `python check_fixed.py`. There are no external dependencies or data files.

## Relationship to prior work

Adamaszek–Adams and Shukla analyzed homotopy/homology of ambient hypercube Vietoris–Rips complexes. Feng established the scale-three ambient wedge decomposition; Adams–Virk established homology propagation bounds. Galetto–Montaño–Wellner determined characteristic-zero representations of the automorphism group on ambient homology, including scale three. The present result instead determines the **integral homotopy type of the geometric fixed-point locus** for a weight-three translation. The ambient representation determines a Lefschetz number, but does not determine the locus's fundamental group or its individual Betti numbers. No part of those prior ambient theorems is presented here as new.

## Limitations

The statement concerns only translations flipping exactly three coordinates and the inclusive scale-three complex, not an arbitrary involution or arbitrary scale. It computes fixed-point homotopy, not equivariant homotopy of the complete ambient complex. It does not claim a classification of all possible fixed subspaces. The literature comparison does not rule out an unindexed equivalent description.

## References

- S. Shukla, *On Vietoris–Rips complexes (with scale 3) of hypercube graphs* (first submitted February 6, 2022), arXiv:2202.02756.
- Z. Feng, *Homotopy types of Vietoris–Rips complexes of Hypercube Graphs* (first submitted May 11, 2023), arXiv:2305.07084.
- H. Adams and Ž. Virk, *Lower Bounds on the Homology of Vietoris–Rips Complexes of Hypercube Graphs*, Bulletin of the Malaysian Mathematical Sciences Society (2024), DOI:10.1007/s40840-024-01663-x.
- F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions* (first submitted June 18, 2026), arXiv:2606.20784.
