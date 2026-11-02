# Two exact spatial tail exponents for Pareto-driven harmonic first-hit returns

## Finding

For a regenerative, two-phase one-dimensional diffusion with free Brownian exploration and *stochastic* Ornstein–Uhlenbeck (OU) first-hit return, the stationary distributions of the two phases have sharply different power-law tails under a Pareto exploration clock. The exploration-phase tail has exponent \(2(\delta-1)\), whereas the return-phase tail has exponent \(2\delta\). Both have explicit leading constants. Consequently, the stationary exploration and return moments have distinct sharp thresholds, even though every mean-finite clock yields a finite-mean renewal cycle. The familiar unconditional harmonic-trap energy identity remains true; **that identity was already identified in the motivating paper and is not claimed as new**.

Precisely, suppose the exploration time \(T\) has survival function \(\Pr(T>t)=(1+t)^{-\delta}\), with \(\delta>1\) and time measured in a fixed common unit. Let \(C=\mathbb E(T+H)\), where \(H\) is the subsequent OU first-hit time defined below. For the unnormalized stationary phase measures \(\pi_{\mathrm{off}}\) and \(\pi_{\mathrm{on}}\), as \(x\to\infty\),

\[
\pi_{\mathrm{off}}(|X|>x)\sim
\frac{(4D)^{\delta-1}\Gamma(\delta-\tfrac12)}{(\delta-1)\sqrt\pi\,C}\,x^{-2(\delta-1)},
\]

\[
\pi_{\mathrm{on}}(|X|>x)\sim
\frac{(4D)^\delta\Gamma(\delta+\tfrac12)}{2\delta a\sqrt\pi\,C}\,x^{-2\delta}.
\]

For every real \(p>0\), the corresponding sharp moment conditions are

\[
\int |x|^p\,\pi_{\mathrm{off}}(dx)<\infty
\iff p<2(\delta-1),\qquad
\int |x|^p\,\pi_{\mathrm{on}}(dx)<\infty
\iff p<2\delta.
\]

These equivalences include divergence **at** the critical exponents. In particular, for \(1<\delta\le2\) the full stationary spatial variance is infinite while the on-phase unnormalized second moment is finite and equal to \(D/a\). The two-phase tail comparison, explicit coefficients and exact cutoff separation are the evaluated result.

## Assumptions and scope

Fix \(D,a>0\). Each independent cycle begins at zero, follows free Brownian motion \(B_t=\sqrt{2D}\,W_t\) until an independent exploration clock \(T\), and then starts an OU return \(dY_s=-aY_s\,ds+\sqrt{2D}\,d\widetilde W_s\) from \(Y_0=B_T\), with fresh independent Brownian noise. The return ends at the first hit \(H=\inf\{s\ge0:Y_s=0\}\); a new independent cycle begins immediately. The phase state is remembered. The Pareto clock has \(\Pr(T>t)=(1+t)^{-\delta}\) for every \(t\ge0\), \(\delta>1\). The two phase measures are **unnormalized** parts of the stationary time-occupation probability \(\pi=\pi_{\mathrm{off}}+\pi_{\mathrm{on}}\), not individually normalized conditional distributions.

For general independent exploration clocks with \(0<\mathbb ET<\infty\), the same model has \(0<C<\infty\) and the more general exact moment tests

\[
\pi_{\mathrm{off}}(|x|^p)<\infty\iff \mathbb ET^{1+p/2}<\infty,
\qquad
\pi_{\mathrm{on}}(|x|^p)<\infty\iff \mathbb ET^{p/2}<\infty
\quad(p>0).
\]

Here \(\pi_{\mathrm{phase}}(|x|^p)\) denotes the integral of \(|x|^p\) against that unnormalized phase measure. No assertion about a Markov stationary law on position alone is needed for non-exponential renewal clocks: the time-occupation law includes an age/phase augmentation. Every expectation is for a newly sampled, independent cycle.

## Proof

**1. Finite renewal normalization.** For OU started from \(y>0\), let \(u_p(y)=\mathbb E_y\int_0^H Y_s^p\,ds\) for \(p>0\); extend evenly to \(y<0\) with \(|Y_s|^p\). The killed-generator equation on the positive half-line, with absorbing condition \(u_p(0)=0\), is

\[
D u_p''(y)-ay u_p'(y)=-y^p,
\quad
u_p'(y)=\frac{e^{ay^2/(2D)}}D\int_y^\infty z^p e^{-az^2/(2D)}\,dz.
\]

For \(p=0\), \(u_0(y)=\mathbb E_yH\), the identical derivative formula has integrand \(1\). It implies \(u_0(y)=O(\log(2+y))\) at infinity and \(u_0(y)=O(y)\) near zero. Since \(B_T\) has finite absolute first moment when \(\mathbb ET<\infty\), \(\mathbb EH=\mathbb Eu_0(|B_T|)<\infty\). Thus \(C=\mathbb ET+\mathbb EH\) is finite and positive. The regenerative occupation theorem defines

\[
\pi_{\mathrm{off}}(f)=C^{-1}\mathbb E\!\int_0^T f(B_t)\,dt,
\qquad
\pi_{\mathrm{on}}(f)=C^{-1}\mathbb E\!\int_0^H f(Y_s)\,ds.
\]

These are stationary occupation measures for the age-augmented regenerative system, and their masses sum to one.

**2. Arbitrary-clock moment tests.** Let \(Z\sim N(0,1)\). The free Brownian absolute moments give the *exact* off-phase identity

\[
\pi_{\mathrm{off}}(|x|^p)
=\frac{(4D)^{p/2}\Gamma((p+1)/2)}{(1+p/2)\sqrt\pi\,C}
\mathbb ET^{1+p/2}.
\]

The OU derivative formula and elementary Laplace endpoint asymptotics show, for every fixed \(p>0\), that \(u_p(y)\sim y^p/(ap)\) as \(y\to\infty\), and \(u_p(y)=O(y)\) as \(y\downarrow0\). Consequently \(\mathbb Eu_p(|B_T|)<\infty\) holds exactly when \(\mathbb E|B_T|^p<\infty\) (using \(\mathbb E|B_T|<\infty\) for the small-argument control). Since \(\mathbb E|B_T|^p=(4D)^{p/2}\Gamma((p+1)/2)\mathbb ET^{p/2}/\sqrt\pi\), this proves the on-phase criterion. For the stated Pareto clock, \(\mathbb ET^q<\infty\) if and only if \(q<\delta\), giving both sharp moment thresholds including equality cases.

**3. Exploration tail with an exact Gaussian mixture.** Write \(S(t)=\Pr(T>t)\) and use Gaussian scaling within the occupation integral. Conditioning first on \(|Z|\), then integrating in \(t\), yields for every \(x>0\) the *finite-distance exact formula*

\[
\pi_{\mathrm{off}}(|X|>x)=\frac1{(\delta-1)C}\,
\mathbb E\left(1+\frac{x^2}{2DZ^2}\right)^{1-\delta}.
\]

By dominated convergence after multiplying by \(x^{2(\delta-1)}\), the limit equals \((2D)^{\delta-1}\mathbb E|Z|^{2\delta-2}/((\delta-1)C)\). Gaussian moment evaluation yields the first displayed amplitude.

**4. Return tail via absorbed OU flux.** Let \(g(y)\) be the density of \(B_T\). On \(x>0\), the unnormalized return occupation density \(q_{\mathrm{on}}(x)\) solves the absorbed stationary forward equation

\[
Dq_{\mathrm{on}}''(x)+a(xq_{\mathrm{on}}(x))'=-g(x)/C,
\qquad q_{\mathrm{on}}(0)=0.
\]

The vanishing flux at infinity and integration from \(x\) to infinity give the exact first-order identity

\[
Dq_{\mathrm{on}}'(x)+axq_{\mathrm{on}}(x)
=\frac{\Pr(B_T>x)}{C},
\]

hence

\[
q_{\mathrm{on}}(x)=\frac{e^{-ax^2/(2D)}}{DC}
\int_0^x e^{ay^2/(2D)}\Pr(B_T>y)\,dy.
\]

By conditioning on \(|Z|\), the two-sided tail of the starting position obeys the *exact* representation

\[
\Pr(|B_T|>x)=\mathbb E\left(1+\frac{x^2}{2DZ^2}\right)^{-\delta}.
\]

Dominated convergence gives \(\Pr(|B_T|>x)\sim c_Tx^{-2\delta}\), where \(c_T=(4D)^\delta\Gamma(\delta+\tfrac12)/\sqrt\pi\). Symmetry gives \(\Pr(B_T>x)\sim c_Tx^{-2\delta}/2\). Laplace endpoint asymptotics for the flux integral then yield

\[
q_{\mathrm{on}}(x)\sim\frac{c_T}{2aC}x^{-2\delta-1}.
\]

Integration over both tails, using symmetry and regular variation, yields \(\pi_{\mathrm{on}}(|X|>x)\sim c_Tx^{-2\delta}/(2\delta aC)\), proving the second stated amplitude. The boundary condition and zero-flux integration can also be obtained directly by integrating the killed OU occupation kernel over the distribution of the return starting point.

**5. Previously known harmonic energy balance.** Applying Dynkin's formula to \(Y_s^2\) stopped at \(H\), justified by localization and the already established finite occupations, gives

\[
\mathbb E_y\int_0^H Y_s^2\,ds
=\frac{y^2+2D\mathbb E_yH}{2a}.
\]

Since \(\mathbb E B_T^2=2D\mathbb ET\), averaging and dividing by \(C\) yields \(\pi_{\mathrm{on}}(x^2)=D/a\). This reproduces the harmonic equipartition identity explicitly discussed by Frydel (2025, equations (11)–(12) and text following). It is included solely to explain the contrast with the newly derived phase-tail exponents. For \(1<\delta\le2\), the free-phase second moment diverges by step 2, but the return-phase second moment is finite by the separate on-phase criterion.

## Verification

The standalone `verify.py` evaluates Gaussian absolute moments, independent integral formulas for Pareto release and exploration tails, the large-distance OU absorbed-flux kernel, OU Poisson-equation residuals, and the cycle energy cancellation using deterministic quadrature. Execute `python verify.py` with the dependency listed in `requirements.txt`. These finite numerical tests check constants and algebra; they do not replace the infinite-dimensional, all-parameter arguments above. Explicit exact Gaussian-mixture identities, the stopped-generator boundary-value problem and dominated-convergence arguments provide the analytical evidence.

## Relationship to prior work

Frydel, *Search by Return* (2025; arXiv:2511.14646), studies the same harmonic first-hit return with exponentially terminated outward diffusion. Its equations (11)–(12) identify the phase-weighted trap-energy identity, and the text explicitly says this identity holds for arbitrary time-varying reset rates. This fact is **not novel here**. Gupta, Plata, Kundu and Pal (2020; arXiv:2004.11679) establish stochastic returns using external traps, including harmonic OU returns, principally under Poisson exploration. Gupta and Plata (2022; arXiv:2206.07618) establish a general renewal-path formulation for work fluctuations with arbitrary exploration-time distributions and analyze harmonic work under Poisson exploration; that general probabilistic framework is acknowledged. Zhou, Xu and Deng (2021; arXiv:2105.12571) study arbitrary exploration clocks with deterministic return rules, including force-driven return, rather than noisy first-hit OU return. Nagar and Gupta (2016; arXiv:1512.02092) examine heavy-tailed renewal resetting with **instantaneous** returns, so the exploration-phase heavy-tail phenomenon is an established precursor. Xu and Xue (2026; DOI 10.1016/j.physa.2026.131628) consider noisy constant-speed returns after Poisson exploration, according to the accessible abstract; its full text was unavailable. The evaluated statement is the pair of exact phase-resolved spatial-tail exponents and constants for Pareto exploration followed by noisy harmonic first-hit return, together with exact separate moment thresholds. None of the inspected primary texts states those paired results. Priority remains subject to independent literature-wide scrutiny.

## Limitations

The theorem is for one-dimensional driftless free Brownian exploration, independent i.i.d. exploration clocks, OU returns with exactly the same diffusion coefficient, instantaneous first-hit termination at zero, and no refractory delay. The general-clock moment tests require a finite, positive mean exploration duration. The explicit power-law constants require the stated Pareto survival, not an arbitrary regularly varying survival without further hypotheses. The stationary law is a regenerative age/phase-augmented occupation law; position alone is not Markov under general renewal clocks. No finite-time relaxation rate or detailed response to external targets is established. Equilibrium trap energy and generic instant-reset heavy tails are already known and are not asserted as new. The evaluated originality is the coupled phase-resolved classification and amplitudes; a broader, unlocated return-occupation theorem may imply parts of it.

## References

1. D. Frydel, *Search by Return: Stochastic Resetting in Fluctuating Harmonic Potentials* (2025), arXiv:2511.14646, https://arxiv.org/abs/2511.14646 (first public version 18 November 2025).
2. D. Gupta, C. A. Plata, A. Kundu, A. Pal, *Stochastic resetting with stochastic returns using external trap* (2020), arXiv:2004.11679, https://arxiv.org/abs/2004.11679.
3. D. Gupta and C. A. Plata, *Work fluctuations for diffusion dynamics submitted to stochastic return* (2022), arXiv:2206.07618, https://arxiv.org/abs/2206.07618.
4. T. Zhou, P. Xu and W. Deng, *Gaussian Process and Lévy Walk under Stochastic Non-instantaneous Resetting and Stochastic Rest* (2021), arXiv:2105.12571, https://arxiv.org/abs/2105.12571.
5. A. Nagar and S. Gupta, *Diffusion with stochastic resetting at power-law times* (2016), arXiv:1512.02092, https://arxiv.org/abs/1512.02092.
6. Y. Xu and Y. Xue, *Two-phase stochastic resetting with noisy returns*, Physica A 695, 131628 (2026), DOI 10.1016/j.physa.2026.131628.
