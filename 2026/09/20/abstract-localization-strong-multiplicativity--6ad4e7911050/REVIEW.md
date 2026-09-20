# Review: Abstract localization rings do not characterize strong multiplicativity

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The counterexample was checked directly.

Let \(A=k[x]\), \(B=k[x,x^{-1}]\), \(C=\prod_{n\ge1}B\), and \(R=A\times C\). For \(e=(0,1_C)\), the set \(T=\{1,e\}\) is strongly multiplicative and \(R_T\cong Re\cong C\). For \(s=(x,1_C)\) and \(S=\{s^n:n\ge0\}\), one has
\[
\bigcap_{n\ge0}s^nR
=
\left(\bigcap_{n\ge0}x^nk[x]\right)\times C
=0\times C,
\]
which contains no element of \(S\); hence \(S\) is not strongly multiplicative.

On the other hand,
\[
R_S\cong k[x,x^{-1}]\times C=B\times C\cong C\cong Re,
\]
where the middle isomorphism is the coordinate shift of a countable product. All isomorphisms in this last display are unital abstract-ring isomorphisms.

The spectral check is consistent: \(D(S)=D_{k[x]}(x)\sqcup\operatorname{Spec}(C)\) is not clopen, while \(D(e)=\operatorname{Spec}(C)\) is clopen. Therefore no isomorphism \(R_S\cong Re\) compatible with the maps from \(R\) can exist.

The corrected condition was also checked. Strong multiplicativity gives a least element \(t\), the source paper's Lemma 2.5 gives \(t=ue\), and localization universal properties produce an \(R\)-algebra isomorphism \(R_S\cong R_e\cong Re\). Conversely, an \(R\)-algebra isomorphism identifies \(IR_S\) with \(Ie\), after which multiplication by \(e\) commutes with arbitrary intersections and the source paper's intersection criterion yields strong multiplicativity.

No computational verification is required for these identities.

## Adversarial checks

Several possible loopholes were tested.

- The infinite product \(C\) is a unital commutative ring, and \(B\times C\cong C\) is a genuine unital ring isomorphism by coordinate reindexing.
- The multiplicative set \(S\) does not contain zero because its first coordinates are the nonzero polynomials \(x^n\).
- The set \(T\) does not contain zero and is multiplicatively closed because \(e^2=e\).
- The localization formula \((A\times C)_{(x,1)}\cong A_x\times C\) follows directly from the universal property of localization for a finite product.
- The counterexample does not rely merely on choosing the wrong idempotent: the literal condition only asks for the existence of some idempotent summand abstractly isomorphic to \(R_S\), and \(e=(0,1_C)\) supplies one.
- The coordinate-shift isomorphism cannot be an \(R\)-algebra isomorphism, because map compatibility would identify the spectral image with \(D(e)\), whereas \(D(S)\ne D(e)\).

## Originality

The current arXiv:2609.16741v1 structural theorem and its proof were inspected. Theorem 2.6 explicitly states the idempotent condition as \(R_S\cong Re\) "as rings". Its proof of the converse then treats ideal extension as \(I\mapsto Ie\), and its spectral implication identifies \(D(S)\) with \(D(e)\); both steps need compatibility with the canonical map from \(R\).

Searches were made for the source title and identifier together with terms including abstract ring isomorphism, idempotent localization, strong multiplicativity, same localization ring, and map compatibility. No prior correction or equivalent explicit counterexample was located.

The main residual originality risk is conceptual simplicity: localization is intrinsically a ring equipped with a map from the base ring, so an author or reader may have intended the phrase "as rings" to mean the canonical map-compatible identification informally, or may independently notice the same issue. The universal-property repair itself is standard and is not claimed as novel. The superseded single-author predecessor arXiv:2512.23935 was identified, but its earlier full versions were not fully inspected; this leaves a smaller residual risk of prior discussion there.

Originality verdict is therefore only to the best of our knowledge.

## Value

The distinction affects the literal statement of the main structural classification in a recent preprint. The example shows that replacing an \(R\)-algebra localization by its abstract target ring loses exactly the information needed to detect the spectral open subset and ideal-extension operation. The repair is minimal and preserves the intended theorem while preventing a false converse.

## Verdict

Correctness: PASS.  
Originality: PASS, to the best of our knowledge.  
Value: PASS.

Same-model review: passed. Independent audit: not yet performed.
