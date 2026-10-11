# Integral icosahedral homology lattice of the dodecahedral scale-three Rips complex

## Finding
Let \(D\) be the twenty-vertex regular dodecahedral graph with the unweighted shortest-path metric. Set \(X=\operatorname{VR}_{\le3}(D)\), where a nonempty vertex subset is a simplex precisely when all pairwise graph distances are at most three. Its full automorphism group is \(G=\operatorname{Aut}(D)\cong A_5\times C_2\). Write \(z\) for central antipodal inversion and \(\delta:G\to\{\pm1\}\) for the homomorphism trivial on \(A_5\) and satisfying \(\delta(z)=-1\). Let \(\mathcal T\) be the ten four-vertex subsets whose six pairwise graph distances are exactly three, and let \(I(\mathcal T)=\ker(\varepsilon:\mathbb Z[\mathcal T]\to\mathbb Z)\), where \(\varepsilon\) sends every tetrahedron basis element to one.

**Integral equivariant classification.** As integral \(G\)-modules,
\[
\widetilde H_3(X;\mathbb Z)\cong \mathbb Z_{\delta}\otimes_{\mathbb Z}I(\mathcal T),
\qquad \widetilde H_j(X;\mathbb Z)=0\quad(j\ne3).
\]
Here \(\mathbb Z_{\delta}\) denotes the one-dimensional sign lattice. The action on \(\mathcal T\) has two five-element \(A_5\)-orbits, interchanged by \(z\). Consequently the fixed integral homology \(\widetilde H_3(X;\mathbb Z)^G\) is infinite cyclic.

In rational terms, let \(V_4=\ker(\mathbb Q^5\xrightarrow{\sum}\mathbb Q)\), with its standard five-object \(A_5\)-action. Then
\[
\widetilde H_3(X;\mathbb Q)
\cong (\mathbf1\oplus V_4)\boxtimes\mathbf1
\ \oplus\ V_4\boxtimes\operatorname{sgn}_{C_2}.
\]
For a rotation \(h\in A_5\), write \(f(h)\) for its number of fixed tetrahedra in either five-element orbit. The complete character is
\[
\chi_3(h)=2f(h)-1,\qquad \chi_3(zh)=1.
\]
Thus the character is \(9,1,3,-1,-1\) on the rotation classes of orders \(1,2,3,5,5\), respectively, and is identically one on the entire orientation-reversing coset. The antipodal \(+1\) and \(-1\) rational eigenspaces have dimensions five and four.

## Assumptions and scope
The graph is the ordinary one-skeleton of the regular dodecahedron (twenty vertices, thirty edges), not a geometric point cloud with arbitrary Euclidean thresholds. The Rips convention is inclusive at the integer graph-metric threshold three. The automorphism action on the simplicial chain complex is induced by permutation of the twenty graph vertices, including its usual orientation signs. There is no assumption of an equivariant deformation retraction in the prior nonequivariant proof.

## Proof
Let \(Y\subset X\) be obtained by deleting the ten tetrahedra \(\mathcal T\) but retaining all their proper faces. Saleh, Titz Mite and Witzel prove that the ten tetrahedra are maximal, that \(Y\simeq\operatorname{VR}_{\le2}(D)\simeq S^2\), and that each tetrahedron's attaching boundary represents a generator of \(H_2(Y;\mathbb Z)\) (their Section 4, Propositions 4.2 and 4.4). Their principal theorem also identifies \(X\simeq\bigvee^9 S^3\). The set \(\mathcal T\) is preserved by the full graph automorphism group, so \(Y\subset X\) is a \(G\)-invariant subcomplex even though the cited deformation retraction need not be equivariant.

Because the relative simplicial chain complex \(C_*(X,Y;\mathbb Z)\) consists of one free generator per tetrahedron in degree three and vanishes in all other degrees, the integral homology exact sequence supplies
\[
0\longrightarrow H_3(X;\mathbb Z)
\longrightarrow\mathbb Z^{\mathcal T}
\xrightarrow{\partial} H_2(Y;\mathbb Z)\cong\mathbb Z
\longrightarrow0.
\]
Choose a generator \(u\) of \(H_2(Y;\mathbb Z)\). Since each \(\partial[\tau]\) equals \(\pm u\), orient each relative tetrahedron basis element \(e_\tau\) so that \(\partial e_\tau=u\). This unit-coefficient property also follows directly from the cited integral homotopy types: vanishing of \(H_2(X;\mathbb Z)\) makes the connecting map surjective, while transitivity of the full group on the ten tetrahedra makes the absolute values of all ten coefficients equal, hence equal to one. In this basis the connecting map is ordinary augmentation.

It remains to determine the \(G\)-action on \(u\). The equivariant inclusion \(\operatorname{VR}_{\le2}(D)\hookrightarrow Y\) induces an integral isomorphism in degree two. Each rotation acts on this copy of \(\mathbb Z\) by a sign, but \(A_5\) has no nontrivial homomorphism to \(\{\pm1\}\), so all rotations act as \(+1\). Inversion \(z\) pairs every vertex with its unique graph-distance-five antipode. No nonempty simplex in \(\operatorname{VR}_{\le2}(D)\) is setwise fixed by \(z\): an invariant subset containing a vertex would also contain its distance-five antipode. Its simplicial Lefschetz number is therefore zero. Since this complex is connected and has the integral homology of \(S^2\), the homological Lefschetz identity \(0=1+\operatorname{tr}(z\mid H_2)\) shows that \(z\) acts on \(u\) by \(-1\). Thus the action on \(H_2(Y;\mathbb Z)\) is precisely \(\delta\).

Now equivariance of \(\partial\) gives \(\partial(g e_\tau)=g u=\delta(g)u\). Since \(g e_\tau\) is \(\pm e_{g\tau}\), the sign must equal \(\delta(g)\). Consequently the whole relative lattice is \(\mathbb Z_\delta\otimes\mathbb Z[\mathcal T]\), its boundary is the sign-twisted augmentation, and its kernel is exactly the claimed integral \(G\)-lattice. Other reduced integral homology groups vanish by the same exact sequence and \(Y\simeq S^2\).

The ten tetrahedra form two five-element orbits under \(A_5\), and antipodal inversion exchanges those orbits; the latter assertion is also exhaustively checked in the accompanying verifier. As rational \(A_5\)-modules, each orbit's permutation space is \(\mathbf1\oplus V_4\). Taking the kernel of total augmentation and incorporating the antipodal sign yields \((\mathbf1\oplus V_4)_+\oplus(V_4)_-\). Equivalently, the twisted permutation-minus-sign character is \(\chi_3(g)=\delta(g)(|\mathcal T^g|-1)\), giving the stated class values. At the integral level, the difference of the two orbit sums lies in the augmentation kernel and is fixed by rotations and by sign-twisted inversion; it generates the rank-one fixed lattice.

## Verification
The included standalone `verify.py` specifies all thirty graph edges and three explicit permutations. Using only the Python standard library, it builds all simplices at graph-metric scale three, enumerates the two five-tetrahedron orbits, generates all sixty rotations and all one hundred twenty automorphisms, and computes exact oriented simplicial Lefschetz traces for every group element. Its output is `VERIFY_OK` after checking the full character, the group action, antipodal exchange and the formula for fixed rational homology.

Independently of the cited sphere-wedge calculation, complete bit-exact augmented boundary reduction over \(\mathbb F_2\) gives face vector \((20,150,540,1000,972,490,100)\), boundary ranks \((1,19,131,409,582,390,100,0)\), and reduced Betti vector \((0,0,0,9,0,0,0)\). The integral module statement is proved above using the cited integral homotopy and attaching-boundary propositions; mod-two ranks alone are not presented as evidence for an integral lattice isomorphism. Run `python3 verify.py` with no network or package installation.

## Relationship to prior work
Saleh, Titz Mite and Witzel, arXiv:2302.14388v1, determine the nonequivariant Rips homotopy types of Platonic solids, including the nine three-spheres at this threshold. Their Section 4 provides the ten exceptional tetrahedra, the two rotation orbits, the deformation retraction of their complement and the integral boundary-generator result. Those are explicitly used here, not claimed as new. Their published statement and Section 4 do not identify the full integral \(A_5\times C_2\)-module, its antipodal twist, its character or the integral invariant line. Those require an equivariant relative-homology argument and a determination of the antipodal action on the two-dimensional reference homology.

Related indexed computations for dodecahedral independence and matching complexes concern different simplicial complexes; results on Rips complexes of the truncated tetrahedron, truncated cube, and Euclidean cuboctahedron do not determine this module. The symmetry representation is not supplied by a nonequivariant wedge-of-spheres statement; it is extracted from the group action on the relative exact sequence and the antipodal degree on the reference sphere.

## Limitations
This is one canonical graph and one inclusive scale. No equivariant **homotopy-type** splitting, persistence-module classification over other scales, or integral direct-sum splitting into antipodal eigenlattices is asserted. The rational decomposition uses Maschke semisimplicity and should not be read as an integral direct sum. The underlying nonequivariant homotopy inputs are cited from the original proof, while the full signed trace data are reproducible from the supplied exact enumerator.

## References
1. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1 (first public 2023-02-28), https://arxiv.org/html/2302.14388v1; *Innovations in Incidence Geometry* 21 (2024), 17–34, DOI 10.2140/iig.2024.21.17.
2. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (different metric family, context only).
