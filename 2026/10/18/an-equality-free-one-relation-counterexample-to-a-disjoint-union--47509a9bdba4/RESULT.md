# An equality-free one-relation counterexample to a disjoint-union preservation normal form

## Finding

Let the signature consist of exactly one binary relation symbol \(R\), with **no equality symbol**. Put
\[
U(x):=\exists y\bigl(R(x,y)\land\neg R(y,y)\bigr),\qquad
V(x):=R(x,x)\land\neg U(x),
\]
and define the identity-free first-order sentence
\[
\Theta:=\bigl(\exists x\,U(x)\bigr)\land
\left[
\forall x\forall y\bigl((V(x)\land V(y))\to R(x,y)\bigr)
\ \lor\
\exists x\exists y\bigl(U(x)\land U(y)\land\neg R(x,y)\bigr)
\right].
\]
The class of nonempty \(R\)-structures satisfying \(\Theta\) is preserved under disjoint unions of any nonempty family, including arbitrary infinite families. Nevertheless, \(\Theta\) is **not** equivalent, even just over finite structures, to any first-order sentence \(\forall x\,\alpha(x)\) where \(\alpha\) is generated from relation atoms and their negations by conjunction, disjunction, unrestricted existential quantification, and two-way restricted universal quantifiers
\[
\forall y\bigl(R(z,y)\to\beta\bigr),\qquad
\forall y\bigl(R(y,z)\to\beta\bigr)
\]
with \(z\) distinct from \(y\). Thus the disjoint-union preservation normal-form conjecture remains false after **both removing equality and restricting the relational signature to one binary symbol**.

## Assumptions and scope

We use ordinary Tarskian first-order semantics, including the standard possibility of repeated variable assignments; repeated occurrences such as \(R(x,x)\) are relation atoms, not equality. The domain is nonempty. A disjoint union has no relation pairs linking different summands. The family of summands is assumed nonempty, as in the usual preservation formulation with a nonempty antecedent family. No conditions (reflexivity, transitivity, seriality) are imposed on \(R\).

The candidate normal-form fragment is the one described in Section 3.4 of van Benthem, ten Cate, and Yang, arXiv:2603.12171. A restricted universal's guard must refer to a variable \(z\ne y\). Other free variables and outer quantifiers are allowed as usual, but **there is no unrestricted universal quantifier inside \(\alpha\)** and negation applies only to atoms in that grammar.

## Proof

**Preservation under disjoint unions.** Suppose each member of a nonempty family \((\mathfrak M_i)_{i\in I}\) satisfies \(\Theta\). If the family has one member, the assertion is immediate. Otherwise select distinct \(i,j\in I\). In each component the leading existential conjunct provides points \(a_i,a_j\) with \(U(a_i)\) and \(U(a_j)\). The formula \(U\) is local to its component: its required outgoing edge and the target's absent loop are unaffected by the disjoint union. Because no cross-component \(R\)-edge exists, \(\neg R(a_i,a_j)\) holds. Thus the second disjunct of the bracket in \(\Theta\) is true in the union. The leading existential conjunct is true as well. This proves preservation, with no finiteness assumption.

**A finite separating pair.** Let \(\mathfrak A\) have universe \(\{p,s,q\}\) and precisely the edges
\[
R^{\mathfrak A}=\{(p,p),(p,s),(q,q)\}.
\]
Let \(\mathfrak B\) have universe \(\{p,s,q_1,q_2\}\) and precisely the edges
\[
R^{\mathfrak B}=\{(p,p),(p,s),(q_1,q_1),(q_2,q_2)\}.
\]
In \(\mathfrak A\), exactly \(p\) satisfies \(U\) and exactly \(q\) satisfies \(V\). Hence its first bracketed disjunct is true, and \(\mathfrak A\models\Theta\). In \(\mathfrak B\), exactly \(p\) satisfies \(U\), while \(q_1,q_2\) satisfy \(V\). The first bracketed disjunct fails at \((q_1,q_2)\), since \(\neg R(q_1,q_2)\); the second fails because its only possible pair of \(U\)-points is \((p,p)\), where \(R(p,p)\). Therefore \(\mathfrak B\not\models\Theta\).

**Fragment transfer lemma.** Suppose \(h:\mathfrak C\hookrightarrow\mathfrak D\) is an induced embedding such that its image is closed under **both incoming and outgoing** \(R\)-neighbors. For every formula \(\alpha\) in the stated existential/two-way-restricted-universal fragment, and every assignment \(\vec a\) into \(\mathfrak C\),
\[
\mathfrak C\models\alpha[\vec a]\quad\Longrightarrow\quad
\mathfrak D\models\alpha[h(\vec a)].
\]
This follows by structural induction. Atoms and their negations are preserved exactly by the induced embedding. Conjunction and disjunction preserve the implication by induction. Existential witnesses in \(\mathfrak C\) remain witnesses in \(\mathfrak D\). For \(\forall y(R(z,y)\to\beta)\), every successor of \(h(z)\) in \(\mathfrak D\) lies in the image and corresponds to a successor of \(z\) in \(\mathfrak C\); apply the induction hypothesis for \(\beta\). Incoming restricted universals are identical using predecessor closure. This proves the lemma without bounding the number of variables or nesting depth.

In \(\mathfrak B\), the subsets \(\{p,s,q_1\}\) and \(\{p,s,q_2\}\) each induce a copy of \(\mathfrak A\), and each is closed under incoming and outgoing neighbors. Every vertex of \(\mathfrak B\) belongs to at least one of these copies. Thus, for any candidate sentence \(\forall x\alpha(x)\), if it holds in \(\mathfrak A\), then the transfer lemma applied to a suitable copy proves \(\alpha\) at every vertex of \(\mathfrak B\), and so \(\mathfrak B\models\forall x\alpha(x)\).

If \(\Theta\) were equivalent over finite structures to such a sentence, its truth in \(\mathfrak A\) would force its truth in \(\mathfrak B\), contrary to the separating pair. The theorem follows.

## Verification

The standalone Python 3 program `check.py`, requiring no third-party packages, reconstructs both models and evaluates the sentence directly. It also exhaustively tests preservation for **155,236 ordered pairs** of satisfying finite relations on domain sizes one through three, and tests transfer on **15,000 deterministically seeded** formulas generated by the restricted grammar. The recorded successful output is:

```text
UNION_PRESERVATION_OK 155236 ordered small-model pairs; satisfying_counts={1: 0, 2: 7, 3: 387}
FRAGMENT_TRANSFER_OK 15000 randomly generated formulas
SEPARATION_OK A_size=3 B_size=4
```

The numerical checks are finite cross-checks; they are not a substitute for the structural induction proving the unrestricted fragment transfer or for the general disjoint-union argument.

## Relationship to prior work

The March 12, 2026 paper of van Benthem, ten Cate, and Yang studies first-order preservation under disjoint unions. Section 3.4 refutes the normal-form conjecture with a sentence explicitly using equality to count elements and leaves the identity-free version open. The present sentence differs materially: it has **one binary relation and no equality**, uses a local loop/terminal-edge marker \(U\), and separates two finite structures by adding an isolated loop without creating new neighbors of existing points. This gives a direct negative answer in the one-binary-relation signature. The earlier paper's equality-based counterexample does not syntactically settle that version.

The standard disjoint-union and generated-submodel constructions in modal model theory provide background for the transfer lemma, but do not by themselves supply the two concrete separating structures and identity-free sentence. Targeted searches did not identify a prior statement equivalent to this specific one-relation negative answer; absence of matches is not a priority proof.

## Limitations

This result concerns **preservation**, not invariance, under disjoint unions. It does not classify all preserved equality-free sentences or all normal forms; it refutes the particular conjectured normal form. The separating structures have sizes three and four, but no claim of minimality is made. The 1985 book where the original conjecture is attributed could not be examined in full; an older unindexed equivalent counterexample remains possible. The presented scientific verification is not an independent audit.

## References

1. Johan van Benthem, Balder ten Cate, and Xi Yang, *When do modal definability and preservation theorems transfer to the finite?*, arXiv:2603.12171v1, first publicly submitted March 12, 2026, especially Section 3.4. https://arxiv.org/html/2603.12171
2. Johan van Benthem, *Modal Logic and Classical Logic*, Bibliopolis, Naples, 1985. Bibliographic record: https://catalogue.bnf.fr/ark:/12148/cb349272600 (full primary text not inspected).
3. Patrick Blackburn and Johan van Benthem, *Modal Logic: A Semantic Perspective*, in *Handbook of Modal Logic*, Elsevier, 2007 (background on disjoint unions and generated submodels), DOI 10.1016/S1570-2464(07)80004-8.
