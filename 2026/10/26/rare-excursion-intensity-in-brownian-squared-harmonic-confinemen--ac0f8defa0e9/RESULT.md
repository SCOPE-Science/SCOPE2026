# Rare-excursion intensity in Brownian-squared harmonic confinement

## Finding

Let \(X_t\) solve the nonstationary, randomly confined Brownian-particle model below. Its full distribution concentrates at zero, but **fixed nonzero displacements remain observable on an exact \(t^{-1/2}\) probability scale**. For every threshold \(u>0\),
\[
\lim_{t\to\infty}\sqrt t\,\mathbb P(|X_t|>u)
=J_{\kappa,\sigma}(u)
=\frac1{\sqrt{2\pi}}\int_{\mathbb R}
\mathbb E\!\left[\operatorname{erfc}\!\left(\frac{u}{\sqrt{2V_a}}\right)\right]da,
\]
where the positive random variances \(V_a\) are defined below. The integral is finite and strictly positive. Its singular small-threshold behavior is **universal in the baseline stiffness**:
\[
\boxed{\lim_{u\downarrow0}u J_{\kappa,\sigma}(u)=\frac{2}{\pi\sqrt\sigma}.}
\]
More strongly, \(\sqrt t\,\mathcal L(X_t)\) converges vaguely on \(\mathbb R\setminus\{0\}\) to a strictly positive, locally finite Gaussian-mixture intensity measure \(\mathcal M\), explicitly given below. This is a rare-excursion limit at fixed physical displacement, **not** the already known Cauchy central scaling of \(\sqrt t X_t\). The two regimes have the same matching coefficient, but convergence of the latter does not imply the former.

## Assumptions and scope

Take independent standard Brownian motions \(B,W\), constants \(\kappa,\sigma>0\), and deterministic \(x_0\in\mathbb R\). Set \(A_t=B_t\) and
\[
dX_t=-(\kappa+\sigma A_t^2)X_t\,dt+\sqrt2\,dW_t,
\qquad X_0=x_0,\quad A_0=0.
\]
The stochastic driving uses the Itô convention, with \(\mathbb E B_t^2=t\) and \(\mathbb E W_t^2=t\). Let \(Z\) denote an independent standard normal. For each \(a\in\mathbb R\), let \(B^{(a)}_s=a+\widetilde B_s\), where \(\widetilde B\) is a fresh standard Brownian motion, and define
\[
V_a=2\int_0^\infty \exp\!\left[-2\kappa s-2\sigma\int_0^s (B^{(a)}_v)^2dv\right]ds.
\]
Almost surely \(0<V_a\le1/\kappa\). Define, for Borel \(E\subset\mathbb R\setminus\{0\}\),
\[
\mathcal M(E)=\frac1{\sqrt{2\pi}}\int_{\mathbb R}\mathbb P(\sqrt{V_a}Z\in E)\,da.
\]
This is locally finite away from zero but has infinite total mass. The first-public-source date of the motivating dynamical model is 2026-09-27. The primary classification is 82C31 (statistical-mechanical transport and stochastic motion).

## Proof

**1. Exact conditional Gaussian representation.** Writing \(K_t=\kappa t+\sigma\int_0^t A_v^2dv\), the integrating-factor formula gives \(X_t\), conditionally on \(A\), as a Gaussian with mean \(m_t=x_0e^{-K_t}\) and variance
\[
V_t=2\int_0^t e^{-2\kappa s-2\sigma\int_{t-s}^t A_v^2dv}\,ds.
\]
In particular \(\lvert m_t\rvert\le\lvert x_0\rvert e^{-\kappa t}\) and \(0<V_t\le1/\kappa\). The decaying mean does not influence the intensity: for any bounded Lipschitz test \(f\), the difference from replacing \(X_t\) with \(\sqrt{V_t}Z\) is at most \(\|f\|_{\mathrm{Lip}}\lvert x_0\rvert e^{-\kappa t}\), whose \(\sqrt t\)-multiple vanishes.

**2. Brownian reversal with an exact endpoint weight.** Write \(p_s(y)=(2\pi s)^{-1/2}e^{-y^2/(2s)}\). For \(0<s<t\) and every nonnegative functional \(F\) of the last \(s\) units of environment, the Markov property, Brownian transition symmetry and reversal of the finite segment give
\[
\mathbb E F(A_t,(A_{t-v})_{0\le v\le s})
=\int_{\mathbb R} da\,\mathbb E_a[F(a,(B^{(a)}_v)_{v\le s})p_{t-s}(B^{(a)}_s)].
\]
For fixed \(a,s\), \(\sqrt t\,p_{t-s}(B^{(a)}_s)\to(2\pi)^{-1/2}\). For \(t\ge2s\) it is bounded by \(\pi^{-1/2}\). The exact harmonic Feynman–Kac integral is, with \(c=2\sqrt\sigma\),
\[
F_s(a):=\mathbb E_a e^{-2\sigma\int_0^s (B^{(a)}_v)^2dv}
=\frac{\exp[-\sqrt\sigma\,a^2\tanh(cs)]}{\sqrt{\cosh(cs)}}
\]
and integration of its Gaussian dependence on \(a\) gives
\[
\int_{\mathbb R}F_s(a)\,da
=\sqrt{\frac{2\pi}{c\sinh(cs)}}.
\]
This is locally proportional to \(s^{-1/2}\) near zero and exponentially decreasing at infinity. In particular,
\(\int_{\mathbb R}\mathbb EV_a\,da<\infty\), and \(\mathcal M\) is finite outside every neighborhood of the origin by Chebyshev's inequality.

**3. Local convergence and tail control.** The reversal identity and Feynman–Kac formula give, for each fixed finite environment window, convergence of the weighted endpoint mixture to Lebesgue measure in \(a\), times Brownian motion started at \(a\). The remaining late-window covariance is uniformly integrable. Indeed, using the exact unconditional expression
\[
\mathbb E e^{-2\sigma\int_{t-s}^t A_v^2dv}
=\left[\cosh(cs)+c(t-s)\sinh(cs)\right]^{-1/2},
\]
its \(\sqrt t\)-multiple is at most \(\sqrt{2/[c\sinh(cs)]}\) for \(0<s\le t/2\), and at most \(\sqrt{2t}\,e^{-cs/2}\) for \(t/2<s<t\). The \(e^{-2\kappa s}\) factor makes both terms uniformly integrable away from finite \(s\). Hence, for every \(R>0\),
\[
\lim_{t\to\infty}\sqrt t\,\mathbb E[V_t;|A_t|>R]
=\frac1{\sqrt{2\pi}}\int_{|a|>R}\mathbb EV_a\,da.
\]
The right side tends to zero as \(R\to\infty\). On bounded endpoint intervals, Brownian bridge convergence and dominated convergence show that \(V_t\) under the weighted endpoint measure tends in distribution to \(V_a\). Applied to centered Gaussian test functions, these facts prove the claimed vague measure limit. Since \(\sqrt t\,\mathbb E X_t^2\) stays bounded, \(\sqrt t\,\mathbb P(|X_t|>R)\le C/R^2\) uniformly at large \(t\). Therefore vague convergence upgrades to the two-sided exceedance formula for every fixed \(u>0\); the limiting Gaussian mixtures have no boundary atoms. Positivity follows because \(V_a>0\) almost surely.

**4. Universal inner boundary of the fixed-threshold intensity.** The displayed Feynman–Kac expression, split into \(s\in(0,1)\) and \(s\ge1\), implies \(\mathbb EV_a\le C_{\kappa,\sigma}/(1+a^2)\): on \((0,1)\), \(\tanh(cs)\ge d s\); on \([1,\infty)\) it is bounded below by a positive constant. For every fixed \(b\ne0\), Brownian scaling in the defining integral shows
\[
\frac{V_{b/u}}{u^2}\ \xrightarrow[u\downarrow0]{\mathbb P}\ \frac1{\sigma b^2}.
\]
For clarity, under \(s=u^2v\) the process is \(b+u^2\widetilde B_v\) inside the integrated square. With probability tending to one its absolute value stays above \(\lvert b\rvert/2\) for \(0\le s\le1\); the contribution beyond \(s=1\), after division by \(u^2\), is at most \(e^{-\sigma b^2/(2u^2)}/(\kappa u^2)\), and compact rescaled intervals converge by dominated convergence. Thus the entire integral converges as stated.

Change variables \(a=b/u\) in \(uJ(u)\). The integrand converges at \(b\ne0\) to \(\operatorname{erfc}(|b|\sqrt{\sigma/2})\). For \(\lvert b\rvert\le1\) it is bounded by one; for \(\lvert b\rvert>1\), the centered Gaussian second-moment bound and \(\mathbb EV_{b/u}\le C/(1+b^2/u^2)\) bound it by \(C/b^2\). Dominated convergence yields
\[
\lim_{u\downarrow0}uJ(u)
=\frac1{\sqrt{2\pi}}\int_{\mathbb R}\operatorname{erfc}(|b|\sqrt{\sigma/2})\,db
=\frac{2}{\pi\sqrt\sigma}.
\]

**5. Moment consistency (not an alternative proof of the intensity).** For every integer \(n\ge1\), the finite upper bound \(V_t\le1/\kappa\) allows the same endpoint argument with \(V_t^n\); mean terms vanish exponentially. Consequently
\[
\lim_{t\to\infty}\sqrt t\,\mathbb E X_t^{2n}
=\frac{(2n-1)!!}{\sqrt{2\pi}}\int_{\mathbb R}\mathbb EV_a^n\,da.
\]
For \(n=1\), inserting the exact Feynman–Kac integral reduces the coefficient to
\[
\frac{\sqrt\pi\,\Gamma(\kappa/(2\sqrt\sigma)+1/4)}
{2\sigma^{3/4}\Gamma(\kappa/(2\sqrt\sigma)+3/4)},
\]
which agrees with the second-moment coefficient published for this model.

## Verification

The standalone `verify_intensity.py` uses direct quadrature to compare the Feynman–Kac-integrated second-moment coefficient with its Gamma-function reduction at three independent parameter choices; it checks convergence of the exact finite-time second moment to the predicted coefficient at increasing times; and it independently integrates the error-function expression for the universal singular constant. All 12 asserted checks passed on the package code. These numerical checks concern finite identities and consistency only; the infinite-time and small-threshold statements are justified in the proof above.

## Relationship to prior work

Gupta and Klapp, arXiv:2609.33751v1 (2026-09-27), study this identical Brownian-squared stiffness model, derive its conditional Gaussian Fourier representation and exact first-fourth moments, and show the even-moment \(t^{-1/2}\) decay. These starting results are **not** claimed here. Cocconi, Alston, Romano and Bertrand, arXiv:2405.09460 (2024-05-15), treat OU-type fluctuating harmonic stiffness, a stationary environment rather than the present nonstationary squared-Brownian stiffness. Gupta and Klapp, arXiv:2507.20915 (2025-07-28), study *stationary Ornstein–Uhlenbeck* stiffness fluctuations.

An earlier Brownian-power stiffness limit establishes that \(\sqrt t X_t\) has a Cauchy limit at power two, with Cauchy-tail coefficient \(2/(\pi\sqrt\sigma)\) under the present diffusion normalization. That result is fully acknowledged; it **does not assert the order-\(t^{-1/2}\) fixed-positive-threshold probabilities** or the Gaussian-mixture intensity measure. Its tail coefficient agrees with the new sequential \(u\downarrow0\) limit, as it should. The sharp boundary between the two results is an interchange of the growing displacement threshold and the time limit; weak convergence alone cannot justify that interchange. More general rare-event intensity theorems for time-inhomogeneous random environments remain a possible originality risk.

## Limitations

Both stiffness parameters are strictly positive and constant, the environment is an *unconfined Brownian motion squared*, the two noises are independent, and the thermal diffusion coefficient is normalized to one. The proof does not give a uniform simultaneous law when \(u=u(t)\to0\), does not compute the intensity integral in elementary closed form for fixed \(u\), and does not analyze random initial conditions depending on \(t\). No independent audit or external certification is claimed.

## References

1. D. Gupta and S. H. L. Klapp, *Non-stationary Statistics and Energetics of Brownian Motion under Stochastic Harmonic Confinement*, arXiv:2609.33751v1, 27 September 2026, https://arxiv.org/html/2609.33751v1.
2. D. Gupta and S. H. L. Klapp, *Nonequilibrium fluctuations in a harmonic trap with annealed stochastic stiffness*, arXiv:2507.20915, 28 July 2025, https://arxiv.org/abs/2507.20915.
3. L. Cocconi, H. Alston, J. Romano and T. Bertrand, *The OU² process: Characterising dissipative confinement in noisy traps*, arXiv:2405.09460, 15 May 2024, https://arxiv.org/abs/2405.09460.
4. Feynman–Kac formula for the quadratic Brownian functional and elementary Brownian heat-kernel reversibility; the exact formulas required here are derived explicitly above.
