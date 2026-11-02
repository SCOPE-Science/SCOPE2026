# Exact toric and singularity census in \(\operatorname{Gr}(3,6)\)

## Finding

Let \(\Pi_M\subset\operatorname{Gr}_{\mathbb C}(3,6)\) denote the closed positroid variety associated with a rank-three positroid \(M\) on the cyclically labeled ground set \(\{1,\ldots,6\}\). Distinct labeled Plücker-support matroids define distinct embedded varieties; abstract isomorphism classes are not being counted. Among the \(883\) such positroid varieties (the overall total is previously known; see OEIS A046802), precisely \(703\) are toric. The complete dimension and smoothness census is:

| Complex dimension | Smooth toric | Singular toric | All toric |
| --- | ---: | ---: | ---: |
| \(0\) | 20 | 0 | 20 |
| \(1\) | 90 | 0 | 90 |
| \(2\) | 180 | 0 | 180 |
| \(3\) | 95 | 120 | 215 |
| \(4\) | 6 | 144 | 150 |
| \(5\) | 0 | 48 | 48 |
| **Total** | **391** | **312** | **703** |

In particular, every one of the \(48\) maximal-dimensional toric positroid varieties is singular, whereas there are exactly \(6\) smooth four-dimensional toric positroid varieties. The complementary \(180\) positroids are not toric with respect to any algebraic torus. The known number \(440\) of *all* smooth rank-three positroid varieties on six elements (Billey–Weaver, Figure 11) implies that precisely \(49\) are smooth but not toric; the value \(440\) is not claimed as new.

## Assumptions and scope

All varieties are over \(\mathbb C\), with the given labeled embedding in \(\operatorname{Gr}(3,6)\). The term *toric* means normal with a dense orbit of some algebraic torus, not necessarily assumed to be the standard diagonal torus. A positroid is specified by its nonvanishing \(3\times3\) Plücker coordinates, or equivalently its collection \(\mathcal B\subset\binom{[6]}3\) of matroid bases. The assertion concerns the finite set of *all* such rank-three positroids, not a sample or an estimate. Dimension is the complex dimension of \(\Pi_M\), and smooth means smooth at every geometric point.

## Proof

**1. Finite parametrization and its exact scope.** By the decorated-permutation/Grassmann-necklace bijection, rank-three positroids on \([6]\) are indexed by decorated permutations with three anti-exceedances. The program `compute.py` enumerates all \(6!\) permutations and both decorations at every fixed point, retaining only those for which the initial anti-exceedance set has size three. For a decorated permutation \(\pi\), its Grassmann necklace \((I_a)\) satisfies

\[
 I_{a+1}=\begin{cases}(I_a\setminus\{a\})\cup\{\pi(a)\},&a\in I_a,\\I_a,&a\notin I_a,\end{cases}
\]

with cyclic indices. The unique base set of its positroid is

\[
\mathcal B(I_1,\ldots,I_6)=\bigl\{B\in\tbinom{[6]}3:B\ge_a I_a\text{ in componentwise Gale order for all }a\bigr\}.
\]

Each of the \(20\) three-element subsets is tested explicitly against the six cyclic Gale inequalities. Exhaustive enumeration produces \(883\) distinct nonempty base collections, with no duplicate, reproducing the previously published total for \(\operatorname{Gr}(3,6)\) (OEIS A046802). Exhaustiveness follows from the cited bijection and the finite permutation/decorations loops, not statistical sampling.

**2. Exact toricity test.** McNeill's toricity theorem proves \(\Pi_M\) is toric for some algebraic torus **if and only if** \(M\) is regular; Quail–Rombach prove that for positroids regularity is equivalent to representability over \(\mathbb F_2\). For each base set \(\mathcal B\), choose its first lexicographic basis \(B_0\) and normalize a candidate binary representation to an identity block on \(B_0\). Every off-pivot entry is then *forced* by the binary indicator of the basis obtained by exchanging that pivot for the column index. Its \(20\) maximal minors are checked by exact Gaussian elimination over \(\mathbb F_2\). If the reconstructed matrix has exactly the input base set, the matroid is binary. Conversely, any binary representation can be reduced to this unique normalized matrix (column scalings over \(\mathbb F_2\) are trivial), so failure of the test excludes binary representability. This counts exactly \(703\) regular/toric positroids and \(180\) nonregular ones. As a separate matroid-theoretic cross-check, `verify.py` also identifies \(U_{2,4}\) minors of all \(883\) rank-three matroids; it agrees in every case with the binary-minor criterion.

**3. Dimensions and singularities.** For regular positroids the standard diagonal torus has a dense orbit, and the corresponding moment polytope is the matroid base polytope \(P(M)\). Its dimension is

\[
 d=6-c(M),
\]

where \(c(M)\) is the number of connected matroid components, including loops and coloops as singleton components. The code identifies components using exactly the pairs of labels occurring in some single-element basis exchange. At a torus-fixed point indexed by a basis \(B\), Billey–Weaver's exact tangent-space criterion identifies the tangent-space dimension with the number of neighboring bases of \(B\) in the Johnson graph \(J(6,3)\). Their smoothness theorem shows that \(\Pi_M\) is smooth precisely when every such vertex has \(d\) neighbors. This checks every basis of every toric matroid, not just a chosen vertex. Counting by the resulting pair \((d,\mathrm{smooth})\) gives all eight nonzero cells of the displayed table. No toric positroid variety can exceed dimension five, since the standard diagonal torus modulo the scalar diagonal has dimension five.

**4. Independent exhaustive representation-space enumeration.** `independent.py` does not enumerate decorated permutations. Instead, it lists *all* reduced-row-echelon \(3\times6\) matrices over \(\mathbb F_2\), which represent the \(1395\) distinct binary three-planes (the Gaussian binomial coefficient \(\genfrac{[}{]}{0pt}{}{6}{3}_2=1395\)). It obtains their sets of nonzero maximal minors and tests the positroid condition using the six cyclic lexicographically minimal bases: a binary matroid is a positroid exactly when its actual bases equal the intersection of the six cyclic Gale upper sets. Uniqueness of binary representations makes this a duplicate-free enumeration of the binary rank-three matroids. It independently produces \(703\) positroid supports. Finally, `verify.py` asserts **support-by-support equality** with all \(703\) supports found by the decorated-permutation algorithm, including equality of each dimension and smoothness classification. Thus the equality of the two distributions is stronger than agreement of their aggregate sums.

## Verification

Place `compute.py`, `independent.py`, and `verify.py` in one directory and run `python3 verify.py`. The saved standalone program returns `VERIFY_OK` and checks \(883\) distinct positroids, \(1395\) binary row spaces, \(703\) common binary-positroid supports, the complete dimension/smoothness table, and all \(883\) binary versus \(U_{2,4}\)-minor decisions. All operations use exact finite integer, bit and set arithmetic. The proof of the reduction from these finite computations to the geometric statements is given above; a finite enumeration is exhaustive here because the universe has been proved finite and completely parametrized.

## Relationship to prior work

McNeill (2026) proves the regularity–toricity equivalence but does not give the \(\operatorname{Gr}(3,6)\) dimension/singularity table. Quail–Rombach (2024/2025) supply the positroid binary/regular characterization and graphic structure, not this enumeration. Billey–Weaver (2022) give the precise Johnson-graph smoothness criterion and enumerate smooth positroids without restricting to the regular/toric subfamily; their Figure 11 includes the already-known total \(440\) in rank three and ground-set size six. Machacek (2024) studies finite-field nonnegative Grassmannians and gives formulas especially in rank two; the inspected text did not state this rank-three geometric table. These results are essential **premises**, not rediscovered theorems. The new statement is their complete, exact dimension-by-singularity intersection in the first symmetric non-rank-two case, with independent support-level certification and a sharp maximal-dimension singularity phenomenon.

## Limitations

The result is a classification of labeled embedded varieties in one fixed Grassmannian, not a classification of varieties up to abstract isomorphism, nor a formula for general rank or ground-set size. Numerical novelty is assessed against the inspected primary sources and indexed records; no universal historical-priority guarantee is asserted. The finite calculation has been checked twice using separate complete parametrizations, but no independent mathematical audit has been performed.

## References

- A. McNeill, *There are no unexpected toric positroid varieties*, arXiv:2610.35914 (first public 2026-10-07), Theorems 1 and 10. https://arxiv.org/abs/2610.35914
- J. Quail and P. Rombach, *Positroid envelopes and graphic positroids*, arXiv:2402.17841 (2024), Section 4. https://arxiv.org/abs/2402.17841
- S. Billey and J. Weaver, *Criteria for smoothness of positroid varieties via pattern avoidance, Johnson graphs, and spirographs*, arXiv:2207.06508 (2022), Theorems 1.5 and 1.7 and Section 9. https://arxiv.org/abs/2207.06508
- J. Machacek, *A finite totally nonnegative Grassmannian*, arXiv:2410.06177 (2024). https://arxiv.org/abs/2410.06177
- OEIS A046802, rank-refined count of all positroid cells; at \(n=6,k=3\) the total is \(883\), a previously known input for comparison. https://oeis.org/A046802
