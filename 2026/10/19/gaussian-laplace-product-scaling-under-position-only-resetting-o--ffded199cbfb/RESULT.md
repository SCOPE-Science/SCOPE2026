# Exact transient characteristic function under position-only resetting of Brownian-square diffusivity

## Finding

Fix \(r,\Lambda>0\), take independent standard Brownian motions \(B,W\), and an independent rate-\(r\) Poisson process. Write \(\omega_t=\sqrt2\Lambda B_t\) and evolve the position between resetting times by \(dX_t=2\Lambda B_t\,dW_t\), starting from \(X_0=0\). At each Poisson event set \(X_t=0\), leaving the Brownian medium \(\omega\) unchanged. The signed noise coefficient is equivalent in position law to the physical nonnegative coefficient \(2\Lambda|B_t|\), since both have the same conditional quadratic variation.

**Exact transient law.** For each \(t>0\), let \(A_t\) be the time since the last reset, set to \(t\) if no reset has occurred, and put \(w=2\Lambda|k|/\sqrt t\). The conditional characteristic function of \(X_t/\sqrt t\), at age \(a\in[0,t]\), has the version
\[
H_t(k,a)=[\cosh(wa)+(t-a)w\sinh(wa)]^{-1/2}.
\]
Consequently the characteristic function at every finite observation time is the one-dimensional single quadrature
\[
\varphi_t(k)=e^{-rt}\,[\cosh(wt)]^{-1/2}
+r\int_0^t \frac{e^{-ra}}{\sqrt{\cosh(wa)+(t-a)w\sinh(wa)}}\,da,
\qquad \varphi_t(0)=1.
\]
The term \((t-a)w\sinh(wa)\) records the inherited Brownian variance at the last position reset. It disappears if the medium is also reset, in which case the conditional kernel is \([\cosh(wa)]^{-1/2}\). Thus at every \(t>0\) and real \(k\ne0\), resetting position alone gives a strictly smaller characteristic function than resetting both position and medium, because the two kernels have identical no-reset terms and are strictly ordered at each interior age. The transient transform, not merely the limiting density or moments, distinguishes the protocols without assuming that the medium clock renews.

## Scaling benchmark and quantitative check

The following large-time laws give a benchmark for the transient formula. The one-time product limit and its density asymptotics are also covered by the same-protocol aging result [4]; they are not asserted as distinct contributions here.

Let \(Z\sim N(0,1)\) and \(L\sim\mathrm{Laplace}(0,1)\) (density \(e^{-|x|}/2\)) be independent, and set \(c=\sqrt2\Lambda/\sqrt r\), \(Y=cZL\). Then for all \(t>0\), with \(W_2\) denoting the quadratic Wasserstein distance,

\[
W_2\bigl(\mathcal L(X_t/\sqrt t),\mathcal L(Y)\bigr)
\le \frac{2\Lambda}{r\sqrt t}+\frac{2\Lambda}{\sqrt r}e^{-rt/2}.
\]

Thus \(X_t/\sqrt t\Rightarrow Y\), with convergence of every fixed absolute moment. Every fixed bounded interval carries vanishing position probability as \(t\to\infty\).

The limiting density, for \(y\ne0\), is

\[
f(y)=\frac{1}{c\sqrt{2\pi}}\int_0^\infty \frac1z
\exp\left(-\frac{z^2}{2}-\frac{|y|}{cz}\right)\,dz.
\]

Its precisely normalized endpoint laws are

\[
f(y)=\frac{1}{c\sqrt{2\pi}}\left[\log\frac{c}{|y|}+O(1)\right],\quad y\to0,
\]
\[
f(y)\sim\frac{1}{c\sqrt3}\left(\frac{|y|}{c}\right)^{-1/3}
\exp\left[-\frac32\left(\frac{|y|}{c}\right)^{2/3}\right],\quad |y|\to\infty.
\]

All even moments have the exact form, for integers \(m\ge1\),

\[
\mathbb E[Y^{2m}]=\left(\frac{4\Lambda^2}{r}\right)^m m!\bigl((2m-1)!!\bigr)^2,
\]

in particular \(\mathbb E[Y^2]=4\Lambda^2/r\) and \(\mathbb E[Y^4]/\mathbb E[Y^2]^2=18\).

## Assumptions and scope

The Poisson clock is homogeneous and independent of both driving Brownian motions. Each event resets position to zero only; neither the medium variable nor its clock is renewed. The medium starts at zero, and the theorem holds for all \(r,\Lambda>0\). The result is one-dimensional. The displayed density is the law of the *scaled limiting variable*, not a stationary density for unscaled position. The characteristic function in the Finding is exact at every positive observation time. Endpoint asymptotics apply to the *limiting* density after the limit \(t\to\infty\) is taken; no claim of uniform finite-time tail equivalence is made.

## Proof

**Poisson age and exact finite-time characteristic function.** Let \(A_t\) be the time elapsed since the last Poisson reset, with \(A_t=t\) if none has occurred. At each fixed \(t>0\), \(A_t\) is independent of \(B,W\) and has the law \(E\wedge t\), where \(E\sim\mathrm{Exp}(r)\). Consequently

\[
X_t=2\Lambda\int_{t-A_t}^{t}B_s\,dW_s.
\]

Conditional on \(A_t=a\) and \(B\), the characteristic function of \(X_t/\sqrt t\) is \(\exp[-(2\Lambda^2 k^2/t)\int_{t-a}^{t}B_s^2\,ds]\). For \(q\ge0\), the Feynman–Kac harmonic-oscillator formula for standard Brownian motion started at \(b\) reads

\[
\mathbb E_b\exp\left(-q\int_0^a B_s^2\,ds\right)=
\frac{\exp\bigl[-\frac12b^2\sqrt{2q}\tanh(a\sqrt{2q})\bigr]}{\sqrt{\cosh(a\sqrt{2q})}}.
\]

To verify this directly, the right-hand side solves \(\partial_a u=\frac12\partial_{bb}u-qb^2u\) with \(u(0,b)=1\). Since \(B_{t-a}\sim N(0,t-a)\), Gaussian integration then yields, putting \(w=2\Lambda|k|/\sqrt t\),

\[
H_t(k,a)=\left[\cosh(wa)+(t-a)w\sinh(wa)\right]^{-1/2}.
\]

Thus the exact finite-time characteristic function is

\[
\varphi_t(k)=e^{-rt}[\cosh(wt)]^{-1/2}
+r\int_0^t e^{-ra}[\cosh(wa)+(t-a)w\sinh(wa)]^{-1/2}\,da,
\]

with its continuous value \(\varphi_t(0)=1\).

**Quantitative coupling and all moments.** Compare the stochastic integral with its frozen-medium approximation:

\[
\frac{X_t}{\sqrt t}=
2\Lambda\frac{B_t}{\sqrt t}(W_t-W_{t-A_t})+R_t,
\quad
R_t=\frac{2\Lambda}{\sqrt t}\int_{t-A_t}^t(B_s-B_t)\,dW_s.
\]

The Brownian medium is independent of \(W\), so Itô isometry remains applicable after conditioning on its entire path. It gives

\[
\mathbb E[R_t^2]=\frac{4\Lambda^2}{t}\mathbb E[A_t^2/2]
\le\frac{4\Lambda^2}{r^2t}.
\]

The normalized increment \((W_t-W_{t-A_t})/\sqrt{A_t}\) is standard Gaussian, independent of \(A_t\) and of \(B_t/\sqrt t\). Thus the principal term can be coupled with \(2\Lambda Z\sqrt E\,G\), for independent standard normals \(Z,G\), by using \(A_t=E\wedge t\). Its additional mean-square coupling error is bounded by

\[
4\Lambda^2\mathbb E\bigl[(\sqrt E-\sqrt{E\wedge t})^2\bigr]
\le4\Lambda^2\mathbb E[(E-t)_+]
=\frac{4\Lambda^2}{r}e^{-rt}.
\]

The triangle inequality in \(L^2\) proves the stated \(W_2\) bound. The Gaussian variance-mixture identity \(\sqrt E\,G\stackrel d=L/\sqrt{2r}\) proves the product representation. All fixed absolute moments converge: conditional Gaussian moment formulas and Jensen's inequality give \(\sup_{t\ge1}\mathbb E|X_t/\sqrt t|^p<\infty\) for every fixed \(p>0\) (use \(\mathbb E[(E\wedge t)^m]\le m!/r^m\) for integer \(m\) and Gaussian Brownian moment bounds). This also supplies uniform integrability at each order.

Since \(Y\) has a continuous law with no atom at zero, \(\mathbb P(|X_t|\le M)\to0\) for each fixed \(M>0\). Therefore no unscaled stationary spatial probability distribution exists.

**Limiting density and its edges.** Conditional on \(|Z|=z\), \(cZL\) is Laplace with scale \(cz\). Integrating against the half-normal law gives the displayed density integral. For \(|y|/c=x\downarrow0\), the interval \(x<z<1\) contributes \(\log(1/x)+O(1)\); the complementary pieces contribute bounded terms. For \(x\to\infty\), set \(z=x^{1/3}v\). The phase is \(x^{2/3}(v^2/2+1/v)\), uniquely minimized at \(v=1\) with value \(3/2\) and second derivative \(3\). Laplace's method gives exactly the displayed \(1/\sqrt3\) prefactor and \(x^{-1/3}\) power. Product moments of a standard Gaussian and unit-scale Laplace yield the even-moment expression.

**Exact variance and a matched-medium contrast.** Independently of the limit, conditional Itô isometry and \(\mathbb E B_s^2=s\) show

\[
\operatorname{Var}(X_t)=\frac{4\Lambda^2}{r^2}\bigl(rt-1+e^{-rt}\bigr).
\]

Replace the random diffusivity by its same-time mean \(D_{\rm det}(t)=\mathbb E[\omega_t^2]=2\Lambda^2t\) and retain precisely the same position-resetting Poisson clock. Conditional on age \(a\), the deterministic process has variance \(4\Lambda^2(ta-a^2/2)\); after division by \(\sqrt t\), its law converges to a centered Laplace distribution with scale \(c=\sqrt2\Lambda/\sqrt r\). Its raw kurtosis is \(6\), whereas the random medium's is \(18\), even though both limiting variances are \(4\Lambda^2/r\).

## Verification

The self-contained `verify.py` specifies 43 deterministic numerical/algebraic checks, including discretized Gaussian covariance-determinant checks for the finite-time expression, comparison with the limiting transform, integration of the variance, the matched deterministic model, and density and coupling checks. The code requires Python, NumPy and SciPy; run `python verify.py`. The rigorous statements above follow analytically; discretization and quadrature are not substitutes for proofs of continuum or asymptotic assertions.

## Relationship to prior work

Santra, Basu and Sabhapandit [1] studied this stochastic diffusivity with **both** position and medium reset. Their free-process characteristic function provides the \(a=t\) benchmark but does not describe the extra inherited-variance term at \(0<a<t\). Bodrova, Chechkin and Sokolov [2] studied the position-only protocol for a **deterministic** time-dependent diffusivity and cover the matched deterministic benchmark. Gupta [3] retains an Ornstein–Uhlenbeck velocity rather than a Brownian-square diffusivity. The same-protocol result [4] contains the one-time scaling law, density core and tail, finite-time moment calculations, and the Brownian freezing estimate underlying the \(W_2\) bound. Its aging and one-time scaling statements do not evaluate the age-conditioned Fourier kernel at finite time. The claim defended here is that exact transient kernel and its Poisson mixture. The Gaussian–Laplace product, moment comparison and quantitative scaling bound are contextual consequences, not separately asserted as novel.

## Limitations

Only homogeneous Poisson position resetting, Brownian-square diffusivity, zero initial medium, and one-dimensional position are covered. The characteristic function gives the transient law; a closed-form inverse transform or uniform finite-time tail asymptotic is not asserted. The convergence bound is an upper bound, not a proved optimal rate. Broader Gaussian quadratic-functional or nonrenewal-reset results may yield equivalent formulas; historical priority is not certified.

## References

[1] I. Santra, U. Basu and S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient* (2022), arXiv:2205.00549, https://arxiv.org/abs/2205.00549 (first public 2022-05-01).

[2] A. S. Bodrova, A. V. Chechkin and I. M. Sokolov, *Non-renewal resetting of scaled Brownian motion* (2018 preprint), arXiv:1812.05664, https://arxiv.org/abs/1812.05664.

[3] D. Gupta, *Stochastic resetting in underdamped Brownian motion* (2018), arXiv:1812.07227, https://arxiv.org/abs/1812.07227.

[4] *Persistent aging correlations under position-only resetting of Brownian diffusivity*, Resultary a81738fe04a3, [Finding and proof](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-persistent-aging-correlations-under-position-only-resetting-of-b--a81738fe04a3/RESULT.md).
