# Exact near-attainment hulls for a generating operator whose bidual is not generating

## Finding

Let \(\mathbb K\in\{\mathbb R,\mathbb C\}\), and let \(J:\ell_1(\mathbb N;\mathbb K)\to c_0(\mathbb N;\mathbb K)\) be the canonical norm-one inclusion. The generating property of \(J\) is known from Kadets, Martín, Merí and Quero [1, Example 2.4(5)]. The new assertion concerns its second adjoint \(J^{**}:\ell_\infty^*\to\ell_\infty\).

Write every \(\varphi\in\ell_\infty^*\) uniquely as \(\varphi=\varphi_a+\varphi_s\), where \(a\in\ell_1\), \(\varphi_a(x)=\sum_{n\ge1}a_nx_n\), and \(\varphi_s\) annihilates \(c_0\). Let \(Q\varphi=\varphi_s\). For every \(0<\delta<1\) put
\[
A_\delta=\{\varphi\in S_{\ell_\infty^*}:\|J^{**}\varphi\|_\infty>1-\delta\},\qquad C_\delta=\overline{\operatorname{conv}}^{\|\cdot\|}(A_\delta).
\]
Then the following exact identities hold:
\[
\boxed{C_\delta=\{\varphi\in B_{\ell_\infty^*}:\|Q\varphi\|\le\delta\}},\qquad
\boxed{\operatorname{dist}(\varphi,C_\delta)=\max\{0,\|Q\varphi\|-\delta\}\quad(\varphi\in B_{\ell_\infty^*}).}
\]
Consequently
\[
\bigcap_{0<\delta<1}C_\delta=B_{\ell_1}\quad\text{inside }\ell_\infty^*,
\]
and the second adjoint \(J^{**}\) is not \(r\)-generating for **any** \(0<r\le1\), even though \(J\) is generating. In particular this gives a counterexample to the converse of Proposition 2.22 in [1].

## Assumptions and scope

All duals are continuous linear duals over the same field, with the ordinary operator and dual norms. The inclusion \(\ell_1\hookrightarrow\ell_\infty^*\) is the canonical coordinate-functional embedding. Closures in the finding are **norm closures**, not weak-star closures. \(B_Z\) and \(S_Z\) denote the unit ball and sphere of a Banach space \(Z\). A norm-one operator \(G:X\to Y\) is \(r\)-generating, \(0<r\le1\), if for every \(\delta>0\) the norm-closed convex hull of \(\{x\in S_X:\|Gx\|>1-\delta\}\) contains \(rB_X\). This is the definition used in [1, Definition 2.2]; the case \(r=1\) is generating. Restricting \(\delta\) to \((0,1)\) is equivalent for this criterion.

## Proof

**1. Canonical norm-additive splitting.** For \(\varphi\in\ell_\infty^*\), set \(a_n=\varphi(e_n)\). For any finite \(F\subset\mathbb N\), choose scalars \(u_n\) of modulus one with \(a_nu_n=|a_n|\). Evaluating \(\varphi\) on \(\sum_{n\in F}u_ne_n\) shows \(\sum_{n\in F}|a_n|\le\|\varphi\|\), hence \(a\in\ell_1\). Let \(\varphi_a(x)=\sum_n a_nx_n\) and \(\varphi_s=\varphi-\varphi_a\). Since \(\varphi_s(e_n)=0\) for all \(n\), continuity makes \(\varphi_s\) vanish on the closure \(c_0\) of the finitely supported sequences. Uniqueness follows by evaluating on the basis.

The triangle inequality gives \(\|\varphi\|\le\|a\|_1+\|\varphi_s\|\). For \(\varepsilon>0\), choose \(x\in B_{\ell_\infty}\) and multiply it by a modulus-one scalar so that \(\operatorname{Re}\varphi_s(x)>\|\varphi_s\|-\varepsilon\). Choose finite \(F\) with \(\sum_{n\notin F}|a_n|<\varepsilon\). Form \(y\) by replacing \(x_n\) for \(n\in F\) by phases satisfying \(a_ny_n=|a_n|\). Since \(y-x\) is finitely supported, \(\varphi_s(y)=\varphi_s(x)\), while \(\operatorname{Re}\varphi_a(y)\ge\sum_{n\in F}|a_n|-\sum_{n\notin F}|a_n|>\|a\|_1-2\varepsilon\). Thus \(\|\varphi\|\ge\|a\|_1+\|\varphi_s\|-3\varepsilon\). Letting \(\varepsilon\downarrow0\) proves
\[
\boxed{\|\varphi_a+\varphi_s\|=\|a\|_1+\|\varphi_s\|.}
\]
Consequently \(Q\) is a norm-one projection onto the annihilator of \(c_0\), and \(\ell_1\) is its kernel.

**2. Formula for the second adjoint.** For each coordinate unit vector \(e_n\in\ell_1=c_0^*\), \(J^*e_n=e_n\in\ell_\infty\). Hence \((J^{**}\varphi)_n=\varphi(J^*e_n)=a_n\), so \(\|J^{**}\varphi\|_\infty=\|a\|_\infty\).

**3. Sharp norm-closed convex hull.** If \(\varphi\in A_\delta\), then \(\|a\|_1\ge\|a\|_\infty>1-\delta\) and norm additivity gives \(\|Q\varphi\|=1-\|a\|_1<\delta\). Since the unit ball and \(\{\varphi:\|Q\varphi\|\le\delta\}\) are norm-closed convex sets, their intersection contains \(C_\delta\).

Conversely, let \(\varphi=\varphi_a+s\in B_{\ell_\infty^*}\) with \(\sigma=\|s\|<\delta\). Norm additivity gives \(\|a\|_1\le1-\sigma\). For every \(n\) and every modulus-one scalar \(\theta\), the functional \(s+(1-\sigma)\theta e_n\) has norm one and its image under \(J^{**}\) has norm \(1-\sigma>1-\delta\); it therefore belongs to \(A_\delta\). The norm-closed convex hull of \(\{\theta e_n:n\in\mathbb N,\ |\theta|=1\}\) in \(\ell_1\) is exactly \(B_{\ell_1}\). Indeed finite linear combinations approximate the whole ball, and zero is the midpoint of opposite unit vectors. Thus \(s+(1-\sigma)B_{\ell_1}\subset C_\delta\), which contains \(\varphi\). If \(\sigma=\delta\), replace \(s\) by \((1-1/k)s\) and take the norm limit. This proves the first boxed identity, including the boundary case.

**4. Exact distance and generating obstruction.** For \(\varphi=a+s\in B_{\ell_\infty^*}\), the contractivity of \(Q\) and its norm constraint on \(C_\delta\) imply that every \(\psi\in C_\delta\) satisfies \(\|\varphi-\psi\|\ge\max\{0,\|s\|-\delta\}\). Conversely let \(t=1\) if \(\|s\|\le\delta\), and let \(t=\delta/\|s\|\) otherwise. Then \(\psi=a+ts\) has norm at most one, \(\|Q\psi\|\le\delta\), hence \(\psi\in C_\delta\); moreover \(\|\varphi-\psi\|=\max\{0,\|s\|-\delta\}\). This proves the distance identity and, by intersection over \(\delta\), the stated intersection identity.

The class of \((1,1,\ldots)\) in \(\ell_\infty/c_0\) has norm one. Hahn--Banach gives a norm-one functional \(s\in\ell_\infty^*\) vanishing on \(c_0\). For each \(0<r\le1\), choose \(0<\delta<r\). Then \(rs\in rB_{\ell_\infty^*}\) but \(\operatorname{dist}(rs,C_\delta)=r-\delta>0\), so \(J^{**}\) is not \(r\)-generating. By [1, Example 2.4(5)], \(J\) is generating; alternatively its norm-attaining set contains all unimodular basis vectors whose norm-closed convex hull is \(B_{\ell_1}\). The proof is complete.

## Verification

The argument independently derives every needed property of the atomic/singular splitting; no finitely additive measure representation theorem is used as an unproved lemma. The formula for \(J^{**}\) is checked coordinatewise against the canonical dual pairings. The inclusion \(C_\delta\subseteq\{\|Q\varphi\|\le\delta\}\) follows from norm additivity; the converse is obtained by convex combinations of explicit unit near-attainers, with a separate norm-limit argument at equality. The exact distance is verified by the contractive quotient projection lower bound and an attaining scaled-singular-part witness. No finite computation or automated search is being treated as an infinite proof.

## Relationship to prior work

[1, Example 2.4(5)] already establishes that \(J:\ell_1\to c_0\) is generating; that statement is used strictly as prior input, not claimed as new. [1, Proposition 2.22] proves the one-way implication that an \(r\)-generating second adjoint forces its original operator to be \(r\)-generating, and expressly leaves the converse open. Its Example 2.23 concerns a **different** diagonal \(c_0\to c_0\) operator whose second adjoint is generating; it does not imply the identities here. The exact norm-closed near-attainment hull and failure for **every** positive generating radius are additional assertions not supplied by those statements. The journal version [2, Proposition 6 and Example 2] retains the same asymmetry and question. Existing broader Banach-space duality results may furnish alternative proofs of individual splitting steps, but none identified in the inspected literature implies the complete asserted hull identity.

## Limitations

The statement is for the canonical inclusion of countable \(\ell_1\) into \(c_0\), over real or complex scalars; it does not classify all generating operators or their adjoints. The closed-convex-hull topology is the Banach norm topology. The formula is proved only for \(0<\delta<1\), which suffices for every positive \(r\)-generating question. Originality is relative to the inspected primary literature and indexed published records; equivalent unindexed observations remain a possible prior-art risk. No independent review or external certification has been performed.

## References

[1] V. Kadets, M. Martín, J. Merí, and A. Quero, *Generating operators between Banach spaces*, arXiv:2306.02645v1, first publicly posted 2023-06-05, in particular Example 2.4(5), Proposition 2.22 and Example 2.23. https://arxiv.org/abs/2306.02645

[2] V. Kadets, M. Martín, J. Merí, and A. Quero, *Generating operators between Banach spaces*, Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas **118**, article 90 (2024), DOI:10.1007/s13398-024-01582-3, published 2024-04-13; see Proposition 6 and Example 2. https://doi.org/10.1007/s13398-024-01582-3
