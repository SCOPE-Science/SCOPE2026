# Two-variable reconstruction of finite divisor lattices

## Finding

For every pair of positive integers \(N,M\), let \(D(N)\) be the finite relational structure whose domain is the set of positive divisors of \(N\), with equality and the single reflexive binary relation \(a\preccurlyeq b\) meaning \(a\mid b\). If \(E(N)\) denotes the multiset of positive exponents in the prime factorization of \(N\) (the empty multiset for \(N=1\)), then
\[
D(N)\equiv_{\mathrm{FO}^{2}}D(M)
\quad\Longleftrightarrow\quad
E(N)=E(M)
\quad\Longleftrightarrow\quad
D(N)\cong D(M).
\]
The logic is ordinary first-order logic with at most two reusable variable symbols, no counting quantifiers and **unrestricted quantifier rank**. The conclusion holds for arbitrary numbers of distinct prime factors and arbitrary positive exponents. Moreover, one-variable first-order logic cannot distinguish any two members of this nonempty family, so width two is sharp.

This is relative identification **within the family of divisor lattices**; it does not say that an individual divisor lattice is identified by two-variable logic among all finite partially ordered sets.

## Assumptions and scope

Write \(N=\prod_{i=1}^{r}p_i^{e_i}\), with distinct primes and positive integer exponents, and \(S=\sum_{i=1}^{r}e_i\). Mapping a divisor to its exponent vector yields the order isomorphism
\[
D(N)\cong P(e_1,\ldots,e_r)
:=\prod_{i=1}^{r}\{0,1,\ldots,e_i\},
\]
with coordinatewise order. The case \(r=0\) is the one-element lattice. Every vector \(z\) has a well-defined rank \(\rho(z)=\sum_i z_i\), and the top element has rank \(S\). The only relation symbol used in the logical formulas is \(\preccurlyeq\), plus equality.

## Proof

**1. Rank is definable using two variables.** Write \(u\prec v\) for \(u\preccurlyeq v\land u\ne v\). For either choice of free variable symbol \(z\in\{x,y\}\), define \(H_0(z):=\top\), and recursively
\[
H_{j+1}(z):=\exists w\,(w\prec z\land H_j(w)),
\]
where \(w\) is the other symbol and the recursive occurrence is alpha-renamed as needed. The definition uses no third variable: each nested quantifier is allowed to shadow a previously bound variable. The product is graded, with a chain of exactly \(\rho(z)\) strict steps below any vector \(z\), so \(H_j(z)\) holds exactly if \(\rho(z)\ge j\). Consequently
\[
\operatorname{Rank}_j(z):=H_j(z)\land\neg H_{j+1}(z)
\]
is a unary \(\mathrm{FO}^{2}\) formula defining exactly rank \(j\). The sentence \(\exists z H_S(z)\land\neg\exists z H_{S+1}(z)\) characterizes the maximum rank \(S\) within the family. Hence equivalent structures have the same \(S\).

**2. Each atom reveals its factor length.** An atom is simply a vector of rank one and is defined by \(\operatorname{Rank}_1(z)\). Suppose \(r\ge2\). The atoms are the coordinate unit vectors \(a_i\). A vector \(v\) is incomparable with \(a_i\) if and only if \(v_i=0\) and at least one other coordinate is positive. Therefore
\[
\max\{\rho(v):v\parallel a_i\}=\sum_{j\ne i}e_j=S-e_i.
\]
The maximum is attained by the vector that is zero in coordinate \(i\) and maximal in every other coordinate. Incomparability is the two-variable atomic combination
\[
\operatorname{Inc}(z,w):=\neg(z\preccurlyeq w)\land\neg(w\preccurlyeq z).
\]
For each \(1\le e<S\), let \(\operatorname{Atom}_{S,e}(z)\) be the unary two-variable formula
\[
\operatorname{Rank}_1(z)\land
\exists w\bigl(\operatorname{Inc}(z,w)\land\operatorname{Rank}_{S-e}(w)\bigr)
\land\neg\exists w\bigl(\operatorname{Inc}(z,w)\land H_{S-e+1}(w)\bigr).
\]
By the displayed maximum identity, this formula selects precisely the atoms belonging to coordinates with exponent \(e\), and no others. Each occurrence of a rank formula is expanded using only the same two symbols; bound-variable shadowing inside that occurrence does not capture occurrences in sibling conjuncts.

**3. The multiplicity of every factor length is definable by a threshold.** Let \(m_e=\#\{i:e_i=e\}\). For every integer \(0\le k\le S\), consider the \(\mathrm{FO}^{2}\) sentence
\[
\Psi_{S,e,k}:=
\exists z\Bigl(\operatorname{Rank}_k(z)\land
\forall w\bigl(\operatorname{Atom}_{S,e}(w)\rightarrow w\preccurlyeq z\bigr)\Bigr).
\]
An element above all \(m_e\) relevant atoms must have value at least one in each of their distinct coordinates and so has rank at least \(m_e\). Conversely, the vector that has one in exactly those coordinates has rank \(m_e\), and it can be increased one unit at a time to every rank from \(m_e\) through \(S\). Therefore
\[
P(e_1,\ldots,e_r)\models\Psi_{S,e,k}
\quad\Longleftrightarrow\quad k\ge m_e.
\]
Thus the least \(k\) satisfying \(\Psi_{S,e,k}\) recovers the exact multiplicity of exponent \(e\), including zero multiplicity. When \(r\ge2\), every exponent is smaller than \(S\), so the recovered multiplicities for \(1\le e<S\) give the full exponent multiset.

**4. Chains and singleton case.** If \(r=1\), the order is a chain; the sentence \(\forall x\forall y\,(x\preccurlyeq y\lor y\preccurlyeq x)\) distinguishes it from every product with at least two nontrivial factors. Its height \(S\) recovers its unique exponent. If \(S=0\), the structure is a singleton and is distinguished by its height. Consequently \(\mathrm{FO}^{2}\)-equivalence implies equal exponent multisets in every case. The converse follows because equal multisets give coordinate-permutation isomorphisms.

**5. Sharp number of variables.** In the one-variable fragment, the only atomic formulas on a variable \(x\) are \(x=x\) and \(x\preccurlyeq x\), both always true. Every one-variable formula in any nonempty reflexive ordered domain is therefore a truth constant after Boolean operations and quantification, and all members of this family have the same \(\mathrm{FO}^{1}\) theory.

## Verification

The bounded checker `verify_divisor_fo2.py` tests the rank and incomparable-atom fingerprint identities, the multiplicity-recovery minimum, and a noncounting unary modal color-refinement witness for logical distinctions. It ran successfully for 102 different positive exponent multisets with total exponent at most ten and divisor-lattice size at most 120; a 57-structure subset yielded pairwise distinct stable modal spectra. A separate direct two-variable syntax generator and finite-model evaluator, `check_fo2_formulas.py`, confirms that the constructed formulas use only the symbols `x` and `y` and distinguish the stated exponent-presence and multiplicity pairs. Run each program with Python 3 and compare against `verification_output.txt` and `formula_output.txt`. All checks are **finite corroboration**; the proof above establishes the unbounded assertions.

A nontrivial example is the pair of exponent vectors \((5,1,1,1)\) and \((3,3,2)\). Both associated lattices have 48 elements and maximum rank eight, but \(\exists z\,\operatorname{Atom}_{8,5}(z)\) distinguishes them. To see why multiplicities matter even with the same exponent support and total height, compare \((1,1,2,2,3)\) and \((1,2,3,3)\), both of total rank nine and exponent support \(\{1,2,3\}\); \(\Psi_{9,1,1}\) is false in the first and true in the second.

## Relationship to prior work

Kiefer, Schweitzer and Selman's 2015 study classifies finite relational structures identified by **two-variable logic with counting** and works with a stronger logic and an identification question over all structures. Its conclusions do not imply that counting-free \(\mathrm{FO}^{2}\) reconstructs exponent multiplicities in arbitrary products of chains. Zeume and Harwath's 2016 work treats decidability and order invariance of two-variable logic on structures with named linear orders and successor. Marzec and Tendera's later work treats satisfiability of restricted two-variable fragments with a partial order and incomparable witnesses. Their examined statements do not provide the displayed divisor-lattice reconstruction.

The classical equivalence between divisibility lattices and products of chains is standard; the claim is exclusively about reconstruction by **pure-order, counting-free two-variable sentences**. Exact historical priority remains subject to further literature review.

## Limitations

The statement is a relative equivalence theorem within finite divisor lattices, not an identification theorem among all finite posets. The formulas can have quantifier rank growing with total prime exponent; no uniform bounded-rank classification or efficient shortest formula is claimed. The result does not recover prime labels or numerical values of the integers: for example, prime powers with the same exponent have isomorphic divisor lattices. Independent external validation has not been performed. General finite lattices need not have the rigidity property: the height-two lattices with three versus four atoms, for example, cannot be distinguished in counting-free two-variable logic.

## References

1. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1, first submitted 2015-03-30; see especially Sections 1–2 and 5. https://arxiv.org/html/1503.08792v1
2. T. Zeume and F. Harwath, *Order-Invariance of Two-Variable Logic is Decidable*, arXiv:1604.05843, first submitted 2016-04-20; see Sections 1–2 and the overview of results. https://arxiv.org/abs/1604.05843
3. D. Marzec and L. Tendera, *On two-variable first-order logic with a partial order*, Journal of Logic and Computation 36 (2026), exaf068, published 2026-01-26; see Sections 1, 3 and 4. https://doi.org/10.1093/logcom/exaf068
