# Exact sign-loss window for first-lag Scarpi convolution quadrature and a sharp positive-exponential approximation barrier

## Finding

For an exponentially transitioning fractional order, the first history coefficient of backward-Euler convolution quadrature has a **complete sharp sign classification** in the three model parameters. When that coefficient changes sign, it does so over exactly one bounded, nonempty timestep interval. In the same regime the associated continuous Scarpi integral kernel necessarily has both signs, and every positive sum-of-exponentials approximation of its Laplace transform incurs an explicit sharp nonzero error on a natural frequency interval.

Write
\[
\alpha(t)=b+(a-b)e^{-ct},\quad 0<a,b<1,\ c>0,\qquad
B(s)=\frac{as+bc}{s+c},\qquad \Psi(s)=s^{-B(s)}\quad(s>0).
\]
The backward-Euler convolution-quadrature weights are uniquely defined by
\[
\sum_{n\geq0}\omega_n(h)z^n=\Psi\!\left(\frac{1-z}{h}\right),\quad h>0,\quad |z|<1.
\]
Set
\[
\boxed{\Theta(a,b,c)=2(a+b)+(a-b)\log\!\left(\frac{cb}{a}\right).}
\]
Then:

1. If \(\Theta>0\), the first history weight \(\omega_1(h)\) is strictly positive for **every** \(h>0\). If \(\Theta=0\), it is nonnegative for all steps, with its only zero at \(h_0=a/(cb)\). If \(a=b\), the weight is strictly positive for every step.
2. If \(\Theta<0\), there are unique \(0<h_-<h_+<\infty\) for which \(\omega_1(h)<0\) **exactly when** \(h_-<h<h_+\); it vanishes at both endpoints and is positive outside their closed interval. These are all possible signs and boundary cases.
3. In the sign-loss regime, define \(x_-<b/a<x_+\) as the two positive roots of
\[
q(x)=ax+\frac{b}{x}+a+b+(a-b)\log(cx)=0.
\]
Then \(h_-=1/(cx_+)\), \(h_+=1/(cx_-)\). The transform \(\Psi\) increases strictly on \([s_-,s_+]\) with \(s_-=cx_-\), \(s_+=cx_+\). If \(\psi\) is its locally integrable inverse Laplace transform, then \(\psi\) is neither nonnegative nor nonpositive almost everywhere.
4. For any finite positive sum of exponentials
\[
f(t)=\sum_{j=1}^Jp_j e^{-\lambda_jt},\qquad p_j\geq0,\quad \lambda_j>0,
\]
its Laplace transform \(F(s)=\sum_jp_j/(s+\lambda_j)\) satisfies the **sharp** minimax obstruction
\[
\boxed{\inf_{J,p_j\geq0,\lambda_j>0}\ \sup_{s\in[s_-,s_+]}|F(s)-\Psi(s)|
=\frac{\Psi(s_+)-\Psi(s_-)}2>0.}
\]
The infimum need not be attained by finite rates. It is approached by a single positive exponential with its rate tending to infinity.
5. Fix \(a\ne b\) and vary \(c\) through the unique tangency value \(c_*=(a/b)\exp[-2(a+b)/(a-b)]\). Writing \(\varepsilon=-\Theta\downarrow0\) from the sign-loss side, the two roots and timesteps exhibit the square-root opening
\[
x_{\pm}=\frac ba\left[1\pm\sqrt{\frac{2\varepsilon}{a+b}}+O(\varepsilon)\right],\qquad
h_{\mp}=\frac{a}{cb}\left[1\mp\sqrt{\frac{2\varepsilon}{a+b}}+O(\varepsilon)\right].
\]

These claims concern the first lag and positive-exponential approximation of the *Laplace symbol*, not the signs of all later quadrature weights or the accuracy of arbitrary signed or blockwise discrete-history compression.

## Assumptions and scope

All parameters and Laplace variables are numerical and dimensionless with a fixed reference scale, as in the specified symbol; the logarithms are of positive dimensionless quantities. Throughout, \(0<a,b<1\), \(c>0\), \(h>0\). The first lag is the coefficient of \(z^1\) in the exact, uncorrected backward-Euler generating series; computed FFT approximations to that coefficient are a separate matter. No hypothesis on the spatial discretization, nonlinear reaction or boundary conditions is required. Existence of the locally integrable Scarpi inversion is supplied by the cited foundational theory and by the motivating source's kernel proposition; positivity is **not** assumed.

## Proof

**Derivative identity.** Direct logarithmic differentiation, keeping the derivative of the order symbol, gives
\[
\frac{\Psi'(s)}{\Psi(s)}=-\frac{q(s/c)}{c(1+s/c)^2},\qquad
q(x)=ax+b/x+a+b+(a-b)\log(cx).
\]
Differentiating the generating series at zero shows
\[
\omega_1(h)=-\frac1h\Psi'(1/h)
=\frac{\Psi(1/h)}{ch(1+1/(ch))^2}\,q\!\left(\frac1{ch}\right).
\]
The prefactor is strictly positive; the entire sign problem is therefore exactly the scalar minimization problem for \(q\).

**Global minimum and all boundaries.** Differentiation and factorization yield
\[
q'(x)=\frac{(x+1)(ax-b)}{x^2}.
\]
The function strictly decreases to its sole critical point \(x_0=b/a\), then strictly increases. Since \(a,b>0\), \(q(x)\to+\infty\) both as \(x\downarrow0\) and \(x\uparrow\infty\). Its global minimum is
\[
q(b/a)=2(a+b)+(a-b)\log(cb/a)=\Theta.
\]
Consequently there are zero, one (tangent), or two positive roots according as \(\Theta\) is positive, zero or negative. Under the monotone bijection \(h=1/(cx)\) their location gives exactly the stated first-lag sign classification and the two unique endpoint formulas. This argument also covers \(a=b\), when \(\Theta=4a>0\), and never relies on sampling a finite step grid.

**Continuous kernel sign and quantitative obstruction.** Suppose \(\Theta<0\). On \((cx_-,cx_+)\), \(q<0\), hence \(\Psi'(s)>0\). A nonnegative inverse Laplace kernel would imply a nonincreasing transform on its domain of convergence; this contradicts strict increase. A nonpositive kernel would have a nonpositive transform, contradicting \(\Psi(s)>0\). The source's inverse-Laplace existence and integrability results justify both comparisons. Thus the continuous integral kernel must assume each sign on a set of positive measure.

Every positive-exponential transform \(F\) is nonincreasing, so if \(E=\sup_{[s_-,s_+]}|F-\Psi|\), then
\[
\Psi(s_+)-\Psi(s_-)\leq
|\Psi(s_+)-F(s_+)|+[F(s_+)-F(s_-)]+|F(s_-)-\Psi(s_-)|\leq2E.
\]
For the reverse inequality, put \(M=[\Psi(s_-)+\Psi(s_+)]/2>0\) and take \(F_\lambda(s)=M\lambda/(s+\lambda)\). This is the Laplace transform of \(M\lambda e^{-\lambda t}\), whose coefficient is nonnegative. As \(\lambda\to\infty\), \(F_\lambda\to M\) uniformly on the compact interval. Since \(\Psi\) increases on that interval, \(\sup|M-\Psi|=[\Psi(s_+)-\Psi(s_-)]/2\). This proves exact equality for the infimum (not a finite-parameter minimizer).

**Saddle-node boundary.** At \(c=c_*\), \(\Theta=0\) and \(x_0=b/a\) is a nondegenerate minimum, because
\[
q''(x_0)=\frac{a^2(a+b)}{b^2}=\frac{a+b}{x_0^2}>0.
\]
Taylor's formula in the relative coordinate \((x-x_0)/x_0\) gives
\[
0=-\varepsilon+\frac{a+b}{2}\left(\frac{x-x_0}{x_0}\right)^2+O\!\left(\left|\frac{x-x_0}{x_0}\right|^3\right).
\]
Solving its two simple branches yields the root expansion, then expanding \(1/(cx)\) yields the timestep expansion. For \(a<b\) the negative window exists on the \(c>c_*\) side; for \(a>b\) it exists on the \(c<c_*\) side.

## Verification

The exact witness \(a=1/5\), \(b=4/5\), \(c=10\) has
\[
\Theta=2-\frac35\log40=-0.21332767246836\ldots,
\]
\[
h_-=0.0136138923459052\ldots,\qquad h_+=0.0497864603752030\ldots,
\]
and \(\omega_1(1/40)=-0.0104835405750087\ldots\). On the increasing Laplace interval, \(\Psi(s_-)=0.301708449959596\ldots\) and \(\Psi(s_+)=0.310912411634484\ldots\). Thus **every** positive SOE Laplace-domain approximation has uniform error at least \(0.004601980837444\ldots\). This witness also meets the motivating paper's sector hypothesis because its left-hand side is at most \((2\pi/5)+(3/5)(1/e+(\log10)/2)<\pi\); here \(C_{\log}\leq1/e\) follows by the elementary substitution \(x\mapsto1/x\).

Run \(\texttt{python3 verify_scarpi.py}\) with a Python 3 standard library to reproduce deterministic derivative probes, exact-formula root brackets, sign tables, transition tangencies and positive-SOE error comparisons. The script gives supporting finite numerical checks; all all-parameter and all-step claims are proved above, not inferred from finite tests.

## Relationship to prior work

Yuan and Zegeling (2026, arXiv:2610.27262v1) define this exponential transition, the Scarpi transform and backward-Euler CQ weights in Sections 2 and 4, and analyze stability and accelerated blockwise SOE history computation. Their full-text statements supply the symbol and kernel-existence premises, but no classification of the sign of the exact first-lag weight or sharp positive-SOE Laplace approximation floor was identified in the inspected material. Their actual compression method permits general discrete block fits; this theorem **does not assert its failure**.

Garrappa and Giusti (2023) derive the same Scarpi symbol and develop numerical CQ weight calculation for exponential transitions; the inspected mathematical analysis and CQ sections do not state the new all-parameter sign-loss phase diagram and error floor. Garrappa, Giusti and Mainardi (2021) already explain loss of complete monotonicity in some variable-order **derivative** kernels; that broader phenomenon is not presented here as novel. Beghin, Cristofaro and Garrappa (2023) examine Bernstein-type conditions on variable-order relaxation equations, a related but different transfer function. The 2026 paper by Al-Mutairi, Furati and Garrappa on approximated Scarpi kernels is potentially relevant; full text was not accessible during this comparison. The resulting historical-priority risk remains explicit.

## Limitations

Only the uncorrected backward-Euler *first* history coefficient is classified; \(\Theta\geq0\) does not assert positivity of later weights or complete monotonicity of the kernel. The SOE bound concerns uniform error on the specified positive-real Laplace interval and only nonnegative exponential amplitudes and rates; signed or complex-exponential methods, time-domain fitting and the source's discrete blockwise compression are not ruled out. The sign-changing conclusion concerns the continuous integral kernel and relies on the established inverse-Laplace representation. The sharpness of the error bound is an infimum attained only in the limit of the exhibited sequence, not necessarily by a finite SOE. Historical novelty has not received independent verification.

## References

- P. Yuan and P. Zegeling, *Convolution Quadrature with Adaptive History Compression for Variable-Order Fractional Reaction–Diffusion Equations*, arXiv:2610.27262v1, first public October 19, 2026, https://arxiv.org/html/2610.27262v1.
- R. Garrappa and A. Giusti, *A Computational Approach to Exponential-Type Variable-Order Fractional Differential Equations*, Journal of Scientific Computing 96 (2023), article 63, https://doi.org/10.1007/s10915-023-02283-6.
- R. Garrappa, A. Giusti and F. Mainardi, *Variable-order fractional calculus: a change of perspective* (2021), arXiv:2102.09932, https://arxiv.org/abs/2102.09932.
- L. Beghin, L. Cristofaro and R. Garrappa, *Renewal processes linked to fractional relaxation equations with variable order* (2023), arXiv:2303.14743, https://arxiv.org/abs/2303.14743.
- N. Al-Mutairi, K. M. Furati and R. Garrappa, *Variable-order Scarpi operators with approximated kernels* (2026), https://doi.org/10.1007/s13540-026-00577-8 (full text not obtained for this review).
