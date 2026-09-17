# Sharp two-mode transient amplification for CG_AOS after exact initialization

**Same-model review: passed. Cross-model review: not yet performed.**

## Statement

Consider the strictly convex quadratic
\[
f(x)=\frac12 x^T A x-b^T x,
\]
with symmetric positive-definite \(A\). Let the first conjugate-gradient step use exact line search from \(x_0\), and from the next step use the Dai--Yuan direction together with the approximately optimal stepsize (AOS)
\[
\alpha_k^{\rm AOS}=-\frac{g_k^T d_k}{d_k^T\bar B_kd_k},
\]
where, with \(s_{k-1}=x_k-x_{k-1}\) and \(y_{k-1}=g_k-g_{k-1}\),
\[
\bar B_k=
\frac{\|y_{k-1}\|^2}{s_{k-1}^Ty_{k-1}}I
-\frac{\|y_{k-1}\|^2}{s_{k-1}^Ty_{k-1}}
 \frac{s_{k-1}s_{k-1}^T}{\|s_{k-1}\|^2}
+\frac{y_{k-1}y_{k-1}^T}{s_{k-1}^Ty_{k-1}}.
\]
This is the CG_AOS stepsize model introduced in Liu (2026).

Assume that the initial error is contained in a two-dimensional invariant subspace of \(A\) with eigenvalues \(0<\mu<L\), and both eigenmodes are present. Set \(\kappa=L/\mu\). Write the normalized first search direction in an eigenbasis as
\[
e=(\cos\theta,\sin\theta)^T,
\qquad \cos\theta\sin\theta\ne0.
\]
Let \(\alpha_1^*\) denote the exact line-search length along the second CG direction. Then the first AOS step satisfies the exact distortion formula
\[
\boxed{
\frac{\alpha_1^{\rm AOS}}{\alpha_1^*}
=r(\theta)
=\frac{\mu L}{\mu^2\cos^2\theta+L^2\sin^2\theta}.}
\]
Consequently,
\[
\boxed{\frac{f(x_2)-f_*}{f(x_1)-f_*}=(r(\theta)-1)^2.}
\]
As the nonzero mode weights vary,
\[
r(\theta)\in(\kappa^{-1},\kappa),
\qquad
\sup_\theta \frac{f(x_2)-f_*}{f(x_1)-f_*}=(\kappa-1)^2.
\]
Thus, for every \(\kappa>2\), there are two-mode initial states for which the AOS step increases the objective even though the preceding step was an exact CG line search.

## Sharp scalar safeguard in the two-mode problem

Replace the first AOS step by the damped step
\[
\widetilde\alpha_1=\gamma\alpha_1^{\rm AOS},\qquad \gamma>0.
\]
Then
\[
\frac{f(x_2)-f_*}{f(x_1)-f_*}=(\gamma r(\theta)-1)^2.
\]
Therefore
\[
\boxed{0<\gamma\le \frac{2}{\kappa}}
\]
is the sharp condition for strict objective decrease at this step for every non-eigenvector two-mode initialization. If \(\gamma>2/\kappa\), an orientation can be chosen with \(r(\theta)>2/\gamma\), and the step increases the objective.

## Explicit unbounded amplification family

Scale \(\mu=1\), \(L=\kappa\), take \(b=0\), and choose
\[
A=\operatorname{diag}(1,\kappa),
\qquad
g_0=(1,\kappa^{-1})^T,
\qquad
x_0=A^{-1}g_0=(1,\kappa^{-2})^T.
\]
The exact first step has
\[
\alpha_0=\frac{\kappa^2+1}{\kappa(\kappa+1)},
\]
and the subsequent CG_AOS/exact-line-search ratio is
\[
r=\frac{\kappa^2+1}{2\kappa}.
\]
Direct simplification gives
\[
\frac{f(x_1)}{f(x_0)}
=\frac{\kappa(\kappa-1)^2}{(\kappa+1)(\kappa^3+1)},
\]
\[
\frac{f(x_2)}{f(x_1)}
=\frac{(\kappa-1)^4}{4\kappa^2},
\]
and hence
\[
\boxed{
\frac{f(x_2)}{f(x_0)}
=\frac{(\kappa-1)^6}
{4\kappa(\kappa+1)(\kappa^3+1)}
\sim \frac{\kappa}{4}.}
\]
Thus one AOS step can produce an arbitrarily large excursion relative even to the initial objective as the condition number grows. For example, at \(\kappa=10\),
\[
\frac{f(x_2)}{f(x_0)}
=\frac{531441}{440440}\approx1.2066138407.
\]

## Proof

Translate the minimizer to the origin, so \(b=0\). The first direction is \(d_0=-g_0\), and exact line search gives
\[
g_1^T d_0=0.
\]
For the Dai--Yuan parameter,
\[
\beta_1^{\rm DY}
=\frac{\|g_1\|^2}{d_0^T(g_1-g_0)}
=\frac{\|g_1\|^2}{\|g_0\|^2},
\]
so after an exact first step it coincides with Fletcher--Reeves. Using
\(g_1-g_0=\alpha_0Ad_0\), one obtains
\[
d_0^TAd_1=0.
\]
In the two-dimensional invariant subspace, the error \(x_1-x_*\) is also \(A\)-orthogonal to \(d_0\). Hence it is parallel to \(d_1\), and the exact second line search would reach \(x_*\) in one step.

Let \(e=d_0/\|d_0\|\), and complete it to an orthonormal basis \((e,q)\). Write
\[
A=\begin{pmatrix}a&h\\h&d\end{pmatrix}
\]
in this basis. Since \(s_0\) is parallel to \(e\) and \(y_0=As_0\), the AOS matrix becomes
\[
\bar B_1=
\begin{pmatrix}
a&h\\
h&a+2h^2/a
\end{pmatrix}.
\]
An \(A\)-conjugate direction to \(e\) is proportional to
\[
v=(h,-a)^T.
\]
A direct calculation yields
\[
v^TAv=a\det A,
\qquad
v^T\bar B_1v=a(a^2+h^2).
\]
Therefore
\[
\frac{\alpha_1^{\rm AOS}}{\alpha_1^*}
=\frac{v^TAv}{v^T\bar B_1v}
=\frac{\det A}{a^2+h^2}.
\]
On the invariant two-mode subspace, \(\det A=\mu L\) and
\[
a^2+h^2=\|Ae\|^2
=\mu^2\cos^2\theta+L^2\sin^2\theta,
\]
which proves the stated formula for \(r(\theta)\).

Because the exact second line search reaches the minimizer,
\[
x_1-x_*=-\alpha_1^*d_1.
\]
After an AOS step,
\[
x_2-x_*=(r-1)\alpha_1^*d_1=-(r-1)(x_1-x_*),
\]
so quadratic homogeneity gives
\[
\frac{f(x_2)-f_*}{f(x_1)-f_*}=(r-1)^2.
\]
The range \(r\in(\kappa^{-1},\kappa)\), the sharp damping threshold, and the explicit family follow by elementary substitution.

## Interpretation

The source paper establishes convergence for its gradient-method specialization, but explicitly leaves theoretical convergence and rates of CG_AOS open. The calculation above identifies a concrete obstruction to importing monotone or Wolfe-type conjugate-gradient arguments directly: the AOS quadratic line model can underestimate the true curvature along the next conjugate direction by a factor approaching \(\kappa\), so the resulting positive step can overshoot beyond the interval of objective decrease.

The result is not a divergence theorem. It shows instead that any global CG_AOS convergence or rate result must tolerate potentially large nonmonotone transients, impose a safeguard, or exploit a mechanism that controls the accumulated AOS distortion.

## Computational model and limitations

- Exact arithmetic and exact gradients/objective values are assumed.
- The theorem concerns a strictly convex quadratic and a two-eigenmode invariant subspace; the construction embeds in any higher dimension containing those two eigenvalues.
- The first step is initialized by exact line search because the AOS matrix uses a previous secant pair. The conclusion concerns the first subsequent CG_AOS step and does not assert that every possible initialization behaves this way.
- The result does not prove asymptotic nonconvergence of CG_AOS.
- The sharp scalar safeguard \(2/\kappa\) uses knowledge of the condition number and is only claimed for this two-mode setting.

## Reproducibility

`artifacts/verify_transient.py` symbolically verifies the explicit \(A=\operatorname{diag}(1,\kappa)\) family and its objective ratios. It was executed with Python 3.13.5 and SymPy 1.14.0.

## Literature context

Liu (2026) defines the same AOS matrix and CG_AOS with the Dai--Yuan parameter, reports favorable numerical experiments, and explicitly asks whether CG_AOS converges theoretically and at what rate. Earlier nonlinear-CG convergence theory for Dai--Yuan and related methods relies on line-search conditions such as Wolfe or Goldstein; objective increase in the construction above shows that the undamped AOS step need not automatically satisfy even monotonic decrease.

Ni and Liu (2024) study a different Dai--Liao conjugate-gradient construction in which approximately optimal stepsize ideas are used to choose conjugacy parameters. Its abstract states sufficient descent and global convergence under additional conditions. The full text was not inspected here, so it remains the closest identified source that could contain related local calculations; its described algorithm is not the CG_AOS method analyzed above.

## References

1. Z. Liu, *A unified framework for inexact adaptive stepsizes in the gradient methods, the conjugate gradient methods and the quasi-Newton methods for strictly convex quadratic optimization*, arXiv:2604.20506v1, 2026. https://arxiv.org/abs/2604.20506
2. Y. Ni and Z. Liu, *A New Dai-Liao Conjugate Gradient Method based on Approximately Optimal Stepsize for Unconstrained Optimization*, Numerical Functional Analysis and Optimization 45 (2024), 333--354. https://doi.org/10.1080/01630563.2024.2333255
3. Y. H. Dai and Y. Yuan, *A Nonlinear Conjugate Gradient Method with a Strong Global Convergence Property*, SIAM Journal on Optimization 10 (1999), 177--182. https://doi.org/10.1137/S1052623497318992
4. W. W. Hager and H. Zhang, *A New Conjugate Gradient Method with Guaranteed Descent and an Efficient Line Search*, SIAM Journal on Optimization 16 (2005), 170--192. https://doi.org/10.1137/030601880
