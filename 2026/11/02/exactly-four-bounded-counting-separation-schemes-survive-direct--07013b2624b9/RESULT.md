# Exactly four bounded-counting Separation schemes survive direct powers

## Finding

Let \(M\) be any set-sized first-order model of \(\mathsf{ZFC}\), and let \(I\) be any set with at least two elements. Give the ordinary direct power \(P=M^I\) coordinatewise membership and coordinatewise equality. For each integer \(j\ge1\), let \(E_j(x)\) assert that \(x\) has at least \(j\) pairwise distinct members. Consider **every** unary formula \(\theta(x)\) that is a finite Boolean combination of the \(E_j(x)\). Then the ordinary Separation sentence
\[
\operatorname{Sep}(\theta):\quad
\forall a\,\exists b\,\forall x\bigl(x\in b\leftrightarrow (x\in a\land\theta(x))\bigr)
\]
is true in \(P\) if and only if \(\theta\), as a finite-cardinality test, is equivalent to one of precisely four possibilities:
\[
\bot,\qquad\top,\qquad E_1(x),\qquad E_1(x)\land\neg E_2(x).
\]

Every other such formula has a Separation counterexample with a parent \(a\) having **exactly four members in the direct power**. No parent having fewer than four members can witness failure, even for a formula outside this counting fragment. The four formulas and this sharp obstruction size are independent of the chosen \(M\) and \(I\).

## Assumptions and scope

A set-sized model \(M\models\mathsf{ZFC}\) is fixed; it need not be transitive or externally well-founded. The index set \(I\) is arbitrary with \(|I|\ge2\), and the external metatheory includes the ordinary axiom of choice. We use ordinary two-valued direct-product semantics: \(f\in^P g\) iff \(M\models f_i\in g_i\) for every coordinate \(i\), with equality of tuples. Only standard finite integers are used in the counting formulas. The Boolean combinations are finite; no parity, infinitary disjunction, modulo-counting operator, or internal definition of cardinal arithmetic is assumed. If there is no set-sized model of \(\mathsf{ZFC}\), the theorem is conditional on the explicitly stated existence of \(M\).

Let \(E_j(x)\) be the first-order formula
\[
\exists z_1\cdots\exists z_j\left(\bigwedge_{r=1}^j z_r\in x\ \land\ \bigwedge_{1\le r<s\le j} z_r\ne z_s\right).
\]
A Boolean combination of these is equivalently a unary pure-equality cardinality condition on the membership fiber of \(x\). For some cutoff \(d\ge2\), its truth value is determined by \(\min(t,d)\), where \(t\) is the number of members of \(x\), with all cardinalities at least \(d\) given the same value. The cutoff may always be enlarged without changing the formula.

## Proof

**1. Membership fibers are boxes.** For \(a=(a_i)_{i\in I}\), put \(A_i=\{u\in M:M\models u\in a_i\}\). The members of \(a\) in \(P\) are exactly \(\prod_{i\in I}A_i\). In particular, two independently varying finite coordinate fibers and singleton fibers elsewhere produce exactly the ordinary product of the two finite sizes. Every membership fiber of a candidate separator \(b\) is also a box. Consequently, the selected members of \(a\) must be rectangular. In a \(2\times2\) box, selecting the corners \((u,v)\) and \((u',v')\) but not \((u,v')\) precludes any separator.

**2. Necessity reduces to a multiplicative Boolean function.** Fix a cutoff \(d\ge2\). Write \(F(n)\in\{0,1\}\) for the value of \(\theta\) on an element having exactly \(n\) members; \(F\) is eventually constant. Every standard finite cardinality occurs as the number of members of some element of \(M\), because \(M\models\mathsf{ZFC}\). Restrict to two varying coordinates, padding other coordinates with sets having exactly one member. The relation on nonnegative integers
\[
R(a,b)\quad\Longleftrightarrow\quad F(ab)=1
\]
must have rectangular support if Separation holds: otherwise two accepted finite-cardinality pairs and a rejected mixed pair give a finite parent with no separator. A nonempty symmetric rectangular relation on \(\mathbb N_0^2\) is \(A\times A\) for some nonempty \(A\subseteq\mathbb N_0\). Thus \(F(ab)=G(a)G(b)\) for the indicator \(G\) of \(A\). Since every \(n\) equals \(n\cdot1\), nonemptiness forces \(G(1)=1\), whence \(G(n)=F(n)\) and
\[
F(ab)=F(a)F(b)\qquad(a,b\ge0).
\]
If \(R\) is empty, \(F\) vanishes identically, giving \(\bot\).

Suppose now that \(F\) is nonzero. Then \(F(1)=1\). If \(F(0)=1\), applying the multiplicative identity to \(0\cdot n\) gives \(F(n)=1\) for every \(n\), yielding \(\top\). Otherwise \(F(0)=0\). Let \(c\) be the eventual constant value of \(F\). If \(c=0\), no \(n\ge2\) can have \(F(n)=1\), since the arbitrarily large powers of \(n\) would all have value one; hence \(F\) is the indicator of \(\{1\}\). If \(c=1\), no \(n\ge1\) can have \(F(n)=0\), since its arbitrarily large positive multiples would all have value zero; hence \(F\) is the indicator of the positive integers. These are the remaining two formulas.

**3. Sufficiency for every nontrivial direct power.** False and true are separated by the empty subset and the original parent. For \(E_1(x)\), a tuple \(x\) has a member if and only if every coordinate \(x_i\) has a member (using choice in the external metatheory). Given parent \(a\), use Separation inside \(M\) to form at coordinate \(i\) the subset of the members of \(a_i\) that are nonempty. Their product is exactly the set of selected parent members. Likewise, a tuple has exactly one member iff every coordinate has exactly one member. Coordinatewise separation in \(M\) by the property of being a singleton produces a separator in \(P\). Extensionality inside \(M\) makes these subsets unique, so their coordinates form a function on any set \(I\) by external Replacement.

**4. Four is the optimal obstruction size.** For any other bounded-counting test, the preceding necessity proof shows that \(R\) is not a rectangle. Thus there exist nonnegative integers \(a,b,c,d\) with \(F(ab)=F(cd)=1\) and \(F(ad)=0\). Such a choice necessarily has \(a\ne c\) and \(b\ne d\). Pick sets of those four respective finite sizes inside \(M\). Let the first two parent coordinates each contain the corresponding two distinct size-representatives and let every additional parent coordinate be a singleton containing a one-element set. The parent has exactly four direct-power members. Its selected subset contains two opposite corners but omits one cross-corner; it is not rectangular, so the Separation instance fails.

For minimality, a parent with at most three members has a membership box with at most three points. Every nonempty finite product with at most three points varies in at most one coordinate. Every subset of such a box is itself a box, and the required finite coordinate subsets exist in \(M\). Thus no formula whatsoever can witness failure on a parent having fewer than four members.

## Verification

The accompanying standalone `checker.py` exhaustively tests every truth table on the cardinality classes \(0,1,\ldots,d-1,\ge d\) for \(2\le d\le8\), using the truncated product \(\min(ab,d)\). It verifies that the only rectangular support tables are the four displayed ones and constructs a \(2\times2\) mixed-corner obstruction for every other table. It checks \(1{,}016\) truth tables, of which \(988\) fail rectangularity, and tests the safe predicates on \(1{,}728\) three-factor configurations. It also checks explicit counterexamples for empty, exactly-two, and at-least-two membership. The command is `python3 checker.py`; the success sentinel is `ALL_CHECKS_OK`. These finite calculations corroborate, rather than establish, the universal statement for arbitrary index sets.

## Relationship to prior work

Jockwich, Venturi, and Yago (arXiv:2610.23219v1, posted 2026-10-16), Section 2, observe that ordinary direct powers of set-theoretic models fail full Separation and prove Separation for positive Horn formulas (Proposition 2.13, using Lemma 2.12). The result here gives an **if-and-only-if** theorem for a separate, natural complete local counting fragment, including a surviving singleton property expressed with negation, and proves an optimal finite obstruction bound. Their broader Boolean-valued alternative is not at issue. The classical Feferman–Vaught theorem analyzes first-order formulas over direct products, but the four-class boundary and sharp four-member witnesses are not stated in the inspected materials. These observations do not establish historical priority against all specialized product-preservation literature.

## Limitations

The classification is restricted to finite Boolean combinations of standard finite membership-count thresholds and ordinary coordinatewise direct powers indexed by a set with at least two elements. It does not classify every possible first-order Separation instance, all formulas with parameters, Boolean-valued models, reduced products, or infinite-language counting operators. Historical priority remains subject to checking further specialized literature; there is no claim of an independent audit.

## References

1. S. Jockwich, G. Venturi, and P. Yago, *Models of Arbitrary Sets*, arXiv:2610.23219v1, 2026-10-16, especially Section 2, Lemma 2.12 and Proposition 2.13. https://arxiv.org/html/2610.23219v1
2. S. Feferman and R. Vaught, *The first order properties of products of algebraic systems*, Fundamenta Mathematicae 47 (1959), 57–103, DOI:10.4064/fm-47-1-57-103.
3. Y. Vourtsanis, *A direct proof of the Feferman–Vaught theorem and other preservation theorems in products*, Journal of Symbolic Logic 56 (1991), 632–636, DOI:10.2307/2274705.
