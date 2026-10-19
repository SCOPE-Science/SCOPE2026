# Gaussian–Laplace product scaling under position-only resetting of Brownian-square diffusivity

## Finding

For an unreset Brownian stochastic diffusivity, resetting *position alone* does not produce a stationary position distribution. Instead, it induces a quantitative non-Gaussian scaling limit: the position divided by \(\sqrt t\) converges to a product of an independent Gaussian and Laplace random variable. The limiting law has a logarithmic density peak, a sharp \(2/3\)-power stretched-exponential tail and raw kurtosis \(18\). A deterministic diffusivity with the same mean and same resetting mechanism has the same limiting variance but a simple Laplace scaling limit with raw kurtosis \(6\).

Here is the exact statement. Fix \(r,\Lambda>0\), take independent standard Brownian motions \(B,W\), and an independent rate-\(r\) Poisson process. Write \(\omega_t=\sqrt2\Lambda B_t\) and evolve the position between resetting times by \(dX_t=2\Lambda B_t\,dW_t\), starting from \(X_0=0\). At each Poisson event set \(X_t=0\), without changing either \(B\) or the Brownian medium \(\omega\). The signed noise coefficient is equivalent in position law to the physical nonnegative coefficient \(\sqrt{2\omega_t^2}=2\Lambda|B_t|\), since both have the same conditional quadratic variation.

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

The Poisson clock is homogeneous and independent of both driving Brownian motions. Each event resets position to zero only; neither the medium variable nor its clock is renewed. The medium starts at zero, and the theorem holds for all \(r,\Lambda>0\). The result is one-dimensional. The displayed density is the law of the *scaled limiting variable*, not a stationary density for unscaled position. At every fixed time the characteristic function below is exact. Endpoint asymptotics apply to the *limiting* density after the limit \(t\to\infty\) is taken; no claim of uniform finite-time tail equivalence is made.

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

The self-contained `verify.py` performs 43 independent deterministic numerical/algebraic checks. They include discretized Gaussian covariance-determinant checks for the Feynman–Kac expression, comparison of finite-time characteristic functions with the closed limiting transform, direct integration of the exact variance, independent Gaussian-quadrature mixture evaluation, matched deterministic-model comparison, explicit coupling-bound calculations, and numerical checks of the logarithmic center and sharp tails. The code requires Python, NumPy and SciPy; run `python verify.py`. All checks were executed successfully. The rigorous statements above follow analytically; discretization and quadrature are not substitutes for proofs of continuum or asymptotic assertions.

## Relationship to prior work

Santra, Basu and Sabhapandit [1] introduced precisely the Brownian-square stochastic diffusivity and studied Poisson resetting of **both** the position and the diffusivity. Their whole-state renewal creates a true stationary position law, with a different stretched-exponential tail. Their free-process characteristic function provides a benchmark for the no-reset term here, but their full-reset renewal does not apply when the Brownian medium retains its history. Bodrova, Chechkin and Sokolov [2] analyzed position-only nonrenewal resetting of a **deterministic** time-dependent diffusivity, thereby covering the matched Laplace benchmark but not the stochastic-medium product law. Gupta [3] studies position resetting with an unreset **Ornstein–Uhlenbeck velocity** (a stationary internal process), rather than the unbounded Brownian-square diffusivity. The new claim is the explicit stochastic-medium product limit, its quantitative \(W_2\) rate, and sharp density diagnostics, not the basic reset-age identity or these earlier processes.

## Limitations

No claim of an exact unscaled stationary density is made; there is none. Only homogeneous Poisson position resetting, Brownian-square diffusivity, zero initial medium, and one-dimensional position are covered. The limiting density's tail asymptotic is taken after the large-time limit. The convergence bound is an upper bound, not a proved optimal rate. Equivalence to a broader published Gaussian-mixture or nonrenewal-reset theorem remains a priority risk; independent scientific validation has not been performed.

## References

[1] I. Santra, U. Basu and S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient* (2022), arXiv:2205.00549, https://arxiv.org/abs/2205.00549 (first public 2022-05-01).

[2] A. S. Bodrova, A. V. Chechkin and I. M. Sokolov, *Non-renewal resetting of scaled Brownian motion* (2018 preprint), arXiv:1812.05664, https://arxiv.org/abs/1812.05664.

[3] D. Gupta, *Stochastic resetting in underdamped Brownian motion* (2018), arXiv:1812.07227, https://arxiv.org/abs/1812.07227.
