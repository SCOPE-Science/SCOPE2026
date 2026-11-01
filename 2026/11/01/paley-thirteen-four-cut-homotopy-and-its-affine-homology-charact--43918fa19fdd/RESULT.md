# Paley-thirteen four-cut homotopy and its affine homology character

## Finding

For the quadratic-residue Paley graph on thirteen vertices, the ordinary four-cut simplicial complex \(X=\Delta_4(P_{13})\) has the **integral homotopy equivalence**
\[
X\simeq\bigvee^{25}S^6.
\]
Its facets have nine vertices, so the complex is pure of dimension eight, but it is not shellable. The natural affine subgroup \(A=\mathbb F_{13}\rtimes(\mathbb F_{13}^{\times})^2\), of order 78, acts on its sixth reduced rational homology as
\[
\widetilde H_6(X;\mathbb Q)\cong\mathbb Q\oplus2\,\mathrm{Aug}(\mathbb Q[\mathbb F_{13}]),
\]
where the augmentation module has dimension twelve. Equivalently, the character is \(25\) at the identity, \(-1\) on the twelve nonidentity translations, and \(1\) on the other 65 affine transformations. Hence the quotient has
\[
\widetilde H_i(X/A;\mathbb Q)\cong
\begin{cases}\mathbb Q,&i=6,\\0,&i\ne6.\end{cases}
\]
This is a statement about the underlying integral homotopy type and a rational homology representation; an equivariant homotopy wedge is not claimed.

## Assumptions and scope

Use the vertex set \(V=\{0,1,\ldots,12\}\) with arithmetic in \(\mathbb F_{13}\). Set the nonzero-square set to \(R=\{1,3,4,9,10,12\}\). Two distinct vertices \(u,v\) are adjacent exactly when \(v-u\in R\). This gives a simple 6-regular, 39-edge graph with strongly regular parameters \((13,6,2,3)\).

For \(D\subseteq V\) with \(|D|=4\), call \(D\) *disconnected* if the induced undirected graph \(P_{13}[D]\) is disconnected. The ordinary four-cut complex \(X\) has facets \(V\setminus D\) for every such \(D\), together with all their subsets. The empty face is included in the mathematical complex, but omitted from the nonempty-face counts and ordinary face-poset matching.

There are \(260\) disconnected four-sets and \(455\) connected four-sets. There are no independent four-sets, so the **total** four-cut complex is void: it is a different construction and is not used in the theorem.

The affine group consists exactly of maps \(g_{a,b}:v\mapsto av+b\) with \(a\in R\), \(b\in\mathbb F_{13}\). Multipliers in \(R\) preserve quadratic-residue adjacency. The rational augmentation module is the codimension-one invariant subspace of \(\mathbb Q^{13}\) consisting of vectors with coordinate sum zero, with the permutation action of \(A\) on the thirteen graph vertices.

## Proof

**(1) Explicit face enumeration.** Enumerating each of the \(\binom{13}{4}=715\) four-subsets by a connected-component traversal gives exactly 260 disconnected subsets. Closing their nine-element complements under taking subsets gives 6,994 nonempty faces. The number of \(i\)-faces for \(0\le i\le8\) is
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8)
=(13,78,286,715,1287,1716,1664,975,260).
\]
A second algorithm inspects every one of the \(2^{13}-1=8191\) nonempty subsets directly and accepts a set precisely when its complement contains a disconnected four-subset; it produces the identical face set. In particular every face of size at most six is present, but exactly \(\binom{13}{7}-1664=52\) seven-subsets are missing.

**(2) Complete acyclic discrete-Morse matching.** On the set of all nonempty faces, process the vertex pivots in the deterministic order
\[
(2,9,7,5,3,12,6,8,0,11,4,1,10).
\]
At a pivot \(j\), pair each currently unmatched face \(F\) omitting \(j\) with \(F\cup\{j\}\) if both faces remain unmatched; remove both from later stages. This constructs 3,484 disjoint elementary Hasse-edge pairs. To certify *global* acyclicity, orient each codimension-one Hasse edge downward except for the selected matching edges, which are oriented upward. A full topological-sort check of all 42,393 nonempty-face Hasse incidences visits all 6,994 faces; hence the directed graph is acyclic. Only one critical zero-cell and 25 critical six-cells remain, with no critical cells in any other dimension.

By discrete Morse theory the complex has the homotopy type of a CW complex with one zero-cell and 25 six-cells, and no cells in dimensions one through five. Every six-cell attaches to a point; therefore the integral homotopy type is exactly \(\bigvee^{25}S^6\). This is stronger than any finite-field Betti calculation. Independently, bit-packed mod-two reductions of the original simplicial boundaries in dimensions one through eight have ranks
\[
(12,66,220,495,792,924,715,260),
\]
which give ordinary mod-two Betti vector \((1,0,0,0,0,0,25,0,0)\), consistent with the homotopy proof.

**(3) Nonshellability.** The facets have nine vertices, so \(X\) is pure eight-dimensional. Since \(\widetilde H_6(X;\mathbb Z)\cong\mathbb Z^{25}\ne0\), it cannot be a pure shellable complex: pure shellable complexes have reduced homology only in their top dimension.

**(4) Affine homology character.** For every one of the 78 affine permutations \(g\), the program checks graph-automorphism status and computes the reduced simplicial Lefschetz number using all setwise fixed nonempty faces, with the orientation sign induced by \(g\) on each ordered face. It verifies
\[
\widetilde L(g)=2\#\{v\in\mathbb F_{13}:g(v)=v\}-1.
\]
The homology from (2) is concentrated in even degree six, so the reduced Hopf trace formula identifies this reduced Lefschetz number with the character of \(\widetilde H_6(X;\mathbb Q)\). An identity has thirteen fixed graph vertices; a nonidentity translation has none; and an affine transformation with nonidentity multiplier has exactly one. Thus the traces are \((25,-1,1)\) on those three classes of elements.

The natural 13-point permutation representation has character equal to the number of fixed vertices. Since its decomposition over \(\mathbb Q\) is \(\mathbb Q\oplus\mathrm{Aug}(\mathbb Q^{13})\), the computed character equals that of \(\mathbb Q\oplus2\,\mathrm{Aug}(\mathbb Q^{13})\). Equality of characters of rational representations of a finite group in characteristic zero yields the asserted isomorphism. Averaging over all 78 elements gives invariant dimension \((25+12(-1)+65(1))/78=1\). Rational homology of the finite simplicial quotient is the invariant rational homology (apply barycentric subdivision to remove inversions and average over the finite group), proving the quotient assertion.

## Verification

The package includes two Python 3 standard-library scripts. Running `python3 verify_paley13_four_cut.py` from the extracted package reconstructs all disconnected sets and faces, checks each matching pair, performs a complete Hasse-acyclicity topological sort, checks all 78 graph automorphisms and their reduced Lefschetz traces, and returns the marker `PALEY13_FOUR_CUT_MORSE_AFFINE_VERIFIED`. Running `python3 crosscheck_paley13_mod2.py` independently enumerates faces by complement tests, forms simplicial boundary matrices over \(\mathbb F_2\), reduces all eight nontrivial boundaries and returns `PALEY13_FOUR_CUT_MOD2_CROSSCHECK_OK`. The package also includes the exact recorded outputs of both executions.

The matching certificate is constructive (the explicitly stated pivot order and face predicates), finite (6,994 faces and 42,393 Hasse incidences), and independently reproducible without any external data or numerical approximations. The mod-two check alone does not prove the integral homotopy equivalence; that follows from the acyclic matching and critical cell dimensions.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduce and develop ordinary cut complexes and establish results for trees, cycles, complete multipartite graphs and several graph operations. Their Theorem 6.1, which constrains homology when the next-to-top skeleton is complete, does not apply here: for this eight-dimensional complex, 52 seven-vertex faces are absent, so the complete seven-skeleton hypothesis fails. Their work supplies the definition and methods, not the present exact Paley graph theorem.

The sequel by Bayer, Denker, Jelić Milutinović, Sundaram and Xue computes cases for disjoint unions, squared paths, grids, paths and cycles, including group representations. It does not include this strongly regular graph or its affine representation. Related available four-cut calculations of other named graphs do not imply the result for \(P_{13}\) because they use different graphs and lack a covering family theorem. The canonical quadratic-residue labeling here is essential to the affine character computation.

## Limitations

The classification is for this specific 13-vertex Paley graph, this particular four-cut construction, and its indicated affine subgroup. No assertion is made for other Paley graph orders, other cut parameters, the full automorphism group beyond the stated subgroup, integral decomposition of the group-module lattice, an equivariant wedge decomposition, or the homotopy type of the quotient. The quotient statement concerns *rational homology* only. Independent external validation has not been performed. A mathematically equivalent unindexed result remains a bibliographic risk.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, first public arXiv version 26 April 2023, arXiv:2304.13675; SIAM J. Discrete Math. 38 (2024), 1630–1675, doi:10.1137/23M1569034.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut Complexes II*, first public arXiv version 11 July 2024, arXiv:2407.08158; SIAM J. Discrete Math. 39 (2025), 1123–1157, doi:10.1137/24M1676077.
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145, doi:10.1006/aima.1997.1650 (standard acyclic-matching-to-CW theorem).
