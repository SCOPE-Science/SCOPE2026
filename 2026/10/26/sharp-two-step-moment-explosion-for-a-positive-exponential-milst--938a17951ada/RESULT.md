# Sharp two-step moment explosion for a positive exponential Milstein scheme

## Finding

**Theorem (sharp numerical-moment frontier).** Fix \(a\ge 0\), \(\sigma>0\), \(p\ge 1\), a deterministic \(x_0>0\), and a constant step size \(h>0\). Consider the Itô SDE
\[
 dY_t=-aY_t\,dt+\frac{\sigma Y_t^2}{1+Y_t}\,dB_t,\qquad Y_0=x_0.
\]
Apply the first-order positive exponential scheme of Bréhier and Cohen (2026), defined precisely below, with independent Brownian increments, and denote its iterates by \(X_n\). Then the exact solution and every numerical iterate are almost surely strictly positive, and the exact solution has finite \(p\)-th moments at every finite time. In contrast, the numerical moments obey the **sharp dichotomy**
\[
\begin{aligned}
 ph\sigma^2<\frac{27}{4}&\ \Longrightarrow\ \mathbb E[X_n^p]<\infty\quad\text{for every }n\ge0,\\
 ph\sigma^2\ge\frac{27}{4}&\ \Longrightarrow\ \mathbb E[X_n^p]=\infty\quad\text{for every }n\ge2.
\end{aligned}
\]
At the critical equality, \(\mathbb E[X_1^p]=\infty\) exactly when \(x_0=2\); if \(x_0\ne2\), the first moment of order \(p\) is finite but the second iterate already has infinite \(p\)-th moment. More generally, for every \(h>0\), \(\mathbb E[X_1^p]\) is finite exactly when
\[
 ph\sigma^2\frac{x_0^2}{(1+x_0)^3}<1.
\]
In particular, with \(a=1\), \(\sigma=3\), \(p=1\), \(h=3/4\), and \(x_0=1\), the first numerical expected value is finite and the second is infinite, whereas \(\mathbb E[Y_{2h}]=e^{-3/2}\).

## Assumptions and scope

The drift and diffusion are \(G(x)=-ax\) and \(g(x)=\sigma x^2/(1+x)\) for \(x\ge0\). Both are twice continuously differentiable, vanish at zero, have bounded first and second derivatives, and have at most linear growth. The coefficients therefore meet the regularity assumptions of the cited scheme; no nonglobally Lipschitz or superlinear-growth mechanism is used.

Define \(F(x)=G(x)/x=-a\), \(f(x)=g(x)/x=\sigma x/(1+x)\) for positive \(x\), with the continuous extensions at zero. Put
\[
q(x)=f'(x)g(x)=\frac{\sigma^2x^2}{(1+x)^3},\qquad
Z_n=\frac{B_{(n+1)h}-B_{nh}}{\sqrt h}\sim N(0,1).
\]
The \(Z_n\) are independent. The exact-arithmetic positive first-order scheme, not its lower-order variant, is
\[
X_{n+1}=X_n\exp\!\left[-ah+f(X_n)\sqrt h\,Z_n+\frac{q(X_n)h}{2}(Z_n^2-1)-\frac{f(X_n)^2h}{2}\right].
\]
All statements concern a fixed \(p\ge1\), any finite iterate index, and one constant step size; they do not assert a weak-order or long-time stability rate.

## Proof

**1. The underlying SDE has all finite-time moments.** Direct differentiation gives bounded first and second derivatives of \(G\) and \(g\), so standard Lipschitz SDE moment estimates give \(\mathbb E[Y_t^r]<\infty\) for every finite \(r\ge1\) and \(t<\infty\). Since \(g(x)=xf(x)\), \(f\) is bounded, and \(G(x)=xF(x)\), the logarithmic stochastic equation up to any possible hitting of zero has bounded drift and volatility; it cannot attain \(-\infty\) in finite time. Thus \(Y_t>0\) almost surely when \(x_0>0\). Every numerical step is strictly positive by its exponential formula.

**2. Exact conditional-moment criterion.** Conditional on \(X_n=x>0\), the Gaussian integral gives, writing \(\delta_p(x)=1-phq(x)\),
\[
\mathbb E[X_{n+1}^p\mid X_n=x]=x^p\exp\!\left[-pah-\frac{ph}{2}(q(x)+f(x)^2)\right]
\frac{\exp\!\left(\frac{p^2f(x)^2h}{2\delta_p(x)}\right)}{\sqrt{\delta_p(x)}}
\quad\text{if }\delta_p(x)>0.
\]
The same conditional moment is infinite if \(\delta_p(x)\le0\). Indeed, after multiplying by the standard normal density the exponent is a quadratic in \(Z_n\) with coefficient \(-\delta_p(x)/2\), so its integral converges if and only if \(\delta_p(x)>0\). This is a one-dimensional Gaussian identity; the earlier article already uses the finite-case identity for its sufficient small-step moment estimates.

**3. Finite-moment side.** Differentiation yields
\[
q'(x)=\frac{\sigma^2 x(2-x)}{(1+x)^4},\qquad
\max_{x\ge0}q(x)=q(2)=\frac{4\sigma^2}{27}.
\]
If \(ph\sigma^2<27/4\), then \(\delta_p(x)\ge1-4ph\sigma^2/27>0\) uniformly in \(x\ge0\). Also \(0\le f(x)\le\sigma\), so Step 2 bounds the conditional moment by \(C_{p,h,a,\sigma}X_n^p\) with a finite constant independent of \(X_n\). Iterating from deterministic \(x_0\) proves finiteness at every finite index.

**4. The first numerical step reaches the critical region from every initial value.** Fix \(x_0>0\). The logarithm of the step multiplier is a strictly convex quadratic in \(Z_0\), since \(q(x_0)>0\). Its minimum occurs at \(-f(x_0)/(q(x_0)\sqrt h)\), so \(X_1\) has support
\[
[m(x_0),\infty),\qquad m(x_0)=x_0\exp\!\left[-ah-\frac h2(q(x_0)+f(x_0)^2)-\frac{f(x_0)^2}{2q(x_0)}\right].
\]
The identity \(f(x)^2/q(x)=1+x\) and the elementary maximum \(\sup_{x>0}x e^{-(1+x)/2}=2e^{-3/2}<2\) give \(m(x_0)<2\). The change-of-variables formula for a nondegenerate quadratic of a standard Gaussian shows that \(X_1\) has a continuous, strictly positive density on \((m(x_0),\infty)\), in particular on a neighborhood of \(2\).

**5. Supercritical explosion.** If \(ph\sigma^2>27/4\), the set \(\{x:phq(x)>1\}\) contains an open interval about \(2\). Step 4 assigns this interval positive probability at the first iteration. The conditional \(p\)-moment in Step 2 is infinite throughout that interval, hence \(\mathbb E[X_2^p]=\infty\).

**6. Explosion at the exact boundary.** At \(ph\sigma^2=27/4\), the function \(\delta_p\) is positive away from \(x=2\), but its minimum is a quadratic zero:
\[
\delta_p(x)=\frac{(x-2)^2}{12}+O((x-2)^3),\qquad x\to2.
\]
Because \(f(2)=2\sigma/3>0\), the finite-case conditional-moment formula from Step 2 grows near \(x=2\) at least as fast as \(c_1\exp(c_2/(x-2)^2)\), for positive constants \(c_1,c_2\). Integrating against the strictly positive continuous density of \(X_1\) from Step 4 yields \(\mathbb E[X_2^p]=\infty\), even though \(\mathbb P(X_1=2)=0\). The one-step claim follows directly from Step 2 and uniqueness of the maximum of \(q\).

**7. Persistence of infinite moments.** For each \(x>0\), Jensen's inequality applied to the random exponent gives the uniform lower bound
\[
\mathbb E[X_{n+1}^p\mid X_n=x]\ge x^p\exp\!\left[-pah-\frac{ph}{2}f(x)^2\right]\ge e^{-pah-ph\sigma^2/2}x^p.
\]
This inequality holds also when the left-hand side is infinite. Thus once \(\mathbb E[X_2^p]=\infty\), every later \(p\)-moment is infinite. The dichotomy is proved. \(\square\)

## Verification

The included `verify.py` checks the coefficient factorization, the exact derivative and maximum of \(q\), the double-zero coefficient \(1/12\) at the critical boundary, the first-step support inequality, and exact-rational test points. It independently integrates the Gaussian step density using high-precision quadrature and compares the results with the conditional-moment formula for subcritical parameters. Execution passes **176 numerical/exact-rational checks plus symbolic identities**. Infinite-moment assertions are established analytically by the nonintegrability arguments in Steps 5–7; they are not claims based on Monte Carlo samples.

## Relationship to prior work

Bréhier and Cohen (2026, arXiv:2608.25689v1) introduce the positive strong-order-one exponential method, derive its Gaussian exponential-moment identity in Proposition 9, and prove sufficient moment bounds for sufficiently small steps. **Neither the integrator nor the Gaussian integral is new.** Their results do not state the sharp necessary-and-sufficient all-iterate threshold on the admissible nonlinear diffusion above, nor the exact-boundary two-step moment explosion from *every* positive starting state. The latter uses a global optimization and a nontrivial reachability-and-nonintegrability argument.

The companion bounded-domain construction of Bréhier and Cohen (2026, arXiv:2608.25685) uses a different state space and separately bounds Gaussian-quadratic exponentials for small steps. Earlier exponential/GBM integrators (Erdoğan and Lord, 2021) principally use exponentials of Brownian increments from linear multiplicative flows. The logarithmically transformed truncated Euler method of Yi, Hu, and Zhao (2020) uses yet another update. These results do not by themselves give the asserted global two-step threshold for this specific scheme.

## Limitations

The threshold concerns the stated saturated nonlinear scalar diffusion and the specified first-order scheme in exact arithmetic. It does not establish divergence for the original SDE or for the source's lower-order positive scheme, nor does it apply automatically to vector-valued, truncated-Gaussian, adaptive, or finite-precision implementations. Its novelty has only been compared with the identified literature and mathematical research records; unlocated specialized prior analyses of quadratic-Gaussian exponentials remain possible.

## References

1. C.-E. Bréhier and D. Cohen, *Analysis of a first-order explicit positivity preserving scheme for a class of scalar SDEs*, arXiv:2608.25689v1, first posted 2026-08-26. https://arxiv.org/html/2608.25689v1 . In particular scheme (3), assumptions in Section 2, and Proposition 9.
2. C.-E. Bréhier and D. Cohen, *Explicit domain preserving numerical schemes for a class of stochastic differential equations*, arXiv:2608.25685v2, first posted 2026-08-26. https://arxiv.org/html/2608.25685v2 .
3. U. Erdoğan and G. J. Lord, *Strong Convergence of a GBM Based Tamed Integrator for SDEs and an Adaptive Implementation*, arXiv:2106.11425v1, first posted 2021-06-21. https://arxiv.org/abs/2106.11425 .
4. Y. Yi, Y. Hu and J. Zhao, *Positivity preserving logarithmic Euler-Maruyama type scheme for stochastic differential equations*, arXiv:2010.16321v1, first posted 2020-10-30. https://arxiv.org/abs/2010.16321 .
