# An age-memory crossover in the stationary modulus covariance of reset scaled Brownian motion

## Finding

For stationary scaled Brownian motion with complete Poisson resetting, the covariance of absolute position exhibits an exact transition in its large-lag algebraic prefactor. With \(Y_t=|X_t|\) and \(C_\beta(t)=\operatorname{Cov}(Y_0,Y_t)\),

\[
C_\beta(t)\sim e^{-rt}\begin{cases}
\frac{2K}{\pi}\Gamma(1+3\beta/2)r^{-3\beta/2}t^{-\beta/2},&0<\beta<1,\\
\frac{2K}{\sqrt\pi}r^{-3/2}t^{-1/2},&\beta=1,\\
\frac{K\beta^2}{\pi}\Gamma(1+\beta/2)r^{-1-\beta/2}t^{\beta/2-1},&1<\beta<2.
\end{cases}
\]

All three leading constants are strictly positive. At \(\beta=1\), the fraction \(3/4\) of the leading coefficient is due to shared Gaussian fluctuations inside a single excursion and \(1/4\) to stochastic variation of the backward age. For each finite \(t>0\), the covariance itself is strictly positive.

## Assumptions and scope

Fix \(K>0\), a reset rate \(r>0\), and a scaled-Brownian exponent \(0<\beta<2\). Independently for each excursion of age \(a\ge0\), start at zero and run \(\sqrt{2K}B_{a^\beta}\), where \(B\) is standard Brownian motion. Reset both position and the internal diffusion clock at the points of an independent rate-\(r\) stationary Poisson point process on the real line. Each excursion has an independent Brownian driver. The resulting stationary process is denoted \(X\); \(Y_t=|X_t|\), and covariance is with respect to its stationary law.

Let \(A\sim\operatorname{Exp}(r)\) be the backward time since the last reset, put \(b=\beta/2\in(0,1)\), and define \(h:[0,1]\to\mathbb R\) by

\[
h(q)=\sqrt{1-q^2}+q\arcsin q-1.
\]

The exact identity, valid for all \(t>0\), is

\[
C_\beta(t)=\frac{4K}{\pi}e^{-rt}\left\{\operatorname{Cov}(A^b,(A+t)^b)+\mathbb E\left[A^b(A+t)^b h\left(\left(\frac A{A+t}\right)^b\right)\right]\right\}.
\]

This is a result for the *modulus*, not the signed position \(X_t\); the signed covariance has a purely exponential lag profile.

## Proof

**1. Renewal separation and stationarity.** In a two-sided stationary Poisson construction, \(A\) has density \(re^{-ra}\). The event \(N_t\) that no reset occurs between times zero and \(t\) has probability \(e^{-rt}\) and is independent of the past. If at least one reset occurs, then \(Y_t\) is independent of \(Y_0\) conditional on the future reset history; moreover \(Y_0\) has its stationary mean independently of that history. The law of total covariance, with the future event independent of \(Y_0\), therefore yields

\[
\operatorname{Cov}(Y_0,Y_t)=e^{-rt}\operatorname{Cov}(Y_0,Y_t\mid N_t).
\]

Conditioned on \(N_t\) and \(A=a\), \((X_0,X_t)\) is centered bivariate Gaussian with variances \(2Ka^{2b}\) and \(2K(a+t)^{2b}\), and correlation \(q=(a/(a+t))^b\). The standard bivariate-normal absolute moment identity gives

\[
\mathbb E(|X_0||X_t|\mid A=a,N_t)=\frac{4K}{\pi}a^b(a+t)^b\bigl[\sqrt{1-q^2}+q\arcsin q\bigr],
\]

while the respective conditional means are \(2\sqrt{K/\pi}\,a^b\) and \(2\sqrt{K/\pi}\,(a+t)^b\). Taking first conditional covariance at fixed \(A\), then the covariance of these conditional means as \(A\) varies, gives the displayed exact identity. Every expectation is finite since \(A\) has moments of all positive orders.

**2. Signs.** Direct differentiation gives \(h(0)=0\) and \(h'(q)=\arcsin q>0\) on \((0,1)\). Hence the within-excursion term is strictly positive. The age covariance is also strictly positive: both \(a\mapsto a^b\) and \(a\mapsto(a+t)^b\) are strictly increasing, so their covariance equals half the strictly positive expectation of the product of their differences on two independent nondegenerate ages.

**3. Age term.** Let \(m_b=\mathbb E A^b\). For each \(a>0\),

\[
\frac{(a+t)^b-t^b}{t^{b-1}}\longrightarrow ba,
\quad
0\le\frac{(a+t)^b-t^b}{t^{b-1}}\le ba,
\]

where the bound follows from concavity because \(0<b<1\). In the centered representation \(\operatorname{Cov}(A^b,(A+t)^b)=\mathbb E[(A^b-m_b)((A+t)^b-t^b)]\), dominated convergence applies to the integrable majorant \(bA|A^b-m_b|\). Therefore

\[
\lim_{t\to\infty}t^{1-b}\operatorname{Cov}(A^b,(A+t)^b)
=b\operatorname{Cov}(A^b,A)
=b^2\Gamma(1+b)r^{-1-b}.
\]

The last identity uses the exact exponential moments \(\mathbb E A^z=\Gamma(1+z)r^{-z}\).

**4. Within-excursion term.** As \(q\downarrow0\), \(h(q)/q^2\to1/2\). Since \(h(q)/q^2\) extends continuously to \([0,1]\), it is bounded there. Consequently,

\[
0\le t^b A^b(A+t)^b h\left(\left(\frac A{A+t}\right)^b\right)
\le c_b A^{3b},
\]

for a finite constant \(c_b\) independent of \(t\). For each \(A=a>0\), the middle expression tends to \(a^{3b}/2\). Dominated convergence now yields

\[
\lim_{t\to\infty}t^b\mathbb E\left[A^b(A+t)^b h\left(\left(\frac A{A+t}\right)^b\right)\right]
=\frac12\Gamma(1+3b)r^{-3b}.
\]

**5. Dominance and boundary.** The two contributions to \(e^{rt}C_\beta(t)\) have decay orders \(t^{b-1}\) and \(t^{-b}\), respectively. Their exponents are equal precisely when \(b=1/2\), equivalently \(\beta=1\). For smaller \(b\), the latter dominates; for larger \(b\), the former dominates. Multiplication by \(4K/\pi\) gives each stated coefficient. At \(b=1/2\), the age and within-excursion coefficients are, respectively, \(K/(2\sqrt\pi r^{3/2})\) and \(3K/(2\sqrt\pi r^{3/2})\), proving both the total coefficient and the \(1/4\) versus \(3/4\) decomposition.

## Verification

The standalone Python program `verify.py` integrates the exact two-term expression using adaptive quadrature with exponential-age weights and independently evaluates a bivariate-normal absolute-moment formula without that decomposition. It compares the two values across 21 parameter pairs, checks strict positive contributions, evaluates normalized leading asymptotics in all three regimes at increasingly large lags, and checks the exact critical coefficient and limiting contribution fraction. Run `python verify.py` with Python 3.10+ and SciPy available; `verification_output.txt` records 73 successful finite checks. These checks are numerical corroboration, **not** a substitute for steps 1–5.

## Relationship to prior work

Méndez and Cristín [1] develop renewal formulas and the first two moments of *integrated* absolute displacement under Poisson and power-law resetting; the stationary long-lag covariance of instantaneous absolute displacement and its three-regime leading constants are not stated. Taźbierski, Metzler and Magdziarz [2] develop a general two-time position law for complete renewal resetting and an explicit *signed-position* covariance for scaled Brownian motion (their sections 3.1.2–3.2.4). This broad law is compatible with, and can be used as a starting point for, the modulus calculation here; the modulus-specific covariance decomposition and competing-power asymptotics require a separate nonlinear moment and asymptotic analysis. Stojkoski, Sandev, Kocarev and Pal [3] study two-time moments and ergodicity for ordinary diffusion under resetting, rather than this anomalous-exponent modulus phase transition. The foundational methods and Gaussian absolute-moment identity are not presented as new.

## Limitations

The claim assumes complete resetting of both position and diffusion clock, Poisson reset times, one-dimensional centered Gaussian excursions, and fixed \(0<\beta<2\). It does not cover incomplete resetting, heavy-tailed reset intervals, higher-dimensional radial observables, or uniformity as \(\beta\) approaches an endpoint. It is a stationary large-lag result; no finite-lag monotonicity is claimed beyond positivity. The originality assessment is preliminary: a general earlier two-time law logically contains integrals of nonlinear observables, and an unlocated explicit evaluation or specialized asymptotic could cover the result. Independent historical-priority and mathematical review have not been performed.

## References

[1] V. Méndez and J. Cristín, *Absolute area under a scaled Brownian motion with resetting*, arXiv:2610.19985v1, posted 2026-10-14. https://arxiv.org/abs/2610.19985

[2] K. Taźbierski, R. Metzler and M. Magdziarz, *Series representation approach to stochastic processes with complete and incomplete renewal resetting*, *New Journal of Physics* **27** (2025), 074603. https://doi.org/10.1088/1367-2630/adee40

[3] V. Stojkoski, T. Sandev, L. Kocarev and A. Pal, *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, *Journal of Physics A* **55** (2022), 104003; arXiv:2107.11686. https://arxiv.org/abs/2107.11686
