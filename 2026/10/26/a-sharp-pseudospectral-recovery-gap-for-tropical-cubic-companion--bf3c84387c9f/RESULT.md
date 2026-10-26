# A sharp pseudospectral recovery gap for tropical cubic companion pencils

## Finding

Let \(U>1\), \(e=U^{-1}\), and define the positive-coefficient scalar cubic
\[
Q_U(t)=e+t+et^2+e^2t^3.
\]
It has two distinct tropical roots \(e\) and \(U\). The direct upper-half pencil prescribed by the tropical companion construction at their geometric midpoint is
\[
S_U(t)=\begin{pmatrix}1+et&1&e\\1&-et&0\\0&-e&et\end{pmatrix}=tX_U+Y_U,
\quad X_U=e\operatorname{diag}(1,-1,1),\quad
Y_U=\begin{pmatrix}1&1&e\\1&0&0\\0&-e&0\end{pmatrix}.
\]
The assigned interval includes \(1\le t\le U\); the source's direct-chart right recovery block is the second coordinate and the left recovery block is the first coordinate.

Set \(W_U(t)=t\|X_U\|_2+\|Y_U\|_2\), and for a nonzero pencil vector set \(\eta_S(t,z)=\|S_U(t)z\|_2/[W_U(t)\|z\|_2]\). For every positive real \(t\) and every nonzero recovered scalar \(x\), the coefficientwise relative polynomial eigenpair error is exactly
\[
\eta_Q(t,x)=\frac{|Q_U(t)|}{e+t+et^2+e^2t^3}=1.
\]
In contrast, for every fixed \(t>0\), including the assigned chart, the best normwise pencil residual obeys
\[
\min_{z\ne0}\eta_S(t,z)
=\frac{\sigma_{\min}(S_U(t))}{W_U(t)}
\sim\frac{t}{\varphi U},\qquad U\longrightarrow\infty,
\qquad \varphi=\frac{1+\sqrt5}{2}.
\]
This convergence is uniform when \(t\) stays in a fixed compact subset of \((0,\infty)\). At \(t=1\), a normalized right/left smallest-singular-value pair \((z_U,w_U)\), phased to have positive third components, satisfies
\[
z_U=(0,-e,1)^\top+O(e^2),\qquad
w_U=(e,-e,1)^\top+O(e^2),
\]
so both nonzero recovery ratios diverge linearly:
\[
\frac{\|z_U\|_2}{|(z_U)_2|}\sim U,\qquad
\frac{\|w_U\|_2}{|(w_U)_1|}\sim U.
\]
In particular, the ratio between the recovered polynomial backward error and the pencil backward error of either singular vector is asymptotic to \(\varphi U\).

There are also exact, sharp thresholds for the *stronger* requirement that a recovery coordinate vanish. Write
\[
T_R=2+2e+3e^2,\quad D_R=e^2(3+2e+e^2),\qquad
T_L=1+3e^2,\quad D_L=e^2(2+e^2),
\]
and \(m(T,D)=\sqrt{\bigl(T-\sqrt{T^2-4D}\bigr)/2}\). At \(t=1\), the least normalized residual among all nonzero right vectors whose second coordinate is zero is precisely
\[
\delta_R(U)=\frac{m(T_R,D_R)}{W_U(1)};
\]
the least normalized *left* residual with first coordinate zero is precisely
\[
\delta_L(U)=\frac{m(T_L,D_L)}{W_U(1)}.
\]
Both minima are attained. Their sharp asymptotics are
\[
U\delta_R(U)\longrightarrow\frac{\sqrt{3/2}}{\varphi},\qquad
U\delta_L(U)\longrightarrow\frac{\sqrt2}{\varphi}.
\]
Thus, being strictly below the exact zero-coordinate thresholds only rules out literal zero recovery; it does **not** prevent both recovered errors from being maximal while pencil residuals are arbitrarily small.

## Assumptions and scope

All matrices and vectors are real, although the singular-value statements also hold over complex vectors. Every \(U>1\) is allowed. The asymptotics take \(U\to\infty\), with \(t\) held in a compact positive interval. The calculated pencil errors are unstructured normwise pencil backward errors; the polynomial error measures independently relative perturbations of the four scalar coefficients. The right/left recovery blocks are those assigned in the direct upper-half chart, with \(t=1\) included as a chart boundary. We do not assert that a particular floating-point QZ implementation returns the singular vectors or the real value \(t=1\).

## Proof

**1. Tropical construction and strong linearization.** The tropical max-function is \(\max(e,r,er^2,e^2r^3)\). Its exposed affine pieces switch at \(r=e\) and \(r=U\), with dominant index \(1\) in between. The geometric midpoint is \(1\). Specializing the construction with degree \(d=3\), interior index \(j=1\), and scale \(U\) gives the displayed \(S_U(t)\). More directly, let
\[
C_Q(t)=\begin{pmatrix}e+e^2t&1&e\\-1&t&0\\0&-1&t\end{pmatrix}.
\]
Then
\[
S_U(t)=\operatorname{diag}(U,-1,1)\,C_Q(t)\,\operatorname{diag}(1,e,e).
\]
The diagonal factors are constant and invertible. Thus \(S_U\) is a strong linearization of \(Q_U\), and a direct determinant calculation gives
\[
\det S_U(t)=-eQ_U(t).
\]
This demonstrates exact spectral equivalence rather than a spurious exact positive eigenvalue.

**2. Polynomial and pencil backward errors.** Because all four coefficients and \(t>0\) are positive, the numerator of the scalar coefficientwise error equals its denominator, giving \(\eta_Q=1\) for every nonzero \(x\). For \(S_U\), the minimum normalized residual over unit vectors is precisely its least singular value divided by \(W_U\). As \(e\downarrow0\), for fixed \(t\),
\[
S_U(t)\longrightarrow S_0=\begin{pmatrix}1&1&0\\1&0&0\\0&0&0\end{pmatrix},
\]
whose two nonzero singular values are \(\varphi\) and \(\varphi^{-1}\). Their product tends to \(1\), while the exact determinant is \(-eQ_U(t)=-et+O(e^2)\) for fixed \(t\). Multiplicativity of singular values therefore gives \(\sigma_{\min}(S_U(t))=et+O(e^2)\); also \(W_U(t)=\varphi+O(e)\). These estimates hold uniformly on compact positive \(t\)-sets. Consequently the normalized least residual is \(t/(\varphi U)+O(U^{-2})\), and the recovered-to-pencil error ratio grows as claimed.

**3. Recovery loss of both singular vectors.** At \(t=1\), the isolated vanishing singular mode of the limit has right and left null directions \(e_3\). Standard simple-singular-mode perturbation (equivalently, the two first-order equations \(S_U(1)z_U=\sigma_Uw_U\) and \(S_U(1)^\top w_U=\sigma_Uz_U\)) with \(\sigma_U=e+O(e^2)\) gives
\[
z_U=e_3-e e_2+O(e^2),\qquad
w_U=e_3+e(e_1-e_2)+O(e^2).
\]
For completeness: the first right-order equation is \(S_0z^{(1)}=(-1,0,0)^\top\), forcing \(z^{(1)}=-e_2\); the first left-order equation is \(S_0^\top w^{(1)}=(0,1,0)^\top\), forcing \(w^{(1)}=e_1-e_2\), with normalization fixing their third coordinates. Thus the source's selected second/right and first/left coordinates are \(-e+O(e^2)\) and \(e+O(e^2)\), respectively, and the claimed divergence follows. They are nonzero for sufficiently large \(U\).

**4. Exact recovery-coordinate vanishing thresholds.** Constraining the right coordinate \(z_2=0\) restricts the matrix to columns \(1\) and \(3\). The Gram matrix of those columns at \(t=1\) has trace \(T_R\) and determinant \(D_R\). Constraining the left coordinate \(w_1=0\) restricts the transpose residual to rows \(2\) and \(3\); the Gram matrix of these rows has trace \(T_L\) and determinant \(D_L\). A positive \(2\times2\) Gram matrix with trace \(T\) and determinant \(D\) has least singular value \(m(T,D)\) for its underlying rectangular matrix. This proves the two exact minima and attainment, not just sufficient bounds. Expanding the small eigenvalues gives \(m(T_R,D_R)\sim e\sqrt{3/2}\) and \(m(T_L,D_L)\sim e\sqrt2\); division by \(W_U(1)\to\varphi\) proves the limits.

## Verification

The companion equivalence and determinant were checked by exact symbolic algebra. Both restricted Gram trace/determinant identities were checked symbolically. Singular-value and singular-vector asymptotics were tested independently for multiple positive scale parameters, with direct matrix computations rather than fitted formulas. Reproduce by running the standalone file `check.py` with Python, NumPy, and SymPy. Numerical tests illustrate but do not replace the universal analytical steps above.

## Relationship to prior work

Pérez (2026), Sections 4–6, introduces this scaled companion pencil and exact-eigenvector recovery bounds; Section 1 explicitly leaves control of **computed** recovery ratios as an unresolved step toward a coefficientwise backward-stable eigensolver. The present calculation gives a sharp quantitative obstruction for unstructured residual-based acceptance on an actual upper-half pencil in that construction. It neither disputes the source's exact-eigenvector theorem nor claims that real positive \(t\) is an exact polynomial eigenvalue.

Higham, Li, and Tisseur (2007), Sections 2 and 3, already establish the general fact that pencil backward stability does not by itself guarantee polynomial backward stability and identify the recovery-block norm factor. Neither that general mechanism nor the usual coefficientwise backward-error definition is claimed as new. The contribution here is the actual source-specific cubic with two true tropical roots, the exact leading pseudospectral separation coefficient, simultaneous right/left recovery scaling, and the two closed sharp recovery-coordinate thresholds. Yang and collaborators (2025) study global bounds for approximate eigenpairs under tropical companion scaling; only their accessible abstract could be checked, so an uninspected specialized comparison is a residual bibliographic risk.

## Limitations

These are statements about normwise **unstructured** pencil residuals and coefficientwise **structured** polynomial perturbations. They are not a failure guarantee for a particular eigensolver, finite precision, every pencil chart, or the source's entire multi-pencil covering. The example is a scalar cubic, not a matrix polynomial with noncommuting coefficients. The two zero-coordinate thresholds are exact for the indicated frozen parameter \(t=1\), not arbitrary \(t\). A source on global tropically scaled companion bounds was accessible only at abstract level; equivalence through specialized stronger earlier results cannot be excluded categorically.

## References

1. J. Pérez, *Scaled Companion Linearizations for Coefficientwise Backward Stability*, arXiv:2610.20285v1 (first public 14 October 2026), especially Sections 1, 2, 4–6. https://arxiv.org/html/2610.20285v1
2. N. J. Higham, R.-C. Li, and F. Tisseur, *Backward Error of Polynomial Eigenproblems Solved by Linearization*, SIAM Journal on Matrix Analysis and Applications 29 (2007), 1218–1241, DOI:10.1137/060663738. Author manuscript: https://eprints.maths.manchester.ac.uk/996/1/hlt07.pdf
3. Z. Yang, Z. Wang, Z. Cao, and X. Wang, *Global bounds of backward errors of polynomial eigenvalue problem solved by a companion linearization*, Computational and Applied Mathematics 44 (2025), article 205, DOI:10.1007/s40314-025-03168-0 (abstract inspected).
