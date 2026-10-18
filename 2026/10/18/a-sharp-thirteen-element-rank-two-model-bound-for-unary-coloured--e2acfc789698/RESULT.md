# A sharp thirteen-element rank-two model bound for unary-coloured equivalence relations

## Finding

In the ordinary first-order language consisting of equality, one equivalence relation \(E\), and one arbitrary unary predicate \(P\), there are exactly **207** complete quantifier-rank-at-most-two theories of **nonempty finite** structures. Every such theory is represented by a structure with at most **13** elements; the bound is sharp. Exactly **two** of the 207 theories have minimum finite model size 13.

The complete distribution, with \(h(s)\) the number of theories whose smallest representative has \(s\) elements, is

\[
\begin{array}{c|rrrrrrrrrrrrr}
s&1&2&3&4&5&6&7&8&9&10&11&12&13\\\hline
h(s)&2&6&10&17&22&28&30&29&26&18&12&5&2
\end{array}.
\]

These results hold for **all** first-order sentences of quantifier rank at most two, without any bound on the number of variable symbols or Boolean connectives. They do not concern counting quantifiers or sentences of higher rank.

## Assumptions and scope

A structure \(A\) is a nonempty finite set with an equivalence relation \(E\subseteq A^2\) and an arbitrary distinguished subset \(P\subseteq A\). Call elements in \(P\) red and others blue. Two such structures are rank-two equivalent if every ordinary first-order sentence of quantifier rank at most two has the same truth value in both. Quantifier rank counts nested quantifiers, not the total number of quantifiers.

An \(E\)-class has a red-blue size pair \((r,b)\). Form its **capped class type** \((\min(r,2),\min(b,2))\), one of the eight pairs

\[
(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2).
\]

The **capped profile** of \(A\) records, for each of these eight types, the smaller of two and the number of classes of that type. Its canonical representative uses exactly the capped class sizes and the capped numbers of classes. It is nonempty, and there are \(3^8-1=6560\) possible nonzero capped profiles.

## Proof

**Step 1: rank-two logical normal form.** For an element \(a\) in any structure, consider the set \(W_A(a)\) of all realized quantifier-free atomic \(2\)-patterns \((\text{colour}(b),a=b,E(a,b))\), as \(b\) ranges over the structure. The atomic colour of \(a\) together with \(W_A(a)\) determines its complete rank-one first-order type: every rank-one formula with the one free variable \(x\) is a Boolean combination of quantifier-free formulas in \(x\), and formulas \(\exists y\,\theta(x,y)\) for quantifier-free \(\theta\). Each quantifier-free \(\theta\) is a Boolean combination of the stated atomic data.

Consequently, the set \(T_A=\{(\operatorname{colour}(a),W_A(a)):a\in A\}\) determines the rank-two *sentence* theory: each sentence of rank at most two is a Boolean combination of sentences asserting that an element of a given rank-one type exists. Conversely, every individual pointed rank-one type is definable by a finite conjunction of present and absent witness-pattern assertions, and its existence is a rank-two sentence. Thus

\[
A\equiv_2 B\quad\Longleftrightarrow\quad T_A=T_B.
\]

This equivalence is an explicit classification, not merely a computational heuristic.

**Step 2: uniform finite-profile reduction.** For \(a\) in an equivalence class \(C\), the possible second moves are: \(a\) itself; a different member of \(C\) of either colour; and a member of a different class of either colour. The existence of the second kind depends only on the size of each colour inside \(C\), capped at two. Existence of the third kind depends on the presence of an outside class containing the requested colour. Replacing all class colour counts by their caps at two and retaining at most two classes of each capped type preserves both conditions for every surviving pointed type; deleted elements have one of the same pointed types as the elements retained. Therefore this reduction preserves \(T_A\), and hence the entire rank-two theory. All nonempty finite theories occur among the 6560 canonical profiles.

**Step 3: exact finite classification and minimization.** The standalone verifier `verify_rank2.py` iterates *every* vector in \(\{0,1,2\}^8\setminus\{0\}\) and builds the logical invariant of Step 1 using only finite sets, tuples, and exact integers. It groups all 6560 representatives by \(T_A\); there are exactly 207 distinct keys. For each key it chooses a representative of smallest cardinality (where a vector \(m\) has size \(\sum_i m_i(r_i+b_i)\)). The resulting histogram is precisely that displayed above. In particular the largest minimum is 13 and exactly two keys attain it. Thus no 12-element model can realize either of those two types, while the displayed 13-element representatives do; this gives a sharp lower bound and construction.

To make the extreme cases reproducible, using the eight class types in the order above, the minimum 13-element profile vectors are

\[
(1,1,1,0,0,1,1,1)\quad\text{and}\quad(1,1,1,0,1,1,0,1).
\]

**Step 4: independent semantic consistency check.** The verifier additionally constructs an explicit finite universe for each canonical profile and computes its rank-two theory by the standard recursive Ehrenfeucht–Fraïssé type tree. Rank-zero types are complete atomic diagrams of currently chosen elements. A rank-\(k+1\) type is the current atomic diagram together with the set of all rank-\(k\) types produced by selecting one more element, including already selected elements. There are exactly 207 distinct recursive root types, and every pair of the 6560 profiles has equal root types if and only if their \(T_A\) invariants agree. This checks the nonstandard computational classification via a separately implemented semantics.

## Verification

With Python 3.9 or later, from the directory containing the supplied file run `python3 verify_rank2.py`. The script has no third-party dependencies. It asserts the exact count 6560, type count 207, full minimum-size histogram, maximum 13, two extremal profiles, and agreement of two independently defined logical signatures on the **whole** canonical-profile universe. Assertions are executable checks; the mathematical justification that this finite census covers *every* eligible finite structure is Step 2, not the execution log.

## Relationship to prior work

Pratt-Hartmann (2015), *The two-variable fragment with counting and equivalence*, studies satisfiability and finite satisfiability for the substantially more expressive two-variable logic **with counting**, in structures containing an equivalence relation. In its Introduction and §§2–6 the focus is decision complexity and model constructions, rather than the exact number and smallest representatives of ordinary rank-two theories in the specific one-unary-predicate language. The current classification uses the standard Ehrenfeucht–Fraïssé method in a sharply restricted signature but determines a precise model-size invariant and all its extremal types.

The uncoloured equivalence-relation classification by truncated class sizes does not decide the present assertion: a structure consisting of a red-red class and a blue-blue class and one consisting of two red-blue classes have the same uncoloured class sizes and global colour totals, yet the rank-two sentence \(\exists x\exists y\,[P(x)\wedge P(y)\wedge x\ne y\wedge E(x,y)]\) separates them. Coloured internal class patterns are essential.

## Limitations

No originality claim is made relative to every unpublished, unindexed, or inaccessible tabulation. The priority search found no earlier exact 207/13 census, but absence from searched records is not a uniqueness proof. The computation is exhaustive only **after** the proved capped-profile reduction. These claims are for nonempty finite models, ordinary first-order quantifiers, exactly one arbitrary unary predicate and exactly one equivalence relation; in particular they do not extend to counting logic, multiple equivalences or quantifier rank three.

## References

1. Ian Pratt-Hartmann, “The two-variable fragment with counting and equivalence,” *Mathematical Logic Quarterly* **61** (2015), 474–515, first published November 25, 2015, DOI: 10.1002/malq.201400102. https://doi.org/10.1002/malq.201400102
2. Leonid Libkin, *Elements of Finite Model Theory*, Springer, 2004, chapters on Ehrenfeucht–Fraïssé games and finite-model expressiveness. https://doi.org/10.1007/978-3-662-07003-1
