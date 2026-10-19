# Sharp positivity cone and hidden stage sign loss in a two-stage Chebyshev two-step integrator

## Finding

Consider the unique nondegenerate, unshifted, two-stage, second-order specialization of the Chebyshev two-step stability-polynomial ansatz of Moisa and Faleichik [1]. Its rational-coefficient realization, for a scalar or vector right-hand side \(f\), is
\[
\begin{aligned}
 v_0&=\tfrac32y_n-\tfrac12y_{n-1},\\
 v_1&=v_0+\tfrac h2 f(t_n+h/2,v_0),\\
 v_2&=2v_1-v_0+h f(t_n+h,v_1),\\
 y_{n+1}&=\tfrac35y_n+\tfrac25v_2.
\end{aligned}
\]
For the scalar decay test equation \(y'=-\lambda y\), let \(z=\lambda h\) satisfy \(0<z<4\), and put
\[
\begin{aligned}
 t(z)&=1-2z+\tfrac12z^2,\\
 a(z)&=\tfrac35(1+t(z)),\qquad b(z)=-\tfrac15t(z),\\
 \ell_\pm(z)&=\frac{3(1+t(z))\pm\sqrt{9t(z)^2-2t(z)+9}}{10}\quad\text{when }t(z)>0.
\end{aligned}
\]
The two-step scalar method is absolutely stable throughout \(0<z<4\), but its sharp **all-iterate positivity region** depends on the starting ratio \(q=y_1/y_0>0\):

1. If \(t(z)\le0\), every two strictly positive starting values produce strictly positive iterates at all indices.
2. If \(t(z)>0\), every iterate is strictly positive **if and only if** \(q\ge\ell_-(z)\). Below that bound some iterate is strictly negative.

For the exact positive starter \(y_0>0\), \(y_1=e^{-z}y_0\), there is a unique threshold \(z_*\in(2+\sqrt2,4)\) determined by
\[
 e^{-z_*}=\ell_-(z_*),\qquad
 z_*=3.480888475257457945\ldots.
\]
Every computed endpoint remains strictly positive precisely for \(0<z\le z_*\). For \(z_*<z<4\), negativity eventually occurs **although the recurrence is absolutely stable**. The index \(N(z)\) of the first strictly negative iterate satisfies
\[
 N(z)=\frac{\log\!\bigl(1/(z-z_*)\bigr)}{\log\!\bigl(\ell_+(z_*)/\ell_-(z_*)\bigr)}+O(1)
 \quad(z\downarrow z_*),
\]
with leading coefficient \(0.331753556229006247\ldots\).

A separate, earlier obstruction occurs within the numerical stages: already at the first update from exact starting values, \(v_0=(3e^{-z}-1)y_0/2<0\) whenever \(z>\log 3\). Thus for \(\log3<z\le z_*\), **every reported endpoint is positive while the very first internal stage is negative**. This matters when the right-hand side is defined only on a positive state domain.

## Assumptions and scope

The ansatz uses \(R_1(\mu)=\alpha[1+T_2(\omega+\beta\mu/4)]\), \(R_0(\mu)=-\eta^2T_2(\omega+\beta\mu/4)\), where \(T_2(u)=2u^2-1\). We impose \(\omega=1\), nondegenerate damping \(0\le\eta^2<1\), consistency, and order two. No claim is made that these coefficients are the same as the small-damping numerical choices used in [1]. Under these conditions the coefficients and corresponding stages above are uniquely fixed. The positivity theorem is for a constant step, a scalar decay rate \(\lambda>0\), and arbitrary *strictly positive* starts. The exact-starter assertion assumes \(y_1=e^{-z}y_0\) and all numerical outputs are interpreted in exact real arithmetic. Internal stages and reported endpoints are distinguished.

## Proof

**Unique rational-coefficient specialization.** Write \(r=\eta^2\). For \(\omega=1\),
\[
 T_2(1+\beta\mu/4)=1+\beta\mu+\beta^2\mu^2/8.
\]
The zeroth-, first-, and second-order conditions for the characteristic polynomials of [1, Eq. (10)] reduce respectively to
\[
 2\alpha-r=1,\qquad
 2\alpha+(\alpha-r)\beta=2,\qquad
 \alpha+\alpha\beta+(\alpha-r)\beta^2/8=2.
\]
Since \(r<1\), the first two give \(\alpha=(1+r)/2\) and \(\beta=2\), and the third gives \((7+5r)/4=2\). Thus \(r=1/5\), \(\alpha=3/5\), and \(\beta=2\). Substitution into the stage realization [1, Eqs. (21),(24)] gives the displayed method. For general sufficiently smooth \(f\), inserting exact past values into the stages gives \(f(t_n+h/2,v_0)=y'(t_n)+h y''(t_n)/2+O(h^2)\) and \(f(t_n+h,v_1)=y'(t_n)+h y''(t_n)+O(h^2)\). The reported value is consequently \(y(t_n)+hy'(t_n)+h^2y''(t_n)/2+O(h^3)\). The characteristic roots at zero step are \(1\) and \(1/5\), so the method is zero-stable and second order under standard smoothness and Lipschitz hypotheses.

**Scalar recurrence and stability.** On \(f(y)=-\lambda y\), the internal calculation gives \(v_2=t(z)v_0\), whence
\[
 y_{n+1}=a(z)y_n+b(z)y_{n-1},\qquad
 \xi^2-a(z)\xi-b(z)=0.
\]
For \(0<z<4\), \(-1\le t(z)<1\). The three strict real Schur conditions are
\[
 |b(z)|<1,\quad 1-a(z)-b(z)=\tfrac25(1-t(z))>0,\quad
 1+a(z)-b(z)=\tfrac85+\tfrac45t(z)>0.
\]
Thus both characteristic roots have modulus below one. At \(z=4\), \(t(z)=1\) and a characteristic root equals one; for \(z>4\), \(1-a(z)-b(z)<0\) implies a root strictly above one, proving the stated positive-axis stability boundary.

**Complete positivity cone.** If \(t(z)\le0\), then \(a(z),b(z)\ge0\), with at least one positive, and induction gives positivity of every iterate from two positive starts. For \(0<t(z)<1\), the discriminant is \((9t^2-2t+9)/25>0\), and both roots \(0<\ell_-<\ell_+<1\) are real. With \(q=y_1/y_0\), the closed solution is
\[
 \frac{y_n}{y_0}
 =\frac{q-\ell_-}{\ell_+-\ell_-}\ell_+^n
 +\frac{\ell_+-q}{\ell_+-\ell_-}\ell_-^n.
\]
If \(q<\ell_-\), the leading coefficient is negative and a negative iterate occurs. If \(q\ge\ell_-\), division by \(\ell_+^n\) shows a linear interpolation (as \((\ell_-/\ell_+)^n\) decreases from one toward zero) between the strictly positive initial value and a nonnegative limiting coefficient. For every finite index the interpolation remains strictly positive, hence all iterates remain positive. Equality corresponds to the exact positive smaller-root mode.

**Exact-starter threshold.** The equation \(t(z)=0\) has roots \(2\pm\sqrt2\). In the lower region \(0<z<2-\sqrt2\), \(\ell_-(z)<1/5<e^{-(2-\sqrt2)}\le e^{-z}\), so positivity holds. In the middle region \(2-\sqrt2\le z\le2+\sqrt2\), \(t\le0\), so positivity holds without restrictions on the starting ratio. On \(2+\sqrt2<z<4\), the function \(t(z)\) increases strictly from zero to one. The smaller root satisfies \(0<\ell_-(t)<1/5\) on \(0<t<1\), since the characteristic polynomial evaluated at \(1/5\) equals \((2/25)(t-1)<0\) and \(1/5\) lies between its roots. It strictly increases with \(t\): differentiating \(\ell_-^2-(3/5)(1+t)\ell_-+t/5=0\), its derivative has the sign of \([(3/5)\ell_--1/5]/[2\ell_--(3/5)(1+t)]\), which is positive because \(0<\ell_-<1/5\). Meanwhile \(e^{-z}\) strictly decreases. The difference is positive at \(2+\sqrt2\) and negative at \(4\), since \(e^{-4}<1/5\). Therefore there is exactly one crossing \(z_*\), with the stated positivity classification.

**First negative index and internal-stage boundary.** For \(z>z_*\), let \(q=e^{-z}\). The explicit root solution yields the exact integer formula
\[
 N(z)=1+\left\lfloor
 \frac{\log[(\ell_-(z)-q)/(\ell_+(z)-q)]}
 {\log[\ell_-(z)/\ell_+(z)]}
 \right\rfloor.
\]
The floor is correct even at equality, because \(N(z)\) denotes the first **strictly negative** value. Strict monotonicity at the crossing gives \(\ell_-(z)-e^{-z}=c(z-z_*)+O((z-z_*)^2)\) for \(c>0\). Taking logarithms in the exact integer formula proves the stated \(O(1)\)-accurate logarithmic onset. Finally, the displayed first stage at exact starting values is \((3e^{-z}-1)y_0/2\), which is negative exactly when \(z>\log3\).

## Verification

The standalone standard-library script `verify.py` checks the rational order identities, stage/recurrence equality over 2,268 exact-rational cases, strict Schur conditions over a rational step grid, high-precision threshold bracketing, and 1,599 finite sequence checks (including first-negative-index predictions). Running `python3 verify.py` produced the embedded `verification_output.txt`. The symbolic recurrences and infinite-time positivity statements are established by the proof above; numerical tests are not substituted for that proof.

## Relationship to prior work

Moisa and Faleichik [1] introduce the stabilized two-step Chebyshev ansatz, derive its polynomial order conditions and stage realizations, and assess extended absolute-stability intervals. The present result derives the unique nondegenerate **unshifted two-stage** branch and establishes its sharp positive-start invariant cone, exact-starter positivity boundary, first-negative delay, and stage-versus-output sign separation; these assertions are not in the relevant sections of [1]. Ketcheson, Gottlieb, and Macdonald [2] treat strong-stability-preserving two-step Runge–Kutta methods and general monotonicity guarantees. Our method has a negative coefficient on the earlier solution and is not claimed to be SSP. The absence of an SSP guarantee does not determine its exact scalar positivity cone or its exact-starter crossing. Positivity restrictions in other integrators do not directly cover this different characteristic polynomial and starting rule.

## Limitations

The classification does not cover arbitrary spatially discretized parabolic systems, other damping or shifting choices, varying time steps, floating-point rounding, or nonlinear dynamics beyond the exhibited initial-stage obstruction. The source's small-damping example coefficients are different from the exact unshifted specialization studied here. Generic second-order recurrence formulas are classical; the claim is the method-specific complete boundary, not discovery of those formulas. Published or unpublished equivalent method-specific analyses might exist beyond the inspected sources. The numeric decimal expansion is a reproducibility aid, not an exact algebraic expression for the transcendental root.

## References

[1] A. Moisa and B. Faleichik, *Second order stabilized two-step Runge–Kutta methods*, arXiv:2303.16267, first public 2023-03-28, especially Sections 2–5 and Eqs. (9), (10), (21), (24). https://arxiv.org/html/2303.16267v1

[2] D. I. Ketcheson, S. Gottlieb, and C. B. Macdonald, *Strong stability preserving two-step Runge–Kutta methods*, arXiv:1106.3626, 2011, especially Sections 1–3 and Theorem 2. https://arxiv.org/pdf/1106.3626
