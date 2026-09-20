# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The key issue is whether compressing a product of Dunford--Pettis operators through a complemented copy of \(L^1(\mathbb T)\) still has a translation-averaging symbol vanishing on Nasseri's strongly independent set. Direct compression alone does not give this, because a factorization
\[
QSTJ=(QS)(TJ)
\]
has its intermediate space in the ambient \(L^1(\lambda)\), not in \(L^1(\mathbb T)\).

The cross-space lemma resolves exactly this point. For positive
\[
A:L^1(\mathbb T)\to L^1(\lambda),\qquad
B:L^1(\lambda)\to L^1(\mathbb T),
\]
first split the intermediate \(L^1(\lambda)\) into atomless and purely atomic bands. The purely atomic contribution factors through \(\ell^1\), hence is representable on \(L^1(\mathbb T)\); its averaged symbol is absolutely continuous and vanishes on the Haar-null set \(P\). On the atomless band there are measure kernels \(\beta_\omega\) for \(A\) and \(\alpha_\omega\) for the restriction of \(B^*\) to \(C(\mathbb T)\). The bilinear form of \(BA\) gives
\[
\sigma(BA)=\int \alpha_\omega*\check\beta_\omega\,d\lambda(\omega).
\]

The atomlessness of both kernels was checked independently. If \(\beta_\omega\) has a measurable atomic graph of positive mass, it defines a positive suboperator \(A_0\le A\). The weighted pushforward of that graph is absolutely continuous with respect to Haar measure, so \(A_0\) is well defined on \(L^1\)-classes. A Rademacher sequence is weakly null in the domain but its image under \(A_0\) has constant positive norm. Since Dunford--Pettis operators form an order ideal among regular operators between the relevant AL-spaces, this contradicts \(A\) being Dunford--Pettis.

For \(\alpha_\omega\), an atomic graph defines \(B_0\le B\). Its pushforward measure \(\eta\) is absolutely continuous with respect to Haar measure. Choosing a Rademacher sequence for the finite atomless measure \(\eta\) and pulling it back along the atomic graph produces a weakly null sequence \(h_n\) in \(L^1(\lambda)\), while \(\|B_0h_n\|_1\) is a fixed positive number. This contradicts the Dunford--Pettis property. The weak-null verification uses the domination
\[
|\tau_*(\phi1_F\lambda)|\le \varepsilon^{-1}\|\phi\|_\infty\eta
\]
for every \(\phi\in L^\infty(\lambda)\).

Nasseri's polar-set lemma therefore applies pointwise to \(\alpha_\omega*\check\beta_\omega\). The extension from positive to arbitrary real and complex operators is legitimate because bounded operators between \(L^1\) spaces are regular in this setting and the Dunford--Pettis operators form an order ideal; the relevant classical lattice result was checked in Kalton--Saab, Theorem 4.8.

With the cross-space lemma, \(\Theta_Z(T)=\sigma(QTJ)|_P\) annihilates every product \(ST\) with \(S,T\in\mathcal D_Z\), hence the whole closed square. For \(J_P\mu=JC_\mu Q\), the identities \(QJ=I\) and \(\sigma(C_\mu)=\mu\) give \(\Theta_ZJ_P\mu=\mu\). Contractivity yields the lower distance bound and \(W=0\) gives equality. Thus the quotient splitting is exact, not merely isomorphic up to constants.

The lower strict inclusion was also checked. Lewis--Stegall gives \(\mathcal G_Z\subseteq\mathcal I_2(Z)\) by inserting a complemented \(\ell^1\). For a Rajchman probability \(\mu\) on \(P\), \((J_P\mu)^2=JC_{\mu^{*2}}Q\) lies in the square. If this operator were representable, its compression would factor through \(\ell^1\), making \(C_{\mu^{*2}}\) representable; Nasseri's convolution criterion would force \(\mu^{*2}\ll m\), contrary to the singularity of the convolution power.

The purely atomic converse is immediate and was checked separately: a finite purely atomic \(L^1\) space is an \(\ell^1\)-space with the Schur property, so all bounded operators are Dunford--Pettis and the identity makes the closed square equal all of \(\mathcal B(Z)\).

## Originality

**PASS, to the best of our knowledge.** Nasseri's arXiv:2609.18348v1 was inspected at the main square theorem, the finite-measure extension, Remark 6.2, and the final questions. It proves the exact square separation on \(L^1(0,1)\), extends only the approximate-identity obstruction to arbitrary finite measure spaces with a nonzero atomless part, explicitly says the complemented-copy argument does not transfer the square theorem because ambient intermediate operators appear, and asks whether exact square-ideal separation extends to every nonseparable finite atomless \(L^1\) space.

After splitting off the purely atomic intermediate band, the kernel representation used on the atomless band was compared with Liu's 1998 presentation of Kalton's theorem for operators from \(L^1(K,\mu)\), with \(K\) compact metric, into an atomless \(L^1(X,\nu)\) space, including the measurable enumeration of atomic parts of the kernel measures. The order-ideal step was checked against Kalton--Saab's theorem on Dunford--Pettis operators in regular-operator lattices. The representable/factor-through-\(\ell^1\) equivalence was checked against the Lewis--Stegall theorem.

Exact and synonymous formulations involving "Dunford--Pettis square ideal", "closed square", "finite atomless L1", "nonseparable L1", "Rajchman", and cross-space atomless kernels were checked. No source was found stating the arbitrary finite-measure exact distance formula, the cross-space polar-product lemma, or the resulting strict chain for every finite measure space with a nonzero atomless part.

The strongest originality evidence is that the current source paper itself isolates precisely this extension as open and identifies the obstacle that the cross-space lemma removes. Residual bibliographic risk remains that older abstract operator-ideal or kernel-disintegration literature may contain an equivalent transference principle under different terminology. No inaccessible paper was identified whose title, abstract, or cited theorem gives concrete evidence of prior coverage.

## Value

**PASS.** The result closes an explicit gap in a very recent operator-ideal theorem and upgrades a separable-model statement to arbitrary finite measure algebras with nonzero atomless part. The extension preserves the strongest feature of the source theorem: an exact distance formula and contractively complemented quotient copy, rather than only properness of the square.

The proof also isolates a reusable mechanism. A Dunford--Pettis factorization through an arbitrary finite-measure \(L^1\) intermediate space has atomless kernels on both sides of the compact-metric model, so the same strongly independent polar set annihilates its translation-averaged symbol. This directly handles the ambient-intermediate-space obstruction that prevents a formal complemented-subspace argument.

The purely atomic converse gives a sharp finite-measure boundary for properness of the closed square.

## Limitations

Only finite measure spaces are covered. The result does not classify higher closed powers of the Dunford--Pettis ideal, ideals strictly between the representable and Dunford--Pettis ideals, or the corresponding situation for infinite/localizable measure spaces. It does not establish incompressibility or quantitative multiplication constants for the ambient quotient. The symbol used in the proof is attached to the complemented circle model, not canonically to the full ambient measure algebra.
