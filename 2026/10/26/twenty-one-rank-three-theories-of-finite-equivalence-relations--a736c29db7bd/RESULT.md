# Twenty-one rank-three theories of finite equivalence relations

## Finding

In the first-order vocabulary consisting only of equality and a binary equivalence relation \(E\), the class of **nonempty finite** structures has **exactly 21** equivalence classes under agreement on all first-order sentences of quantifier rank at most \(3\). Every class has a representative on at most \(9\) elements, and this universal bound is optimal.

A representative is a disjoint union of equivalence classes. An exhaustive classification table of all \(63\) reduced multiplicity profiles is supplied in `verification/rank3_classes.csv`; it partitions the profiles into exactly \(21\) theory classes. Each table row also gives a smallest representative among these profiles.

## Assumptions and scope

All domains are finite and nonempty. The signature is exactly \(\{E\}\) with built-in equality; \(E\) is reflexive, symmetric, and transitive. No ordering, class labels, additional relations, constants, generalized quantifiers, or counting quantifiers are present. Ordinary first-order quantifier rank counts *nesting depth*, not total quantifier occurrences. Two structures are \(\equiv_3\)-equivalent exactly when every sentence of quantifier rank at most \(3\) has the same truth value in both.

For a structure \(A\), let \(n_1\) be its number of singleton \(E\)-classes, \(n_2\) its number of two-element classes, and \(n_{3+}\) its number of classes with at least three elements. Define its reduced profile to be \(p(A)=(\min(3,n_1),\min(3,n_2),\min(3,n_{3+}))\). Its canonical representative \(A_p\) has exactly \(p_1\) singleton classes, \(p_2\) doubleton classes and \(p_3\) tripleton classes. There are \(4^3-1=63\) nonzero profiles.

## Proof

**Reduction to 63 profiles.** In a three-round Ehrenfeucht–Fraïssé game, Duplicator maintains a one-to-one correspondence between equivalence classes already visited, respecting the size categories singleton, doubleton, and at least three, and a partial isomorphism between the chosen elements. For a move into an already visited class, there is an unused matching element whenever required: exact sizes match below three, and both sides have at least three elements otherwise. For a move into a new class of a given category, at most two classes in that category have been visited, so if the initial numbers are equal below three or are both at least three, another matching class is available. Therefore every nonempty \(A\) satisfies \(A\equiv_3 A_{p(A)}\). This is a mathematical all-size reduction, not an inference from a bounded experiment.

**Exact finite classification.** For an ordered tuple \(\bar a\) in a canonical structure \(A_p\), let \(Q_0(A_p,\bar a)\) be the complete quantifier-free diagram of equality and \(E\) on tuple positions. Recursively define
\[
Q_{r+1}(A_p,\bar a)=\left(Q_0(A_p,\bar a),\ \{Q_r(A_p,\bar a b):b\in A_p\}\right).
\]
By induction on formulas, two pointed structures have equal \(Q_r\) exactly when they satisfy the same first-order formulas of quantifier rank at most \(r\) in the displayed free variables. Existential quantification is precisely set membership of a child type; universal quantification follows by negation; Boolean combinations are covered by the atomic diagrams and set equality. Thus \(Q_3(A_p,())\) is a complete exact signature for the rank-three sentence theory.

`verification/census.py` enumerates all \(63\) reduced profiles, constructs these signatures with exact integer/tuple/set operations, and checks the supplied complete classification table. It finds precisely \(21\) distinct signatures. The \(21\) canonical shortest profile representatives in table order are
\[
\begin{gathered}
(1,0,0),(0,1,0),(2,0,0),(0,0,1),(1,1,0),(3,0,0),\\
(0,2,0),(1,0,1),(2,1,0),(0,1,1),(1,2,0),(2,0,1),\\
(0,0,2),(0,3,0),(1,1,1),(2,2,0),(0,2,1),(1,0,2),\\
(2,1,1),(2,0,2),(0,0,3).
\end{gathered}
\]
The largest of their orders \(p_1+2p_2+3p_3\) is \(9\). As a separate check, `verification/game_crosscheck.py` directly solves the two-sided minimax three-round game for every one of the \(63\) assigned profiles versus its representative, and for all \(\binom{21}{2}=210\) distinct pairs of representatives. It confirms all identifications and separations. The checker uses the game recursion rather than the syntactic-type recursion.

**Sharpness of nine.** Consider the structure with three equivalence classes, each of size three. It satisfies the rank-three sentence that there are at least three distinct equivalence classes,
\[
\exists x\exists y\exists z\;(\neg E(x,y)\land\neg E(x,z)\land\neg E(y,z)),
\]
and the rank-three sentence that *every* equivalence class has at least three elements,
\[
\forall x\exists y\exists z\;(x\ne y\land x\ne z\land y\ne z\land E(x,y)\land E(x,z)).
\]
Any \(\equiv_3\)-equivalent structure must satisfy both, so it has at least three classes of at least three elements each and hence at least nine elements. The witness itself has nine elements.

## Verification

Extract the three supplied standalone `verification/` files without changing their relative paths, then run `python verification/census.py` and `python verification/game_crosscheck.py` using Python 3 standard library only. Both completed successfully. The first checked the \(63\) rows against the exact type signatures and obtained \(21\) classes and a maximal minimum representative order of \(9\); the second checked all \(63\) class memberships and \(210\) pairwise separations. The universal profile reduction and the two sharpness sentences are separately proved above.

## Relationship to prior work

Mwesigye and Truss (2018 online; 2019 journal) analyze optimal finite representatives under short Ehrenfeucht–Fraïssé games for *coloured linear orders*, with detailed attention to two and three moves. Their objects have a linear order and colours; the present objects instead have only an equivalence relation. Their specific character/cutting results do not imply the \(21\)-type count or nine-element optimum here. Fagin, Lenchner, Vyas, and Williams (2022) distinguish quantifier rank from total quantifier count and study exact logical resources for finite structures, including rooted trees, not the rank-three theory census of equivalence partitions. Standard Ehrenfeucht–Fraïssé theory (e.g. Immerman's chapter) gives the game characterization used here, not the particular classification and optimum. Comparable previously catalogued exact rank-type results for one-red linear orders and finite Boolean algebras concern different signatures and are not direct implications.

## Limitations

The numerical classification concerns precisely quantifier rank three and nonempty *finite* pure equivalence structures; it does not assert a formula for higher ranks, results for ordered or enriched signatures, or minimum *total* quantifier counts. The finite certificate is exhaustive **because** of the separately proved profile reduction; the scripts alone are not proofs of the reduction. No independent external validation has been performed. A previously unlocated direct classification in historical logic literature remains a residual priority risk.

## References

1. F. Mwesigye and J. K. Truss, *On Optimal Representatives of Finite Coloured Linear Orders*, published online 2 May 2018, *Order* 36 (2019), 107–117. DOI: `10.1007/s11083-018-9458-3`. Lawful full text: `https://eprints.whiterose.ac.uk/id/eprint/129275/15/Mwesigye-Truss2019_Article_OnOptimalRepresentativesOfFini.pdf`.
2. R. Fagin, J. Lenchner, N. Vyas, and R. Williams, *On the Number of Quantifiers as a Complexity Measure*, first posted 30 June 2022, `arXiv:2207.00104`, `https://arxiv.org/pdf/2207.00104`.
3. N. Immerman, *Descriptive Complexity*, Chapter 6, “Ehrenfeucht–Fraïssé Games,” `https://people.cs.umass.edu/~immerman/book/ch6.pdf` (background game equivalence).
