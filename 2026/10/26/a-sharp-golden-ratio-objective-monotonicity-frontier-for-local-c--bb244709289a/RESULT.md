# A sharp golden-ratio objective-monotonicity frontier for local-curvature descent 3

## Finding

Consider the exact local-curvature descent 3 (LCD3) step introduced by Richtárik, Giancola, Lubczyk and Yadav [1]. On the isotropic convex quadratic \(f(x)=\tfrac12\|x\|_2^2\), with an admissible constant but possibly anisotropic curvature lower bound \(C\), the sharp one-step objective amplification can be computed in every dimension. Put
\[
\varphi=\frac{1+\sqrt5}{2},\qquad F(u)=\frac{u^2(1-u)}{1+u},\qquad u_\kappa=\min\!\left\{\varphi^{-1},\sqrt{1-\kappa^{-1}}\right\}.
\]
For every integer \(d\ge2\), \(\kappa\ge1\), and symmetric positive definite \(C\in\mathbb R^{d\times d}\) with extreme eigenvalues \(\lambda_{\max}(C)=1\) and \(\lambda_{\min}(C)=\kappa^{-1}\),
\[
\boxed{\sup_{x\in\mathbb R^d\setminus\{0\}}\frac{f(x^+)}{f(x)}=M(\kappa):=\kappa F(u_\kappa).}
\]
This supremum is attained using only the extreme eigenspaces of \(C\). More explicitly,
\[
M(\kappa)=\begin{cases}
\bigl(1-\kappa+\sqrt{\kappa(\kappa-1)}\bigr)^2,&1\le\kappa\le\varphi,\\
\tfrac12(5\sqrt5-11)\kappa,&\kappa\ge\varphi.
\end{cases}
\]
The two expressions coincide at \(\kappa=\varphi\). The exact universal objective-monotonicity threshold is
\[
\boxed{f(x^+)\le f(x)\text{ for all }x\quad\Longleftrightarrow\quad
\kappa\le\kappa_{\mathrm c}:=\frac{11+5\sqrt5}{2}.}
\]
Thus, for admissible fixed curvature bounds with \(\kappa>\kappa_{\mathrm c}\), LCD3 may *increase* an isotropic objective in one step. At \(\kappa=12\) the sharp factor is \(6(5\sqrt5-11)\approx1.082039324994\); as \(\kappa\to\infty\), the worst amplification diverges linearly with coefficient \((5\sqrt5-11)/2\).

## Assumptions and scope

Fix \(d\ge2\) and \(\kappa\ge1\). Set \(f(x)=\|x\|_2^2/2\), \(f_\star=0\), and use any fixed real symmetric positive definite \(C\) satisfying \(\lambda_{\max}(C)=1\) and \(\lambda_{\min}(C)=1/\kappa\). If \(\kappa=1\), \(C=I\). These matrices meet the local lower and upper quadratic-support conditions of [1]: for every \(x,y\),
\[
f(y)+\nabla f(y)^\top(x-y)+\tfrac12\|x-y\|_C^2\le f(x)
\le f(y)+\nabla f(y)^\top(x-y)+\tfrac12\|x-y\|_{C+L_C I}^2,
\]
with \(L_C=1-\kappa^{-1}\). Indeed \(C\preceq I\preceq C+L_C I\). When \(\kappa=1\), take \(L_C=0\), for which these are equalities.

The precise LCD3 update from [1, §3.3, Appendix C.1] is
\[
x^+=x-\alpha(x)C^{-1}x,\qquad
\alpha(x)=1-\sqrt{1-\frac{\|x\|_2^2}{x^\top C^{-1}x}},\qquad x\ne0.
\]
The square root is real because \(C^{-1}\succeq I\). The classification concerns *one step* and a known minimizer value; it does not assert a global rate or nonconvergence. The normalization \(\lambda_{\max}(C)=1\) is essential, and condition number alone without a scale convention is not asserted sufficient.

## Proof

Write \(B=C^{-1}\), whose eigenvalues lie in \([1,\kappa]\) and include both endpoints. In an orthonormal eigenbasis, for any \(x\ne0\) put \(w_i=|x_i|^2/\|x\|^2\), so \(\sum_iw_i=1\). Define
\[
m_1=\sum_iw_i\lambda_i=\frac{x^\top Bx}{\|x\|^2},\qquad
m_2=\sum_iw_i\lambda_i^2=\frac{x^\top B^2x}{\|x\|^2}.
\]
Then \(1\le m_1\le\kappa\), \(\alpha=1-\sqrt{1-m_1^{-1}}\), and direct expansion gives the *exact* identity
\[
\frac{f(x^+)}{f(x)}=1-2\alpha m_1+\alpha^2m_2.\tag{1}
\]
For every eigenvalue \(1\le\lambda\le\kappa\), the nonnegative product \((\lambda-1)(\kappa-\lambda)\) implies
\[
\lambda^2\le(\kappa+1)\lambda-\kappa.
\]
Averaging gives \(m_2\le(\kappa+1)m_1-\kappa\). Equality holds exactly when the support of \(x\) is concentrated in the eigenvalues \(1\) and \(\kappa\), a possibility in every allowed matrix. For any requested \(m_1\in[1,\kappa]\), the squared weight \(p=(m_1-1)/(\kappa-1)\) at eigenvalue \(\kappa\) realizes that mean and attains equality (for \(\kappa>1\)). Since \(\alpha^2\ge0\), (1) is sharply maximized at that endpoint mixture for fixed \(m_1\).

Put \(u=\sqrt{1-m_1^{-1}}\), so \(m_1=(1-u^2)^{-1}\), \(\alpha=1-u\) and \(0\le u\le\sqrt{1-\kappa^{-1}}\). Substituting the sharp bound for \(m_2\) into (1) and simplifying yields
\[
1-\frac{2(1-u)}{1-u^2}
+(1-u)^2\!\left(\frac{\kappa+1}{1-u^2}-\kappa\right)
=\kappa\frac{u^2(1-u)}{1+u}=\kappa F(u).\tag{2}
\]
Differentiation gives
\[
F'(u)=\frac{2u(1-u-u^2)}{(1+u)^2}.
\]
Thus \(F\) increases until its unique positive stationary point \(u=\varphi^{-1}\), and decreases afterwards. On the allowed interval, its maximizer is \(u_\kappa\), establishing the boxed sharp supremum. The interior maximizer is feasible precisely if \(\sqrt{1-\kappa^{-1}}\ge\varphi^{-1}\), equivalently \(\kappa\ge\varphi\). At that point \(m_1=\varphi\), \(\alpha=\varphi^{-2}\), and \(F(\varphi^{-1})=(5\sqrt5-11)/2\). For \(1\le\kappa\le\varphi\), the maximizing direction is an eigenvector for \(\lambda=\kappa\) in \(B\); its multiplier is \(1-\kappa+\sqrt{\kappa(\kappa-1)}\), proving the other branch. At \(\kappa=1\) the update sends every nonzero \(x\) to zero, as the formula also states.

For \(\kappa\ge\varphi\), the sharp factor is a positive constant times \(\kappa\); its equality with one occurs exactly at \(\kappa_{\mathrm c}=(11+5\sqrt5)/2>\varphi\). The lower branch never exceeds one because it is increasing up to \(M(\varphi)<1\). Hence all one-step objectives are nonincreasing exactly at and below \(\kappa_{\mathrm c}\).

For an explicit strict witness when \(\kappa>\kappa_{\mathrm c}\), take \(C=\operatorname{diag}(1,\kappa^{-1})\), \(p=(\varphi-1)/(\kappa-1)\), and \(x=(\sqrt{1-p},\sqrt p)^\top\). Then \(m_1=\varphi\), all inequalities above are equalities, and \(f(x^+)/f(x)=\tfrac12(5\sqrt5-11)\kappa>1\). The same witness extends to larger dimensions by embedding the two eigendirections.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It checks the closed-form branches and exact-boundary witness at multiple condition numbers, verifies the scalar moment reduction against explicit two-eigenvalue updates over a deterministic grid, and tests the sharp upper envelope with reproducibly seeded random mixtures in several dimensions. Its finite tests are corroboration only: (1), the polynomial spectral inequality, (2), the derivative sign, and the endpoint witness establish the universal claim analytically. Run `python3 verify.py`.

## Relationship to prior work

Richtárik, Giancola, Lubczyk and Yadav [1] define LCD3 and its exact metric-projection update; their 2024 original preprint and the 2025 published version [2] provide convergence results for LCD1/LCD2 but not a general LCD3 theorem. Their special quadratic/Newton computation uses *the curvature matrix equal to the Hessian*, whereas here the admissible curvature lower bound is generally **strictly smaller and anisotropic** than the identity Hessian, so the one-step exact-Newton conclusion does not apply. The new statement is the **all-dimensional sharp worst-direction envelope** for LCD3 and the exact curvature-condition frontier; the algorithm, localization set, and the elementary fact of possible nonmonotonicity are not claimed as new.

Abdukhakimov, Xiang, Kamzolov and Takáč [3] study preconditioned *stochastic* Polyak steps. Those scalar-stepsize and stochastic-preconditioner rules are not the LCD3 square-root projection update. Related spectral performance bounds for standard scaled Polyak or other preconditioned gradient iterations need not imply the nonlinear \(\kappa F(u)\) envelope here. A possible preexisting equivalent formulation under generalized ellipsoid-projection terminology is a residual originality risk.

For comparison, LCD2 projects onto the *same* localization ellipsoid in the Euclidean metric, so its objective on this radial quadratic is nonincreasing for every \(\kappa\): the ellipsoid is closed and convex, contains the origin, and Euclidean metric projection cannot increase distance to the origin. The contrast isolates the consequence of choosing the curvature-induced metric rather than the Euclidean one.

## Limitations

The result is for exact arithmetic, a single fixed curvature matrix satisfying \(C\preceq I\) and \(\lambda_{\max}(C)=1\), the isotropic quadratic objective, and a single LCD3 step. It does not establish divergence, cycling, a global rate, or instability of LCD3 for arbitrary objectives. The curvature-condition number cannot be separated from its normalization for more general classes. The conclusion does not invalidate the published LCD2/LCD1 convergence theorems or the one-step Newton result when the curvature matches the Hessian. The assessed originality remains subject to independent literature review.

## References

[1] P. Richtárik, S. M. Giancola, D. Lubczyk, R. Yadav, *Local Curvature Descent: Squeezing More Curvature out of Standard and Polyak Gradient Descent*, arXiv:2405.16574v1, first posted 2024-05-26, §§2–4 and Appendix C, https://arxiv.org/html/2405.16574v1 .

[2] P. Richtárik, S. M. Giancola, D. Lubczyk, R. Yadav, same work, *Advances in Neural Information Processing Systems* 38 (2025), §§3–4 and Appendix D.2, DOI: 10.52202/085713-0373, https://proceedings.neurips.cc/paper_files/paper/2025/file/107aaa54d9481515e981e332e2e115b1-Paper-Conference.pdf .

[3] F. Abdukhakimov, C. Xiang, D. Kamzolov, M. Takáč, *Stochastic Gradient Descent with Preconditioned Polyak Step-size*, arXiv:2310.02093v1, 2023-10-03, https://arxiv.org/abs/2310.02093 .
