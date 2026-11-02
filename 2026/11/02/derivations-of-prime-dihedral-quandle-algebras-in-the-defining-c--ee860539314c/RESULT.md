# Derivations of prime dihedral quandle algebras in the defining characteristic

## Finding

Let \(p\) be any odd prime, \(k\) any field of characteristic \(p\), and \(A=k[R_p]\) the \(p\)-dimensional dihedral quandle algebra with basis \(e_i\), indexed by \(i\in\mathbb F_p\), and product \(e_i\star e_j=e_{2j-i}\). Put
\[
o=\operatorname{ord}_p(2),\quad L=\operatorname{lcm}(2,o),\quad d=(p-1)/L.
\]
There is a linear identification of \(A\) with the truncated polynomial vector space \(B=k[u]/(u^p)\) under which the quandle product is \(F\star G=F(-u)G(2u)\), using ordinary multiplication on the right.

Define \(U=\operatorname{span}_k\{u^{1+jL}:0\le j<d\}\subseteq B\). **Every** \(k\)-linear derivation of \(A\) is uniquely
\[
D_{a,b}(F)=a(u)F(u)+b(u)F'(u),\qquad a,b\in U.
\]
These derivations form a Lie algebra under commutator, with **complete** bracket
\[
[D_{a,b},D_{c,e}]
=D_{\,bc'-ea',\,be'-eb'}.
\]
In particular,
\[
\dim_k\operatorname{Der}(A)=2d=\frac{2(p-1)}{\operatorname{lcm}(2,\operatorname{ord}_p(2))}.
\]
As a Lie algebra it is \(U\rtimes (U\partial_u)\), with \(U\) as an abelian ideal and \(U\partial_u\) acting through differentiation and multiplication. For every finite field \(k=\mathbb F_q\) of characteristic \(p\), the exact number of derivations is \(q^{2d}\).

The dimensions for \(p=3,5,7,11,17,31\) are respectively \(2,2,2,2,4,6\); in particular, the first larger example in this list occurs at \(p=17\).

## Assumptions and scope

The integer \(p\) is any odd prime; no algebraic-closedness or finiteness hypothesis is imposed on \(k\). A derivation means a \(k\)-linear endomorphism satisfying \(D(x\star y)=D(x)\star y+x\star D(y)\). The operation \(\star\) is nonassociative in general; polynomial multiplication and differentiation on \(B\) are **auxiliary**, not substitutes for the quandle product. The derivative descends to \(B\) since \(\operatorname{char}k=p\) and \((u^p)'=0\).

The first-public-source anchor is the July 18, 2006 preprint by Carter, Crans, Elhamdadi and Saito on linearized self-distributive structures; this is **not** a claimed date for the present derivation theorem.

## Proof

**1. Polynomial transport.** The truncated exponential \(E(t)=\sum_{r=0}^{p-1}t^r/r!\) is defined in \(B\), since each factorial below \(p\) is invertible. Map \(e_i\mapsto E(iu)\). The coefficients of \(E(iu)\), for \(i=0,\ldots,p-1\), form a Vandermonde matrix with its columns scaled by invertible factorials, hence a basis. Truncated exponentials multiply by addition of their arguments; therefore
\[
E(iu)\star E(ju)=E((2j-i)u)=E(-iu)E(2ju).
\]
Bilinearity proves the stated product \(F\star G=F(-u)G(2u)\) for all \(F,G\in B\).

**2. Eigen-space constraints from two generators.** Let \(D\) be a derivation. Write \(a=D(1)\); here \(1\) is the constant polynomial, not a two-sided unit for \(\star\). The identity \(1\star1=1\) gives
\[
a(u)=a(-u)+a(2u).
\]
For a coefficient of degree \(j\), this reads \((1-(-1)^j-2^j)a_j=0\). The degree-zero coefficient vanishes because \(p\) is odd; even positive degrees vanish because \(2^j\ne0\); odd degrees survive exactly when \(2^{j-1}=1\pmod p\). Hence \(a\in U\), and in particular \(a(-u)=-a(u)\), \(a(2u)=2a(u)\).

Write \(D(u)=ua+b\). Applying the Leibniz identity first to \(1\star u=2u\), then to \(u\star1=-u\), and using these identities for \(a\), gives
\[
b(2u)=2b(u),\qquad b(-u)=-b(u).
\]
The coefficient conditions imply \(b\in U\) by the same parity/order argument.

**3. Sufficiency and uniqueness.** For any \(a,b\in U\), the operator \(D_{a,b}=a+b\partial_u\) satisfies the Leibniz identity because
\[
\begin{aligned}
D_{a,b}(F(-u)G(2u))
&=aFG+b\bigl(-F'(-u)G(2u)+2F(-u)G'(2u)\bigr),
\end{aligned}
\]
where \(FG\) denotes \(F(-u)G(2u)\); this is exactly \(D_{a,b}(F)\star G+F\star D_{a,b}(G)\) after substituting \(a(-u)=-a(u)\), \(a(2u)=2a(u)\), and the corresponding equations for \(b\). It also has \(D_{a,b}(1)=a\) and \(D_{a,b}(u)=ua+b\).

Thus \(D-D_{a,b}\) is a derivation vanishing on \(1\) and \(u\). These generate the **nonassociative** algebra because \(u\star u^{r}=-2^r u^{r+1}\) for \(1\le r<p-1\), with invertible scalars. Induction yields \(D=D_{a,b}\) on every monomial. The parameters are uniquely recovered from \(D(1)\) and \(D(u)\).

**4. Lie structure and counts.** The ordinary commutator of two first-order operators \(a+b\partial_u\) and \(c+e\partial_u\) equals
\[
(bc'-ea')+(be'-eb')\partial_u.
\]
The exponents of \(a,b,c,e\) are congruent to \(1\pmod L\). Every product of one such polynomial with the derivative of another again has exponents congruent to \(1\pmod L\), or vanishes in \(B\). Thus both displayed coefficients belong to \(U\), proving closure and the bracket identity. Counting basis exponents \(1,1+L,\ldots,1+(d-1)L\) gives \(\dim U=d\) and \(\dim\operatorname{Der}(A)=2d\). Over \(\mathbb F_q\), a vector space of dimension \(2d\) has exactly \(q^{2d}\) elements.

## Verification

The complete standard-Python program `verify.py` independently forms the Leibniz linear system in the **original** quandle basis, and computes its nullity for \(p=3,5,7,11,17\). The nullities are \(2,2,2,2,4\), agreeing with the theorem. For all of \(p=3,5,7,11,17,31\), it also verifies every predicted basis derivation on **every ordered pair** of polynomial monomials and checks all pairwise basis Lie-bracket identities. The polynomial checks for \(p=31\) do not independently establish exhaustive classification; the algebraic uniqueness proof does so for every prime. Run `python3 verify.py` using only the standard library. The terminal marker is `MODULAR_QUANDLE_DERIVATION_OK`.

## Relationship to prior work

Carter–Crans–Elhamdadi–Saito (2006) established vector-space linearizations of quandle self-distributivity. Elhamdadi–MacQuarrie–Restrepo (2010) determined automorphisms of the **underlying dihedral quandle**, which do not determine the derivations of its linearization. Bardakov–Passi–Singh (2017) initiated the systematic study of quandle rings and their ideals.

Elhamdadi–Makhlouf–Silvestrov–Zappala (2021), the closest direct antecedent, defined quandle-algebra derivations and classified dihedral derivations **in characteristic zero** (Theorem 3.9), with positive-characteristic tables for orders \(3\) through \(6\) (Section 4.2). Their small matching-characteristic cases \(p=3,5\) are **known instances**, not claimed independently. The result here is the unrestricted defining-characteristic prime family, the exact multiplicative-order dependence, and the full first-order-operator Lie bracket.

Sangare–Ta (2026) treated quandle-algebra automorphisms and commutators; Proposition 4.6 is an integral odd-order result, while Theorem 4.13 expresses automorphisms at **even** order in terms of those at odd order. Neither states the defining-characteristic derivation formula. Zhang (2026) provides group-ring descriptions of Alexander-quandle augmentation structures, not their derivation Lie algebra. The auxiliary group-ring transport itself is not presented as a unique new concept.

An earlier computation of the modular idempotent locus of \(k[R_p]\) describes the same algebra but classifies solutions of \(x\star x=x\). It does not imply a classification of Leibniz derivations or their Lie brackets. The coincidence of the integer \(d\) in the two problems follows from the same scalar-substitution eigenvalues; it is not a claim that the geometric questions are interchangeable.

## Limitations

The classification requires prime quandle order equal to the coefficient characteristic and does not extend as stated to composite quandle orders, different characteristics, or arbitrary Alexander quandles. It concerns linear derivations only, not the full automorphism group scheme, its smoothness, inner derivations, or deformation cohomology. Finite checks serve as corroboration, not a substitute for the uniform proof. The inspected literature does not establish global publication priority: especially relevant unindexed or newer treatments could contain equivalent statements. Independent mathematical audit has not been performed.

## References

1. J. S. Carter, A. Crans, M. Elhamdadi, M. Saito, *Cohomology of Categorical Self-Distributivity* (first public preprint 2006-07-18), arXiv:math/0607417.
2. M. Elhamdadi, J. MacQuarrie, R. Restrepo, *Automorphism groups of Quandles* (first public preprint 2010-12-23), arXiv:1012.5291.
3. V. G. Bardakov, I. B. S. Passi, M. Singh, *Quandle rings* (2017), arXiv:1709.03069.
4. M. Elhamdadi, A. Makhlouf, S. Silvestrov, E. Zappala, *The derivation problem for quandle algebras* (2021), arXiv:2106.08289, Theorem 3.9 and Section 4.2.
5. B. Sangare, L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras* (2026), arXiv:2608.01550, Proposition 4.6 and Theorem 4.13.
6. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings* (2026), arXiv:2610.08204.
