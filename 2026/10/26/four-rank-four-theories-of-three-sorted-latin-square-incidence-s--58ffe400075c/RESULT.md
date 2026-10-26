# Four rank-four theories of three-sorted Latin-square incidence structures and a sharp rank-five algebraic witness

## Finding

Let \(L\) be a nonempty finite Latin square of order \(n\geq 1\). Encode it as the **three-sorted incidence structure** \(\mathcal I(L)\): its universe is the disjoint union of a row sort \(R\), a column sort \(C\), and a symbol sort \(S\), each containing \(n\) elements; the language contains three unary sort predicates and one ternary relation \(T(r,c,s)\) asserting that the entry in row \(r\), column \(c\) is symbol \(s\). No constants, functions, orderings, or identifications between the sorts are supplied.

For any two finite Latin squares \(L\) and \(M\) of orders \(n,m\geq 1\), respectively,

\[
\mathcal I(L)\equiv_4\mathcal I(M)\quad\Longleftrightarrow\quad \min(n,4)=\min(m,4).
\]

Thus exactly four distinct rank-four first-order theories occur in this entire class, with orders \(1\), \(2\), \(3\), and \(\geq4\), respectively. The least representative size for the last class is **12 domain elements**, since a Latin square of order \(4\) has four elements in each of the three sorts. This bound is sharp among members of the class.

The rank-four collapse is also **optimal as a bound on sensitivity to the Latin-square multiplication pattern**. Let \(L_4^{\mathrm{cyc}}\) and \(L_4^{\mathrm{bool}}\) be the addition tables of \(\mathbb Z/4\mathbb Z\) and \((\mathbb Z/2\mathbb Z)^2\), with independent row, column, and symbol copies. Their incidence structures agree through quantifier rank four and disagree at rank five. More generally, a rank-five sentence identifies, among addition tables of finite abelian groups, those with an element of order greater than two. The latter assertion is a *relative definability* statement inside this class of tables, not a classification of all rank-five Latin-square theories.

## Assumptions and scope

- The universe consists of three **disjoint copies** of the row index set, column index set, and symbol set. Equality between different sorts is always false.
- A Latin square has each symbol exactly once in each row and in each column; order one is permitted.
- The logic is ordinary first-order logic over equality, the three named unary sort predicates, and the ternary incidence predicate \(T\). Quantifier rank counts maximal nesting depth, not the total number of quantifiers written.
- \(\equiv_k\) denotes agreement on all first-order sentences of quantifier rank at most \(k\).
- No result here transfers unchanged to the **one-sorted** group-operation language with an identity constant, or to a functional quasigroup signature. Those signatures reveal more atomic information.

## Proof

**1. Separation of the four orders.** For \(j=2,3,4\), the sentence asserting that there are \(j\) pairwise distinct rows has quantifier rank \(j\). Therefore structures with different truncated orders \(\min(n,4)\) are not rank-four equivalent. Rank one already asserts that each sort is nonempty; it does not split these four cases further.

**2. Small orders.** Every Latin square of order \(1\), \(2\), or \(3\) is unique up to independent permutations of rows, columns, and symbols (isotopy). This is also recorded in the first three lines of the isotopy count in McKay--Meynert--Myrvold's enumeration. Isotopies are precisely isomorphisms of the three-sorted encoding. Hence all structures of a fixed order below four are isomorphic.

**3. One-point extension lemma.** Consider any two Latin squares of orders at least four. Suppose a tuple of at most three (possibly repeated) elements in one incidence structure and a tuple of equal length in the other have the same quantifier-free atomic diagram. Then the **sets of quantifier-free diagrams of one-element extensions** are identical.

To prove the lemma, first preserve any repetitions of already named elements. For a genuinely new element, only the distinct elements in the old tuple matter. With at most three old distinct elements, their sort multiplicities have, up to permuting the three sorts, the forms \(3\), \(2+1\), \(1+1+1\), or a subcase involving fewer elements.

- In the \(3\) case, all old elements lie in one sort. A fresh element in that sort exists because its size is at least four. No new ternary incidence with three different sorts can be formed; other sorts are nonempty.
- In the \(2+1\) case, if the new element is taken from the missing sort, there are two **different** symbols/rows/columns completing the two old cross-sort pairs, by Latin uniqueness. Either completion can be chosen, as can a third element missing both completions, because each sort has at least four elements. If the new element is taken from an already represented sort, only equality and freshness matter (and enough fresh elements exist).
- In the \(1+1+1\) case, there is one old element of each sort, whose incidence truth value is part of the atomic diagram. A new element from, say, the row sort can complete the old column-symbol pair in exactly one row. That row equals the old row if and only if the old triple is incident. If the triple is nonincident, the completion row is fresh. In either case a different fresh row avoiding the pair is available, since there are at least four rows. The other two sorts are symmetric.
- With fewer old distinct elements, the same Latin uniqueness and the lower bound of four guarantee matching equality, freshness, and incidence patterns.

The lemma concerns **all** Latin squares of these orders, not a sampled list and not their isotopy classes.

**4. Four-round game.** After zero, one, two, or three moves of the ordinary Ehrenfeucht--Fraïssé game, Duplicator maintains equality of the atomic diagrams of the ordered played tuples. Upon the next move, the extension lemma supplies a response with the same extended diagram, in either direction. After four moves the played correspondence is a partial isomorphism. The Ehrenfeucht--Fraïssé theorem therefore gives \(\mathcal I(L)\equiv_4\mathcal I(M)\) for every two orders at least four. Together with Steps 1--2 this proves the displayed iff and the sharp representative bound.

**5. A rank-five separator within order four.** Define the following sentence, where sort assertions are abbreviated in the displayed matrix:

\[
\begin{aligned}
\Phi_5:=\exists r\,\exists r'\,\exists c\,\exists c'\bigl[&R(r)\land R(r')\land C(c)\land C(c')\\
&\land r\ne r'\land c\ne c'\\
&\land \exists s\bigl(S(s)\land T(r,c,s)\land T(r',c',s)\bigr)\\
&\land \exists t\bigl(S(t)\land T(r,c',t)\land\neg T(r',c,t)\bigr)\bigr].
\end{aligned}
\]

The four outer existential quantifiers are followed by **two sibling** existential subformulas. Therefore \(\operatorname{qr}(\Phi_5)=5\), not six. The first sibling requires equal symbols at the two diagonal corners of a \(2\times2\) rectangle; the second requires different symbols at the off-diagonal corners. By the Latin condition the rectangle then has exactly three distinct symbols.

In \(\mathbb Z/4\mathbb Z\), take rows \(0,1\) and columns \(0,1\). The entries are \(0,1;1,2\), giving three distinct symbols, so \(\Phi_5\) holds (interchange the two columns if needed to place the equal entries on the displayed diagonal). In \((\mathbb Z/2\mathbb Z)^2\), write the rows as \(a,a+u\), columns as \(b,b+v\), for nonzero \(u,v\). The four entries are \(a+b,a+b+v;a+b+u,a+b+u+v\). If a diagonal pair agrees then \(u=v\), and the off-diagonal pair agrees too, so \(\Phi_5\) fails. These two 12-element structures agree at rank four by Step 4, establishing the exact least distinguishing rank five. Because the published order-four isotopy census has exactly two classes and the displayed formula distinguishes these representatives, they represent the two different isotopy classes.

For any finite abelian group \(G\), the same rectangle computation shows that the diagonal entries can agree while the off-diagonal entries differ exactly when some group element \(u\) satisfies \(2u\ne0\). Indeed choose row and column increments equal to \(u\), reversing the indicated column order for the diagonal. Conversely diagonal equality forces the two increments to be equal up to sign, and equality of the other diagonal fails exactly when twice that increment is nonzero. Thus \(\Phi_5\) captures exponent greater than two for abelian addition tables.

## Verification

The standalone `verify_latin_rank4.py` file independently constructs finite incidence diagrams for cyclic addition tables of orders one through six and for the Klein-four table. For every ordered tuple of at most three elements, it computes the set of quantifier-free diagrams attainable by adding one element; it asserts that this set depends only on the old atomic type. For all examples of order at least four, the complete extension-type dictionaries agree. The recorded distribution of atomic prefix types at lengths zero through three is \(1,3,12,63\), respectively, and the corresponding numbers of distinct extension diagrams (summed over prefix types) are \(3,12,63,417\).

The program also exhaustively enumerates all **four** reduced Latin squares of order four and all **56** reduced Latin squares of order five, checks that every resulting extension profile agrees with the cyclic order-four profile, and verifies the explicit rank-five rectangle witness and its absence in the Klein-four table. It reports `VERIFY_OK`. These finite checks are consistency tests; the universal four-round equivalence follows from the symbolic one-point extension lemma above, not from interpolation of the computed cases.

Reproduction: run `python3 verify_latin_rank4.py` with the supplied file in the same directory. The observed standard output is included as `verification_output.txt`. No external packages or input data files are needed.

## Relationship to prior work

McKay, Meynert, and Myrvold enumerate isotopy and related combinatorial equivalence classes of small Latin squares. In particular their order-four table has two isotopy classes, whereas the result here shows that neither is distinguishable from the other by any rank-four sentence in the **three-sorted incidence** language. Their paper does not itself supply the four-round EF classification or the sharp five-round witness in the relevant examined sections and full-text term searches.

Libkin's *Elements of Finite Model Theory*, Chapter 3, supplies the general game theorem and rank conventions, but the present Latin-square extension lemma and explicit classification are not an instance stated there. Gomaa's work on descriptive complexity of finite abelian groups uses a **one-sorted** ternary operation relation with a named identity constant; those extra cross-coordinate identifications make its estimates inapplicable as exact depth bounds for the three-disjoint-sort encoding here. The present result neither contradicts nor generalizes his one-sorted bounds. The examined results on isotopy enumeration, general games, and one-sorted group complexity do not imply the present exact three-sorted depth classification. This comparison is not a uniqueness proof against all literature.

## Limitations

The theorem is specific to the three named sorts, one ternary relation, and ordinary first-order quantifier rank. It is not a claim about counting logic, variable-width logics, algebraic functional signatures, or the number of rank-five classes of *all* Latin squares. The rank-five statement gives one sharp structural distinction, not an exhaustive rank-five classification. No independent external proof audit was performed. Some potentially relevant literature may be inaccessible or absent from searched indexes.

## References

1. B. D. McKay, A. Meynert, W. Myrvold, *Small Latin Squares, Quasigroups and Loops*, Journal of Combinatorial Designs 15 (2007), 98--119. First online publication 2006-03-02. DOI: `10.1002/jcd.20105`. Relevant inspected material: definition, isotopy discussion, Table 2.
2. L. Libkin, *Elements of Finite Model Theory*, Springer; accessible author text at `https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf`. Chapter 3, especially Definition 3.8 and Theorem 3.9.
3. W. Gomaa, *Model Theory and Complexity Theory*, University of Maryland PhD dissertation (2007), Chapter 3, especially Definition 3.1 of its one-sorted group signature. `https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440`.
4. W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087--1116. DOI: `10.1142/S0218196710006047` (abstract inspected; the dissertation supplies accessible detailed language definitions).
