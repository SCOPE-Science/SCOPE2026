# Cyclic-coordinate geometric fixed points of multinary Hamming Rips complexes

## Finding

Let \(q\geq3\) be an integer and let \(X_q=\operatorname{VR}_{\leq2}([q]^3,d_H)\) be the inclusive scale-two Vietoris–Rips complex of the three-fold \(q\)-letter Hamming space. Let \(\rho(a,b,c)=(b,c,a)\) cyclically rotate the coordinates. Then the geometric fixed-point space has the natural homotopy classification

\[
F_q=|X_q|^{\langle\rho\rangle}\simeq\bigvee^{(q-1)^2}S^1.
\]

More precisely, the fixed-point space has an equivariant finite graph model under simultaneous permutation of the alphabet. Its vertices are the \(q\) letters; it has one oriented edge from \(a\) to \(b\) for every ordered pair of distinct letters \(a\ne b\) (both opposing orientations are separate geometric edges). Hence, writing \(P_q\) for the free integral permutation module on ordered pairs of distinct letters and \(U_q=\ker(\varepsilon:\mathbb Z^{[q]}\to\mathbb Z)\), there is a natural exact sequence of integral \(S_q\)-modules

\[
0\longrightarrow H_1(F_q;\mathbb Z)\longrightarrow
P_q\overset{\partial}{\longrightarrow}U_q\longrightarrow0,
\qquad \partial[a,b]=e_b-e_a.
\]

For every permutation \(\sigma\in S_q\) fixing exactly \(f\) alphabet symbols, its character on rational first homology is

\[
\operatorname{tr}(\sigma\mid H_1(F_q;\mathbb Q))=(f-1)^2.
\]

The integral representation is identified by the explicit boundary-kernel lattice, not merely by this rational character. For example, at alphabet size three the fixed locus is a wedge of four circles and the \(S_3\)-character on first homology has traces \(4,0,1\) at identity, a transposition and a three-cycle respectively.

## Assumptions and scope

The alphabet \([q]=\{0,\ldots,q-1\}\) is a discrete set, not a field. The Hamming metric counts unequal coordinate positions. A simplex of \(X_q\) is a nonempty set of words having all pairwise distances at most two. The fixed space consists of points of the *geometric realization* invariant under coordinate rotation; it need not be the realization of the vertexwise fixed subcomplex. The action of \(S_q\) relabels all coordinates simultaneously and commutes with \(\rho\). The assertions hold for every integer \(q\ge3\); the binary endpoint is excluded from the novelty assertion.

## Proof

**Fixed-point orbit model.** For any finite simplicial complex with a finite simplicial group action, the fixed points in each invariant simplex are the convex hull of the barycenters of its vertex orbits. These convex hulls agree on invariant intersections, so the entire geometric fixed space is homeomorphic to the abstract complex whose vertices are those vertex orbits that themselves span simplices, with a set of orbit-vertices forming a simplex precisely if the union of their original vertices is a simplex. This description follows directly by equality of barycentric coefficients along every orbit, with no assumption that the group fixes original vertices.

**Admissible orbits.** A word with three identical letters \((a,a,a)\) is a one-point orbit denoted \(C_a\). A word with exactly two copies of \(a\) and one copy of a different letter \(b\) yields a three-element orbit \(D_{ab}\). Any two of its words differ in two positions, so it is admissible. A word with three distinct letters gives an orbit whose successive words disagree in all three positions, so its orbit cannot belong to any simplex of \(X_q\). These \(q+q(q-1)=q^2\) orbits are exactly the vertices in the fixed-space orbit model.

**Orbit compatibility.** Two distinct constant orbits \(C_a,C_b\) are incompatible, as their words have distance three. The pair \(C_c,D_{ab}\) is compatible exactly when \(c=a\) or \(c=b\): otherwise the constant word disagrees with all three positions of every orbit word. Finally \(D_{ab},D_{cd}\), when distinct, are compatible exactly when \(a=c\). If their repeated letters agree, any two words share that letter in at least one position, as each has it in two of the three positions. If their repeated letters differ, rotate the two orbit words so that the unique exceptional positions line up when the two exceptional letters differ, or so that the exceptional positions are different when the two exceptional letters are identical; in either case one can choose an orbit-word pair disagreeing in all positions. This exhausts both cases and proves incompatibility.

Consequently the orbit model consists of \(q\) pairwise vertex-disjoint full simplices

\[
\Delta_a=\operatorname{Simplex}\big(\{C_a\}\cup\{D_{ab}:b\ne a\}\big),\qquad a\in[q],
\]

and the \(q(q-1)\) additional cross-edges \([D_{ab},C_b]\). No cross-edge belongs to a triangle: two different repeated-letter blocks are incompatible, and there is only one constant vertex at its target. Thus this is the *complete* face classification, not merely a one-skeleton computation.

**Homotopy and integral symmetry.** Each \(\Delta_a\) is contractible and the blocks are disjoint. Collapsing these disjoint simplex subcomplexes to points is a homotopy equivalence for this CW complex (the subcomplex inclusions are cofibrations); this construction respects alphabet permutations. The quotient is the connected multigraph \(G_q\) with \(q\) vertices and one geometric edge for each ordered pair \((a,b)\) with distinct entries, joining \(a\) to \(b\). Its fundamental group is free of rank \(q(q-1)-q+1=(q-1)^2\), proving the wedge-of-circles claim.

The cellular chain complex of \(G_q\) has \(C_1=P_q\), \(C_0=\mathbb Z^{[q]}\), and boundary \(\partial[a,b]=e_b-e_a\). Connectedness makes the image precisely the integral augmentation lattice \(U_q\), with kernel \(H_1(F_q;\mathbb Z)\). Every map is \(S_q\)-equivariant; the quotient is an equivariant homotopy equivalence and hence the identification is integral and natural. For \(\sigma\) fixing \(f\) letters, exactly \(f(f-1)\) ordered distinct pairs are fixed and \(\operatorname{tr}(\sigma\mid U_q\otimes\mathbb Q)=f-1\); taking traces in the exact sequence gives \(f(f-1)-(f-1)=(f-1)^2\). All claims now follow.

## Verification

The included standalone Python 3 script `verify.py` reconstructs every cyclic orbit from literal three-letter words, tests Hamming-distance compatibility directly, compares against the orbit-block classification, enumerates all faces of the resulting finite model, and independently calculates mod-two homology for \(2\le q\le6\). The observed positive reduced Betti numbers in degree one are respectively \(1,4,9,16,25\), with all other reduced Betti numbers zero. For all \(S_q\) permutations at \(q\le5\), it separately computes the signed simplicial reduced Lefschetz number; all 152 permutation tests agree with \(-(f-1)^2\), as required for a degree-one-only complex. Run `python3 verify.py` with standard Python 3; success prints `ALL CHECKS PASSED`. The infinite-family theorem is established by the combinatorial and cellular proof, not by finite experiments.

## Relationship to prior work

Bendersky, Elia and Grbić (2026) study cohomology and connectivity of scale-dependent Rips complexes of the *binary* hypercube, not cyclic-coordinate geometric fixed points of multinary triples. Galetto, Montaño and Wellner (2026) study ambient binary-cube homology representations; a character on ambient homology does not determine a fixed-space homotopy type. Antolín Camarena and Carnero Bravo (2023) investigate independence complexes of three-factor categorical products, including a conjectural nonequivariant sphere count, but do not identify the geometric cyclic-coordinate fixed subcomplex of the multinary Hamming Rips construction or its integral alphabet-permutation module. Two publicly indexed exact computations of the ambient ternary three-cube Rips filtration yield 46 three-spheres at scale two; this *ambient* assertion does not imply the four fixed-space circles here. A previously recorded cyclic-coordinate fixed-point result for the binary alphabet does not cover \(q\ge3\) or this \(S_q\)-integral lattice.

## Limitations

This theorem is for exactly three coordinate positions, scale two, and cyclic coordinate rotation; it does not classify other scales, higher Cartesian powers, arbitrary isometries, or the ambient homotopy of every multinary cube. The graph quotient is a homotopy model, not a claim that the original fixed-point complex is graph-dimensional. The integral representation is a kernel lattice, not a claimed decomposition into irreducible integral summands. Indexed and full-text comparisons reduce but cannot eliminate the possibility of an equivalent unindexed prior result. Independent scientific validation has not been performed.

## References

1. M. Bendersky, S. Elia, J. Grbić, “Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph,” arXiv:2605.00705 (first public 2026-05-01), https://arxiv.org/abs/2605.00705.
2. F. Galetto, J. Montaño, Z. Wellner, “Homology of Vietoris–Rips complexes of hypercube graphs via group actions,” arXiv:2606.20784 (first public 2026-06-18), https://arxiv.org/abs/2606.20784.
3. O. Antolín Camarena, A. Carnero Bravo, “Homotopy type of the independence complex of some categorical products of graphs,” arXiv:2307.12401 (2023-07-23), https://arxiv.org/abs/2307.12401.
4. S. Goyal, S. Shukla, A. Singh, “Homotopy Type of Independence Complexes of Certain Families of Graphs,” arXiv:1905.06926 (2019-05-16), https://arxiv.org/abs/1905.06926.
5. “Complete Vietoris–Rips persistence of the ternary three-cube,” published mathematical record (2026), especially its complete RESULT.md proof concerning ambient Rips homotopy.
6. “The ternary Hamming Rips filtration and the \(K_3\times K_3\times K_3\) case,” published mathematical record (2026), especially its complete RESULT.md proof concerning ambient Rips homotopy.
