# A four-value obstruction to finite extension preservation in semiring semantics

## Finding

**Theorem (finite capped-counting obstruction).** Let \(S\) be a commutative naturally ordered, zero-sum-free semiring satisfying all three conditions
\[
(\forall s\in S)\;s\preceq s^2,\qquad 1+z=1\Longrightarrow z=0,\qquad (\exists u\in S)\;u^2\ne u.
\]
Then the first-order sentence \(\theta=\exists x\,\forall y\,R(x)\), with one unary relational symbol, is preserved under extensions of finite model-defining \(S\)-interpretations, but agrees with no existential first-order sentence on all such interpretations.

For each integer \(M\ge3\), this applies to the finite capped-counting semiring
\[
S_M=\{0,1,\ldots,M\},\qquad a\oplus b=\min\{M,a+b\},\quad a\odot b=\min\{M,ab\}.
\]
Thus failure already occurs for a **four-element semiring**, and persists at every larger finite cap. For \(M=1,2\), the *specified witness sentence* agrees on all finite interpretations with \(\exists x\,R(x)\). This final statement does not classify all preservation properties of those smaller semirings.

## Assumptions and scope

A semiring is commutative, with \(0\ne1\), and has a partial natural order \(a\preceq b\) defined by \(a+c=b\) for some \(c\). Zero-sum-free means a finite sum can equal zero only when every summand is zero. All domains are finite; the empty domain may also be allowed, where both existential sentences evaluate to zero. An interpretation assigns weights to each ground relational literal and its negation, with exactly one of the pair having weight zero. Equality and inequality have their usual zero/one values. Conjunction and universal quantification use semiring multiplication, and disjunction and existential quantification use semiring addition. Formulae are in negation normal form. Extension means inclusion of domains with unchanged annotations on old ground literals. Existential means \(\Sigma_1\), equivalently a prefix of existential quantifiers followed by a quantifier-free NNF formula, with no semiring-valued constants beyond logical truth and falsity.

Write \(w_a\) for the weight of \(R(a)\), and write \(n\) for domain size. Then
\[
\llbracket\theta\rrbracket=\sum_{a\in A}w_a^n,
\]
where all sums and powers use the given semiring operations. In particular, no combinatorial count over Boolean truth values is being substituted for semiring equality of evaluations.

## Proof

**Extension preservation.** By the hypothesis \(s\preceq s^2\), induction using multiplication monotonicity gives \(s^m\preceq s^{m+1}\) for positive \(m\). If a finite interpretation on \(A\) extends to one on \(B\supseteq A\), each old weight is unchanged and
\[
\sum_{a\in A}w_a^{|A|}\preceq\sum_{a\in A}w_a^{|B|}\preceq\sum_{b\in B}w_b^{|B|}.
\]
This proves preservation, including the empty-domain case.

**Two-domain nondefinability certificate.** For any \(t\in S\setminus\{0\}\), let \(I_t\) have domain \(\{a\}\), positive annotation \(R(a)=t\), and negative annotation \(\neg R(a)=0\). Let \(J_t\) extend \(I_t\) by \(b\), annotated \(R(b)=0\) and \(\neg R(b)=1\). These are model-defining interpretations. Directly,
\[
\llbracket\theta\rrbracket_{I_t}=t,\qquad
\llbracket\theta\rrbracket_{J_t}=t^2.
\]
Suppose an existential sentence \(\varphi\) agreed with \(\theta\) on every finite interpretation. Expand its quantifier-free matrix by distributivity and expand each existential quantifier as a sum over assignments. Every resulting monomial is a product of annotations and Boolean equality factors. The sum of monomials whose existential variables are assigned only \(a\) in \(J_t\) is exactly \(\llbracket\varphi\rrbracket_{I_t}\). The remaining monomials, with at least one variable assigned \(b\), have sum \(\Delta_t\). Consequently
\[
\llbracket\varphi\rrbracket_{J_t}
=\llbracket\varphi\rrbracket_{I_t}+\Delta_t.
\]
For \(t=1\), equivalence to \(\theta\) forces \(1=1+\Delta_1\); by hypothesis \(\Delta_1=0\). Zero-sum-freeness forces every monomial contributing to \(\Delta_1\) to be zero. Every atomic or equality factor in such a monomial, at \(t=1\), is zero or one. Hence a zero monomial has a zero factor. When \(t\) changes from one to the selected \(u\), the only changing literal weight is \(R(a)\); it changes from \(1\) to \(u\), while every factor previously equal to zero stays zero. Therefore every extra monomial remains zero, and \(\Delta_u=0\). The supposed equivalence would imply
\[
 u^2=\llbracket\theta\rrbracket_{J_u}
=\llbracket\varphi\rrbracket_{J_u}
=\llbracket\varphi\rrbracket_{I_u}
=\llbracket\theta\rrbracket_{I_u}=u,
\]
contradicting the selection of \(u\). This argument handles arbitrary numbers of existential variables, arbitrary quantifier-free Boolean combinations in NNF, equality, and repeated literals.

**Finite family and sharpness for this witness.** The saturating map \(h_M:\mathbb N\to S_M\), \(h_M(a)=\min\{M,a\}\), is a semiring homomorphism, proving the semiring laws. Its natural order is the ordinary order; it is zero-sum-free; \(1\oplus z=1\) implies \(z=0\); and \(s\preceq s\odot s\) for all \(s\). For \(M\ge3\), choose \(u=2\); then \(u\odot u=\min(M,4)\ne2\). Conversely, if \(M\in\{1,2\}\), every \(s\in S_M\) has \(s\odot s=s\). Thus every positive power \(s^n\) equals \(s\), proving \(\theta\equiv\exists x\,R(x)\) on all finite nonempty interpretations; for empty domains both sides are zero.

## Verification

Run `python3 checker.py` using Python's standard library. It tests exact semiring associativity, distributivity and commutativity for caps \(1\) through \(7\); exhaustive extension monotonicity for domains of cardinalities \(1\) through \(3\), all possible positive literal weights and all single-element extensions; the two-domain witness; and the claimed collapse for caps \(1,2\). The output is `ALL_CHECKS_OK axioms=1295 extension_pairs=10269 witness_cases=13`. Finite tests do not replace the algebraic proof for unbounded cap or the nondefinability argument over all existential formulae.

## Relationship to prior work

Brinke, Dawar, Grädel and Pago (2026) establish semiring extension-preservation results, including failure on the unbounded natural semiring (their Theorem 5.1 and Lemma 3.1), and positive finite-interpretation results for non-Boolean lattice semirings (Theorem 5.11). They employ the same basic sentence with unbounded powers, but their reported negative case is an **infinite** coefficient semiring, while their positive finite cases use **lattice operations**. The present theorem gives a finite, non-lattice counterexample class; its two-interpretation proof survives saturation of coefficient values. Theorem 5.11 does not imply this statement because capped counting addition is not idempotent. The 2026 compactness paper by Brinke, Dawar, Grädel, Mrkonjić and Naaf treats a different property, not this finite extension-preservation obstruction.

## Limitations

This is an exact statement about model-defining semiring valuations, not Boolean satisfaction or the classical finite extension-preservation theorem. Only the designated witness sentence is shown existentially definable at caps \(1\) and \(2\); no classification of these semirings is claimed. The most relevant accessible full conference manuscript was inspected, but the longer arXiv version was not fully available; an equivalent statement in its omitted proof details or older semiring literature remains a priority risk. No independent verification has been performed.

## References

1. Sophie Brinke, Anuj Dawar, Erich Grädel, Benedikt Pago, *Preservation Theorems in Semiring Semantics*, arXiv:2605.10829 (first posted 2026-05-11); ICALP 2026, LIPIcs 374, article 172. DOI: 10.4230/LIPIcs.ICALP.2026.172. Open full conference HTML: https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.172/LIPIcs.ICALP.2026.172.html.
2. Sophie Brinke, Anuj Dawar, Erich Grädel, Lovro Mrkonjić, Matthias Naaf, *Compactness in Semiring Semantics*, CSL 2026, LIPIcs 363, article 13. DOI: 10.4230/LIPIcs.CSL.2026.13.
