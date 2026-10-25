# Integral collineation modules of affine-plane Vietoris–Rips homology

## Finding
For every finite affine plane \(\mathcal A\) of order \(q\ge3\), let \(G\) be its unweighted point–line incidence graph. Let \(K=\operatorname{VR}_{\le2}(G)\) be the inclusive scale-two Vietoris–Rips complex and let \(\Gamma\) be the full collineation group of the plane. Its **entire integral homology representation** is determined as follows. Put \(\mathcal C\) for the \(q+1\) parallel classes, \(A_C=\ker(\mathbb Z[C]\xrightarrow{\sum}\mathbb Z)\), and \(\operatorname{or}(\mathcal C)=\bigwedge^{q+1}\mathbb Z[\mathcal C]\). Then the natural \(\Gamma\)-module isomorphisms are
\[
\widetilde H_j(K;\mathbb Z)\cong
\begin{cases}
H_1(G;\mathbb Z),&j=2,\\
\operatorname{or}(\mathcal C)\otimes\displaystyle\bigotimes_{C\in\mathcal C} A_C,&j=q,\\
0,&j\notin\{2,q\}.
\end{cases}
\]
The unordered tensor product is interpreted by choosing an order on \(\mathcal C\), with the usual symmetry isomorphisms when classes are permuted; the orientation line supplies the sign of that permutation. Both displayed lattices are free abelian, of ranks \((q-1)^2(q+1)\) and \((q-1)^{q+1}\). The degree-two lattice is the integral cycle space of the original incidence graph, not merely an abstract free abelian group.

For any collineation \(g\), let \(f_{\mathrm{flag}}(g)\), \(f_{\mathrm{point}}(g)\), and \(f_{\mathrm{line}}(g)\) count fixed incident point–line flags, points, and lines. Let \(\pi_g\) be its permutation of the parallel classes; if \(O\) is a cycle of length \(\ell\), choose a class \(C_O\) in that cycle and let \(f_{C_O}(g^{\ell})\) count lines in it fixed by \(g^{\ell}\). The complete rational characters are
\[
\chi_2(g)=f_{\mathrm{flag}}(g)-f_{\mathrm{point}}(g)-f_{\mathrm{line}}(g)+1,
\qquad
\chi_q(g)=\operatorname{sgn}(\pi_g)\prod_{O}\bigl(f_{C_O}(g^{|O|})-1\bigr).
\]

A further consequence holds for the Desarguesian plane \(\operatorname{AG}(2,q)\), for any prime power \(q\ge3\). Its translation subgroup \(T\cong(\mathbb F_q)^2\) acts on \(K\), and the rational homology of its topological quotient satisfies
\[
\widetilde b_2(|K|/T;\mathbb Q)=0,
\qquad
\widetilde b_q(|K|/T;\mathbb Q)=
\frac{(q-1)^{q+1}+(q^2-1)(q-1)(-1)^q}{q^2}.
\]
The second quantity is zero for \(q=3\) but is positive for every prime-power \(q\ge4\); for example its values at orders \(4\) and \(5\) are \(18\) and \(160\). Thus the translation quotient exhibits a genuine transition in its rational top homology despite the underlying nonequivariant sphere-wedge formula.

## Assumptions and scope
A finite affine plane of order \(q\) has \(q^2\) points and \(q(q+1)\) lines. Each line has \(q\) points, each point lies on \(q+1\) lines, and each pair of distinct points lies on a unique line. Lines have \(q+1\) parallel classes, each with \(q\) disjoint lines; lines from distinct classes intersect uniquely. No assumption of field coordinates is made in the first statement; non-Desarguesian planes are included whenever they exist. The quotient formula additionally assumes the usual translation action on \(\operatorname{AG}(2,q)\) for a prime power \(q\). All homology groups are reduced unless written as \(H_1(G;\mathbb Z)\), which is the ordinary graph-cycle lattice; the complex is connected. The threshold is inclusive, and all group actions are by simplicial automorphisms.

The representation \(\operatorname{or}(\mathcal C)\) is a rank-one integral sign lattice for permutations of parallel classes; the augmentation lattice \(A_C\) consists of coefficient vectors on the \(q\) lines of \(C\) with sum zero. The isomorphisms are \(\Gamma\)-equivariant, but the underlying wedge-of-spheres equivalence need not be equivariant.

## Proof
**Natural equivariant cover.** Distances in the incidence graph are: two points have distance \(2\); intersecting lines distance \(2\); parallel distinct lines distance \(4\); and a point and line have distance \(1\) or \(3\) according to incidence. Write \(P\) and \(L\) for its vertex classes, \(P_\ell\) for the points on a line \(\ell\), and \(L_p\) for lines through \(p\). A scale-two clique with at least two points and a line must lie in \(\{\ell\}\cup P_\ell\); one with at least two lines and a point lies in \(\{p\}\cup L_p\). No clique has two points and two lines, since two points share only one line.

Set
\[
B=*_{C\in\mathcal C}D_C,\qquad
U=\Delta(P)\cup\bigcup_{\ell\in L}\Delta(\{\ell\}\cup P_\ell),\qquad
V=B\cup\bigcup_{p\in P}\Delta(\{p\}\cup L_p),
\]
where \(D_C\) is the discrete \(q\)-vertex complex on class \(C\), and \(\Delta(S)\) is the simplex on \(S\). Every line-only clique chooses at most one line from each parallel class, so these subcomplexes satisfy \(K=U\cup V\) and \(U\cap V=G\), literally the one-dimensional incidence graph. Collineations preserve all three complexes. Each line apex in \(U\) has a simplex link and can be removed, so \(U\) collapses onto \(\Delta(P)\). Each point apex in \(V\) likewise can be removed, so \(V\) collapses onto \(B\). These individual collapses need not be equivariant, but the inclusions are equivariant homotopy equivalences on the resulting homology groups.

**Integral Mayer–Vietoris.** Because \(q\ge3\), \(B\) is \((q-1)\)-connected with reduced integral homology in degree \(q\) only. In the natural integral Mayer–Vietoris sequence for \(K=U\cup V\), the graph intersection has homology only in degrees zero and one and is connected. Since \(U\) is contractible and \(V\simeq B\), the connecting homomorphism gives a \(\Gamma\)-equivariant integral isomorphism \(\widetilde H_2(K;\mathbb Z)\xrightarrow{\cong}H_1(G;\mathbb Z)\); the inclusion \(V\hookrightarrow K\) gives \(\widetilde H_q(V;\mathbb Z)\xrightarrow{\cong}\widetilde H_q(K;\mathbb Z)\). The same exact sequence proves all other reduced homology vanishes. Its rank formulas follow from the edge and vertex counts of \(G\) and from the join formula for \(B\).

**Integral orientation of the top join.** For any finite set \(C\), \(\widetilde H_0(D_C;\mathbb Z)\cong A_C\). The oriented reduced chain complex of a join is the suspension of the tensor product of augmented chain complexes. Repeated application of this chain-level isomorphism identifies \(\widetilde H_q(B;\mathbb Z)\) with \(\operatorname{or}(\mathcal C)\otimes\bigotimes_C A_C\). When two discrete factors are transposed, the join orientations of their top faces differ by \(-1\), as each reduced degree-zero factor has suspended degree one. This is exactly the sign in \(\operatorname{or}(\mathcal C)\), independent of a temporary ordering of classes. This proves the top-module formula integrally.

**Character formulas.** Orient every incidence edge from point to line. The cellular boundary gives a natural exact sequence of \(\Gamma\)-modules \(0\to H_1(G;\mathbb Q)\to\mathbb Q[\mathrm{flags}]\to\mathbb Q[P\sqcup L]\to\mathbb Q\to0\). Taking traces yields \(\chi_2(g)\). For the top tensor representation, a permutation \(\pi_g\) of the factors has tensor-trace equal to the product, over its cycles \(O\), of traces of the return maps \(g^{|O|}\) on \(A_{C_O}\). The trace on the augmentation lattice of a finite line set is the number of fixed lines minus one. Multiplying by the orientation-line character \(\operatorname{sgn}(\pi_g)\) proves \(\chi_q(g)\).

**Translation quotient.** In \(\operatorname{AG}(2,q)\), a nonzero translation fixes no point, fixes precisely the \(q\) lines parallel to its displacement, and fixes no incident flag. It fixes every parallel class setwise. Therefore its two characters are \(\chi_2(t)=1-q\) and \(\chi_q(t)=(q-1)(-1)^q\). At the identity they are the ranks \((q-1)^2(q+1)\) and \((q-1)^{q+1}\). Averaging over the \(q^2\) translations gives zero degree-two invariants and the stated degree-\(q\) formula. A finite group acting simplicially has quotient rational homology equal to invariant rational homology: barycentric subdivision removes simplex inversions, and averaging identifies rational chain coinvariants and invariants. Positivity is clear for even \(q\ge4\); for odd \(q\ge5\), \((q-1)^{q+1}>(q^2-1)(q-1)\). At \(q=3\), the numerator is \(16-16=0\). This completes the proof.

## Verification
The independent pure-Python checker `verify_affine_equivariant.py` reconstructs the order-three affine plane from field coordinates and independently constructs the complete shortest-path distance-two clique complex. It checks equality with the proof's two-cover construction, computes all mod-two homology ranks by simplicial boundary elimination, and enumerates all \(432\) affine collineations. For each it compares the signed simplicial Lefschetz number of the entire complex and of the line-only join with the two separate asserted characters. This tests both the Koszul sign for permuted parallel classes and nonidentity translations. Its output confirms \(949\) simplices, reduced homology ranks \(16\) in degrees two and three, and full character agreement for every group element. The general integral isomorphism and arbitrary-order cases are proved above and not inferred from finite computation. Run `python3 verify_affine_equivariant.py` from the package; no third-party dependencies are required.

## Relationship to prior work
The published 2026 results *Mixed-dimensional Vietoris–Rips homotopy of affine-plane incidence graphs* and *Affine-plane incidence Rips complexes have two sphere dimensions* already establish the entire ordinary homotopy type and persistence for these same affine incidence graphs; **neither their homotopy theorem nor their accompanying proof gives a collineation-module classification**. The new statement is the natural integral action in two degrees, especially the parallel-class orientation twist and the translation-quotient transition, which cannot be inferred from the ranks of a sphere wedge alone. A previous projective-plane incidence result identified a related incidence-cycle representation, but projective planes have no affine line parallel classes and do not imply the new \(q\)-dimensional tensor module or quotient formula.

Feng and Nukala analyze scale-two Rips homotopy of several symmetric-difference subset metric spaces; their collection models are not affine incidence graphs and do not determine collineation representations. Adamaszek's graph-power theorems include graph-square stability at high girth and descriptions of edge-subdivision graph powers; affine incidence graphs of order at least three have many degree-\(q\) line vertices and a nontrivial parallelism join, so those special graphs do not subsume this calculation. General bipartite-relation work concerns other comparisons between graph-square complexes; no full equivariant module statement was identified from the accessible abstract. These distinctions are comparisons of mathematical implications rather than title-based novelty claims.

## Limitations
There is no assertion that affine planes exist for every integer order or that their collineation groups are uniformly known. The prime-power translation formula is restricted to the Desarguesian plane, while the integral representation theorem applies to all existing finite affine planes of order at least three. The statement computes homology representations, not an equivariant homotopy-type decomposition, nor integer homology of the orbit space. An independently performed audit is not asserted. Unindexed equivalent equivariant statements may exist, and abstract-only access to a general bipartite-relation paper is a residual comparison risk. The order-three computation is finite corroboration, not a proof for arbitrary orders.

## References
Feng, Z.; Nukala, N. C. P., *On Vietoris-Rips complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664, first publicly submitted 2023-02-28 (primary subject areas algebraic topology and combinatorics).

Adamaszek, M., *Clique complexes and graph powers*, arXiv:1104.0433, first publicly submitted 2011-04-03.

*Mixed-dimensional Vietoris–Rips homotopy of affine-plane incidence graphs*, published result, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-vietoris-rips-homotopy-of-affine-plane-inciden--721bc8ceb957.

*Affine-plane incidence Rips complexes have two sphere dimensions*, published result, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-affine-plane-incidence-rips-complexes-have-two-sphere-dimensions--3087baeea0a4.

Kawamura, K., *A variant of the bipartite relation theorem and its application to clique graphs*, Contributions to Discrete Mathematics 6 (2011), 91–100, DOI: 10.55016/ojs/cdm.v6i2.62059.
