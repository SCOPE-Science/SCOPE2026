# Root-deletion equivalence and integral symmetry of two-independence complexes of height-two trees

## Finding
For every integer \(m\geq2\) and positive integers \(q_1,\ldots,q_m\), let \(T=T(q_1,\ldots,q_m)\) be the rooted tree with root \(x\), children \(y_1,\ldots,y_m\), and exactly \(q_i\) pendant leaves adjacent to \(y_i\). There are no other vertices or edges. The two-independence complex \(X=\operatorname{Ind}_2(T)\) consists of subsets whose induced connected components all have at most two vertices.

Deletion of the root induces a homotopy equivalence equivariant under the root-preserving automorphism group \(G=\operatorname{Aut}(T,x)\):
\[
|\operatorname{Ind}_2(T-x)|\longrightarrow |\operatorname{Ind}_2(T)|.
\]
In particular,
\[
|X|\simeq\bigvee^{\prod_{i=1}^m(q_i-1)}S^{2m-1},
\]
where a wedge of zero spheres means a contractible space. All reduced integral homology except possibly degree \(2m-1\) vanishes, and the top integral \(G\)-module is
\[
\widetilde H_{2m-1}(X;\mathbb Z)\cong\bigotimes_{i=1}^{m}A_i,
\qquad A_i=\ker\bigl(\mathbb Z^{L_i}\xrightarrow{\mathrm{sum}}\mathbb Z\bigr).
\]
Here \(L_i\) is the set of \(q_i\) leaves below \(y_i\). Within each leaf set, permutations act naturally on \(A_i\); permutations of equally sized branches permute tensor factors *without a sign*.

For any \(g\in G\), let \(\sigma_g\) denote its permutation of the branches. For each cycle \(C\) of \(\sigma_g\), let \(\rho_C\) be the monodromy permutation of a chosen branch's leaves induced by composing the leaf bijections along \(C\). Then
\[
\operatorname{tr}\bigl(g\mid\widetilde H_{2m-1}(X;\mathbb Z)\bigr)
=\prod_{C\in\operatorname{Cyc}(\sigma_g)}\bigl(|\operatorname{Fix}(\rho_C)|-1\bigr).
\]
This remains valid when a branch has a single leaf, in which case the entire top module is zero.

## Assumptions and scope
All graphs are finite and simple. The root \(x\) is specified, not inferred canonically; the symmetry group fixes it. The integers satisfy \(m\ge2\) and \(q_i\ge1\). A \(G\)-homotopy equivalence means a \(G\)-equivariant homotopy inverse with equivariant homotopies. The claim concerns ordinary geometric realization and integral simplicial homology, not an equivalence of simplicial complexes. The character formula gives the integral homology action; it is not a claim about full equivariant homeomorphism type.

## Proof
**1. Root deletion and star factors.** Write \(K_q=\operatorname{Ind}_2(K_{1,q})\). Removing \(x\) leaves \(m\) disjoint stars. Since two-independence complexes send disjoint unions of graphs to simplicial joins,
\[
A:=\operatorname{Ind}_2(T-x)=K_{q_1}*\cdots*K_{q_m}.
\]

**2. Homology of a star.** Let \(D_q\) be the discrete complex on its \(q\) leaves. A face of \(K_q\) either omits the center, in which case any leaf subset is allowed, or contains the center, in which case at most one leaf is allowed. Thus \(K_q=\Delta(L)\cup(y*D_q)\), whose intersection is \(D_q\). Both displayed subcomplexes are contractible. Mayer–Vietoris and its naturality identify
\[
\widetilde H_1(K_q;\mathbb Z)\cong\widetilde H_0(D_q;\mathbb Z)
=\ker(\mathbb Z^{L}\xrightarrow{\mathrm{sum}}\mathbb Z).
\]
Other reduced homology vanishes. More precisely, by the homotopy-pushout description, \(K_q\simeq\bigvee^{q-1}S^1\) for \(q\ge2\), and \(K_1\) is a filled edge and hence contractible. This gives a natural leaf-permutation action on the integral group.

**3. The root link.** Put \(B=\Delta(\bigsqcup_iL_i)\) and \(B_{-i}=\Delta(\bigsqcup_{j\ne i}L_j)\). Any face containing the root may contain at most one \(y_i\). If it contains \(y_i\), it may contain no leaf of \(L_i\), but all leaves of other branches remain permissible. Consequently, the root link is exactly
\[
L:=\operatorname{lk}_X(x)=B\cup\bigcup_{i=1}^m(y_i*B_{-i}).
\]
Because \(m\ge2\) and every \(q_j\ge1\), each \(B_{-i}\) is nonempty. Fixing every point of \(B\) and sliding each \(y_i\) linearly to the barycenter of \(B_{-i}\) defines a well-defined piecewise-linear strong deformation retraction \(|L|\to|B|\). The homotopies on different cones agree on their intersections inside \(B\). This retraction commutes with all root-preserving automorphisms: a branch automorphism sends the barycenter of \(B_{-i}\) to that of \(B_{-\sigma_g(i)}\). The simplex \(B\) contracts equivariantly to its invariant barycenter; hence \(L\) is \(G\)-contractible.

**4. Equivariant deletion equivalence.** The original complex is the equivariant simplicial pushout \(X=A\cup(x*L)\), with intersection \(L\). The inclusion \(L\to x*L\) is a \(G\)-homotopy equivalence since \(L\) is \(G\)-contractible and \(x\) is \(G\)-fixed. The gluing theorem for \(G\)-CW cofibrations (or equivalently its fixed-subgroup versions and equivariant Whitehead) therefore makes \(A\to X\) a \(G\)-homotopy equivalence.

**5. Join and integral representation.** Taking joins of the star factors yields, if all \(q_i\ge2\), a wedge of \(\prod_i(q_i-1)\) spheres in degree \(2m-1\), since every join of \(m\) circles has degree \(2m-1\). If a factor \(K_1\) is contractible, their join is contractible. Naturality of the integral join Künneth isomorphism identifies the top homology with the tensor product of the augmentation lattices \(A_i\), with no torsion. Transposing two degree-one homology factors in the join contributes the Koszul sign \((-1)^{(1+1)(1+1)}=+1\). Therefore branch permutations shuffle tensor factors without signs.

**6. Character formula.** For each branch-permutation cycle, the trace of the corresponding cyclic tensor-factor operator equals the trace of the induced monodromy on one augmentation lattice. Since the permutation module \(\mathbb Z^{L_i}\) has trace equal to the number of fixed leaves and its trivial summand has trace one, the augmentation trace is \(|\operatorname{Fix}(\rho_C)|-1\). Multiplication over independent cycles proves the displayed character formula. All statements follow.

## Verification
The self-contained scripts `CHECK_HOMOLOGY.py` and `CHECK_CHARACTERS.py` may be run with Python 3 and require no external libraries. The first enumerates all faces and reduces mod-two boundary matrices for the seven parameter vectors \((2,2)\), \((2,3)\), \((3,3)\), \((2,2,2)\), \((1,3,2)\), \((1,1)\), and \((3,3,2)\), comparing the resulting reduced Betti ranks to the proposed dimensions and multiplicities. All seven assertions pass. The second enumerates all root-preserving graph automorphisms in four cases and verifies their **signed** reduced simplicial Lefschetz numbers against minus the proposed top-homology trace. All 140 group-element comparisons pass (8, 12, 48, and 72, respectively). Since the only possible nonzero reduced homology is in odd degree \(2m-1\), the comparison sign is negative. The unbounded and integral assertions are proved above, not inferred from finite checks.

## Relationship to prior work
Rutuja Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees* (arXiv:2605.25150v1, first public 24 May 2026), proves vertex decomposability for every tree and \(r\ge1\), hence a general wedge-of-spheres property, but does not provide the present uniform-in-parameters root-deletion equivalence, exact sphere count, or integral automorphism module. Deshpande and Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types* (arXiv:2001.05448), calculate fully whiskered graphs under a hypothesis requiring an attached leaf at **every** nonleaf vertex (their Theorem 3.10); the root of our trees has no attached leaf, so that theorem does not apply. Their Theorem 5.6 determines ordinary homotopy for perfect regular branching trees and **does cover** a balanced subfamily of our formula; the present arbitrary nonuniform branching and complete integral symmetry action are not conclusions of that theorem. The general tree vertex-decomposability result and these previously solved subfamilies are not claimed as new.

## Limitations
The statement is restricted to two-independence complexes of rooted height-two trees with at least two nonempty branches and to automorphisms preserving the specified root. It does not classify higher parameters \(r\), all rooted trees, or graph automorphisms that move the root. The reduced integral top-homology representation is established, but no equivariant PL homeomorphism type is asserted. Complete exclusion of implicit or unindexed equivalent prior work is not possible from the inspected literature. Independent validation has not been performed.

## References
1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1 (2026), https://arxiv.org/html/2605.25150v1.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (2020), https://arxiv.org/abs/2001.05448; especially Theorems 3.10 and 5.6.
3. M. Abdelmalek et al., *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863 (2021), https://arxiv.org/abs/2106.10863.
