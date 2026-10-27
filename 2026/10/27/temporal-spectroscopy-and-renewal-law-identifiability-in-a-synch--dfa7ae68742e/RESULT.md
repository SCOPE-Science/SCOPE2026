# Temporal spectroscopy and renewal-law identifiability in a synchronously reset Brownian gas

## Finding
Fix an integer \(N\ge1\), \(D>0\), and a strictly positive reset interarrival time \(W\) with \(0<\mu=\mathbb EW<\infty\) and \(\mathbb EW^2<\infty\). In the stationary two-sided renewal environment, let \(N\) independent Brownian motions of generator \(D\partial_{xx}\) restart at zero simultaneously at each renewal epoch, with independent Brownian noises during all intervals. For any particle and every \(t\ge0\), its stationary positional covariance is
\[
 C(t)=\mathbb E[X_i(0)X_i(t)]=\frac D\mu\,\mathbb E[(W-t)_+^2].
\]
For distinct particles, \(\mathbb E[X_i(0)X_j(t)]=0\) for all \(t\), although their squared positions are correlated. The entire waiting-time law is identifiable from one particle's temporal covariance: its right-hand second derivative satisfies
\[
 C''_+(t)=\frac{2D}{\mu}\mathbb P(W>t),\qquad \mathbb P(W>t)=\frac{C''_+(t)}{C''_+(0)}.
\]
The two-sided power spectral density \(S(\omega)=2\int_0^\infty C(t)\cos(\omega t)\,dt\), interpreted as an improper cosine integral for \(\omega\ne0\), is exactly
\[
 S(\omega)=\frac{4D}{\mu\omega^2}\int_0^\infty\mathbb P(W>s)[1-\cos(\omega s)]\,ds>0\quad(\omega\ne0).
\]
It obeys the protocol-independent ultraviolet law \(S(\omega)\sim4D/\omega^2\) as \(|\omega|\to\infty\). The zero-frequency spectral value is finite **if and only if** \(\mathbb EW^3<\infty\), in which case \(S(0)=2D\mathbb EW^3/(3\mu)\); otherwise \(S(\omega)\to\infty\) as \(\omega\to0\).

For the Lomax protocol \(\mathbb P(W>t)=(1+t/\tau)^{-\alpha}\), \(\tau>0\) and \(\alpha>2\), one obtains
\[
 C(t)=\frac{2D\tau}{\alpha-2}(1+t/\tau)^{2-\alpha}.
\]
For \(2<\alpha<3\),
\[
 S(\omega)\sim\frac{4D\tau^{\alpha-1}}{\alpha-2}\Gamma(3-\alpha)\sin\!\left(\frac{\pi(\alpha-2)}2\right)|\omega|^{\alpha-3}.
\]
For \(\alpha=3\), \(S(\omega)=4D\tau^2\log(1/(\tau|\omega|))+O(1)\); for \(\alpha>3\), \(S(0)=4D\tau^2/[(\alpha-2)(\alpha-3)]\). These conclusions are one coherent temporal-spectrum theorem, not separate findings.

## Assumptions and scope
The renewal process is stationary on the whole real time axis, built by size-biasing the renewal interval that contains time zero and placing time zero uniformly inside it. Independent, centered Brownian paths are started anew at each renewal epoch; all particles share reset times but not their Brownian innovations. The finite-second-moment assumption guarantees a finite stationary positional covariance. Waiting times may be discrete or continuous and need not possess a density. The physical frequency \(\omega\) is angular frequency; \(S\) is a two-sided spectrum and has no extraneous \(2\pi\) normalization.

## Proof
Let \(A\) and \(R\) be the time since and until the neighboring reset around time zero. The stationary renewal inspection identity gives, for any nonnegative function \(f\),
\[
 \mathbb Ef(A,R)=\frac1\mu\mathbb E\left[\int_0^W f(a,W-a)\,da\right].
\]
Conditioning on \((A,R)\), the Brownian increment from time zero to \(t\) preserves the previous position exactly when \(R>t\). On this event the covariance is \(2DA\); otherwise the fresh, centered Brownian path is independent. Thus
\[
 C(t)=\frac{2D}\mu\mathbb E\int_0^W a\,\mathbf1_{\{W-a>t\}}\,da=\frac D\mu\mathbb E(W-t)_+^2.
\]
The same calculation for different particles gives zero as independent centered Gaussian increments have vanishing cross products conditionally on the renewal environment.

Differentiation of the truncated quadratic under expectation is justified by \(\mathbb EW^2<\infty\); \(C'(t)=-(2D/\mu)\mathbb E(W-t)_+\) and its right derivative is \(C''_+(t)=(2D/\mu)\mathbb P(W>t)\). Since \(W>0\) almost surely, \(C''_+(0)=2D/\mu>0\), proving exact identification of the survival function (and hence every atom, as a right derivative).

The covariance is decreasing to zero, convex, continuously differentiable, and its derivative tends to zero. Two integrations by parts, first on finite intervals then taking limits, give
\[
 S(\omega)=\frac2{\omega^2}\left[-C'(0)-\int_0^\infty C''_+(s)\cos(\omega s)\,ds\right]
 =\frac{4D}{\mu\omega^2}\int_0^\infty\overline F(s)(1-\cos\omega s)\,ds.
\]
Here \(C''_+\) is the a.e. derivative (possible countably many discontinuities do not change the integral), and \(\overline F(s)=\mathbb P(W>s)\). The integral is absolutely convergent because \(\int_0^\infty\overline F=\mu\). Positivity follows from \(W>0\), which makes \(\overline F\) positive on an interval adjacent to zero. The Riemann–Lebesgue lemma gives \(S(\omega)\sim4D/\omega^2\) as \(|\omega|\to\infty\).

For \(\omega\to0\), \((1-\cos(\omega s))/\omega^2\to s^2/2\), dominated by \(s^2/2\). If \(\mathbb EW^3<\infty\), dominated convergence and \(\int_0^\infty s^2\overline F(s)ds=\mathbb EW^3/3\) give the finite intercept. If the third moment diverges, Fatou's lemma forces \(S(\omega)\to+\infty\). For the Lomax law, \(\mu=\tau/(\alpha-1)\) and two elementary integrations produce the stated covariance. For \(2<\alpha<3\), scaling \(u=|\omega|s\) in the positive spectral formula and dominated convergence yield a constant involving \(\int_0^\infty u^{-\alpha}(1-\cos u)du\). Two integrations by parts and Euler's cosine transform give the displayed gamma-sine coefficient. At \(\alpha=3\), the logarithm comes from the intermediate range \(\tau\ll s\ll1/|\omega|\), with a bounded remainder obtained by splitting at those two scales. At \(\alpha>3\), the third-moment formula gives the exact intercept.

## Verification
Run `python verification.py` with SciPy installed. It checks 27 independently evaluated deterministic assertion groups: the exponential-renewal Poisson limit of the covariance and spectrum, Lomax truncated-moment integrals and covariance curvature, finite-third-moment coefficients, and universal ultraviolet asymptotics. These are finite checks supporting, not replacing, the distribution-free analytic arguments. The code is shipped as part of this result.

## Relationship to prior work
De Mauro, Biroli, Majumdar and Schehr (arXiv:2509.06658) establish the same synchronous non-Poissonian Brownian gas and its stationary equal-time distributions and correlations. Their time-dependent two-particle quadratic correlator compares different particles at **the same time**, rather than following a single particle at two stationary times. Majumdar and Oshanin (arXiv:1806.03435) derive a general covariance transform and spectra for **constant-rate Poisson resetting**; its Brownian exponential-covariance case is recovered here as a check. Stojkoski and collaborators (arXiv:2107.11686) address two-time correlation under **Poisson** resetting. Renewal-age/residual-life power-correlation bounds in other work do not determine the Brownian observable's spectrum. The standard renewal inspection identity, Fourier transforms, and Brownian covariance are pre-existing mathematics and are not claimed as independently new. The novel candidate contribution assessed here is the fully general positive renewal-spectrum formula together with waiting-law reconstruction and the exact third-moment boundary in this motivating gas. A broader unexamined general renewal-reward spectral theorem could subsume it; independent priority assessment is necessary.

## Limitations
The theorem treats centered independent Brownian motions with globally shared, fully renewing reset epochs. It does not apply unchanged to a partial-reset protocol, drift, interacting particles, nonrenewing increments, or to transient processes initialized at a reset time. A stationary *distribution* exists already for finite mean interarrivals, but the covariance requires a finite second moment. Neither the general positivity formula nor the identified spectral transition claims a novel abstract Fourier or renewal theorem. The originality assessment is not an independent audit.

## References
1. G. de Mauro, M. Biroli, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, initially posted 2025-09-08; https://arxiv.org/pdf/2509.06658.
2. S. N. Majumdar, G. Oshanin, *Spectral content of fractional Brownian motion with stochastic reset*, arXiv:1806.03435; https://arxiv.org/pdf/1806.03435.
3. V. Stojkoski, T. Sandev, L. Kocarev, A. Pal, *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, arXiv:2107.11686; https://arxiv.org/html/2107.11686v1.
4. A. S. Bodrova, I. M. Sokolov, *Continuous-time random walks under power-law resetting*, arXiv:2001.01350; https://arxiv.org/abs/2001.01350.
