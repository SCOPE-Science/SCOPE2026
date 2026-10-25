# The \(S_7\)-homology character of the seven-point intersecting-triples complex

## Finding
Let \(X\) be the simplicial complex whose 35 vertices are the three-element subsets of \([7]\) and whose faces are pairwise-intersecting families. Equivalently, \(X=\operatorname{Ind}(\operatorname{KG}(3,1))\), where the Kneser graph joins disjoint triples. The permutation group \(S_7\) acts on \(X\) by relabeling. Over \(\mathbb Q\), its complete reduced-homology representation is
\[
\widetilde H_d(X;\mathbb Q)\cong
\begin{cases}
\mathbf 1\oplus S^{(4,3)}\oplus S^{(2,2,2,1)},&d=6,\\
\bigwedge^6\mathbb Q^7\cong S^{(1,1,1,1,1,1,1)}\oplus S^{(2,1,1,1,1,1)},&d=9,\\
0,&\text{otherwise},
\end{cases}
\]
where \(S^\lambda\) denotes the rational Specht module for the partition \(\lambda\) and \(\mathbb Q^7\) is the seven-dimensional permutation representation. The sixth-homology representation has dimensions \(1+14+14=29\) and exactly one \(S_7\)-invariant line. Its two nontrivial irreducible constituents are sign twists of one another.

For a permutation \(g\in S_7\), let \(F_j(g)\) be the number of \(g\)-invariant \(j\)-element subsets of \([7]\). The characters admit the explicit formulas
\[
\chi_6(g)=1+(1+\operatorname{sgn}(g))(F_3(g)-F_2(g)),\qquad
\chi_9(g)=\operatorname{sgn}(g)F_1(g).
\]

## Assumptions and scope
All homology representations in the statement use rational coefficients. The complex has exactly 35 vertices; the action is the **natural** full symmetric group on the underlying seven points, not the action of an arbitrarily chosen subgroup. This is a statement about the linear action on ordinary reduced homology, not about Borel equivariant homology or equivariant homotopy type. The only external non-elementary input is the rational Betti-number and vanishing theorem for intersecting triples on seven points, as established in [1, Theorem 18]: \(\widetilde H_6(X;\mathbb Q)\cong\mathbb Q^{29}\), \(\widetilde H_9(X;\mathbb Q)\cong\mathbb Q^7\), with every other reduced rational group zero. The representation refinement is proved below.

## Proof
**1. A signed six-subset basis in degree nine.** For each six-element subset \(S\subset[7]\), let \(X_S\subset X\) be the induced subcomplex on the 20 triples contained in \(S\). Within \(S\), two triples are disjoint exactly when complementary. Thus, the ten complementary pairs yield \(X_S=(S^0)^{*10}\cong S^9\). Let \(z_S\) be an integral oriented fundamental cycle.

Choose a decomposition \(S=A\sqcup B\) into two three-sets and define the ten-vertex simplex
\[
F_{S,A}=\{A\}\cup\bigl\{\{a\}\cup C: a\in A,\ C\in\tbinom B2\bigr\}.
\]
Any two of its triples intersect: the triples other than \(A\) have two elements in a three-set \(B\), and hence their \(B\)-parts intersect. It selects one triple from each of the ten complementary pairs. No set of at most two ground points meets all ten triples: for a pair contained in \(B\) use \(A\); for a pair contained in \(A\) use a triple with its \(A\)-point outside the pair; and for a mixed pair \(\{a,b\}\) use \(\{a'\}\cup(B\setminus\{b\})\), with \(a'\ne a\). (Smaller sets are covered by these cases.) Consequently no triple using the seventh point meets all ten members, so \(F_{S,A}\) is a maximal nine-simplex of \(X\). Its ten triples have union \(S\). Its characteristic integral nine-cochain is a cocycle, taking value \(\pm1\) on \(z_S\) and zero on \(z_T\) for any distinct six-set \(T\). Hence the seven \([z_S]\) are integrally linearly independent, indeed a split free subgroup in ninth homology. Since [1, Theorem 18] gives rational dimension seven, these classes are a rational basis. This basis argument is compatible with the cross-polytopal lower bound of [2, Theorem 10], whose existence is not claimed as new here.

The stabilizer \(S_6\) of a six-set permutes the ten complementary pairs and may exchange their endpoints. On the oriented boundary of the cross-polytope its degree is the determinant of that signed permutation of ten axes. A transposition of two labels fixes four complementary pairs without exchanging endpoints and permutes the remaining six pairs in three two-cycles, giving degree \((-1)^3=-1\). Thus the stabilizer acts on \([z_S]\) by its sign character. Relabeling carries \(z_S\) to \(\pm z_{gS}\), with sign equal to the induced ordering of the six elements. Therefore, the oriented six-set basis is exactly \(\bigwedge^6\mathbb Q^7\). Its decomposition into the two indicated hook Specht modules follows by the standard decomposition of exterior powers of the permutation module. This proves the ninth-degree part and its trace formula.

**2. The reduced Lefschetz trace as an independence polynomial.** Fix a permutation \(g\in S_7\). Its action on the 35 vertices (triples) has orbits. Discard any orbit containing two disjoint triples. Put an edge between two remaining orbits if any triple in one is disjoint from any triple in the other. Call the resulting finite graph \(Q_g\). The \(g\)-stable simplices of \(X\) are precisely the unions of independent sets of vertices of \(Q_g\). A union of \(r\) triple-orbits has the signed trace contribution \((-1)^{r-1}\) to the alternating simplicial-chain trace, since a cycle of length \(\ell\) contributes the orientation sign \((-1)^{\ell-1}\). Including the reduced empty-face contribution, the reduced Lefschetz number is therefore
\[
\widetilde L(g)=-I(Q_g;-1),\qquad
I(Q;t)=\sum_{J\text{ independent in }Q}t^{|J|}.
\]
For any vertex \(v\) of \(Q\), this is evaluated exactly by
\[
I(Q;-1)=I(Q-v;-1)-I(Q-N[v];-1),\qquad I(\varnothing;-1)=1.
\]
The 15 possible cycle types of \(S_7\) are exhausted in the following table. The `verify_s7_kneser.py` artifact independently checks each signed polynomial both by this recurrence and by directly enumerating every independent subset of \(Q_g\).

| Cycle type | Usable orbits | \(\widetilde L\) | \(\chi_9\) | \(\chi_6\) |
|---|---:|---:|---:|---:|
| \((7)\) | 2 | 1 | 0 | 1 |
| \((6,1)\) | 5 | 2 | -1 | 1 |
| \((5,2)\) | 3 | 1 | 0 | 1 |
| \((5,1,1)\) | 7 | -3 | 2 | -1 |
| \((4,3)\) | 3 | 1 | 0 | 1 |
| \((4,2,1)\) | 9 | 0 | 1 | 1 |
| \((4,1,1,1)\) | 11 | 4 | -3 | 1 |
| \((3,3,1)\) | 13 | 4 | 1 | 5 |
| \((3,2,2)\) | 7 | -1 | 0 | -1 |
| \((3,2,1,1)\) | 11 | 3 | -2 | 1 |
| \((3,1,1,1,1)\) | 15 | -5 | 4 | -1 |
| \((2,2,2,1)\) | 15 | 2 | -1 | 1 |
| \((2,2,1,1,1)\) | 21 | 2 | 3 | 5 |
| \((2,1,1,1,1,1)\) | 25 | 6 | -5 | 1 |
| \((1,1,1,1,1,1,1)\) | 35 | 22 | 7 | 29 |

**3. Identifying the degree-six module.** By the concentration theorem [1, Theorem 18], only degrees six and nine can contribute to reduced rational homology. The Lefschetz identity therefore gives \(\widetilde L(g)=\chi_6(g)-\chi_9(g)\), producing the final column. The permutation character on the \(j\)-subsets is \(F_j(g)\). Young's rule for these subset-permutation modules gives \(\chi_{S^{(4,3)}}(g)=F_3(g)-F_2(g)\). Conjugating a partition twists its Specht character by sign, so \(\chi_{S^{(2,2,2,1)}}(g)=\operatorname{sgn}(g)(F_3(g)-F_2(g))\). For each of the 15 cycle types the computed trace is exactly their sum plus one. The irreducible characters are independent and rational representations of a finite group are semisimple. This proves the degree-six decomposition and the displayed formula.

## Verification
Run `python3 verify_s7_kneser.py` using Python 3 (standard library only). It checks all seven supporting cross-polytopes and their maximal-face dual cocycles, all 720 six-symbol relabelings and their orientation signs, the quotient-graph construction for all 15 conjugacy types, two **independent** exact calculations of \(I(Q_g;-1)\), and the resulting irreducible-character orthogonality. At the identity conjugacy class the exhaustive branch enumerates 1,278,686 invariant faces, including the empty face. Its final output is `VERIFY_OK`; `character_table.txt` records the full computation. All calculations use integers. The proof's reliance on the published rational concentration theorem is stated explicitly and not disguised as an independent reproof of that theorem.

## Relationship to prior work
Feng's October 12, 2026 manuscript [1, Theorem 18] determines the rational Betti numbers in degrees six and nine for all triple Kneser independence complexes, and [1, Questions 20–21] discusses spherical representatives and asks for degree-six bases. Feng and Wang's April 16, 2024 paper [2, Theorem 10] constructs independent cross-polytopal ninth-degree cycles and cohomological detectors. These sources cover the dimensions and the six-set independence input; combining them already yields the number of ninth-degree spherical basis elements. Neither source identifies the full natural \(S_7\)-module in sixth homology, its two conjugate 14-dimensional constituents, or the unique fixed line. Published symmetric-group calculations for other graph complexes concern different objects and do not imply this character. The claim is precisely this **equivariant refinement**, not a new Betti-number calculation.

## Limitations
The theorem treats the seven-point case and rational representations. It does not supply an explicit geometric cycle representing the unique degree-six invariant line, classify the integral \(S_7\)-lattice, prove an integral homotopy splitting, or extend the representation to ground sets of eight or more points. Character computation is exhaustive for the finite fifteen-class group, not a proof of a statement for arbitrary ground-set size. The cited 2026 rational Betti theorem is a preprint mathematical input and has not been independently reproduced by the provided verifier. Bibliographic priority remains subject to unindexed literature.

## References
[1] Z. Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394v1 (first submitted 2026-10-12), Theorem 18 and Questions 20–22. https://arxiv.org/html/2610.17394

[2] Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566v1 (first submitted 2024-04-16), Lemma 9 and Theorem 10. https://arxiv.org/pdf/2404.10566

[3] Standard facts: simplicial Lefschetz trace formula, Young's rule for subset-permutation modules, and the sign-twist correspondence for conjugate Specht partitions.
