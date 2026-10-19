# A metric-dependent relaxation front in nested Brownian resetting

## Finding

For the equal-rate nested Brownian resetting chain started at the origin, the marginal at depth \(n\) is an explicitly truncated gamma mixture of centered Gaussians. The exact one-Wasserstein distance from stationarity has a positive order-one limit on the \(\sqrt n\)-wide temporal wavefront, whereas total variation is of order \(n^{-1/2}\) at the same times. Their **distinct, sharp critical profiles** are expressed by a normal overshoot function. For every fixed real \(z\), with \(t_n(z)=(n+z\sqrt n)/r\),

\[
\lim_{n\to\infty} W_1(\mu_{n,t_n(z)},\mu_{n,*})
=\sqrt{\frac{D}{\pi r}}\,[\varphi(z)-z\Phi(-z)],
\]

and

\[
\lim_{n\to\infty}\sqrt n\,d_{\rm TV}(\mu_{n,t_n(z)},\mu_{n,*})
=\varphi(1)[\varphi(z)-z\Phi(-z)].
\]

Here \(\varphi\) and \(\Phi\) are the standard-normal density and cumulative distribution. The first result measures an **absolute displacement discrepancy** that survives at the front even while the second proves asymptotic indistinguishability under bounded position tests. These limits, including the constants, refer to the unrescaled physical position in the first distance and to the usual scale-invariant total variation in the second.

For every integer \(n\ge1\) and \(t>0\), an additional exact non-asymptotic identity holds:

\[
W_1(\mu_{n,t},\mu_{n,*})
=\sqrt{\frac{4D}{\pi r}}
\left[\frac{\Gamma(n+\frac12,rt)}{\Gamma(n)}
-\sqrt{rt}\,\frac{\Gamma(n,rt)}{\Gamma(n)}\right].
\]

Here \(\Gamma(a,x)=\int_x^\infty u^{a-1}e^{-u}\,du\) is the upper incomplete gamma function. This identity is interpreted directly, not by subtracting numerically rounded tail values when cancellation is severe.

The front is sharp at the macroscopic time scale: if \(t=sn/r\) for fixed \(s\in(0,1)\), then

\[
\lim_{n\to\infty}\frac{W_1(\mu_{n,sn/r},\mu_{n,*})}{\sqrt n}
=\sqrt{\frac{4D}{\pi r}}(1-\sqrt s),
\]

and

\[
\lim_{n\to\infty}d_{\rm TV}(\mu_{n,sn/r},\mu_{n,*})
=2\left[\Phi\left(\frac{x_s}{\sqrt s}\right)-\Phi(x_s)\right],
\qquad x_s=\sqrt{\frac{s\log(1/s)}{1-s}}.
\]

For fixed \(s>1\), both distances tend to zero. At \(s=1\), the two critical formulas with \(z=0\) give the sharper conclusions.

## Assumptions and scope

Take any \(D,r>0\). For each integer \(n\ge1\), consider \(n\) diffusing coordinates on the real line with independent standard Brownian drivers and diffusion generator \(D\partial_{xx}\). All coordinates start at zero. Each coordinate has its own independent rate-\(r\) Poisson clock. When coordinate one rings it is set to zero; when coordinate \(j\ge2\) rings it is set to the simultaneous position of coordinate \(j-1\). Let \(\mu_{n,t}\) be the law of coordinate \(n\) at time \(t\) and \(\mu_{n,*}\) its stationary marginal. Distances are between **one-coordinate marginals**, not between full joint laws.

Define \(G_n\) to have gamma density \(g^{n-1}e^{-g}/\Gamma(n)\) for \(g>0\), and let \(Z\) be a standard normal independent of \(G_n\). The previously established finite-time marginal identity [1, equation (2.10)] is equivalent to

\[
\mu_{n,t}=\mathcal L\left(\sqrt{\frac{2D}{r}\min(G_n,rt)}\,Z\right),
\qquad
\mu_{n,*}=\mathcal L\left(\sqrt{\frac{2D}{r}G_n}\,Z\right).
\]

The proof below begins from this previously published marginal formula and does not claim it as new. We write \(d_{\rm TV}(\mu,\nu)=\tfrac12\int|f-g|\,dx\) when densities exist, and \(W_1\) is transport cost with \(|x-y|\) on \(\mathbb R\). Limits take \(n\to\infty\) with fixed \(D,r\); \(z\) and \(s\) are fixed. The observation time \(t_n(z)\) is positive for sufficiently large \(n\), as required.

## Proof

**1. Exact transport identity.** Couple the two mixing variables by using the same \(G_n\). Since \(\min(G_n,rt)\le G_n\), for \(x>0\) each centered Gaussian in the truncated mixture has a cumulative distribution at \(x\) at least as large as the corresponding untruncated Gaussian; for \(x<0\) the inequality reverses. Therefore the difference of the two cumulative distributions has exactly one sign on each half-line. The one-dimensional integral formula for \(W_1\) and symmetry give the *equality*

\[
W_1(\mu_{n,t},\mu_{n,*})
=\mathbb E|X_{n,*}|-\mathbb E|X_{n,t}|
=\sqrt{\frac{4D}{\pi r}}\,\mathbb E\left[\sqrt{G_n}-\sqrt{\min(G_n,rt)}\right].
\]

This is an optimal-transport identity, not just a bound obtained from the coupling. Integrating the gamma tail gives the stated incomplete-gamma expression.

**2. Wasserstein front.** Put \(a_n=n+z\sqrt n\), \(H_n=(G_n-n)/\sqrt n\), and \(A(z)=\mathbb E[(Z-z)_+]=\varphi(z)-z\Phi(-z)\). Since \(G_n\) is a sum of \(n\) unit exponentials, \(H_n\Rightarrow Z\) and \(\sup_n\mathbb E H_n^2=1\). The identity

\[
\sqrt{G_n}-\sqrt{\min(G_n,a_n)}
=\frac{(G_n-a_n)_+}{\sqrt{G_n}+\sqrt{a_n}}
\]

shows that its expectation tends to \(A(z)/2\): on events where \(G_n/n\to1\) the denominator divided by \(\sqrt n\) tends to two, and the numerator divided by \(\sqrt n\) converges in distribution to \((Z-z)_+\); uniform integrability follows from the bounded second moments of \(H_n\), together with Cauchy–Schwarz and an exponentially small gamma-deviation complement. Multiplying by the exact prefactor proves the first front formula.

**3. Total-variation front.** Rescale positions by \(\sqrt{2Dn/r}\), which leaves total variation unchanged. Let \(h_v(x)=(2\pi v)^{-1/2}\exp[-x^2/(2v)]\), \(V_n=G_n/n\), and \(U_n=\min(G_n,a_n)/n\). The two rescaled marginal densities are \(\mathbb E h_{U_n}\) and \(\mathbb E h_{V_n}\). On the event \(|V_n-1|\le1/2\), both variances eventually belong to \([1/2,2]\); the first two variance derivatives of \(h_v\) are uniformly integrable in \(x\) on this compact variance interval. Taylor's formula in \(L^1(dx)\), combined with

\[
\mathbb E(U_n-V_n)
=-\frac1{\sqrt n}\,\mathbb E[(H_n-z)_+],
\qquad \mathbb E(V_n-1)^2=\frac1n,
\]

and \(\mathbb E(U_n-1)^2=O_z(n^{-1})\), gives

\[
\left\|\sqrt n\,[\mathbb E h_{U_n}-\mathbb E h_{V_n}]
+A(z)\,\partial_v h_v\big|_{v=1}\right\|_{L^1(dx)}\longrightarrow0.
\]

The complement \(|V_n-1|>1/2\) has exponentially small probability by a gamma Chernoff bound, and each Gaussian density has \(L^1\)-norm one; thus its contribution is negligible even after multiplying by \(\sqrt n\). Finally

\[
\partial_v h_v(x)\big|_{v=1}=\tfrac12(x^2-1)\varphi(x),
\quad
\tfrac12\int_{\mathbb R}\left|\partial_v h_v(x)\big|_{v=1}\right|\,dx
=\varphi(1).
\]

(The last equality follows by splitting the Gaussian integral at \(|x|=1\).) Taking one-half of the limiting \(L^1\)-norm proves the sharp total-variation coefficient.

**4. Macroscopic front.** For fixed \(s\in(0,1)\), gamma concentration yields \(G_n/n\to1\) in probability, and \(\min(G_n,sn)/n\to s\). In the same coupling as step 1, the expectation of the square-root difference divided by \(\sqrt n\) tends to \(1-\sqrt s\) by uniform integrability, proving the Wasserstein limit. After rescaling positions by \(\sqrt{2Dn/r}\), the two Gaussian variance mixtures converge in \(L^1\) to the centered normal densities of variances \(s\) and one: the densities converge pointwise by bounded continuity in the variance and have unit mass, so Scheffé's lemma applies. These two limiting densities cross only at \(\pm x_s\), hence their total-variation distance equals the stated Gaussian-cdf expression. For fixed \(s>1\), the *same* gamma variable gives an exact coupling of the distributions except on \(G_n>sn\). The latter probability decays exponentially, controlling total variation; the Wasserstein tail also vanishes by Cauchy–Schwarz and the same deviation bound. At \(s=1\), steps 2–3 with \(z=0\) apply.

## Verification

The standalone `verification/check.py` performs 53 reproducible numerical comparisons against the analytic identity and asymptotic formulas, using independent gamma-quantile quadrature, direct numerical integration of the difference of stationary and finite-time mixture densities, and tests on both sides of the macroscopic front. Execution: `python verification/check.py` with NumPy and SciPy installed. These finite checks supplement, but cannot prove, the statements for all \(n\), \(D\), \(r\), \(s\), or \(z\).

## Relationship to prior work

Britton, Le Jeune, Alston, Bressloff and Bertrand [1, Sec. 2.1 and Appendix A] derive the **full finite-time marginal density** (equation (2.10)), stationary marginals, and spatially resolved accumulation-time wavefronts. That explicit density, the gamma-mixture representation obtained by rewriting it, and the linear-in-depth relaxation delay are **not new claims here**. The present claim concerns the *exact optimal-transport distance* and the *simultaneous large-depth limiting profiles in two inequivalent probability metrics*, including the distinction between an order-one physical displacement error and a vanishing total variation at the same front time. The earlier Alston–Britton–Bertrand theory [2] supplies the original stationary nested-resetting model and correlations; its joint stationary results are not claimed as new. The fact that source [1]'s explicit marginal logically determines every distance means that the present result is an asymptotic and metric-geometric consequence of a previously solved forward model, not a new solution of that forward model.

## Limitations

The findings concern homogeneous Poisson reset rates, a single coordinate marginal, all-zero initial conditions, independent Brownian noises, and \(n\to\infty\) at fixed positive \(D,r\). They do not establish analogous profiles for heterogeneous reset rates, the full multivariate law, stronger pathwise metrics, or nonzero initial distributions. The exact finite-time density is published; the claim of an additional scientific contribution rests on the sharp **two-metric** limit and its interpretation, which may be implicitly contained in general normal-scale-mixture asymptotics. No independent scholarly originality assessment has been performed.

## References

[1] C. Britton, B. Le Jeune, H. Alston, P. C. Bressloff and T. Bertrand, *Approach to Steady-State in Nested Resetting Processes*, arXiv:2609.25252v1 (first public September 21, 2026), especially equation (2.10), Section 3 and Appendix A. https://arxiv.org/abs/2609.25252

[2] H. Alston, C. Britton and T. Bertrand, *Nested Stochastic Resetting: Nonequilibrium Steady States and Exact Correlations*, arXiv:2502.03225v1 (first public February 5, 2025), including its supplemental material. https://arxiv.org/abs/2502.03225
