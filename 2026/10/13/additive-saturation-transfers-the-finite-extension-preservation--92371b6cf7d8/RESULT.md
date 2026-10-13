# Additive saturation transfers the finite extension-preservation hierarchy to capped counting semirings

## Finding

**Theorem (saturation transfer and capped-counting application).** Let \(S=(S,+,\cdot,0,1)\) be a commutative, naturally ordered semiring without zero divisors. Suppose there exist an integer \(r\ge1\) and a fixed \(t\ne0\) such that

\[
\underbrace{s+\cdots+s}_{r\text{ summands}}=t\quad\text{for every }s\in S\setminus\{0\}.
\]

For every integer \(n\ge1\), some first-order sentence is preserved under extensions of **finite, nonempty, model-defining \(S\)-interpretations** but is not equivalent on that class to any prenex \(\Sigma_n\) sentence (one starting existentially and having at most \(n\) alternating quantifier blocks). The finite vocabulary may depend on \(n\).

In particular, for every integer \(k\ge2\), the capped counting semiring

\[
S_k=\{0,1,\ldots,k\},\qquad a\oplus b=\min(k,a+b),\qquad a\otimes b=\min(k,ab)
\]

satisfies this conclusion. The three-element semiring \(S_2\) therefore already exhibits failure of finite extension preservation at **every fixed level** of the existential-first quantifier-prefix hierarchy. This semiring is not a lattice semiring, since \(1\oplus1\ne1\).

## Assumptions and scope

The language is finitary first-order logic over a finite relational vocabulary, with equality allowed. Negations occur only on atomic formulas. A model-defining \(S\)-interpretation \(\pi\) on a finite nonempty universe assigns semiring values to each atomic literal and its negation, exactly one of the two values being zero. The associated classical structure \(M_\pi\) satisfies a ground literal exactly when its value is nonzero. Equality and inequality have their usual Boolean valuations.

Formula valuation uses semiring addition for disjunction and existential quantification, and semiring multiplication for conjunction and universal quantification. An extension \(\pi_A\subseteq\pi_B\) has \(A\subseteq B\) and identical values on every literal over \(A\). For preservation we require \(\pi_A\llbracket\psi\rrbracket\le\pi_B\llbracket\psi\rrbracket\) in the natural semiring order. A \(\Sigma_n\) formula is understood in ordinary first-order syntax; numerical semiring parameters are not allowed in the formula language.

The only external mathematical input is the proved finite classical extension-preservation hierarchy of Dawar and Sankaran: for each \(n\) there is a first-order sentence \(\varphi_n\), over a finite relational vocabulary, whose finite classical models are extension closed, but which is not equivalent over finite classical structures to any \(\Sigma_n\) sentence. The witness \(\varphi_n\) is taken in negation normal form without changing its first-order meaning.

## Proof

**1. Boolean support.** Natural order is a partial order, so if \(a+b=0\), then \(a\le0\) and \(0\le a\); hence \(a=0\), and similarly \(b=0\). Thus the semiring is zerosumfree. Together with the no-zero-divisors assumption, the map

\[
h:S\longrightarrow\{0,1\},\qquad h(s)=\begin{cases}0,&s=0,\\1,&s\ne0,\end{cases}
\]

preserves finite addition and multiplication, zero and one. Induction over an arbitrary negation-normal-form first-order formula \(\eta\), including the empty sums/products if necessary, therefore yields on every finite interpretation

\[
h\bigl(\pi\llbracket\eta\rrbracket\bigr)=1\quad\Longleftrightarrow\quad M_\pi\models\eta.
\]

This also covers equality literals, which already have Boolean values.

**2. A saturated first-order sentence.** For each \(n\), let \(\psi_n\) be the disjunction of \(r\) syntactically separate copies of \(\varphi_n\). Finite semiring sums obey the assumed saturation property, hence

\[
\pi\llbracket\psi_n\rrbracket=\begin{cases}t,&M_\pi\models\varphi_n,\\0,&M_\pi\not\models\varphi_n.\end{cases}
\]

The element \(t\) is greatest in the natural order: for every \(s\ne0\), the saturation identity exhibits \(s+u=t\), while \(0+t=t\). If \(\pi_A\subseteq\pi_B\), their classical structures are related by an induced-substructure inclusion. Since the finite models of \(\varphi_n\) are extension closed, the pair of values of \(\psi_n\) is one of \((0,0),(0,t),(t,t)\), all weakly increasing. Therefore \(\psi_n\) is extension preserved on finite \(S\)-interpretations.

**3. No bounded existential-first prefix.** Suppose a prenex \(\Sigma_n\) sentence \(\theta\) were \(S\)-equivalent to \(\psi_n\) on every finite model-defining interpretation. For an arbitrary finite classical structure \(M\), construct its canonical \(S\)-interpretation \(\iota_M\) by assigning \(1\) to each true ground literal and \(0\) to its false complement. By Step 1,

\[
M\models\theta\ \Longleftrightarrow\ \iota_M\llbracket\theta\rrbracket\ne0
\ \Longleftrightarrow\ \iota_M\llbracket\psi_n\rrbracket\ne0
\ \Longleftrightarrow\ M\models\varphi_n.
\]

This is a classical \(\Sigma_n\) definition of the finite models of \(\varphi_n\), contradicting the Dawar–Sankaran hierarchy. Thus no such \(\theta\) exists.

**4. Capped-counting instances.** Addition and multiplication in \(S_k\) are truncations of the corresponding natural-number operations at \(k\). Associativity, distributivity, zero and unit follow from the truncation identities for nonnegative integers; the natural order is the usual chain and a product is zero precisely when a factor is zero. For every nonzero \(s\in S_k\), the \(k\)-fold capped sum equals \(k\). Taking \(r=t=k\) applies Steps 1–3. In particular \(S_2=\{0,1,2\}\) is a three-element non-idempotent instance.

## Verification

The included standalone Python 3 script `aux/verify.py` independently checks the semiring axioms for all elements of \(S_k\) for \(1\le k\le8\), and compares Boolean support with semiring valuation and \(k\)-fold saturation for six nontrivial first-order test formulas, with both quantifiers and negative literals. Its reproducible run reports **2,024 semiring-operation triples, 13,948 model-defining valuations, and 83,688 formula-support/saturation tests**, all passing. The code uses exact integer arithmetic and a fixed seed for larger finite samples. The infinitely many semirings, all formulas and arbitrary finite structures are covered by the proof, not the tests.

Reproduce using `python3 aux/verify.py` after extracting the embedded file with that path.

## Relationship to prior work

Brinke, Dawar, Grädel and Pago (2026) develop extension-preservation theory under semiring semantics, establish its finite validity for non-Boolean lattice semirings and several other important semirings, and give a failure for the infinite natural-number semiring. Their finite positive result includes the three-element min-max lattice semiring. The **different** three-element capped-counting semiring above yields failure, separating equal cardinality from algebraic idempotence in this preservation setting. The inspected version does not assert the capped-counting family or its all-prefix failure.

Dawar and Sankaran (2020) prove the classical finite, unbounded quantifier-prefix obstruction used as a premise here. That theorem alone does not imply semiring extension preservation: the latter compares actual numeric annotation values, not just Boolean truth. The additional saturated-valuation argument of Steps 1–2 supplies the transfer, while Step 3 preserves their nondefinability through Boolean support. Hence this finding is a transfer theorem, not a new classical hierarchy construction or an independent proof of that hierarchy.

## Limitations

The result is confined to finite, nonempty interpretations and to the stated semirings (or those meeting its saturation/no-zero-divisors hypotheses). It does not determine the status for arbitrary finite semirings, fixed-vocabulary uniform witnesses, homomorphism preservation, or infinite-universe interpretations. The deeper classical witness hierarchy is imported from the cited theorem, not reproved here. The small-model computation verifies the algebraic mechanism only and is not an exhaustive check of the universal claim. Older statements of equivalent semiring-support transfer principles could reduce originality; the named primary texts and database searches did not establish such coverage.

## References

1. S. Brinke, A. Dawar, E. Grädel and B. Pago, *Preservation Theorems in Semiring Semantics*, arXiv:2605.10829v1, first public 2026-05-11, Sections 2, 5 and 8. https://arxiv.org/html/2605.10829v1
2. A. Dawar and A. Sankaran, *Extension Preservation in the Finite and Prefix Classes of First Order Logic*, arXiv:2007.05459v2, Sections 3–4 and Theorem 4.1 (first public arXiv version in 2020). https://arxiv.org/html/2007.05459v2
