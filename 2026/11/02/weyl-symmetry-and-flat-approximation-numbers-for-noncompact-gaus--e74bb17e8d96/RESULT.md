# Weyl symmetry and flat approximation numbers for noncompact Gaussian Fock operators

## Finding
Let \(\mathcal F^2\) be the standard complex Bargmann–Fock Hilbert space and let \(T\) be a bounded operator with Gaussian integral kernel
\[
(Tf)(z)=\pi^{-1}\int_{\mathbb C}\exp(\alpha z^2+\beta\overline w^{\,2}+\gamma z\overline w+\eta z+\delta\overline w)f(w)e^{-|w|^2}\,dA(w).
\]
If \(T\) is noncompact, its distance to *every* compact operator is its norm, and all its approximation numbers are flat:
\[
\|T\|_{\mathrm{ess}}=a_n(T)=\|T\|\quad(n\ge1),\qquad
 a_n(T)=\inf_{\mathrm{rank}(F)<n}\|T-F\|.
\]
Moreover, there are nonzero displacements \(u,v\in\mathbb C\) and a unimodular \(c\) such that \(TW_u=cW_vT\), where \((W_uf)(z)=e^{z\overline u-|u|^2/2}f(z-u)\). Conversely, each bounded compact member has approximation numbers tending to zero. The noncompact conclusion includes genuinely nonunitary kernels.

## Assumptions and scope
The five coefficients \(\alpha,\beta,\gamma,\eta,\delta\) are arbitrary complex numbers for which the displayed kernel defines a bounded operator on \(\mathcal F^2\); no invertibility, normality, or unitarity is assumed. The inner product is normalized by \(\pi^{-1}e^{-|z|^2}dA(z)\). The kernel's rank-one case \(\gamma=0\), when bounded, is compact and is therefore outside the asserted noncompact conclusion. The proof invokes the boundedness/compactness classification of Sang and Zhao (2026), whose precise hypotheses are checked below; all remaining steps are proved here.

## Proof
**1. Reduction to a degenerate quadratic form.** Suppose \(T\) is bounded and not compact. Sang–Zhao's Theorems 1.1, 1.2, and 1.4 give \(\gamma\ne0\), \(|\alpha|,|\beta|<1/2\), and, writing
\[
D=1-4|\alpha|^2>0,\qquad N=\overline\beta+\alpha\overline\gamma^{\,2}/D,
\]
the boundedness and failure of compactness imply
\[
|\gamma|^2/D+2|N|=1. \tag{1}
\]
Indeed boundedness means the real quadratic polynomial \(\Theta_\alpha\) in their Eq. (1.1) is bounded above. Consequently its quadratic part is negative semidefinite, equivalent to a non-strict inequality in (1). Strict inequality is equivalent to compactness by their Theorem 1.2. We do not need to assume or solve the separate linear compatibility restriction on \(\eta,\delta\); boundedness already supplies it.

**2. Construct exact displacement covariance.** The normalized coherent states \(k_w(z)=\exp(z\overline w-|w|^2/2)\) span a dense linear subspace. Direct Gaussian integration (or the Fock reproducing property) gives
\[
Tk_w(z)=\exp(\alpha z^2+\beta\overline w^{\,2}+\gamma z\overline w+\eta z+\delta\overline w-|w|^2/2).
\]
For any \(u\in\mathbb C\), \(W_uk_w=\exp((\overline u w-u\overline w)/2)k_{w+u}\). Comparing the coefficients in \(TW_uk_w\) and \(W_vTk_w\) shows that their ratio is constant in \(z,w\) exactly when
\[
\gamma v=u-2\beta\overline u,\qquad
\gamma\overline u=\overline v-2\alpha v. \tag{2}
\]
Substituting \(v=(u-2\beta\overline u)/\gamma\) makes (2) equivalent to \(A\overline u+Bu=0\), with
\[
A=|\gamma|^2-1-4\alpha\beta\overline\gamma/\gamma,
\qquad B=2(\overline\beta+\alpha\overline\gamma/\gamma).
\]
Expansion gives the exact algebraic identity
\[
D(|A|^2-|B|^2)=(|\gamma|^2-D)^2-4|D\overline\beta+\alpha\overline\gamma^{\,2}|^2. \tag{3}
\]
By (1), \(|\gamma|^2-D=-2D|N|\), and \(D\overline\beta+\alpha\overline\gamma^2=DN\). Hence (3) vanishes: \(|A|=|B|\). If both are zero, select any nonzero \(u\). Otherwise choose \(u\ne0\) with \(u/\overline u=-A/B\), possible since the right side has modulus one. Then (2) holds. Also \(v\ne0\), since \(v=0\) would imply \(|2\beta|=1\), contrary to \(|\beta|<1/2\).

For these \(u,v\), comparison of the constant exponents yields
\[
TW_u=cW_vT,\quad
c=\exp\!\left(\beta\overline u^{\,2}+\delta\overline u-|u|^2/2-\alpha v^2+\eta v+|v|^2/2\right). \tag{4}
\]
The identities on coherent states extend to the whole Fock space by density and boundedness. Both Weyl operators are unitary, and \(T\ne0\), so taking operator norms in (4) proves \(|c|=1\). For positive integers \(m\), their collinear Weyl powers have no projective phase and give \(TW_{mu}=c^mW_{mv}T\).

**3. Essential norm and finite-rank approximation.** For every fixed \(f\in\mathcal F^2\), \(W_{mu}f\rightharpoonup0\) as \(m\to\infty\), since matrix coefficients between coherent states decay like \(\exp(-|mu+z-w|^2/2)\); use their totality and uniform boundedness to extend this to all \(f\). Every compact \(K\) therefore satisfies \(KW_{mu}f\to0\) in norm. For a unit \(f\), Eq. (4) yields
\[
\|T-K\|\ge\limsup_{m\to\infty}\|(T-K)W_{mu}f\|\ge\|Tf\|.
\]
Taking the supremum over \(f\) gives \(\|T-K\|\ge\|T\|\) for every compact \(K\); \(K=0\) gives equality. Every finite-rank operator is compact, so its distance from \(T\) is at least \(\|T\|\), with the zero approximant giving equality at every rank cutoff. This proves the asserted formula for all \(n\ge1\).

**4. A nonunitary boundary point.** Set \(\alpha=1/10\), \(\beta=1/5\), \(\gamma=2\sqrt3/5\), \(\eta=\delta=0\). Then \(D=24/25\), \(N=1/4\), and \(|\gamma|^2/D+2|N|=1\), while the linear term vanishes. The source classification guarantees boundedness and noncompactness. The displacements \(u=1\), \(v=\sqrt3/2\) satisfy (2) and give \(c=1\). This operator is not a scalar multiple of a unitary: its coherent-state output norm varies with \(\operatorname{Im}w\), since the source reproducing-kernel calculation has \(\Theta_\alpha(w)=-(\operatorname{Im}w)^2/2\).

## Verification
The standalone script `verification_check.py` evaluates Eq. (3) on reproducible random complex parameters, verifies the exact nonunitary boundary parameters and the displacement coefficient equations, and compares the two Gaussian exponent formulas at sampled complex coherent-state and spatial arguments. These finite checks detect arithmetic errors but do not establish the infinite-dimensional statement, which follows from steps 1–3 and the cited published classification.

## Relationship to prior work
Sang and Zhao (2026) give the five-parameter boundedness and compactness conditions, and analyze Schatten membership in the compact regime. This proof uses those conditions but adds a nonzero Weyl covariance at the boundary and exact distances from every compact operator. Dong and Zhu (2025) determine the compact-versus-unitary dichotomy for a restricted two-parameter canonical family and singular values in its compact regime. Their noncompact family consists only of unitaries, whereas the explicit example above is nonunitary. Standard finite-rank approximation and displacement facts alone do not identify that the degeneracy condition forces exact covariance for all five parameters. Earlier oscillator-semigroup and Gaussian convolution theory may encode similar covariance under different terminology, so no absolute publication-priority conclusion is asserted.

## Limitations
This is a Hilbert-space statement about one complex variable and the exact five-parameter Gaussian kernel. It does not classify approximate numbers for general bounded Fock integral operators, nor approximation numbers of compact Gaussian kernels. It assumes the Sang–Zhao boundedness/compactness theorem; it does not provide a new independent proof of that classification. The novelty comparison is best knowledge, subject to broader oscillator-semigroup literature and independent verification.

## References
1. Y. Sang and L. Zhao, *Boundedness and Compactness of Gaussian Integral Operators between Fock Spaces* (2026), arXiv:2610.28279v1, first posted 2026-10-20, https://arxiv.org/html/2610.28279v1 . Theorems 1.1, 1.2, 1.4 and Section 5.
2. G. Dong and K. Zhu, *Canonical integral operators on the Fock space II* (2025), arXiv:2509.16672v1, https://arxiv.org/abs/2509.16672 . Introduction and Theorems A–B.
3. G. Cao, J. Li, M. Shen, B. D. Wick and L. Yan, *A boundedness criterion for singular integral operators of convolution type on the Fock space* (2020), arXiv:1907.00574, https://arxiv.org/abs/1907.00574 . Contextual restricted convolution family.
