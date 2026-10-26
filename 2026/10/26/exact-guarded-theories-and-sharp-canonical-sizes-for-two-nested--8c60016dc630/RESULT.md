# Exact guarded theories and sharp canonical sizes for two nested equivalences

## Finding
Fix an integer \(k\geq 0\), put \(c=2^k\), and consider nonempty structures over exactly \(k\) unary predicates, equality, and two binary equivalence relations \(E_1\subseteq E_2\). There are no other nonlogical symbols and no counting quantifiers. Use the ordinary guarded fragment \(\mathrm{GF}\).

Write \(\mathcal A=\{0,1,2\}^{c}\setminus\{\mathbf0\}\) and \(\mathcal B=\{0,1,2\}^{\mathcal A}\setminus\{\mathbf0\}\). An \(E_1\)-class has type \(a\in\mathcal A\) when its counts of elements of each unary colour, truncated at two, form \(a\). An \(E_2\)-class has type \(b\in\mathcal B\) when its counts of constituent \(E_1\)-classes of each type \(a\), again truncated at two, form \(b\). Let \(S(M)\subseteq\mathcal B\) be the set of types of \(E_2\)-classes occurring in \(M\), without recording how many \(E_2\)-classes have each type.

**Theorem.** For all nonempty finite or infinite such structures, \(M\equiv_{\mathrm{GF}}N\) if and only if \(S(M)=S(N)\). Each nonempty subset \(S\subseteq\mathcal B\) is the complete \(\mathrm{GF}\)-theory of some finite structure, characterized by a guarded sentence of quantifier rank at most five. Thus every guarded sentence is, over this class, equivalent to a guarded sentence of quantifier rank at most five, and the exact number of complete theories is
\[
2^{\,3^{\,3^c-1}-1}-1.
\]

More precisely, for \(a\in\mathcal A\) put \(w(a)=\sum_{t=1}^{c}a_t\), and for a nonempty \(S\subseteq\mathcal B\) put
\[
\mu(S)=\sum_{b\in S}\sum_{a\in\mathcal A}b_a w(a).
\]
The smallest cardinality of a model with profile set \(S\) is **exactly** \(\mu(S)\). Consequently the sharp, formula-independent upper bound on the size of a smallest model of any satisfiable guarded sentence in the signature is
\[
B_k=c\,3^c\,3^{\,3^c-1}=2^k3^{2^k}3^{3^{2^k}-1}.
\]
For \(k=0\) there are \(255\) theories and \(B_0=27\); for \(k=1\) there are \(2^{6560}-1\) theories and \(B_1=118098\). The distribution of exact minimum canonical-model sizes is encoded by
\[
\prod_{b\in\mathcal B}\left(1+z^{\sum_{a\in\mathcal A}b_a w(a)}\right)-1.
\]

## Assumptions and scope
All domains are nonempty. The predicates \(E_1,E_2\) are genuine reflexive, symmetric and transitive relations, with \(E_1\subseteq E_2\). Atomic unary colours are the \(c\) complete Boolean assignments to the \(k\) unary predicates, including negative literals. Both relations may be equal, and their classes may be infinite. A truncated value \(2\) means at least two, not exactly two. Complete theories mean equivalence classes under agreement on every \(\mathrm{GF}\) sentence over this fixed vocabulary, not complete unrestricted first-order theories.

The hypotheses exclude other binary or higher-arity free predicates, constants, functions, counting operators and unguarded two-variable quantification. These exclusions are essential: unrestricted two-variable logic can compare elements in different \(E_2\)-classes, which the guarded fragment cannot do in this vocabulary.

## Proof
**1. Defining an inner class type.** Let \(C_t(x)\) assert unary colour \(t\). Define guarded formulas
\[
L_t(x):=\exists y\bigl(E_1(x,y)\wedge C_t(y)\bigr),
\]
\[
D_t(x):=\exists y\bigl(E_1(x,y)\wedge C_t(y)\wedge
\exists z(E_1(y,z)\wedge z\ne y\wedge C_t(z))\bigr).
\]
Because \(E_1\) is an equivalence, these say that the \(E_1\)-class of \(x\) has at least one or at least two elements of colour \(t\), respectively. They have quantifier ranks at most one and two. For any \(a\in\mathcal A\), let \(T_a(x)\) be the conjunction, over all \(t\), of \(\neg L_t(x)\) if \(a_t=0\), \(L_t(x)\wedge\neg D_t(x)\) if \(a_t=1\), and \(D_t(x)\) if \(a_t=2\). This is guarded of rank at most two and holds exactly on \(E_1\)-classes of type \(a\).

**2. Defining an outer class type.** For each inner type \(a\), define
\[
P_a(x):=\exists y\bigl(E_2(x,y)\wedge T_a(y)\bigr),
\]
\[
Q_a(x):=\exists y\bigl(E_2(x,y)\wedge T_a(y)\wedge
\exists z(E_2(y,z)\wedge\neg E_1(y,z)\wedge T_a(z))\bigr).
\]
These say that the \(E_2\)-class of \(x\) contains at least one or at least two **distinct** \(E_1\)-classes of type \(a\). All guards are positive atomic occurrences of \(E_1\) or \(E_2\); the negative \(E_1\)-condition is inside an \(E_2\)-guard. The maximum quantifier rank is four. Form the guarded formula \(U_b(x)\), for \(b\in\mathcal B\), by taking \(\neg P_a\), \(P_a\wedge\neg Q_a\), or \(Q_a\) according as \(b_a=0,1,2\). Thus \(U_b(x)\) holds precisely when the containing \(E_2\)-class has type \(b\).

For nonempty \(S\subseteq\mathcal B\), the sentence
\[
\Theta_S:=\bigwedge_{b\in S}\exists x\,U_b(x)
\ \wedge\ \bigwedge_{b\notin S}\neg\exists x\,U_b(x)
\]
is guarded and has quantifier rank at most five. Quantification of a one-free-variable formula can be guarded by \(x=x\). Exactly the models with profile set \(S\) satisfy \(\Theta_S\).

**3. Profile preservation under all guarded formulas.** Consider the family of partial maps between two structures with equal \(S\) whose domains and ranges are nonempty *guarded sets*: either singletons or pairs of elements related by \(E_2\). Require each map to preserve equality, colours and both relations, and require corresponding elements to have matching inner and outer profiles. Include precisely maps satisfying these conditions. The family is nonempty for every guarded subset in either structure.

It has the guarded back-and-forth property. For a move to a singleton or an \(E_2\)-related pair with no remembered elements, equality of the realized outer-profile sets supplies a counterpart: any requested colour is present in a requested inner class, two different elements of one colour require inner multiplicity at least two, and two different inner classes of the same type require outer multiplicity at least two. For a move sharing exactly one existing element, choose the counterpart in the existing \(E_2\)-class and then, as specified by the new pair, either in the same \(E_1\)-class or in a different one. The two capped multiplicities guarantee the needed distinct element or distinct inner class. Moves sharing two elements have no new element to choose because guards have arity at most two. The same constructions work in both directions, even for infinite classes; elements discarded when a guarded move forgets them need not remain distinct from later choices.

The usual induction on guarded formulas now proves invariance under these maps: atomic clauses hold by partial isomorphism; Boolean steps are immediate; and a guarded quantifier chooses a singleton or a guarded pair whose overlap with the current guarded tuple can be matched by the back-and-forth property. Closed sentences hold alike because every guarded tuple has a counterpart. Conversely, \(S(M)\ne S(N)\) is distinguished by one of the sentences \(\exists x\,U_b(x)\). This proves the equivalence criterion and the rank-five collapse.

**4. Canonical sizes and sharpness.** An inner class of type \(a\) has at least \(w(a)\) elements, and it can realize its type with exactly \(w(a)\) elements. Therefore an outer class of type \(b\) has at least \(\sum_a b_aw(a)\) elements, with equality attainable using precisely \(b_a\) inner classes of each type. To realize profile set \(S\), take exactly one such minimum outer class for each \(b\in S\). Distinct outer profiles cannot be satisfied by one outer class, so the resulting size \(\mu(S)\) is minimal. Every nonempty \(S\) is realizable.

The largest \(\mu(S)\) occurs at \(S=\mathcal B\). Its value is
\[
\sum_{b\in\mathcal B}\sum_{a\in\mathcal A}b_aw(a)
=3^{|\mathcal A|}\sum_{a\in\mathcal A}w(a)
=3^{3^c-1}\,c3^c.
\]
The first identity uses \(\sum_{v\in\{0,1,2\}^{\mathcal A}}v_a=3^{|\mathcal A|}\), and the second follows by summing each colour-coordinate over the \(3^c\) vectors. The sentence \(\Theta_{\mathcal B}\) forces this full size, so no smaller universal bound is possible. Independent selection of outer profiles proves the theory count and the size-generating product.

## Verification
A standalone standard-library Python checker constructs unlabelled two-level coloured partitions, computes their capped profiles, and independently evaluates the greatest fixed-point guarded-bisimulation game on all guarded singleton/pair partial isomorphisms. It compared \(1007\) pairs of examples using one colour and at most six elements and \(6328\) pairs using two colours and at most four elements; in every case the bisimulation outcome agreed with equality of profile sets. It also exhaustively checked the sharp-bound summation for one and two colours, and symbolically checked the identities for four colours.

To reproduce, execute \(\texttt{python3 check\_nested.py}\) with Python's standard library from the package directory. Expected final marker: \(\texttt{NESTED\_EQUIVALENCE\_GF\_CHECK\_OK}\). The experiment corroborates the finite game and summation claims; the proof above, not extrapolation from finite cases, covers all sizes and infinite structures.

## Relationship to prior work
Fiuk's 2026 treatment of the guarded fragment with nested equivalence relations motivates the hierarchy. That article studies considerably richer signatures and establishes general decidability and complexity statements for equality-free formulas, with undecidability boundaries for adding equality in richer signatures. It does not provide the present exact classification of the monadic, equality-allowed, two-level signature or its sharp formula-independent minimum canonical-model sizes. The 2025 work of Fiuk, Kieroński and Michielini proves an exponential-model property for the broader unguarded two-variable fragment with nested equivalences but does not give this exact guarded-theory enumeration or sharp per-theory canonical sizes. The 2015 work of Kieroński, Pratt-Hartmann and Tendera studies equivalence closure and guarded two-variable satisfiability in general richer signatures, not this complete enumeration of guarded theories. The classical guarded-bisimulation preservation principle is used rather than claimed as new. Single-equivalence unary multiplicity profiles are the one-level analogue; two nested relations require an additional independent truncated multiplicity layer and give a different complete-theory spectrum.

## Limitations
The sharpness is across all guarded sentences in the fixed signature, allowing large sentences, not a formula-length complexity bound. Rank five is a uniform upper bound, not asserted optimal. The theorem does not extend as stated to extra relations, constants, counting, unguarded \(\mathrm{FO}^2\), three-variable witnesses, or unrestricted first-order logic. The exact profile criterion requires nested genuine equivalences. Historical priority is subject to specialized literature outside the inspected sources; this work does not establish independence from all known logical normal-form theorems.

## References
1. Oskar Fiuk, *The Guarded Fragment with Nested Equivalences*, arXiv:2605.15072v1, first made public 14 May 2026. https://arxiv.org/abs/2605.15072
2. Emanuel Kieroński, Ian Pratt-Hartmann and Lidia Tendera, *Equivalence closure in the two-variable guarded fragment*, *Journal of Logic and Computation* 27 (2017), 999–1021, first published 4 December 2015. https://doi.org/10.1093/logcom/exv075
3. Vince Bárány, Georg Gottlob and Martin Otto, *Querying the Guarded Fragment*, *Logical Methods in Computer Science* 10 (2014), arXiv:1309.5822. https://arxiv.org/abs/1309.5822
4. Oskar Fiuk, Emanuel Kieroński and Vincent Michielini, *Two-Variable Logic for Hierarchically Partitioned and Ordered Data*, KR 2025, pages 316–325, https://doi.org/10.24963/kr.2025/31; preprint arXiv:2512.09508.
