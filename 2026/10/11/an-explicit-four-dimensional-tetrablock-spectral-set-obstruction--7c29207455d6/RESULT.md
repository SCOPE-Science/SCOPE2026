# An explicit four-dimensional tetrablock spectral-set obstruction with a golden-ratio gap

## Finding
Let \(\Omega=\overline{\mathbb E}\) be the closed tetrablock, where
\[
\mathbb E=\{z\in\mathbb C^3:1-z_1\lambda-z_2\mu+z_3\lambda\mu\ne0\ \text{for all }|\lambda|,|\mu|\le1\}.
\]
Put \(\varphi=(1+\sqrt5)/2\), and let
\[
E_{11}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
E_{22}=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
A_1=\varphi^{-1}E_{11},\ A_2=\varphi^{-1}E_{22},\ A_3=\varphi^{-1}J.
\]
Define commuting \(4\times4\) matrices
\[
T_j=\begin{pmatrix}0_2&A_j\\0_2&0_2\end{pmatrix}\quad(j=1,2,3).
\]
Then \(\Omega\) is a scalar spectral set for \(T=(T_1,T_2,T_3)\), whose joint spectrum is \(\{(0,0,0)\}\). For every real \(\varphi^{-1}<\rho<1\), the following *explicit* \(2\times2\) rational matrix function has no poles on \(\Omega\):
\[
F_\rho(z)=\frac{1}{1-\rho^2z_1z_2}
\begin{pmatrix}
 z_1(1-\rho^2 z_3)&\rho(z_3-z_1z_2)\\
 \rho(z_3-z_1z_2)&z_2(1-\rho^2 z_3)
\end{pmatrix}.
\]
It satisfies the exact norm identities
\[
\sup_{z\in\Omega}\|F_\rho(z)\|=1,\qquad
\|F_\rho(T)\|=\frac{1+\rho}{\varphi}>1.
\]
For example, \(\rho=3/4\) gives \(\|F_{3/4}(T)\|=7/(4\varphi)=(7\sqrt5-7)/8>1\). Thus \(\Omega\) is **not** a complete spectral set for these concrete matrices. The \(\rho\)-threshold is exact for this test family: the displayed norm exceeds one if and only if \(\rho>\varphi^{-1}\). The \(2\times2\) off-diagonal block size is smallest possible among centered equal-block Parrott constructions witnessing non-complete spectrality (the size-one block case is necessarily completely contractive).

## Assumptions and scope
All spaces and matrices are complex, with Hilbert-space operator norms. A compact set \(\Omega\) is a spectral set for a commuting tuple \(T\) when every scalar rational function without a pole on \(\Omega\) satisfies \(\|f(T)\|\le\sup_\Omega|f|\). It is a complete spectral set when the inequality holds with all matrix-valued rational functions, using their operator norms. Matrix functional calculus is applied entrywise, and \(\Omega\) includes its distinguished boundary. The claim of smallest dimension concerns **only** tuples \(T_j=\left(\begin{smallmatrix}0_n&A_j\\0_n&0_n\end{smallmatrix}\right)\) with equal square blocks and center zero; no global minimum over arbitrary commuting triples is claimed.

## Proof
**1. Scalar spectral-set inequality.** All products \(T_iT_j\) vanish, so \(T\) commutes and has joint spectrum \(\{0\}\). The scalar derivative ball at the origin of the tetrablock, computed in [1, Proposition 2.1], is the unit ball of \(X=\ell_1^2\oplus_\infty\mathbb C\): \(\|(a,b,c)\|_X=\max\{|a|+|b|,|c|\}\). Consider the linear map
\[
u(a,b,c)=\varphi^{-1}\begin{pmatrix}a&c\\c&b\end{pmatrix}.
\]
This map has norm exactly one. Indeed, for \(|a|+|b|\le1\) and \(|c|\le1\), convexity reduces its unscaled norm maximum to a matrix with precisely one diagonal entry of modulus one and one off-diagonal entry of modulus one. The two singular-value squares there are \((3\pm\sqrt5)/2\), hence its norm is \(\varphi\). Equality occurs at \((a,b,c)=(1,0,1)\).

For a scalar rational \(f\) with \(\|f\|_{\Omega}\le1\), write \(a=f(0)\). If \(|a|<1\), the disk automorphism \(h=(f-a)/(1-\overline a f)\) has \(h(0)=0\) and \(Dh(0)=Df(0)/(1-|a|^2)\). The derivative-ball bound gives \(\|u(Df(0))\|\le1-|a|^2\). If \(|a|=1\), the maximum-modulus principle makes \(f\) constant. Finally, a block triangular matrix \(\left(\begin{smallmatrix}aI&B\\0&aI\end{smallmatrix}\right)\) is a contraction exactly when \(\|B\|\le1-|a|^2\) (Schur complement). Since
\[
f(T)=\begin{pmatrix}f(0)I_2&u(Df(0))\\0_2&f(0)I_2\end{pmatrix},
\]
we obtain \(\|f(T)\|\le1\) for every normalized scalar rational \(f\). This establishes the spectral-set claim. The cited derivative-ball theorem is independently identifiable as the single non-elementary geometric input; this proof does not infer scalar contractivity from tests of finitely many functions.

**2. Exact rational test and its uniform norm.** Set \(\Delta=z_3-z_1z_2\), \(P(z)=\operatorname{diag}(z_1,z_2)\), and \(S(z)=\operatorname{diag}(z_2,z_1)\). Direct matrix multiplication shows that
\[
F_\rho=P+\rho\Delta J(I_2+\rho S J)^{-1},
\]
which equals the matrix in the Finding. Every \(z\in\Omega\) satisfies \(|z_1|,|z_2|\le1\), so \(|\rho^2z_1z_2|<1\) and the denominator is nonzero on a neighborhood of \(\Omega\).

The distinguished boundary of the tetrablock [1, Section 2; 2] is
\[
b\mathbb E=\{(\omega\overline q,q,\omega):|\omega|=1,\ |q|\le1\}.
\]
At such a point put \(r=|q|\), \(Q=\rho\omega J\), and \(P=\operatorname{diag}(\omega\overline q,q)\). Then \(P^*Q=\rho SJ\) and \(\rho\Delta J=(1-r^2)Q\), giving
\[
F_\rho=P+(1-r^2)Q(I_2+P^*Q)^{-1}.
\]
When \(r>0\), write \(P=rU\) with \(U\) unitary and set \(W=U^*Q\), so \(\|W\|=\rho<1\). Then
\[
U^*F_\rho=(rI_2+W)(I_2+rW)^{-1},
\]
and the defect identity
\[
I_2-(U^*F_\rho)^*(U^*F_\rho)
=(1-r^2)(I_2+rW)^{-*}(I_2-W^*W)(I_2+rW)^{-1}\succeq0
\]
proves contraction. At \(r=0\), \(F_\rho=Q\), so its norm is \(\rho\). At \(r=1\), \(\Delta=0\) and \(F_\rho=P=U\) is unitary. Taking scalar matrix coefficients and using the Shilov-boundary maximum principle proves \(\sup_\Omega\|F_\rho\|=1\) exactly.

**3. Exact amplification.** Since \(F_\rho(0)=0\) and
\[
(\partial_1F_\rho(0),\partial_2F_\rho(0),\partial_3F_\rho(0))
=(E_{11},E_{22},\rho J),
\]
all products \(T_iT_j=0\) reduce the rational calculus to the derivative. Up to a canonical tensor-factor flip, \(F_\rho(T)\) is an upper block nilpotent matrix with single nonzero block
\[
\varphi^{-1}K_\rho,\qquad
K_\rho=E_{11}\otimes E_{11}+E_{22}\otimes E_{22}+\rho J\otimes J.
\]
Relative to the basis \((e_1\otimes e_1,e_1\otimes e_2,e_2\otimes e_1,e_2\otimes e_2)\),
\[
K_\rho=\begin{pmatrix}1&0&0&\rho\\0&0&\rho&0\\0&\rho&0&0\\\rho&0&0&1\end{pmatrix}.
\]
Its four eigenvalues are \(1+\rho,1-\rho,\rho,-\rho\); because \(0<\rho<1\), its operator norm is \(1+\rho\). Consequently \(\|F_\rho(T)\|=(1+\rho)/\varphi\), which exceeds one precisely for \(\rho>\varphi-1=\varphi^{-1}\). The value at \(\rho=3/4\) is an exact algebraic number, not a numerical estimate.

**4. Restricted minimality.** If the common Parrott off-diagonal block size is one, the corresponding map \(u:X\to\mathbb C\) is a bounded scalar functional. Every bounded scalar functional on any operator space is completely bounded with identical norm; in particular, for the minimal cotangent operator space [1, Theorem 2.8], every contractive \(u\) is completely contractive. The derivative characterization [1, Lemma 3.1] then implies that a scalar-spectral-set tuple of this equal-block form is a complete-spectral-set tuple. Thus the present block size two, hence total dimension four, is minimal **within that family**.

## Verification
The block operator, the rational function, and their finite matrix amplifications are specified exactly above; no unstated numerical search is required. The accompanying `verify_tetrablock.py` checks with exact rational arithmetic the multiplication table \(T_iT_j=0\) (up to the common symbolic scale), the four eigenvector identities for \(K_{3/4}\), and the positive polynomial test \((7/4)^2-7/4-1=5/16>0\), which certifies \(7/4>\varphi\). The boundary contraction proof and the scalar spectral-set proof are analytic, not deductions from finite sampling. Run with `python3 verify_tetrablock.py`; no third-party packages are needed.

## Relationship to prior work
Mandal and Ray [1] explicitly compute the tetrablock cotangent operator space and give a general rational interpolant (Theorem 2.6); their Theorem 3.2 and Corollary 3.3 establish the **existence** of a finite-dimensional Parrott spectral-set counterexample, without providing the concrete \(4\times4\) tuple or the present \(2\times2\) rational witness or quantitative golden-ratio threshold. We use their scalar derivative geometry and the analytic interpolation mechanism as prior inputs, and provide the explicit minimal-within-family selection and norm certificate.

Earlier work of Pal [3] gave an infinite-dimensional proposed counterexample using shift-space operators; Ball and Sau [4] subsequently showed that a purported necessary condition used in that line of reasoning was not necessary. Neither work supplies the finite explicit rational witness here. The closed tetrablock distinguished-boundary parametrization [2] is prior geometry. The result does **not** claim discovery of the general failure of rational dilation or originality for the interpolation formula itself.

## Limitations
This is a counterexample for the concrete \(4\times4\) tuple, with a \(2\times2\) rational matrix witness. It is not a global minimum-dimension theorem for arbitrary commuting triples, and it does not determine the entire completely bounded norm of the associated linear map. Exact amplification is proved for the displayed witness family only. The theoretical scalar derivative-ball and Shilov-boundary identifications are taken from the cited primary literature; all remaining inequalities are reconstructed above. An unindexed older explicit equivalent is a residual literature risk, even after targeted source and record comparisons.

## References
[1] Shubhankar Mandal and Samya Kumar Ray, *Failure of Rational Dilation on the Tetrablock via Parrott Homomorphisms*, arXiv:2609.37698v1 (first public 2026-09-29), https://arxiv.org/html/2609.37698v1, especially Proposition 2.1, Theorems 2.6 and 2.8, Lemma 3.1, and Corollary 3.3.

[2] A. A. Abouhajar, M. C. White, and N. J. Young, *A Schwarz lemma for a domain related to \(\mu\)-synthesis*, J. Geom. Anal. 17 (2007), 717–750; corrected arXiv:0708.0637v3, https://arxiv.org/abs/0708.0637v3.

[3] Sourav Pal, *The failure of rational dilation on the tetrablock*, arXiv:1405.4985 (2014), https://arxiv.org/pdf/1405.4985, Section 5.

[4] Joseph A. Ball and Haripada Sau, *Rational dilation of tetrablock contractions revisited*, arXiv:1907.10832v1 (2019), https://arxiv.org/pdf/1907.10832, especially the Introduction and counterexample-to-necessity discussion.
