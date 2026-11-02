# Critical temporal-memory regimes for Brownian diffusion with a slowly refreshed stochastic reset rate

## Finding

For a Brownian particle whose position is reset to zero at a Cox-process intensity that is independently redrawn at Poisson rate \(\mu>0\), the stationary two-time covariance has an exact survival-transform representation. If the fresh intensity law has density \(f(\lambda)\sim c\lambda^{\alpha-1}\) at zero, two distinct critical indices, \(\alpha=1\) and \(\alpha=2\), govern the slow-refresh limit \(\mu\downarrow0\).

Write \(D>0\) for the Brownian diffusivity, \(S_\mu(t)\) for the probability that no position reset occurs during a stationary interval of duration \(t\), and define
\[
 g(z)=\int_0^\infty\frac{f(\lambda)}{\lambda+z}\,d\lambda,\qquad
 h(z)=\int_0^\infty\frac{f(\lambda)}{(\lambda+z)^2}\,d\lambda.
\]
For every \(\mu>0\), every \(t\ge0\), and \(z\ge0\),
\[
 \boxed{\int_0^\infty e^{-zt}S_\mu(t)\,dt=\frac{g(\mu+z)}{1-\mu g(\mu+z)},\qquad
 C_\mu(t)=2D\int_t^\infty S_\mu(s)\,ds,}
\]
where \(C_\mu(t)=\mathbb E[X_0X_t]\) for the unique stationary square-integrable position process. Thus its variance and integrated *normalized* covariance are
\[
 \boxed{C_\mu(0)=\frac{2Dg(\mu)}{1-\mu g(\mu)},\qquad
 \tau_\mu:=\int_0^\infty\frac{C_\mu(t)}{C_\mu(0)}\,dt
 =\frac{h(\mu)}{g(\mu)[1-\mu g(\mu)]}.}
\]

For \(0<\alpha<1\), the complete normalized slow-refresh correlation profile exists on the scale \(t=u/\mu\): for every fixed \(u\ge0\),
\[
 \boxed{\frac{C_\mu(u/\mu)}{C_\mu(0)}\longrightarrow
 \frac{\Gamma(1-\alpha,u)}{\Gamma(1-\alpha)}.}
\]
Here \(\Gamma(s,u)=\int_u^\infty v^{s-1}e^{-v}\,dv\) is the upper incomplete gamma function. At the boundary \(\alpha=1\), let \(\lambda_*>0\) be any fixed reference rate and set \(t_\mu(q)=\lambda_*^{-1}(\lambda_*/\mu)^q\). For every fixed \(q\ge0\),
\[
 \boxed{\frac{C_\mu(t_\mu(q))}{C_\mu(0)}\longrightarrow(1-q)_+:=\max\{1-q,0\}.}
\]

The complete sharp asymptotics of the integrated normalized correlation time are
\[
 \boxed{\tau_\mu\sim
 \begin{cases}
 (1-\alpha)/\mu,&0<\alpha<1,\\
 1/[\mu\log(\lambda_*/\mu)],&\alpha=1,\\
 c\Gamma(\alpha)\Gamma(2-\alpha)\,\mu^{\alpha-2}/m_1,&1<\alpha<2,\\
 (c/m_1)\log(\lambda_*/\mu),&\alpha=2,\\
 m_2/m_1,&\alpha>2,
 \end{cases}}
\]
where \(m_j=\int_0^\infty\lambda^{-j}f(\lambda)\,d\lambda\) appears only when finite. The variance satisfies
\[
 C_\mu(0)\sim
 \begin{cases}
 2Dc\Gamma(\alpha)\Gamma(1-\alpha)\mu^{\alpha-1},&0<\alpha<1,\\
 2Dc\log(\lambda_*/\mu),&\alpha=1,\\
 2Dm_1,&\alpha>1.
 \end{cases}
\]
Consequently, throughout \(1<\alpha\le2\), the stationary variance tends to a finite positive limit although the integrated correlation time diverges. Both exponents are sharp, for every density in the stated class.

## Assumptions and scope

Let \(\mu,D>0\). The environmental intensity \((\lambda_t)_{t\in\mathbb R}\) is the stationary piecewise-constant Markov process that, independently of its state, redraws a fresh value from a probability density \(f\) on \((0,\infty)\) at the event times of an independent rate-\(\mu\) Poisson clock. Redraws are independent, even when successive rate values coincide. Conditional on the *entire* environment, position resets occur as an inhomogeneous Poisson process of instantaneous intensity \(\lambda_t\); they set \(X\) to zero without redrawing \(\lambda\). Between resets, \(dX_t=\sqrt{2D}\,dB_t\), with \(B\) independent of all environmental and reset randomness. The result concerns equilibrium-in-time *stationary position* correlations, not first-passage observables or covariance of the environmental rate.

Assume \(f(\lambda)\sim c\lambda^{\alpha-1}\) as \(\lambda\downarrow0\), where \(c>0\) and \(\alpha>0\), and \(f\) is a probability density with no atom at zero. No upper-tail moments of \(f\) are required. All limits take \(\mu\downarrow0\) with \(D,f,\lambda_*\) fixed. For each positive \(\mu\), the stationary covariance and its integral are finite. At the exact boundary exponents, logarithms are interpreted in dimensionless form using the arbitrary fixed rate \(\lambda_*\); their leading coefficients do not depend on this choice.

## Proof

**1. Exact killed-survival transform.** Put \(\phi(t)=\mathbb E_f[e^{-\lambda t}]\) and \(S_\mu(t)=\mathbb E[\exp(-\int_0^t\lambda_s\,ds)]\). Conditioning on the first redraw of the environmental rate yields the renewal equation
\[
 S_\mu(t)=e^{-\mu t}\phi(t)+\mu\int_0^t e^{-\mu s}\phi(s)S_\mu(t-s)\,ds.
\]
Its Laplace transform is \(R_\mu(z)=g(\mu+z)/[1-\mu g(\mu+z)]\), because \(\int_0^\infty e^{-zt}\phi(t)dt=g(z)\). The denominator is strictly positive at \(z\ge0\): indeed \(0<\mu g(\mu+z)\le\mathbb E[\mu/(\mu+\lambda)]<1\). In particular \(R_\mu(0)=\int_0^\infty S_\mu(t)dt<\infty\).

**2. Stationary covariance.** Construct a stationary two-sided environment, its conditional reset process, and an independent two-sided Brownian motion. Denote the most recent position reset before \(t\) by \(T(t)\). Then \(X_t=\sqrt{2D}[B_t-B_{T(t)}]\), interpreted conditionally on the reset history. The square-integrability follows from \(\mathbb E[t-T(t)]=R_\mu(0)<\infty\). For \(t\ge0\), the Brownian increments common to the two reset intervals \((T(0),0]\) and \((T(t),t]\) occur exactly when no reset occurs across their union from an earlier time to \(t\). Conditional Brownian isometry and stationary increments of the reset point process give
\[
 C_\mu(t)=2D\int_{-\infty}^{0}\Pr\{\text{no reset on }(s,t]\}\,ds
 =2D\int_t^\infty S_\mu(u)\,du.
\]
Therefore \(C_\mu(0)=2D R_\mu(0)\). Tonelli's theorem gives \(\tau_\mu=\int_0^\infty tS_\mu(t)dt/R_\mu(0)=-R_\mu'(0)/R_\mu(0)\). Differentiating the exact renewal transform and using \(g'(z)=-h(z)\), justified for every \(z>0\), produces the displayed exact formula.

**3. Two moment thresholds.** Elementary changes of variables \(\lambda=\mu v\), followed by dominated comparison using the density asymptotic near zero and finite bounds away from zero, yield
\[
 g(\mu)\sim\begin{cases}
 c\Gamma(\alpha)\Gamma(1-\alpha)\mu^{\alpha-1},&0<\alpha<1,\\
 c\log(\lambda_*/\mu),&\alpha=1,\\
 m_1,&\alpha>1,
 \end{cases}
\]
and
\[
 h(\mu)\sim\begin{cases}
 c\Gamma(\alpha)\Gamma(2-\alpha)\mu^{\alpha-2},&0<\alpha<2,\\
 c\log(\lambda_*/\mu),&\alpha=2,\\
 m_2,&\alpha>2.
 \end{cases}
\]
The constants in the noninteger cases are beta-integrals. Since \(\mu g(\mu)=o(1)\) in every regime, substitution in the exact formulas gives all variance and integrated-correlation asymptotics, including both logarithmic boundaries.

**4. Nontrivial full correlation profile below the first threshold.** Define the probability density \(p_\mu(t)=S_\mu(t)/R_\mu(0)\) on \([0,\infty)\). Under \(0<\alpha<1\), the Laplace transform of the rescaled random variable \(\mu V_\mu\), with \(V_\mu\) of density \(p_\mu\), is
\[
 \frac{R_\mu(\mu z)}{R_\mu(0)}
 =\frac{g(\mu(1+z))}{g(\mu)}
 \frac{1-\mu g(\mu)}{1-\mu g(\mu(1+z))}
 \longrightarrow(1+z)^{-(1-\alpha)}
 \quad(z\ge0).
\]
This is the Laplace transform of the shape-\((1-\alpha)\), unit-rate gamma law. By uniqueness and continuity of that limiting distribution, \(\Pr(\mu V_\mu>u)\) converges to its gamma survival function at every \(u\ge0\). But \(\Pr(\mu V_\mu>u)=C_\mu(u/\mu)/C_\mu(0)\), giving the claimed incomplete-gamma profile.

**5. The logarithmic-time boundary profile.** At \(\alpha=1\), the Abelian relation \(\phi(t)\sim c/t\) as \(t\to\infty\) follows from the assumed density. Conditioning on all redraw times partitions \([0,t]\) into subintervals; their independent fresh intensities produce a product of factors \(\phi(\Delta_j)\). As the functions \(\lambda\mapsto e^{-\lambda\Delta_j}\) are all decreasing, repeated positive-association/Chebyshev integral inequalities show \(\prod_j\phi(\Delta_j)\le\phi(t)\). Conversely, the no-redraw event gives a lower bound. Therefore
\[
 e^{-\mu t}\phi(t)\le S_\mu(t)\le\phi(t),\qquad
 0\le\int_0^t[\phi(s)-S_\mu(s)]ds
 \le\mu\int_0^t s\phi(s)ds.
\]
For fixed \(0<q\le1\), the upper limit \(t_\mu(q)=\lambda_*^{-1}(\lambda_*/\mu)^q\) satisfies \(t_\mu(q)\le O(1/\mu)\), so the final bound is \(O(1)\), while \(\int_0^{t_\mu(q)}\phi(s)ds\sim cq\log(\lambda_*/\mu)\). Since \(R_\mu(0)\sim c\log(\lambda_*/\mu)\), it follows that \(\int_0^{t_\mu(q)}S_\mu(s)ds/R_\mu(0)\to q\). Subtracting this fraction from one proves the profile for \(0<q\le1\). At \(q=0\) the bounded time interval contributes a vanishing fraction. For \(q>1\), monotonicity of \(C_\mu(t)\) and the \(q=1\) case force limit zero. This completes every asserted boundary and regime.

## Verification

The accompanying standalone `verify.py` separately evaluates the killed-generator matrix for two-point intensity laws, reproduces the exact transform and integrated-correlation formula, compares the gamma-family Stieltjes integrals with special-function representations, and checks the asymptotic constants and deterministic-rate limit. It reports its number of finite deterministic assertions when run with Python and `mpmath`. The analytical argument above, not these finite checks, proves the universal claims. The covariance profile is pointwise in fixed scaled lag, and no uniform-in-all-lags error estimate is claimed.

## Relationship to prior work

Arutkin and Reuveni (arXiv:2509.25365v1, 2025) introduce precisely the Cox-reset model with Poisson-redrawn intensity and determine its stationary spatial characteristic function for arbitrary intensity law (their Eq. (23)); the general survival functional already appears in their Eq. (11). Accordingly, the one-time stationary characteristic function and its transform are **not new contributions here**. The advance assessed here is the explicit two-time covariance/integrated-memory theorem together with the two distinct low-intensity thresholds and the gamma and logarithmic observation-time scaling profiles. The earlier spatial transform determines the same killed-survival kernel implicitly, which is recognized as a potential route to these consequences; the temporal scaling results require the additional covariance identity and singular weak-refresh asymptotics.

Stojkoski, Sandev, Kocarev and Pal (arXiv:2107.11686) derive stationary temporal autocorrelations for fixed-rate Poisson resetting and discuss general reset-time distributions; the special constant-rate case of our formula agrees with their exponential correlation. Their fixed-rate renewal case does not have independent rate refreshes that persist across particle resets. Taźbierski (2025 dissertation, Chapter 3) treats mixed-Poisson and Cox-guided resetting, emphasizing displacement and mean-square displacement, while his separate memory-resetting chapter concerns resetting of internal memory without position relocation. Neither supplies the specific refreshed-rate stationary temporal profiles stated here. General Karamata/Abelian results are used as standard analytic tools and are not claimed as original.

## Limitations

The finding is a self-contained mathematical conclusion under a stationary Poisson-redrawn environment and Brownian displacement with complete position reset. It does not cover nonstationary rate laws, rate dynamics correlated with Brownian motion, reset rules that also refresh the rate, non-Brownian driver memory, or first-passage quantities. The limits are as \(\mu\downarrow0\), and are not universal for arbitrary density families changing with \(\mu\). The source's known spatial transform and classical Tauberian tools account for substantial reusable structure; existing general process results could potentially imply the temporal scaling limits, and independent publication-priority assessment is not claimed.

## References

1. M. Arutkin and S. Reuveni, *Diffusion with doubly stochastic resetting*, arXiv:2509.25365v1 (first public 2025-09-29), https://arxiv.org/html/2509.25365v1 .
2. V. Stojkoski, T. Sandev, L. Kocarev and A. Pal, *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, arXiv:2107.11686, https://arxiv.org/abs/2107.11686 .
3. K. Taźbierski, *Representations and applications of stochastic processes with resetting*, doctoral dissertation (2025), https://bip.pwr.edu.pl/d/HGBUKOTtQKxVvBFh6GDxYBxZIQnh4WUFABWdbExYbWGFBRAg9RgNtcXccVjU3ClVBDkNLfnxcVVQU/d_tazbierski_k_rozprawa_doktorska.pdf .
4. T. Miyaguchi, T. Uneyama and T. Akimoto, *Brownian motion with alternately fluctuating diffusivity: Stretched-exponential and power-law relaxation*, arXiv:1907.06819, https://arxiv.org/abs/1907.06819 (distinct fluctuating-diffusivity model).
