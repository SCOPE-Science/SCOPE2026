# The sharp four-round collapse of Latin-square incidence theories

## Finding

Write \(\mathcal L(L)\) for the three-sorted incidence structure of a finite Latin square \(L\). For any Latin squares \(L\) and \(L'\) of respective positive orders \(n\) and \(m\), in the language of equality, three named sorts, and one ternary incidence relation,

\[
\mathcal L(L)\equiv_4\mathcal L(L')
\quad\Longleftrightarrow\quad
\min(n,4)=\min(m,4).
\]

Thus there are exactly **four** first-order equivalence classes at quantifier rank four among all finite, nonempty Latin squares: orders one, two, three, and the class of all orders at least four. The final class contains arbitrarily large, mutually nonisotopic squares.

The collapse is **sharp as a uniform independence-of-isotopy statement**. Let \(C_4\) and \(V_4\) denote the Cayley Latin squares of the cyclic and Klein-four groups. They have the same order and satisfy

\[
\mathcal L(C_4)\equiv_4\mathcal L(V_4),
\qquad
\mathcal L(C_4)\not\equiv_5\mathcal L(V_4).
\]

The rank-five separator says that some two-by-two rectangle repeats a symbol on one diagonal but not on the other.

## Assumptions and scope

A Latin square of order \(n\ge1\) is a function \(L:R\times C\to S\), where \(R,C,S\) are *disjoint, named* sets, each of size \(n\), and each of the maps obtained by fixing either a row or a column is a bijection onto \(S\). The structure \(\mathcal L(L)\) has domain \(R\sqcup C\sqcup S\), unary sort predicates for the three parts, equality, and the ternary relation \(M(r,c,s)\) holding exactly when \(L(r,c)=s\). The sorts have no imposed identifications and no names for distinguished elements. It is equivalently a transversal design \(TD(3,n)\) with its three groups distinguished and its blocks encoded by a ternary relation.

Here \(\equiv_q\) means agreement on all first-order sentences of quantifier rank at most \(q\); quantifier rank is nesting depth, not the total number of quantifier occurrences. Typed quantifiers are abbreviations for sorted first-order quantifiers and have the same nesting count.

## Proof

**Lemma (three-point extension completeness).** If \(L\) and \(L'\) have orders at least four, any correspondence between at most three previously selected elements which preserves sorts, equality, and all selected \(M\)-atoms can be extended after either side selects one further element, preserving the complete atomic diagram.

**Proof of lemma.** Repeated selections are answered by the corresponding previously selected element. Suppose the new selection is distinct from the old values. If among the four selections no triple has one row, one column, and one symbol, no new \(M\)-atom can arise. The only constraint is availability of a fresh element of the chosen sort; at most three values of that sort are already selected, so one exists at order at least four.

If a new \(M\)-atom may arise, the old three selections (after accounting for possible repetitions) must contain either (i) one value of each sort or (ii) two values of one sort and one of another sort. In case (i), adjoining a value of an old sort can create at most one new incidence, namely the uniquely determined completion of the fixed pair from the two other sorts. If that completion is already the selected value, no distinct new choice satisfies the incidence. Otherwise, exactly one fresh choice satisfies it, and at least one fresh choice does not. The corresponding alternatives on both sides agree, since the existing triple's incidence is part of the matched atomic diagram.

In case (ii), adjoining a value of the previously absent sort may complete two triples. If the two old values of the repeated sort are distinct, their two completions are distinct by the Latin property; the possible new incidence vectors are \((1,0)\), \((0,1)\), and \((0,0)\), all realized since there are at least four values of the new sort. If the two old values coincide, the vectors are \((1,1)\) and \((0,0)\). These lists depend only on the existing equality pattern, not on the Latin square. All remaining sort distributions reduce to the no-new-incidence case. This establishes the lemma in both directions. \(\square\)

Duplicator applies the lemma after each of the first three moves and answers the fourth by its one-point extension rule, maintaining a partial isomorphism throughout. The four-round Ehrenfeucht--Fraisse theorem gives \(\mathcal L(L)\equiv_4\mathcal L(L')\) for all \(n,m\ge4\).

For orders one, two, and three, each Latin square is unique up to independent permutations of rows, columns, and symbols: normalize the first row and column, then the Latin conditions force the remaining entries. Hence all squares of a fixed such order are isomorphic as three-sorted incidence structures. For \(k=2,3,4\), the sentence saying that there exist \(k\) pairwise distinct rows has quantifier rank \(k\) and distinguishes orders \(k-1\) from all orders at least \(k\). This proves the stated iff classification.

For sharpness, consider the rank-five sentence \(\Phi\):

\[
\begin{aligned}
\exists r,r'\in R\ \exists c,c'\in C\;[\;&r\ne r'\land c\ne c'\\
&\land\bigl(\exists s\in S\;[M(r,c,s)\land M(r',c',s)]\bigr)\\
&\land\neg\bigl(\exists t\in S\;[M(r,c',t)\land M(r',c,t)]\bigr)].
\end{aligned}
\]

The four outer quantifiers are followed by either of two **non-nested** one-quantifier subformulas. Thus \(\Phi\) has quantifier rank five (although it contains six quantifier occurrences).

In \(C_4\), index rows, columns, and symbols by residues modulo four and use \(L(r,c)=r+c\pmod4\). The choice \(r=0\), \(r'=1\), \(c=0\), \(c'=3\) has equal main-diagonal symbols \(0\), while the off-diagonal symbols are \(3\) and \(1\). Thus \(C_4\models\Phi\). In \(V_4\), indexing by \(\mathbf F_2^2\), equality \(r+c=r'+c'\) implies \(r+c'=r'+c\) by characteristic two. Therefore \(V_4\not\models\Phi\), as required. \(\square\)

## Verification

The mathematical lemma, the forced small-order classification, and the explicit sentence establish the infinite theorem without computational extrapolation. Two standalone computational cross-checks accompany this note:

1. `checks/latin_extension_spectrum.py` enumerates all four reduced Latin squares of order four and all 56 reduced squares of order five. For every ordered triple (including repetitions), it calculates the complete atomic one-point extension set and verifies that the extension data are identical in all 60 squares and in three specified Cayley squares. It also enumerates rectangle witnesses to \(\Phi\).
2. `checks/latin_ef.cpp` independently builds the complete recursive Ehrenfeucht--Fraisse types of all tuples for both order-four group tables and confirms equivalence at ranks one through four and inequivalence at rank five. This checker considers all elements and repeated choices, not just distinct tuples.

The recorded deterministic outputs are `checks/latin_extension_spectrum.out` and `checks/latin_ef.out`. Reproduction with Python 3 and a C++17 compiler requires no third-party libraries.

## Relationship to prior work

McKay--Meynert--Myrvold enumerate isotopy classes of small Latin squares, including two classes at order four, and explain the three-part orthogonal-array representation. Devillers--Hall study rank-three **permutation-group actions** on Latin-square designs, a different meaning of rank. Cavenagh--Greenhill--Wanless analyze two-row cycle structure, including intercalates, but not Ehrenfeucht--Fraisse depth. These sources establish classical context; their stated results do not themselves assert a four-round collapse for **all** finite Latin squares or the sharp five-round separator.

## Limitations

The equivalence classification applies **only** to the three-sorted *relational incidence language*, without an identification of row, column, and symbol domains, a multiplication-function symbol, parameters, or counting quantifiers. It does not assert ordinary elementary equivalence, preserve graph signatures under unproved interpretations, or classify the theories at rank five. The rank-five statement is an explicit separation, not a full classification at rank five. Independent historical-priority confirmation and external mathematical audit are not part of this result.

## References

- B. D. McKay, A. Meynert, W. Myrvold, *Small Latin Squares, Quasigroups and Loops*, first published 2 March 2006, DOI: 10.1002/jcd.20105. Open author PDF: https://users.cecs.anu.edu.au/~bdm/papers/ls_final.pdf.
- A. Devillers, J. I. Hall, *Rank 3 Latin square designs*, J. Combin. Theory Ser. A **113** (2006), 894--902, DOI: 10.1016/j.jcta.2005.06.004. Author manuscript: https://users.math.msu.edu/users/halljo/research/rk3lsd_rev_30-Jun-05-submit.pdf.
- N. J. Cavenagh, C. Greenhill, I. M. Wanless, *The cycle structure of two rows in a random Latin square*, Random Structures & Algorithms **33** (2008), 286--309, DOI: 10.1002/rsa.20216. Author PDF: https://users.monash.edu.au/~iwanless/papers/randLS2rowRSA.pdf.
