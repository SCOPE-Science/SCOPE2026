# Boundary-coupling invariance and a sharp Gaussian-KL law for a three-dimensional Lanczos inverse compression

## Finding
Consider the real symmetric positive-definite tridiagonal matrix
\[
 A=\begin{pmatrix}\alpha&\beta&0\\\beta&a&c\\0&c&b\end{pmatrix},
 \qquad \alpha>0,\quad \beta>0,\quad b>0,\quad ab>c^2,
 \quad \Delta=b(a-\beta^2/\alpha)-c^2>0.
\]
Let \(C=A^{-1}\), \(R=b^2+c^2\), and let the orthogonal change of coordinates have columns
\[
 q=(1,0,0)^\mathsf T,\qquad
 \widetilde u=(0,b,-c)^\mathsf T/\sqrt R,\qquad
 \widetilde v=(0,c,b)^\mathsf T/\sqrt R.
\]
Write \(C'=Q^\mathsf TCQ\). Define the **boundary-aligned isotropic-bulk compression** \(\widehat C'\) by retaining every entry of \(C'\) except setting its \((2,3)\) and \((3,2)\) entries to zero; set \(\widehat C=Q\widehat C'Q^\mathsf T\). Both covariance matrices are positive definite.

Set
\[
 \delta=\frac{c^2(ab-c^2)}{(b^2+c^2)^2}.
\]
For centered Gaussian laws, the exact *two directed* relative entropies are
\[
 \boxed{D_{\mathrm{KL}}\big(\mathcal N(0,C)\,\|\,\mathcal N(0,\widehat C)\big)=\frac12\log(1+\delta),}
\]
\[
 \boxed{D_{\mathrm{KL}}\big(\mathcal N(0,\widehat C)\,\|\,\mathcal N(0,C)\big)=\delta-\frac12\log(1+\delta).}
\]
In particular, both quantities are **exactly independent** of the resolved curvature \(\alpha\) and the nonzero Lanczos boundary coupling \(\beta\) throughout the positive-definite domain. Both vanish precisely when \(c=0\).

If \(\kappa=\kappa_2(T)\ge1\), where \(T=\begin{psmallmatrix}a&c\\c&b\end{psmallmatrix}\) is the *uncorrected* compressed complement, then the following are sharp over all admissible \(A\) with this \(\kappa\):
\[
 0\le\delta\le\frac{(\kappa-1)^2}{4\kappa},
\]
\[
 \boxed{D_{\mathrm{KL}}\big(\mathcal N(0,C)\,\|\,\mathcal N(0,\widehat C)\big)
 \le\log\frac{\kappa+1}{2\sqrt\kappa},}
\]
\[
 \boxed{D_{\mathrm{KL}}\big(\mathcal N(0,\widehat C)\,\|\,\mathcal N(0,C)\big)
 \le\frac{(\kappa-1)^2}{4\kappa}-\log\frac{\kappa+1}{2\sqrt\kappa}.}
\]
For \(\kappa>1\), equality holds exactly when, upon scaling the eigenvalues of \(T\) to \(1,\kappa\), the squared component of its larger-eigenvalue eigenvector along the **third coordinate** is \(1/(\kappa^2+1)\). A nonzero \(\beta\) satisfying the displayed positivity condition can always be selected. The limiting equality case \(\kappa=1\) has \(T\) scalar and zero discrepancy.

A concrete boundary phenomenon follows. Fix \(\alpha=a=b=1\), \(c=1/2\) and \(\beta^2=3/4-\varepsilon\), with \(0<\varepsilon<3/4\). Then \(\kappa_2(T)=3\), whereas the coupling-corrected Schur matrix
\[
 S=T-\frac{\beta^2}{\alpha}e_1e_1^\mathsf T
 =\begin{pmatrix}1/4+\varepsilon&1/2\\1/2&1\end{pmatrix}
\]
has \(\kappa_2(S)\sim25/(16\varepsilon)\). Despite this divergence, the two Gaussian relative entropies remain exactly \(\frac12\log(28/25)\) and \(3/25-\frac12\log(28/25)\), respectively, for **every** such \(\varepsilon\). Hence the Schur condition number alone can give an arbitrarily pessimistic indication of the actual relative-entropy loss in this aligned minimal-dimensional compression.

## Assumptions and scope
The setting is exact real arithmetic, a three-dimensional positive-definite inverse covariance, a one-vector Lanczos space generated from \(q\), a two-dimensional complement, and the explicitly defined rotation and compression above. The chosen \(\beta>0\) guarantees a nonzero first Lanczos residual. The vector \(\widetilde u\) is the normalized direction of the complement component of \(A^{-1}q\), because the Schur inverse satisfies \(S^{-1}e_1=(b,-c)^\mathsf T/\Delta\). The perpendicular complement has dimension one, so its trace-matched isotropic variance equals its exact diagonal variance. This construction is the minimal-dimensional boundary-aligned specialization motivated by the Krylov-complement covariance model in Fifen, Karambal and Hennig (2026); all conclusions are stated for the explicit operator above and require no assumptions about other implementations.

## Proof
Positive definiteness of \(A\) follows by the Schur criterion from \(\alpha>0\), \(T\succ0\), and \(S=T-(\beta^2/\alpha)e_1e_1^\mathsf T\succ0\). Write \(q\), \(\widetilde u\), \(\widetilde v\) as the columns of \(Q\). Block inversion gives
\[
 C=\begin{pmatrix}
 \alpha^{-1}+\beta^2\alpha^{-2}(S^{-1})_{11}&-\beta\alpha^{-1}e_1^\mathsf TS^{-1}\\
 -\beta\alpha^{-1}S^{-1}e_1&S^{-1}
 \end{pmatrix},\quad
 S^{-1}=\Delta^{-1}\begin{pmatrix}b&-c\\-c&a-\beta^2/\alpha\end{pmatrix}.
\]
Because \(S^{-1}e_1=(b,-c)^\mathsf T/\Delta\), the \((1,3)\) entry of \(C'\) vanishes. Direct multiplication gives
\[
 C'_{23}=-\frac cR,\qquad C'_{33}=\frac bR,
 \qquad (C'^{-1})_{23}=\frac{c(ab-c^2)}R.
\]
The two-dimensional leading principal block of \(\widehat C'\) is that of positive-definite \(C'\), while its final diagonal entry is \(b/R>0\); thus \(\widehat C'\succ0\).

For a matrix whose \((1,3)\) entry vanishes, deleting the two symmetric \((2,3)\) entries changes its determinant by \(C'_{11}(C'_{23})^2\). The top-left entry of \(C\) equals \((ab-c^2)/\det A\), and \(\det C=1/\det A\). Consequently
\[
 \frac{\det\widehat C}{\det C}
 =1+\frac{C'_{11}(C'_{23})^2}{\det C'}
 =1+\frac{c^2(ab-c^2)}{R^2}=1+\delta.
\]
Since \(\widehat C'\) is block diagonal for the partition \(\{1,2\}\cup\{3\}\) and \(C'\) differs only in the \((2,3)\) and \((3,2)\) entries,
\[
 \operatorname{tr}(\widehat C^{-1}C)=3.
\]
The reverse trace is computed without an inverse expansion:
\[
 \operatorname{tr}(C^{-1}\widehat C)-3
 =-2(C'^{-1})_{23}C'_{23}=2\delta.
\]
Inserting these two trace identities and the determinant ratio into the exact centered-Gaussian formula
\[
 D_{\mathrm{KL}}(\mathcal N(0,M)\|\mathcal N(0,N))
 =\tfrac12\big(\operatorname{tr}(N^{-1}M)-3+\log(\det N/\det M)\big)
\]
proves both identities. Strict positivity of \(ab-c^2\) gives \(\delta=0\) exactly when \(c=0\).

For sharp optimization, scale \(T\) so that its eigenvalues are \(1,\kappa\), and put \(p\in[0,1]\) for the squared projection of a larger-eigenvalue eigenvector onto the third coordinate. Then
\[
 b=1+(\kappa-1)p,\quad c^2=(\kappa-1)^2p(1-p),\quad
 ab-c^2=\kappa,\quad R=1+(\kappa^2-1)p.
\]
Therefore
\[
 \delta(p)=\frac{\kappa(\kappa-1)^2p(1-p)}{[1+(\kappa^2-1)p]^2}.
\]
For \(\kappa>1\), differentiating shows its sign is that of \(1-(\kappa^2+1)p\). Hence the unique maximizing \(p\) is \(1/(\kappa^2+1)\), with value \((\kappa-1)^2/(4\kappa)\). Both displayed divergences increase strictly with \(\delta\ge0\), proving the sharp bounds and equality statements. Finally, in the stated example \(\det S=\varepsilon\), \(\operatorname{tr}S=5/4+\varepsilon\), giving \(\kappa_2(S)\sim25/(16\varepsilon)\); direct substitution yields \(\delta=3/25\).

## Verification
The independent finite-arithmetic reproduction script `verify.py` uses direct matrix inverses, determinant-based Gaussian divergences and eigenvalue computations for 4,500 randomly generated positive-definite instances; it also tests six analytic sharp extremizers and four Schur-near-singularity cases. Optional SymPy identities verify symbolically that the determinant ratio is \(1+\delta\), that the reverse trace is \(3+2\delta\), and that the boundary-rotated cross entry vanishes. The actual embedded source script passed 4,513 checks when executed before packaging. These checks corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work
Fifen, Karambal and Hennig (arXiv:2609.10080v1, 9 September 2026) introduce a Lanczos-residual-aligned inverse-covariance approximation and give a condition-number-based isotropic-complement error guarantee, including a coarse Gaussian KL bound in their Theorem 13. Their Schur correction and classical block-inversion identities are not claimed as new here. The result above supplies an exact *three-dimensional, two-direction Gaussian KL law* for the stated boundary-aligned compression, proving independence of boundary coupling and the sharp dependence on the **uncorrected** compressed-complement condition number, including a family where the Schur condition number diverges while both KL losses stay constant. Gaussian KL formulas and standard spectral extremization are used as known ingredients. Zhang et al. (arXiv:2102.05485) discuss more general KL comparisons between multivariate Gaussians, but the accessible abstract does not assert this structured coupling-invariance law. Exact equivalent coverage beyond the inspected primary material remains possible.

## Limitations
This result applies only to the explicitly defined real three-dimensional positive-definite matrix family, a single resolved Lanczos direction, one isotropic bulk direction, and centered Gaussian KL divergences. It says nothing about higher-dimensional bulk structure, finite-precision Lanczos, stochastic trace estimation errors, the posterior interpretation of computational uncertainty, or solver convergence. It does not prove that any independent implementation follows the same compression if its choice of boundary direction differs. No independent audit has been performed.

## References
1. H. Fifen, I. Karambal and P. Hennig, *Stochastic Lanczos Quadrature for Computational Uncertainty in Linear Algebra*, arXiv:2609.10080v1 (first public 2026-09-09), especially the Krylov-complement coupling construction and Theorem 13. https://arxiv.org/abs/2609.10080 ; https://arxiv.org/html/2609.10080
2. Y. Zhang, W. Liu, Z. Chen, J. Wang and K. Li, *On the Properties of Kullback-Leibler Divergence Between Multivariate Gaussian Distributions*, arXiv:2102.05485v1 (2021). https://arxiv.org/abs/2102.05485
3. G. H. Golub and C. F. Van Loan, *Matrix Computations*, 4th ed. (2013), standard block inversion and numerical linear algebra background.
