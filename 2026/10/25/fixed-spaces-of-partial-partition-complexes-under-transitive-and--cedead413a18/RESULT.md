# Fixed spaces of partial-partition complexes under transitive and Young symmetries

## Finding

Let \(\Omega\) be a finite set with \(|\Omega|=n\ge2\). Define \(D(\Omega)\) to be the simplicial complex whose vertices are nonempty subsets of \(\Omega\) and whose simplices are pairwise disjoint families of those subsets. Let \(H\le\operatorname{Sym}(\Omega)\) act transitively, choose \(x\in\Omega\), and write \(H_x\) for its stabilizer. Then the entire **geometric** fixed-point space is a finite discrete PL space with a natural bijection

\[
|D(\Omega)|^H\ \cong_{\mathrm{PL}}\ \{K:H_x\le K\le H\}_{\mathrm{disc}}.
\]

Every point is the barycenter of the simplex given by an \(H\)-invariant partition of \(\Omega\); there are no other fixed points, fixed arcs, or higher-dimensional fixed cells. In particular, if \(b(H,x)\) is the number of subgroups between \(H_x\) and \(H\),

\[
\widetilde H_i(|D(\Omega)|^H;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{\,b(H,x)-1},&i=0,\\
0,&i\ne0.
\end{cases}
\]

Thus a transitive permutation group is primitive precisely when this fixed-point space has exactly two points (the homotopy type \(S^0\)). If \(H=C_n\) acts regularly by an \(n\)-cycle, the number of fixed points is the divisor-counting function \(\tau(n)\). More generally, when any finite group \(G\) acts by left translation on its own underlying set, the fixed points correspond to **all subgroups** of \(G\). Its commuting right-translation group acts on these points by conjugation: right multiplication by \(a\) sends the point for \(K\le G\) to the point for \(a^{-1}Ka\). Hence its reduced integral zeroth-homology lattice, with this commuting action, is the augmentation lattice

\[
\ker\!\left(\mathbb Z[\operatorname{Sub}(G)]\xrightarrow{\sum}\mathbb Z\right).
\]

The same geometric fixed-point method also gives an explicit **non-discrete** classification for full Young subgroups. Partition \(\Omega=A_1\sqcup\cdots\sqcup A_t\) into \(t\ge1\) labeled macroblocks, each of cardinality at least two, and let \(Y=\prod_{i=1}^t\operatorname{Sym}(A_i)\). Let \(L_t\) have two kinds of vertices: \(u_I\) for every nonempty \(I\subseteq[t]\), supported on \(I\), and \(x_i\) for every \(i\in[t]\), supported on \(\{i\}\). Distinct vertices form a simplex exactly when their supports are pairwise disjoint (thus \(x_i\) and \(u_{\{i\}}\) cannot occur in the same simplex). Then

\[
\boxed{\ |D(\Omega)|^{Y}\cong_{\mathrm{PL}}|L_t|.\ }
\]

In particular, the fixed-space PL type depends only on the **number** \(t\) of Young factors, not their respective sizes. The complex \(L_t\) is the partial-partition complex \(D([t])\) with each singleton vertex duplicated as a nonadjacent twin. Define \(a(m,j)\) to count set partitions of an \(m\)-element set into \(j\) nonempty blocks, each of size at least two; put \(a(0,0)=1\) and all other inadmissible values equal to zero. Its complete reduced integral homology is torsion-free, with

\[
\boxed{\ \operatorname{rank}\widetilde H_q(|D(\Omega)|^Y;\mathbb Z)
=\sum_{s=0}^t\binom ts\,a(t-s,q-s+1),\qquad q\ge0.\ }
\]

All reduced groups in other degrees vanish. For \(t=2\) the fixed space is exactly a circle disjoint from one point, independently of both block sizes. For \(t=3\), its reduced Betti numbers in degrees zero, one, and two are respectively \(1,3,1\). These positive-dimensional fixed spaces distinguish intransitive Young actions from the discrete fixed spaces of transitive groups, even on the same ambient partial-partition complex.

## Assumptions and scope

The group \(H\) is finite because it acts on the finite set \(\Omega\), and its action on \(\Omega\) must be transitive. The fixed-point notation always refers to the **geometric realization**, not the simplicial subcomplex consisting of individually fixed vertices; invariant simplices can have fixed barycenters even when none of their vertices is fixed. The transitive result is simultaneous for every \(n\ge2\) and every transitive subgroup \(H\le\operatorname{Sym}(\Omega)\). In the regular-action statement, \(G\) may be abelian or nonabelian. In the Young result all macroblocks have cardinality at least two; singleton factors are excluded from its orbit classification.

## Proof

1. Every point \(y\in|D(\Omega)|\) has a unique minimal supporting simplex \(F=\{B_1,\ldots,B_r\}\), where the \(B_i\) are pairwise disjoint nonempty subsets and all supporting barycentric coordinates are strictly positive. If \(y\) is fixed by \(H\), uniqueness implies \(hF=F\) for every \(h\in H\). Thus \(U=\bigcup_{B\in F}B\) is nonempty and \(H\)-invariant. Transitivity gives \(U=\Omega\), so \(F\) is a full partition.

2. For any block \(B\in F\), the union of the orbit \(H\cdot B\) is a nonempty \(H\)-invariant subset of \(\Omega\), hence all of \(\Omega\). If \(F\) had two different block-orbits, each would cover \(\Omega\), contradicting disjointness of the blocks. Consequently \(H\) acts transitively on the set \(F\) of blocks. Invariance of the barycentric coordinates now forces all coordinates to equal \(1/r\). Therefore \(y\) is the barycenter of the full invariant partition \(F\). Conversely, such a barycenter is fixed. No invariant full partition can be strictly enlarged by another disjoint nonempty vertex, and the resulting finitely many barycenters form a discrete set in the realization.

3. Identify \(\Omega\) with \(H/H_x\) by \(hH_x\mapsto hx\). For an invariant partition \(F\), its unique block \(B\) containing \(x\) has setwise stabilizer \(K=\{h\in H:hB=B\}\) with \(H_x\le K\le H\). Moreover \(B=Kx\): if \(b=hx\in B\), then \(hB\) contains \(b\) and intersects \(B\), so \(hB=B\) and \(h\in K\). The converse inclusion is immediate. Conversely every \(K\) between \(H_x\) and \(H\) gives the invariant partition by the translates of \(Kx\). These constructions are inverse, proving the displayed PL classification and reduced homology groups.

4. The two subgroups \(H_x\) and \(H\) always occur and are distinct because \(n\ge2\). A transitive action is primitive exactly when the point stabilizer is maximal, equivalently when these are the only two intermediate subgroups; this yields the two-point criterion. In the regular cyclic case \(H_x=1\), and cyclic subgroups correspond bijectively to divisors of \(n\).

5. In the regular action of \(G\) on itself, \(H_x=1\) and the block-system for \(K\) is the collection of left cosets \(gK\). Right multiplication by \(a\) maps each \(gK\) to \((ga)(a^{-1}Ka)\), hence maps the fixed barycenter indexed by \(K\) to that indexed by \(a^{-1}Ka\). Reduced zeroth homology of a finite discrete set is the kernel of the sum map on its integral permutation lattice, proving the stated natural commuting-action representation.

6. For any simplicial action, a fixed point has an invariant minimal simplex, uniquely decomposed into vertex-orbits. Such an orbit can occur in a simplex only if its distinct constituent vertices are pairwise disjoint. The fixed region inside that invariant simplex is a simplex with one vertex at the uniform barycenter of each vertex-orbit. These regions glue to the geometric realization of the simplicial complex of compatible admissible vertex-orbits; the barycentric-coordinate rescaling by orbit cardinalities is a PL homeomorphism.

7. Consider the Young action. An orbit of a nonempty subset \(B\subseteq\Omega\) has pairwise disjoint members only in two cases: either \(B\) is the union of whole macroblocks \(A_i\), yielding a fixed vertex \(u_I\), or \(B\) is a singleton from one macroblock, yielding its full singleton orbit \(x_i\). Indeed, if a subset contains a nonempty proper part of a macroblock of cardinality at least two, the symmetric group on that macroblock produces intersecting translates unless the subset consists of just one element there and is empty on every other macroblock. Two admissible orbits are compatible if and only if their macroblock supports are disjoint. Applying step 6 gives the claimed exact PL identification with \(L_t\).

8. Start with \(D([t])\). To obtain \(L_t\), duplicate each singleton vertex \(v_i=\{i\}\) by an additional vertex with exactly the same link but no simplex containing both copies. At any intermediate stage, adding this second apex forms \(K'=K\cup_{\operatorname{link}_K(v_i)}(v_i'*\operatorname{link}_K(v_i))\). Since the inclusion of the link into \(K\) is nullhomotopic through the cone with the original apex \(v_i\), the reduced Mayer–Vietoris sequence has zero connecting inclusion maps, giving split short exact homology sequences (the relevant groups are free by induction). Iterating over duplicated singletons and using \(\operatorname{link}_{D([t])}(\{\{i\}:i\in S\})\cong D([t]\setminus S)\), we obtain as abelian groups

\[
\widetilde H_q(L_t;\mathbb Z)\cong\bigoplus_{S\subseteq[t]}
\widetilde H_{q-|S|}(D([t]\setminus S);\mathbb Z).
\]

The empty ground-set complex has one reduced augmented homology generator in degree minus one; this convention accounts for the term with \(S=[t]\). For \(t=1\) the two-vertex fixed complex verifies the same formula directly. Gottstein's integral homology theorem for the ordinary partial-partition complex gives \(\operatorname{rank}\widetilde H_{j-1}(D([m]);\mathbb Z)=a(m,j)\), with no torsion. Summing over the \(\binom ts\) subsets of size \(s\) proves the full displayed integral formula. For \(t=2\), \(L_2\) has a four-cycle on \(u_{\{1\}},x_1,u_{\{2\}},x_2\) and an isolated \(u_{\{1,2\}}\), proving the stated PL type. This also independently checks the degree-zero convention.

## Verification

The standalone program `check_fixed_points.py` exhaustively enumerates all partial partitions (including those with unused labels) for a regular \(n\)-cycle through \(n=9\), then verifies that precisely \(\tau(n)\) nonempty simplices are invariant. It also checks regular actions of the Klein four group, the symmetric group of degree three, and the dihedral group of order eight against independently enumerated subgroup lattices; their respective fixed-point counts are \(5\), \(6\), and \(10\). For each invariant face, the program separately verifies full support and transitivity on its blocks. In the three noncyclic examples it also checks the commuting right-regular action on coset systems.

The second standalone program `check_young_fixed.py` enumerates fixed simplices for Young factors of sizes \((2,2)\), \((2,3)\), \((3,3)\), \((2,2,2)\), and \((2,2,2,2)\), reconstructs the orbit-complex faces, and checks equality without using the formula. It also computes exact mod-two simplicial boundary ranks for \(L_t\), \(1\le t\le5\), and matches the displayed integral rank formula in all degrees. Reproduce with `python3 check_fixed_points.py` and `python3 check_young_fixed.py`, using standard Python 3. The completion markers are `PARTIAL_PARTITION_TRANSITIVE_FIXED_VERIFIED` and `PARTIAL_PARTITION_YOUNG_FIXED_VERIFIED`. These are finite corroborations; the eight proof steps above establish both quantified classifications for all allowed parameters.

## Relationship to prior work

Gottstein, *Homology of Partial Partitions Ordered by Inclusion* (arXiv:2311.11190, initial public version November 19, 2023; subsequently revised as *The Partial Partition Complex*), defines this same complex, computes its nonequivariant homology, constructs cross-polytope generators, and proves its full automorphism group is the symmetric group. Neither of the two fixed-point classifications nor the Young fixed-space integral Betti formula is among its stated results. The transitive argument is independent of shelling; the Young homology formula explicitly uses the established nonequivariant homology theorem as an input. The geometric fixed-space identification is an additional step.

Arone and Brantner, *The Action of Young Subgroups on the Partition Complex* (arXiv:1801.01491; published 2021), treat the different object given by the **order complex of the proper nontrivial partition poset**. Its fixed-point subgroup-poset theorem is a close thematic antecedent, but an order complex of refinement chains is not the partial-partition complex of disjoint nonempty subsets. The existing correspondence between block systems and intermediate subgroups in permutation-group theory supplies the last step of the proof, not the geometric fixed-point identification.

## Limitations

The transitive result and the indicated full Young subgroups are not a classification of **all** possible subgroups; arbitrary intransitive subgroups need not have either form. The Young rank formula is for ordinary integral homology and does not assert a canonical integral module splitting under external block-factor permutations. The statement concerns ordinary geometric fixed points, not homotopy fixed points or the full equivariant stable homotopy type. The subgroup lattice and the correspondence between intermediate subgroups and imprimitivity systems are classical; the claimed result is specifically their realization as the **entire fixed-point topology** of the stated simplicial complex and the commuting-action identification in the regular case. A previously unindexed equivalent description remains possible. No independent mathematical audit has been performed.

## References

1. M. J. Gottstein, *Homology of Partial Partitions Ordered by Inclusion* (2023), arXiv:2311.11190, initial version November 19, 2023; revised title *The Partial Partition Complex*. https://arxiv.org/abs/2311.11190
2. G. Z. Arone and D. L. B. Brantner, *The Action of Young Subgroups on the Partition Complex*, arXiv:1801.01491 (2018), Publications Mathématiques de l'IHÉS **133** (2021), 47–156. https://doi.org/10.1007/s10240-021-00123-7
3. A. Lucchini, M. Moscatiello, and P. Spiga, *A Polynomial Bound for the Number of Maximal Systems of Imprimitivity of a Finite Transitive Permutation Group* (2019), arXiv:1907.08477. https://arxiv.org/abs/1907.08477
