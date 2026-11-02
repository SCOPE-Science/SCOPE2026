# Rayleigh extremes persist under subquadratic confinement in a collectively reset Brownian gas

## Finding
For every confining exponent \(1<\alpha<2\), diffusivity \(D>0\), potential coefficient \(\kappa>0\), and Poisson reset rate \(r>0\), consider \(N\) otherwise independent one-dimensional diffusions subject to simultaneous resetting to the origin. Let \(M_N\) be their largest position in the stationary state. Then
\[
\frac{M_N}{\sqrt{(4D/r)\log N}}\ \xrightarrow[N\to\infty]{\mathrm d}\ Z,
\qquad \Pr\{Z\le z\}=\begin{cases}0,&z<0,\\1-e^{-z^2},&z\ge0.\end{cases}
\]
Thus the limiting density is \(2ze^{-z^2}\) on \(z>0\), exactly as for free Brownian particles with simultaneous resetting, despite the presence of genuine confinement. In particular,
\[
\frac{M_N}{[(D/\kappa)\log N]^{1/\alpha}}\ \xrightarrow{\Pr}\ 0.
\]
The second statement shows that the proposed nondegenerate soft-confinement scaling for the entire range \(\alpha>1\) in the motivating article does **not** apply to the strict subquadratic interval \(1<\alpha<2\). The article presents that classification as a simulation-supported expectation, not a proved theorem.

## Assumptions and scope
Write the potential as \(V(x)=\kappa|x|^\alpha\). Between common reset events, each coordinate solves the independent-noise stochastic equation
\[
dX_t=-\kappa\alpha\,\operatorname{sgn}(X_t)|X_t|^{\alpha-1}\,dt+\sqrt{2D}\,dW_t,\qquad X_0=0.
\]
The Brownian motions are independent across particles; only a rate-\(r\) Poisson reset clock is shared. All coefficients and \(r\) are fixed as \(N\to\infty\). The maximum refers to a simultaneous stationary snapshot, not the maximum accumulated over a time interval. Exponents \(\alpha=1\), \(\alpha=2\), and \(\alpha>2\) are not included in this theorem. The additive-noise diffusion has a unique global solution because its inward drift is continuous and monotone (one-sided dissipative), with no explosion.

## Proof
**1. A pathwise comparison independent of the noise distribution.** Fix a duration \(t>0\) and a continuous forcing path \(B:[0,t]\to\mathbb R\) with \(B(0)=0\). The integral equation is
\[
X_s=B_s-\kappa\alpha\int_0^s \operatorname{sgn}(X_u)|X_u|^{\alpha-1}\,du.
\]
Let \(R_t=\sup_{0\le u\le t}B_u-\inf_{0\le u\le t}B_u\). If \(X_s>0\), let \(q\) be its last zero before \(s\). Since \(X_u>0\) for \(u\in(q,s]\), the integrated restoring force there is nonnegative, and
\[
0<X_s=B_s-B_q-\kappa\alpha\int_q^s X_u^{\alpha-1}\,du\le B_s-B_q\le R_t.
\]
The same argument with signs reversed applies when \(X_s<0\). Therefore \(\sup_{s\le t}|X_s|\le R_t\), and, by the integral equation,
\[
\sup_{s\le t}|X_s-B_s|\le\kappa\alpha t R_t^{\alpha-1}.\tag{1}
\]
All signs, zero crossings, and the bound are pathwise; no Gaussian approximation has been made.

**2. An exact fixed-age logarithmic tail.** Specialize to \(B_s=\sqrt{2D}W_s\) and put \(\beta=\alpha-1\in(0,1)\). The reflection bound implies
\[
\Pr(R_t>h)\le4\exp[-h^2/(16Dt)].
\]
Consequently, for each \(\delta>0\), inequality (1) gives
\[
\Pr\{|X_t-B_t|>\delta x\}\le4\exp\!\left[-\frac1{16Dt}\left(\frac{\delta x}{\kappa\alpha t}\right)^{2/\beta}\right].\tag{2}
\]
Because \(2/\beta>2\), this error is superexponentially small at the Gaussian \(x^2\) scale. In particular,
\[
\Pr\{B_t>(1+\delta)x\}-\Pr\{|X_t-B_t|>\delta x\}\le\Pr\{X_t>x\}
\]
and
\[
\Pr\{X_t>x\}\le\Pr\{B_t>(1-\delta)x\}+\Pr\{|X_t-B_t|>\delta x\}.
\]
Since \(B_t\) is centered normal with variance \(2Dt\), first let \(x\to\infty\), and then \(\delta\downarrow0\). It follows, without any uniform-in-time assumption, that for **each** fixed \(t>0\),
\[
\boxed{\lim_{x\to\infty}\frac{1}{x^2}\log\Pr\{X_t>x\}=-\frac1{4Dt}.}\tag{3}
\]
The same conclusion holds for the left tail by symmetry. The restoring drift is nonzero but is too weak at very large displacement to change this fixed-time logarithmic rate.

**3. Conditional maximum at a fixed reset age.** Let \(X_t^{(1)},\ldots,X_t^{(N)}\) be independent copies, and write \(m_N(t)=\max_iX_t^{(i)}\). For any \(a>0\), apply (3) at \(x=a\sqrt{4Dt\log N}\):
\[
\Pr\{X_t>x\}=N^{-a^2+o(1)}.
\]
For \(a>1\), the union bound gives \(\Pr\{m_N(t)>x\}\le N^{1-a^2+o(1)}\to0\). For \(0<a<1\), independence gives
\[
\Pr\{m_N(t)\le x\}=\bigl(1-\Pr\{X_t>x\}\bigr)^N\le\exp[-N^{1-a^2+o(1)}]\to0.
\]
Thus
\[
\frac{m_N(t)}{\sqrt{4Dt\log N}}\xrightarrow{\Pr}1 \qquad (t>0\ \text{fixed}).\tag{4}
\]
This uses only the logarithmic tail, not finite-sample Gumbel convergence or simulation.

**4. Mix over the common reset age.** In the stationary state of the common rate-\(r\) Poisson resetting clock, the backward time \(T\) since the last reset has density \(re^{-rt}\) for \(t>0\). Conditional on \(T=t\), the particle positions are independent copies of the reset-free diffusion observed at age \(t\), as in equation (13) of the motivating article. For every \(z>0\), (4) gives
\[
\lim_{N\to\infty}\Pr\left\{m_N(t)\le z\sqrt{\frac{4D}{r}\log N}\right\}=\mathbf1_{\{t<z^2/r\}}
\]
for all \(t\ne z^2/r\). Bounded convergence with respect to \(re^{-rt}dt\) yields
\[
\lim_{N\to\infty}\Pr\left\{M_N\le z\sqrt{\frac{4D}{r}\log N}\right\}
=\int_0^{z^2/r}re^{-rt}\,dt=1-e^{-z^2}.\tag{5}
\]
At \(z=0\), symmetry and conditional independence give \(\Pr\{M_N\le0\}=2^{-N}\to0\). For \(z<0\), monotonicity bounds the probability by the \(z=0\) case. This proves convergence at every continuity point.

Finally, \(M_N/\sqrt{(4D/r)\log N}\) is tight by (5), while
\[
\frac{\sqrt{(4D/r)\log N}}{[(D/\kappa)\log N]^{1/\alpha}}
=\sqrt{4D/r}\,(\kappa/D)^{1/\alpha}(\log N)^{1/2-1/\alpha}\longrightarrow0
\]
for \(\alpha<2\). Hence the alternative proposed normalization converges to zero in probability. All conclusions follow.

## Verification
The standalone script `verify.py` checks the exact discrete-implicit analogues of the two pathwise inequalities in step 1 on four nontrivial subquadratic exponents and many reproducible forcing paths (430,080 scalar inequalities); it also checks normal logarithmic-tail constants and the exponential-age mixture algebra. The checks passed. They are **sanity checks only**: step 2 is an analytic infinite-deviation argument, and steps 3–4 are proved probabilistic limits, not extrapolations from finite numerical samples. Run with `python verify.py` using Python, NumPy, and SciPy.

## Relationship to prior work
De Mauro, Majumdar, and Schehr (arXiv:2606.31634, initially public June 30, 2026) establish the exact common-age mixture for arbitrary potential. In their Section VII, equation (222), Table 1, and discussion around equations (224)–(228), they **conjecture on heuristic and simulation grounds** that every fixed \(1<\alpha<\infty\) has maximum scale \(((D/\kappa)\log N)^{1/\alpha}\), with a nontrivial bounded-support limiting shape. The present proof isolates the omitted order of limits: at each fixed reset age, the very far tails for \(1<\alpha<2\) remain Gaussian at logarithmic leading order. Consequently, their proposed normalization collapses and the free-gas Rayleigh limit survives. This is a correction to an explicitly heuristic extension, not a refutation of their rigorously derived harmonic or box results.

Biroli, Larralde, Majumdar, and Schehr (arXiv:2211.00563) already obtain the Rayleigh edge law for **unconfined** Brownian particles. The present theorem's novel scope is every strictly confining, subquadratic power \(1<\alpha<2\). De Mauro, Biroli, Majumdar, and Schehr (arXiv:2509.06658) generalize the resetting clock for **free** Brownian particles; this does not cover the present subquadratic potential. The deterministic pathwise bound and Gaussian-tail principle are elementary ingredients; they are not asserted to be novel in isolation.

## Limitations
Only a fixed-parameter, infinite-particle, single-stationary-snapshot limit is claimed. The proof does not give a uniform asymptotic in a resetting age growing with \(N\), a finite-\(N\) error bound, a second-order Gumbel correction, or the extreme-value laws at \(\alpha=2\) or \(\alpha>2\). Slow convergence at moderate \(N\) can coexist with the strict asymptotic result; numerical observations in the motivating article need not look Rayleigh at accessible sizes. The logarithmic tail comparison is a new argument applied to this model, but standard broad diffusion-tail theorems may provide alternative derivations. A literature search does not establish independent priority certification.

## References
1. G. de Mauro, S. N. Majumdar, and G. Schehr, *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations*, arXiv:2606.31634 (first public 2026-06-30), https://arxiv.org/abs/2606.31634, Section II equation (13); Section VII equation (222) and Table 1.
2. M. Biroli, H. Larralde, S. N. Majumdar, and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563 (first public 2022-11-01), https://arxiv.org/abs/2211.00563.
3. G. de Mauro, M. Biroli, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (first public 2025-09-08), https://arxiv.org/abs/2509.06658.
