# An exact occupation-variance transition for memory-reset Ornstein–Uhlenbeck motion

## Finding

An Ornstein–Uhlenbeck particle that is independently reset, at constant rate \(r\), to a uniformly sampled point on *its own preceding path* can have the exact equilibrium Gaussian law at **every** observation time and nevertheless display a sharp transition in the fluctuation rate of its time-averaged position.

Let \(\overline X_T=T^{-1}\int_0^T X_t\,dt\). For all \(T>0\), \(\mathbb E\overline X_T=0\). Put \(v=D/\mu\), \(b=\mu+r\) and \(p=2r/(\mu+r)\in(0,2)\). For \(p\ne1\),

\[
\operatorname{Var}(\overline X_T)=\frac{2v}{b(p-1)T}\left[{}_1F_1(1-p;2;-bT)-1\right].
\]

At \(p=1\), the continuous extension is

\[
\operatorname{Var}(\overline X_T)=\frac{2v}{bT^2}\int_0^T\frac{(T-u)(1-e^{-bu})}{u}\,du.
\]

The sharp large-time trichotomy is

\[
\operatorname{Var}(\overline X_T)\sim
\begin{cases}
\displaystyle\frac{2v}{\mu-r}\,T^{-1},&0<r<\mu,\\[4pt]
\displaystyle\frac{v}{\mu}\,\frac{\log(2\mu T)}{T},&r=\mu,\\[4pt]
\displaystyle\frac{2v(\mu+r)^{p-2}}{(p-1)\Gamma(p+1)}\,T^{p-2},&r>\mu.
\end{cases}
\]

In particular, \(\overline X_T\to0\) in \(L^2\) for all finite \(r>0\), but the squared-error decay crosses at exactly \(r=\mu\) from the classical inverse-time law to a nonclassical \(T^{-2\mu/(\mu+r)}\) law. The critical logarithm and every displayed coefficient are exact.

## Assumptions and scope

Take \(D,\mu,r>0\). Let \(X_0\sim\mathcal N(0,D/\mu)\), independent of a standard Brownian motion, a homogeneous rate-\(r\) Poisson process and the auxiliary random variables used for resets. Between resets, \(dX_t=-\mu X_t\,dt+\sqrt{2D}\,dW_t\). At a reset time \(t>0\), independently draw \(U_t\) uniformly in \([0,t]\), conditional on the whole path up to \(t-\), and set \(X_t=X_{U_t}\). Values at the finitely many earlier reset instants are immaterial to uniform sampling. The entire preceding path, not a fresh trajectory and not a single fixed location, is the source of every reset. All assertions are in continuous time and in the unconditional probability law. The path law is non-Markovian, and *constant one-time marginals must not be called temporal stationarity*.

## Proof

**Equilibrium one-time law.** The unreset Ornstein–Uhlenbeck semigroup preserves \(\mathcal N(0,v)\). Whenever every earlier one-time marginal has this law, a reset to a uniform previous time also has this law, since its unconditional law is the time average of the preceding marginals. By uniqueness of the linear marginal evolution, \(X_t\sim\mathcal N(0,v)\) for every \(t\ge0\). In particular \(\mathbb E X_t=0\) and \(\mathbb E X_t^2=v\). This fact is also the zero-mode/equilibrium case of the marginal theory in the motivating reference, but **does not** determine correlations across times.

**Closed second-moment equations.** Define \(B_t=\int_0^t X_s\,ds\), \(c(t)=\mathbb E[X_t B_t]\), and \(y(t)=\mathbb E[B_t^2]\). Since \(B_t\) has continuous finite-variation paths, \(y'(t)=2c(t)\). Applying the diffusion and reset generators to \(X_tB_t\) gives, for \(t>0\),

\[
c'(t)=v-(\mu+r)c(t)+\frac r t\,y(t).
\]

The last term is exact: conditional on the preceding path, the mean reset value is \(t^{-1}\int_0^tX_s\,ds=B_t/t\), so its contribution to \(\mathbb E[X_tB_t]\) is \(r[y(t)/t-c(t)]\). The Brownian cross-variation with \(B\) vanishes. Since \(B_0=0\), \(y(0)=y'(0)=0\), and

\[
y''(t)+b y'(t)-\frac{2r}{t}y(t)=2v.\tag{1}
\]

As \(|\mathbb E[X_sX_t]|\le v\), \(0\le y(t)\le v t^2\); consequently all Laplace transforms below are justified for positive transform parameter.

**Exact transform and inversion.** Let \(Y(s)=\int_0^\infty e^{-st}y(t)\,dt\), \(s>0\). The identity \(\mathcal L[y(t)/t](s)=\int_s^\infty Y(u)\,du\) turns (1) into

\[
s(s+b)Y(s)-2r\int_s^\infty Y(u)\,du=\frac{2v}{s}.
\]

Differentiate, multiply by the positive integrating factor \(s^{1+p}(s+b)^{1-p}\), and impose \(s^{1+p}(s+b)^{1-p}Y(s)\to0\) as \(s\to\infty\), which follows from \(Y(s)=O(s^{-3})\). A single elementary integral gives, for \(p\ne1\),

\[
Y(s)=\frac{2v}{b(p-1)s^2}\left[\left(1+\frac bs\right)^{p-1}-1\right].\tag{2}
\]

The standard transform \(\mathcal L[t\,{}_1F_1(a;2;-bt)](s)=s^{-2}(1+b/s)^{-a}\), initially by its absolutely convergent Taylor expansion for \(s>b\) and then by analytic continuation for all \(s>0\), inverts (2) to the claimed finite-time formula. When \(p=1\), its limit is \(Y(s)=(2v/b)s^{-2}\log(1+b/s)\). Since \(\log(1+b/s)=\mathcal L[(1-e^{-bt})/t](s)\), convolution proves the critical integral formula. Thus no extrapolation through the singular parameter \(p=1\) is required.

**Sharp asymptotics.** For \(0<p<1\), the standard negative-real-axis Kummer asymptotic \({}_1F_1(1-p;2;-z)\sim z^{p-1}/\Gamma(1+p)\to0\) gives \(y(t)\sim 2vt/[b(1-p)]=2vt/(\mu-r)\). At \(p=1\), the critical integral equals

\[
\frac{2v}{b}\left\{T[\log(bT)+\gamma_E+E_1(bT)-1]+\frac{1-e^{-bT}}b\right\},
\]

where \(E_1(z)=\int_z^\infty e^{-u}u^{-1}\,du\), and hence is asymptotic to \((2v/b)T\log(bT)\). For \(1<p<2\), the same Kummer expansion instead grows as \((bT)^{p-1}/\Gamma(1+p)\), yielding \(y(T)\sim[2vb^{p-2}/((p-1)\Gamma(p+1))]T^p\). Divide throughout by \(T^2\); note \(p-2=-2\mu/(\mu+r)\). All coefficients are positive in their regimes, and each squared-error variance tends to zero. This proves the complete claim.

## Verification

The bundled `verify.py` independently checks the moment ODE against the analytic hypergeometric expression on multiple parameter grids, exact rational Taylor recurrences against (1), Laplace-transform identities, asymptotic constants and three direct Euler/OU-history Monte Carlo comparisons. Run `python -m pip install -r requirements.txt` and then `python verify.py`. The numerical trials only check finite-time diagnostics; the infinite-time assertions follow from the proof above.

## Relationship to prior work

Boyer and Majumdar, arXiv:2405.10283v1 (16 May 2024), derive Gibbs equilibrium one-time marginals and algebraic relaxation of **one-time densities** for memory resetting in confining potentials; for harmonic confinement their slowest exponent is \(\mu/(r+\mu)\). Their article does not compute the finite-time variance of the integrated position or the occupation-error transition at \(r=\mu\). The later broader kernel treatment by Boyer, Evans and Majumdar, arXiv:2411.00641v1, likewise derives one-time marginal relaxation, not this two-time additive-functional result. Boyer, Evans and Majumdar, arXiv:1611.06743v1, treat resetting with memory in unconfined diffusion, not harmonic time-average fluctuation rates. Stojkoski, Sandev, Kocarev and Pal, arXiv:2107.11686, derive time-average and autocorrelation behavior for resetting **to a fixed initial position**, a different and renewal-based protocol. The present argument requires a genuinely history-dependent jump generator, whose past-time conditional expectation is essential to the \(r y(t)/t\) term.

## Limitations

The statement is about the unconditional **variance** and convergence in \(L^2\), not a central limit theorem, a pathwise law of large numbers, or a full distributional limit of the rescaled time average. It assumes a Gaussian equilibrium initial marginal, time-uniform sampling of the complete past, linear harmonic confinement, independent Poisson reset opportunities and independent Brownian noise. Different memory kernels or initial laws require new calculations. The time-average exponent is not a consequence of one-time marginal convergence alone. General stochastic-approximation or reinforced-process theory could contain an implicit equivalent; independent priority assessment remains to be performed.

## References

- D. Boyer and S. N. Majumdar, *Power-law relaxation of a confined diffusing particle subject to resetting with memory*, arXiv:2405.10283v1, first submitted 2024-05-16, https://arxiv.org/abs/2405.10283.
- D. Boyer, M. R. Evans and S. N. Majumdar, *Diffusion with preferential relocation in a confining potential*, arXiv:2411.00641v1, first submitted 2024-11-01, https://arxiv.org/abs/2411.00641.
- D. Boyer, M. R. Evans and S. N. Majumdar, *Long time scaling behaviour for diffusion with resetting and memory*, arXiv:1611.06743v1, first submitted 2016-11-21, https://arxiv.org/html/1611.06743v1.
- V. Stojkoski, T. Sandev, L. Kocarev and A. Pal, *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, arXiv:2107.11686, first submitted 2021-07-24, https://arxiv.org/abs/2107.11686.
