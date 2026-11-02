# Sharp frequency-dependent resetting design for a diffusive particle

## Finding

Consider a one-dimensional diffusing particle whose position is instantaneously multiplied by a fixed signed factor \(a\in(-1,1)\) at the times of an independent rate-\(r>0\) Poisson process. Its free diffusivity is \(D>0\). Among all such stationary partial-reset protocols, there is a **sharp spectral-design threshold** at angular frequency \(\omega=r\).

With the two-sided spectral-density convention \(S_a(\omega)=\int_{\mathbb R}e^{-i\omega t}\operatorname{Cov}(X_0,X_t)\,dt\), for all real \(\omega\),

\[
S_a(\omega)=\frac{4D}{(1+a)[r^2(1-a)^2+\omega^2]}.
\]

Put \(z=|\omega|/r\). If \(0\le z<1\), the **unique global minimizer** over \(-1<a<1\) is

\[
a_*(z)=\frac{1-\sqrt{4-3z^2}}{3}\in[-1/3,0),\qquad
\min_{-1<a<1}S_a(\omega)
=\frac{54D}{r^2(2+\sqrt{4-3z^2})(4-\sqrt{4-3z^2})^2}.
\]

At \(z=1\), the minimum is \(2D/r^2\), attained **uniquely** at \(a=0\). For \(z>1\), there is **no minimizing admissible stationary protocol**; the sharp infimum is \(2D/\omega^2\), approached precisely by taking \(a\uparrow1\). The minimum/infimum as a function of \(|\omega|\) is continuous at \(r\), but its left and right slopes there are \(-2D/r^3\) and \(-4D/r^3\), respectively.

The zero-frequency spectral design also optimizes the long-time variance rate of the stationary temporal mean. In particular, for \(\overline X_T=T^{-1}\int_0^T X_t\,dt\),

\[
\sqrt{T}\,\overline X_T\ \Longrightarrow\ \mathcal N(0,S_a(0)),\qquad
\lim_{T\to\infty}T\operatorname{Var}(\overline X_T)=S_a(0).
\]

The unique variance-rate optimizer is \(a=-1/3\), giving \(S_{-1/3}(0)=27D/(8r^2)\), exactly \(27/32\) of the classical complete-reset value \(S_0(0)=4D/r^2\). In particular, the spectral optimum cannot be chosen independently of the monitored frequency.

## Assumptions and scope

Let \((B_t)\) be standard real Brownian motion, let \((N_t)\) be an independent Poisson process of rate \(r\), and define the right-continuous jump diffusion by

\[
dX_t=\sqrt{2D}\,dB_t+(a-1)X_{t-}\,dN_t,
\quad D,r>0,\quad -1<a<1.
\]

At a jump, \(X_t=aX_{t-}\); there are no refractory intervals, external drifts, position-dependent hazards or measurement-noise contributions. All covariance statements use the **unique stationary version**. The two-sided spectral convention includes no \(1/(2\pi)\) factor. The angular frequency is real and its absolute value alone matters. The excluded endpoint \(a=1\) has ordinary unconfined Brownian motion and no stationary position distribution; hence the infimum for \(|\omega|>r\) is genuinely not attained.

## Proof

**1. Stationary construction and second moment.** Drive a process from the infinite past by independent Brownian increments and Poisson events. If \(N(s,t]\) counts events in \((s,t]\), then the limiting stationary solution can be written conditionally on the Poisson history as

\[
X_t=\sqrt{2D}\int_{-\infty}^t a^{N(s,t]}\,dB_s.
\]

The driving Poisson history is independent of Brownian motion, so conditional Itô isometry applies. Since \(\mathbb E[a^{2N(s,t]}]=\exp[-r(1-a^2)(t-s)]\), the integral converges in \(L^2\) and

\[
\sigma_a^2:=\mathbb E X_t^2
=2D\int_0^\infty e^{-r(1-a^2)u}\,du
=\frac{2D}{r(1-a^2)}.
\]

A synchronous coupling of any two finite-second-moment solutions obeys \(X_t-Y_t=a^{N_t}(X_0-Y_0)\). Thus the stationary distribution is unique in that class, and the same contraction gives mixing and ergodicity. Finite higher moments follow from the exponential inter-jump intervals and geometric contraction, or recursively from the polynomial generator.

**2. Full stationary two-time covariance.** For \(t\ge0\), condition on \(X_0\). Independence of future noise gives \(\mathbb E[X_t\mid X_0]=\mathbb E[a^{N_t}]X_0=e^{-r(1-a)t}X_0\). Stationarity and time symmetry of a scalar covariance then give, for all real \(t\),

\[
C_a(t)=\operatorname{Cov}(X_0,X_t)
=\frac{2D}{r(1-a^2)}e^{-r(1-a)|t|}.
\]

Fourier transformation using \(\int_{\mathbb R}e^{-\lambda|t|}e^{-i\omega t}\,dt=2\lambda/(\lambda^2+\omega^2)\), with \(\lambda=r(1-a)>0\), yields the spectral formula in the finding.

**3. Sharp optimization, including boundaries.** Minimizing the positive spectrum equals maximizing

\[
F(a)=(1+a)[r^2(1-a)^2+\omega^2],\qquad -1<a<1.
\]

It satisfies both the factorized comparison

\[
F(a)-2\omega^2=(1-a)[r^2(1-a^2)-\omega^2]
\]

and the exact stationary equation

\[
F'(a)=\omega^2-r^2(1-a)(1+3a)=0.
\]

For \(0\le z<1\), the two stationary roots are \(a_\pm=(1\pm\sqrt{4-3z^2})/3\), with \(a_-<0\) (allowing \(a_-=-1/3\) at zero frequency) and \(a_+>2/3\). The derivative changes from positive to negative at \(a_-\), and from negative to positive at \(a_+\). The left boundary has \(F(-1)=0\). At the negative root, substituting the stationary equation into the comparison gives

\[
F(a_-)-F(1)=-2r^2a_-(1-a_-)^2>0.
\]

Thus \(a_-\) is the unique global maximum, despite the possible competing right boundary. Using the stationary equation again,

\[
F(a_-)=2r^2(1-a_-)(1+a_-)^2,
\]

which yields the displayed closed-form minimum.

If \(z\ge1\), the factorized comparison implies \(F(a)\le2\omega^2=\lim_{a\uparrow1}F(a)\) for every admissible \(a\). For \(z>1\), this inequality is strict. At \(z=1\), equality holds in the interior exactly when \(a=0\). This proves the threshold, uniqueness and nonattainment claims. Differentiating the optimal spectrum on the respective sides gives the stated one-sided derivatives. In particular, there is no single stationary reset factor that minimizes all frequencies.

**4. Temporal-average variance and Gaussian limit.** The covariance is integrable, so a direct double integral gives

\[
\operatorname{Var}(\overline X_T)=\frac{2\sigma_a^2}{T^2}
\left[\frac{T}{\lambda}-\frac{1-e^{-\lambda T}}{\lambda^2}\right],\qquad
\lambda=r(1-a).
\]

Consequently \(T\operatorname{Var}(\overline X_T)\to2\sigma_a^2/\lambda=S_a(0)\). For the distributional limit, compensate the Poisson jumps and set

\[
M_T=X_T-X_0+\lambda\int_0^T X_t\,dt.
\]

This is a square-integrable martingale with predictable quadratic variation

\[
\langle M\rangle_T=2DT+r(1-a)^2\int_0^T X_t^2\,dt.
\]

By ergodicity, \(T^{-1}\langle M\rangle_T\to 2D+r(1-a)^2\sigma_a^2=4D/(1+a)\) almost surely. Finite fourth moments yield the martingale Lindeberg condition. The martingale central limit theorem, together with \((X_T-X_0)/\sqrt T\to0\) in \(L^2\), proves the stated Gaussian limit with variance \([4D/(1+a)]/\lambda^2=S_a(0)\). Finally, maximizing \((1-a)^2(1+a)\) on \((-1,1)\) gives the unique solution \(a=-1/3\); the corresponding variance ratio is exactly \(27/32\).

## Verification

Execute `python3 check.py` using Python's standard library. The checker implements exact rational second-moment and martingale-bracket identities, checks the closed optimizer against dense finite parameter grids, compares independently computed numerical Fourier integrals and time-window covariance integrals with their formulas, and samples the stationary process via its backward Gaussian/Poisson representation followed by exact forward jump epochs. All deterministic checks and seeded finite simulations passed when run from this package. These finite diagnostics corroborate but are not the proof of the continuum optimization, almost-sure ergodicity or infinite-time central limit theorem; those are supplied above.

## Relationship to prior work

Biroli, Feld, Hartmann, Majumdar and Schehr (2024), arXiv:2406.08387v1, established the full signed rescaling-reset model, exact one-time stationary spatial distribution and first-passage search optimization. Their equations for the dynamics and stationary distribution are used as known starting points; they do not state the stationary two-time spectral optimization or the sharp frequency threshold proved here. Olsen and Löwen (2024), arXiv:2406.10039v1, derived a general Fourier–Laplace propagator and moments in a model with refractory periods (including the zero-refractory limit); their studied reset parameter lies in \((0,1)\), and their analysis optimizes stationary kurtosis with respect to refractory duration, not the signed reset factor for a fixed spectral frequency. The exact stationary second moment and the exponential covariance are elementary consequences of the earlier model and are not separately asserted as new results. The assessed claim is the **complete signed-parameter frequency-by-frequency optimization, its attained/nonattained threshold, the cusp and its long-time averaging interpretation**.

## Limitations

The result is for continuous time, one dimension, constant Poisson rate, independent Brownian forcing and deterministic signed contraction with \(|a|<1\). It does not optimize resetting rate jointly with the multiplier, any finite-frequency band integral, physical resetting cost, transient rather than stationary spectra, other noise colors, or a model containing refractory intervals. The high-frequency optimum is an infimum rather than a stationary protocol. Literature searches and source comparisons do not prove global publication uniqueness, and a broader unindexed spectral-control result could affect priority. The Gaussian limit is about the time-integrated position, not a Gaussian claim for the non-Gaussian stationary position law.

## References

1. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1 (first posted 2024-06-12), https://arxiv.org/abs/2406.08387.
2. K. Stølevik Olsen and H. Löwen, *Partial stochastic resetting with refractory periods*, arXiv:2406.10039v1 (first posted 2024-06-14), https://arxiv.org/abs/2406.10039.
3. American Mathematical Society, *MSC2020*, class 82C31 (stochastic methods in time-dependent statistical mechanics), https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82C31.
