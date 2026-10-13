# Exact affine collapse and a vanishing quadratic constant in logarithmic-exponent NMLM
## Finding
Consider Algorithm 1, the nonmonotone modified Levenberg--Marquardt method (NMLM) of Zheng--Yang--Cao, on a homogeneous linear system
\[
F(x)=Ax,
\]
where \(A\in\mathbb R^{{m\times n}}\) has full column rank. For every nonzero iterate, every first trial is accepted and
\[
\widehat r_k\ge 1.
\]
Hence the inner rejection loop is never entered, and because the source assumes \(p_2<1\), the accepted-step update always takes its most aggressive branch,
\[
\mu_{{k+1}}=\max\left\{{\frac{{\mu_k}}4,m}}\right\},
\qquad
\mu_k=\max\left\{{\mu_0 4^{{-k}},m}}\right\}.
\]
Thus the nonmonotone memory length and the thresholds \(p_0,p_1,p_2\) do not affect the iterates on this exact-model class.

Writing \(B=A^{{\mathsf T}}A\), the accepted iterate is exactly
\[
x_{{k+1}}=\lambda_k(B+\lambda_k I)^{{-1}}x_k.
\]
If
\[
\Lambda=\mu_0 e^{{1/e}},
\qquad
q=\frac{{\Lambda}}{{\sigma_{{\min}}(A)^2+\Lambda}},
\]
then \(q<1\) and every nonzero iterate satisfies
\[
\|x_{{k+1}}\|\le q\|x_k\|.
\]
For the mathematical continuation with the practical stopping tolerance suppressed, eventually \(\mu_k=m\), \(\|Ax_k\|<1\), and
\[
\delta_k=1+\frac1{{\ln(k+e)}}.
\]
Along that tail,
\[
\frac{{\|x_{{k+1}}\|}}{{\|x_k\|^2}}\longrightarrow0.
\]
This is Q-superquadratic in the explicit sense that the quadratic error ratio tends to zero. It is sharper on this class than the source theorem's quadratic specialization for Hölder exponents \(\gamma=\nu=1\).

## Assumptions and scope
The matrix \(A\) is finite dimensional and has full column rank, so \(B=A^{{\mathsf T}}A\succ0\) and the unique zero is \(x_\star=0\). The NMLM parameters satisfy the source conditions \(N_0>0\), \(\mu_0>m>0\), and \(0<p_0\le p_1\le p_2<1\). The exact acceptance and contraction statements apply to every nonterminal iteration of the printed algorithm. The asymptotic statement concerns the underlying mathematical iteration continued with stopping tolerance \(\varepsilon=0\), or equivalently the formal continuation beyond any positive practical tolerance.

No claim is made for rank-deficient \(A\), inexact linear solves, nonlinear \(F\), floating-point stopping behavior, or the source's singular benchmark problems.

## Proof
Put \(B=A^{{\mathsf T}}A\). At a nonzero iterate the source damping parameter \(\lambda_k\) is positive, and the LM step is
\[
d_k=-(B+\lambda_k I)^{{-1}}Bx_k.
\]
Therefore
\[
x_k+d_k=\lambda_k(B+\lambda_k I)^{{-1}}x_k.
\]
Because \(F\) is affine, its linear model is exact:
\[
F(x_k+d_k)=F_k+J_kd_k.
\]
Full column rank makes every eigenvalue of \(B\) positive, while each spectral factor \(\lambda_k/(\lambda_i(B)+\lambda_k)\) lies strictly between zero and one. Hence
\[
\|F(x_k+d_k)\|<\|F_k\|,
\]
so the predicted reduction is positive.

Let \(M_k=\|F_{{l(k)}}\|\), the source's maximum residual over its nonmonotone window. Since the current residual belongs to that window, \(M_k\ge\|F_k\|\). Exactness of the linear model gives
\[
\widehat r_k
=\frac{{M_k^2-\|F(x_k+d_k)\|^2}}{{\|F_k\|^2-\|F(x_k+d_k)\|^2}}
=1+\frac{{M_k^2-\|F_k\|^2}}{{\|F_k\|^2-\|F(x_k+d_k)\|^2}}
\ge1.
\]
Since \(p_2<1\), the trial is accepted immediately and Step 5 yields
\[
\mu_{{k+1}}=\max\left\{{\mu_k/4,m}}\right\}.
\]
Induction gives the displayed exact formula for \(\mu_k\).

It remains to control \(\lambda_k\). If \(t=\|Ax_k\|\ge1\), then the source uses \(\delta_k=1/t\), and
\[
t^{{\delta_k}}=t^{{1/t}}\le e^{{1/e}}.
\]
If \(t<1\), then \(1<\delta_k\le2\), so \(t^{{\delta_k}}<1\). The denominator in the source formula for \(\lambda_k\) is at least one and \(\mu_k\le\mu_0\), hence
\[
0<\lambda_k\le\Lambda:=\mu_0 e^{{1/e}}.
\]
The spectral norm of \(\lambda_k(B+\lambda_kI)^{{-1}}\) is at most
\[
\frac{{\Lambda}}{{\sigma_{{\min}}(A)^2+\Lambda}}=q<1,
\]
proving the global contraction and therefore \(x_k\to0\).

After finitely many iterations, \(\mu_k=m\) and \(\|Ax_k\|<1\). Set \(\epsilon_k=1/\ln(k+e)\), so \(\delta_k=1+\epsilon_k\). The source damping formula and the smallest eigenvalue of \(B\) give, for a constant \(C>0\) independent of large \(k\),
\[
\|x_{{k+1}}\|
\le C\|x_k\|^{{2+\epsilon_k}}.
\]
In particular, once \(\|x_k\|<1\),
\[
\|x_{{k+1}}\|\le C\|x_k\|^2.
\]
Choose a later index \(K\) with \(C\|x_K\|<1\). Then \(z_k=C\|x_k\|\) satisfies \(z_{{k+1}}\le z_k^2\), whence
\[
-\ln\|x_{{K+j}}\|\ge c2^j-O(1)
\]
for some \(c>0\). Consequently
\[
\epsilon_k\,|\ln\|x_k\||\longrightarrow\infty,
\qquad
\|x_k\|^{{\epsilon_k}}\longrightarrow0.
\]
Dividing the earlier bound by \(\|x_k\|^2\) therefore yields
\[
0\le\frac{{\|x_{{k+1}}\|}}{{\|x_k\|^2}}
\le C\|x_k\|^{{\epsilon_k}}\longrightarrow0.
\]

## Verification
The proof uses only spectral calculus for the positive definite matrix \(A^{{\mathsf T}}A\), the exact affine-model identity, and the elementary maximum \(\sup_{{t\ge1}}t^{{1/t}}=e^{{1/e}}\). The included verifier independently checks the acceptance-ratio identity, the exact quartering of \(\mu_k\), the matrix recurrence on a multi-mode diagonal example, the uniform contraction bound, and a log-domain scalar tail in which the logarithm of the quadratic ratio tends rapidly to \(-\infty\).

## Relationship to prior work
Zheng--Yang--Cao introduce the logarithmic exponent \(1+1/\ln(k+e)\), the residual/gradient-normalized damping parameter, the nonmonotone ratio, and the quartering safeguard. Their general local theorem gives order \(\gamma(1+\nu)\), hence a quadratic bound when \(\gamma=\nu=1\); their numerical section uses nonlinear singular tests rather than full-column-rank affine systems.

Earlier nonmonotone LM papers establish global and superlinear or quadratic convergence for different damping laws. Zhao--Tang use a fixed exponent in a general convex combination of residual and gradient powers and cap their general rate at order two. Amini--Rostami study an accelerated two-step construction and a different adaptive exponent schedule. These results motivate comparison but do not imply the exact NMLM acceptance collapse, the source-specific formula for \(\mu_k\), or the vanishing quadratic ratio for the logarithmic-exponent NMLM iteration.

## Limitations
The asymptotic tail is a property of the mathematical zero-tolerance continuation. With the source's required positive stopping tolerance, execution can terminate before the tail is numerically observed. The result does not assert a fixed Q-order strictly greater than two: the source exponent approaches one, and the proved statement is specifically that the quadratic ratio tends to zero. The comparison search did not obtain lawful full text of the 2015 Amini--Rostami paper; its abstract and the detailed description in the 2026 primary source were inspected, leaving a residual bibliographic risk of an unindexed affine special-case remark there.

## References
1. Y. Zheng, Y. Yang, M. Cao, *The modified Levenberg--Marquardt method with nonmonotone technique*, AIMS Mathematics 11 (2026), 2527--2546. DOI: 10.3934/math.2026102.
2. L. Zhao, J. Tang, *Levenberg--Marquardt method with a general LM parameter and a nonmonotone trust region technique*, Journal of Applied Analysis & Computation 14 (2024), 1959--1976. DOI: 10.11948/20220441.
3. K. Amini, F. Rostami, *A modified two steps Levenberg--Marquardt method for nonlinear equations*, Journal of Computational and Applied Mathematics 288 (2015), 341--350. DOI: 10.1016/j.cam.2015.04.040.
4. Z. Wu, *A new modified efficient Levenberg--Marquardt method for solving systems of nonlinear equations*, Mathematical Problems in Engineering (2021), 5608195. DOI: 10.1155/2021/5608195.
