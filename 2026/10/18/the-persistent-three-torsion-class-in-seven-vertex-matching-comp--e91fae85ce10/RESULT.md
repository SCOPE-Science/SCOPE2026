# The persistent three-torsion class in seven-vertex matching complexes

## Finding

Let \(F\) be the simple graph on \(\{0,1,2,3,4,5,6\}\) with exactly the thirteen edges
\[
\{01,05,06,13,14,23,24,25,26,35,36,45,46\}.
\]
For every simple graph \(G\) with at most seven vertices, the following equivalence holds:
\[
\operatorname{Tor}\widetilde H_1(\mathcal M(G);\mathbb Z)\ne0
\quad\Longleftrightarrow\quad
F\text{ is isomorphic to a spanning subgraph of }G.
\]
In the nonzero case the torsion is \(\mathbb Z/3\). More precisely, the inclusion into the complete seven-vertex graph induces an **isomorphism on the three-torsion subgroups**:
\[
\operatorname{Tor}\widetilde H_1(\mathcal M(G);\mathbb Z)
\overset{\cong}{\longrightarrow}
\widetilde H_1(\mathcal M(K_7);\mathbb Z)\cong\mathbb Z/3.
\]
Under this canonical identification, an automorphism \(g\) of \(G\) acts by multiplication by \(\operatorname{sgn}(g)\in\{\pm1\}\) on three-torsion, where the sign is taken on the original seven graph vertices. Thus the class persists through all edge additions within seven vertices, and every odd graph automorphism negates it.

## Assumptions and scope

All graphs are finite, loopless, undirected and simple, and may have isolated vertices. To interpret a graph with fewer than seven vertices, add isolated vertices; this does not change its matching complex. The matching complex \(\mathcal M(G)\) has one vertex for each edge of \(G\) and one simplex for each set of pairwise disjoint edges. All homology is reduced integral simplicial homology. Automorphisms act on oriented simplices by their induced signed permutations. The preceding theorem is limited to the stated finite order bound, not all graphs.

## Proof

**1. Complete-graph three-torsion and its sign action.** Enumerate the vertices, edges and triangles of \(\mathcal M(K_7)\), obtaining respective counts \(21,105,105\). Its connected one-skeleton has a spanning tree with twenty edges, so its first-cycle lattice has rank eighty-five. In its fundamental-cycle basis, the integral second-boundary matrix is \(85\times105\). Exact elimination gives rank eighty-four modulo three, while a deterministically selected \(85\times85\) minor has determinant \(-3\). Therefore the full integral cokernel has order three, so
\[
\widetilde H_1(\mathcal M(K_7);\mathbb Z)\cong\mathbb Z/3.
\]
The same calculation gives \(\widetilde H_2\cong\mathbb Z^{20}\). An explicit mod-three cocycle \(\varphi\), obtained by reducing the eighty-five fundamental cycles modulo triangle boundaries, detects a nonzero first-homology generator. Its values on all \(5040\) vertex-permuted images of that generator equal the original value multiplied by the permutation sign. Hence the complete action on integral first homology is the one-dimensional sign representation over \(\mathbb F_3\).

**2. A nonzero torsion-class inclusion from the minimal graph.** The matching complex of \(F\) has \(13\) vertices, \(42\) edges and \(30\) triangles. Its second-boundary matrix has rank twenty-nine modulo three. The exact checker constructs a nonzero vector \(c\) in its mod-three kernel, lifts each coefficient to \(\{0,1,2\}\subset\mathbb Z\), and forms the integral one-cycle
\[
z=\partial_2 c/3.
\]
All entries of \(\partial_2 c\) are divisible by three and \(\partial_1z=0\). Evaluation of the **independently constructed** complete-graph cocycle on the image of \(z\) is \(2\pmod3\), not zero. Thus \([z]\) is an element of order exactly three in \(\widetilde H_1(\mathcal M(F);\mathbb Z)\) whose image in \(\widetilde H_1(\mathcal M(K_7);\mathbb Z)\) is nonzero.

**3. The finite upward-filter classification.** The complement of \(F\) inside \(K_7\) consists of eight edges. Every labelled spanning supergraph is therefore one of the \(256\) choices of those edges. Exhaustive canonicalization under all \(5040\) permutations produces exactly **forty** graph-isomorphism classes. The standalone checker compares their complete canonical bit-mask set with the forty Graph Atlas representatives in the published exhaustive torsion census; these two forty-element sets agree exactly. That earlier census establishes that these are all isomorphism classes with nonzero first-homology torsion among graphs with at most seven vertices, and that each torsion group is \(\mathbb Z/3\). The computation here adds a canonical single-pattern and functoriality explanation, not another unqualified claim to have discovered the census.

**4. Persistence and natural symmetry.** If \(F\subseteq G\subseteq K_7\), the homology map from \(F\) to \(K_7\) factors through \(G\). Since the image of \([z]\) in \(K_7\) is nonzero, its image in \(G\) is nonzero, and the inclusion from \(G\) to \(K_7\) maps the unique order-three torsion subgroup isomorphically. Any relabelling of \(F\) gives the same conclusion. Naturality under the inclusion \(G\subseteq K_7\) transfers the complete-graph sign action to every automorphism of \(G\). This proves the theorem.

## Verification

The two accompanying pure-Python checkers and the frozen forty-entry graph-mask data form a self-contained computational certificate. Run `python verify_torsion_inclusions.py` from their directory. This executes `verify_m7_sign.py` and then checks all \(5040\) automorphisms of the complete graph, the integer determinant \(-3\), the mod-three kernel and its integral Bockstein lift, the nonzero inclusion cocycle pairing, and the equality of the two sets of forty graph classes. All checks completed successfully in the supplied package. The numeric counts are exact, not randomized tests.

## Relationship to prior work

Bouc's established theorem (as recorded in Shareshian–Wachs) gives the cyclic order-three first homology of the seven-vertex complete-graph matching complex. Shareshian–Wachs also give a concrete cycle and general generating formulas, from which the complete-graph sign character may be deduced. **That character alone is not the new assertion.** The new assertion is that the unique torsion classes of **every** one of the forty torsion-bearing seven-vertex graph complexes survive their natural maps into the complete-graph complex. The closest published finite graph census lists precisely forty torsion classes and a unique thirteen-edge threshold graph, but does not identify these inclusion homomorphisms or an all-class persistent torsion generator. Its published exact class list is a premise for the equivalence, not itself a new discovery. Jonsson's complete-graph exact sequences and Bate–Everitt–Ford–Ramos's rational representations do not calculate these subgraph inclusion homomorphisms.

## Limitations

This is a theorem at graph order at most seven, not a monotonicity theorem for unrestricted graph orders. The forty-class exhaustiveness assertion uses the cited finite census as established input; the checker independently verifies its complete graph-isomorphism relationship to the stated supergraph family but does not rerun that census's entire Smith-form calculation. The finite Bockstein and the complete-graph integral torsion and symmetry calculations are verified from definitions. The original full text of Bouc's 1992 article was not materially inspected; an equivalent treatment of these inclusion maps there or in unindexed literature remains a bibliographic risk. No independent external audit has been performed.

## References

1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, originally publicly posted 2004-09-03; §1, especially Theorem 1.3 and Remark 1.4; https://arxiv.org/abs/math/0409054.
2. J. Jonsson, *Exact Sequences for the Homology of the Matching Complex*, arXiv:1203.5641 (public preprint 2012-03-26); https://arxiv.org/abs/1203.5641.
3. *Sharp edge threshold for torsion in matching complexes of seven-vertex graphs*, complete forty-class finite census and frozen Graph Atlas records, published-finding corpus published record 2026-10-11; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-edge-threshold-for-torsion-in-matching-complexes-of-seven--f0ba41f16bfb.
4. M. Bate, B. Everitt, S. Ford and E. Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750; https://arxiv.org/abs/2312.13750.
5. S. Bouc, *Homologie de certains ensembles de 2-sous-groupes des groupes symétriques*, J. Algebra (1992); https://doi.org/10.1016/S0021-8693(05)80054-7.
