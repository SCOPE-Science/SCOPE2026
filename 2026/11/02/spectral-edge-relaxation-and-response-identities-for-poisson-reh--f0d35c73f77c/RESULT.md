# Spectral-edge relaxation and response identities for Poisson-reheated power-law cooling

## Finding

For the stationary, globally Poisson-reheated deterministic cooling model defined below, the centered granular-temperature covariance has an **explicit strictly positive continuous relaxation-rate spectrum**. Its density is positive at every rate strictly above \(r\), with topological support \([r,\infty)\), no atom at \(r\), and lower-edge density exponent \(p\), and its long-lag decay is

\[
C(h)\sim \frac{pT_0}{c^p}\,\frac{\partial\mu}{\partial r}\,
 e^{-rh}h^{-(p+1)}\qquad(h\to\infty).
\]

The covariance is strictly completely monotone on nonnegative lags (using right derivatives at zero) and strictly log-convex. Its instantaneous logarithmic decay rate decreases strictly to \(r\), with correction \((p+1)/h\). Consequently the stationary covariance alone identifies the reset rate \(r\) and the cooling exponent \(p\); knowing the reset temperature \(T_0\), the stationary mean additionally identifies the cooling constant \(c\). The initial covariance slope also obeys the exact reset-jump identity

\[
-C'(0+)=\frac r2\,\mathbb E[(T_0-T_t)^2].
\]

This constitutes one temporal-covariance and identification theorem, rather than a statement about particle-level collision fluctuations.

## Assumptions and scope

Fix \(T_0>0\), \(r>0\), \(c>0\), and \(p>0\). Let independent global reheating events form a stationary, two-sided homogeneous Poisson point process of rate \(r\). Between events, the **macroscopic temperature in the deterministic homogeneous-cooling closure** follows \(f(a)=T_0(1+ca)^{-p}\), where \(a\ge0\) is time elapsed since the most recent reheating event. At each event the temperature jumps to exactly \(T_0\). Denote the elapsed time at observation time \(t\) by \(A_t\), and set \(T_t=f(A_t)\). This defines a unique stationary version: \(A_t\) has exponential distribution with rate \(r\). All asserted limits are for this stationary process; all lags satisfy \(h\ge0\). Write

\[
\mu=\mathbb E[T_t]
=T_0r\int_0^\infty e^{-ra}(1+ca)^{-p}\,da,
\qquad
C(h)=\operatorname{Cov}(T_t,T_{t+h}).
\]

Here \(p=2\) is the constant-restitution Haff cooling case; \(p=5/3\) is the generalized viscoelastic example treated in the motivating source. The physical cooling-time parameter is \(c=1/\tau_0\). No assumption of particle-level Gaussianity, finite-particle molecular dynamics, thermal bath noise, non-Poisson reheating, or incomplete resetting is included in the theorem.

Define the positive gamma-Laplace density and a strictly positive kernel, for \(u,v>0\), by

\[
m_p(u)=\frac{T_0u^{p-1}e^{-u/c}}{\Gamma(p)c^p},
\quad
K_r(u,v)=\frac{ruv}{(r+u+v)(r+u)(r+v)}.
\]

## Proof

**1. Stationary renewal identity.** Let \(A\sim\operatorname{Exp}(r)\). A fresh Poisson event during a lag interval makes its terminal temperature independent of the temperature at the start. If no event occurs, whose probability is \(e^{-rh}\), the terminal age is \(A+h\). Subtracting the stationary product of means gives the exact identity

\[
C(h)=e^{-rh}\,\operatorname{Cov}(f(A),f(A+h))
=e^{-rh}r\int_0^\infty e^{-ra}(f(a)-\mu)f(a+h)\,da.
\]

At zero lag this is precisely the stationary variance \(C(0)=\operatorname{Var}(T_t)>0\). All integrals converge because \(0<f(a)\le T_0\).

**2. Positive spectral representation.** The gamma integral provides

\[
f(a)=\int_0^\infty m_p(u)e^{-ua}\,du.
\]

Fubini is valid by boundedness and nonnegativity of the uncentered products. For \(u,v>0\), independence of the stationary age transform gives

\[
\operatorname{Cov}(e^{-uA},e^{-vA})
=\frac{r}{r+u+v}-\frac{r^2}{(r+u)(r+v)}
=K_r(u,v)>0.
\]

Inserting both Laplace mixtures and grouping the factor containing \(h\) produces

\[
\boxed{\quad C(h)=\int_0^\infty e^{-(r+v)h}w_p(v)\,dv,\quad
w_p(v)=m_p(v)\int_0^\infty m_p(u)K_r(u,v)\,du>0.\quad}
\]

Every positive \(v\) carries positive weight and no weight occurs outside \((0,\infty)\). In particular the relaxation rates have spectral support exactly \([r,\infty)\), with no atom at \(r\). Exponential decay of \(m_p\) at large arguments and positive denominators ensure finite weighted moments of every nonnegative integer order. Differentiation under the integral therefore gives \((-1)^k C^{(k)}(h)>0\) for all integers \(k\ge0\) and all \(h>0\), including right-hand derivatives at \(h=0\). Under the exponentially tilted probability density proportional to \(e^{-(r+v)h}w_p(v)\), one has

\[
-\frac{d}{dh}\log C(h)=r+\mathbb E_h[V]>r,
\qquad
\frac{d^2}{dh^2}\log C(h)=\operatorname{Var}_h(V)>0.
\]

Strictness follows from positive weight at every \(v>0\), which excludes a point-mass relaxation spectrum.

**3. Edge coefficient and static response.** Direct differentiation of the mean with respect to the reset rate, justified by exponential domination, yields

\[
Q:=\frac{\partial\mu}{\partial r}
=\int_0^\infty m_p(u)\frac{u}{(r+u)^2}\,du>0.
\]

Using \(K_r(u,v)/v\to u/(r+u)^2\) as \(v\downarrow0\), dominated convergence (and a first-order Taylor bound on its rational denominator) gives

\[
\boxed{\quad
w_p(v)=\frac{T_0Q}{\Gamma(p)c^p}\,v^p(1+O(v))
\quad(v\downarrow0).\quad}
\]

This explicit positive edge is the critical nonstandard calculation: the covariance of the two age exponentials vanishes to **first order in the slower Laplace frequency** \(v\), which creates one additional power beyond the bare temperature's cooling exponent. Watson's lemma then gives

\[
C(h)=\frac{pT_0Q}{c^p}
 e^{-rh}h^{-(p+1)}(1+O(h^{-1})).
\]

The rational kernel is smooth in \(v\) near zero after factoring out \(v\); its Taylor expansion under the integrable gamma density permits a differentiated two-term Watson expansion. Therefore

\[
\Lambda(h):=-\frac{C'(h)}{C(h)}
=r+\frac{p+1}{h}+O(h^{-2})\qquad(h\to\infty).
\]

For Haff cooling, \(p=2\), the leading algebraic factor is \(h^{-3}\); for the viscoelastic exponent \(p=5/3\) it is \(h^{-8/3}\). In both cases the exponential prefactor is \(e^{-rh}\).

**4. Short-time identity.** The stationary age generator on differentiable bounded test functions is \((\mathcal Lg)(a)=g'(a)+r(g(0)-g(a))\). Stationarity of \((f-\mu)^2\) gives

\[
2\mathbb E[(f(A)-\mu)f'(A)]
+r\bigl((T_0-\mu)^2-C(0)\bigr)=0.
\]

Differentiating the exact lag covariance at zero from the right and substituting this relation yields

\[
C'(0+)=\mathbb E[(f(A)-\mu)f'(A)]-rC(0)
=-\frac r2\bigl(C(0)+(T_0-\mu)^2\bigr)
=-\frac r2\mathbb E[(T_0-T_t)^2].
\]

This is an application of the general stationary jump-generator quadratic identity, not an assertion of a new general fluctuation-dissipation theorem.

**5. Exact parameter identifiability.** Positivity of \(C\) ensures that its logarithmic derivative is observable mathematically. The preceding asymptotic and strict complete monotonicity give

\[
\boxed{\quad
r=\lim_{h\to\infty}\Lambda(h),\qquad
p=\lim_{h\to\infty}h(\Lambda(h)-r)-1.
\quad}
\]

Given known \(T_0\), the map \(c\mapsto\mu\) is continuous and strictly decreasing from \(T_0\) to zero because

\[
\frac{\partial\mu}{\partial c}
=-pT_0\mathbb E[A(1+cA)^{-p-1}]<0.
\]

Thus \(\mu\in(0,T_0)\) determines exactly one \(c>0\). If the full stationary one-time law is available, its essential supremum is \(T_0\); this removes the need to specify \(T_0\) externally. The rate also has an independent stationary short-lag characterization:

\[
r=\frac{-2C'(0+)}{C(0)+(T_0-\mu)^2}.
\]

These formulas concern identifiability from exact probability laws, not statistical efficiency from finite or noisy data.

## Verification

The reproducible \(\texttt{verify.py}\) compares the renewal-age integral against the independently discretized positive gamma-mixture double integral; checks the small-rate spectral-edge constant, the stationary-mean derivative, and convergence to the sharp long-time amplitude; checks strict finite-difference log-convexity; and tests the short-lag generator identity. Across \(288\) comparisons at multiple positive rate, cooling, and exponent parameters it passes. The largest relative discrepancy among tested renewal and gamma-mixture covariances is \(4.82\times10^{-7}\) (limited by finite quadrature order); all finite checks supplement, rather than replace, the analytic proof. Run \(\texttt{python verify.py}\) with Python, NumPy and SciPy.

For the independent benchmark \(T_0=2\), \(r=1.3\), \(c=0.8\), \(p=2\), quadrature gives \(\mu=1.018092185024425\), \(Q=0.338910900548878\) and long-time amplitude \(2.118193128430484\). The \(O(h^{-1})\) correction was tested at increasing finite lags; numerical tests alone do not establish the infinite-lag limits.

## Relationship to prior work

Bodrova, Chechkin and Dubey [1] explicitly establish the model's generalized Haff cooling, complete stationary **one-time** temperature distribution, mean and variance, including \(p=2\) and \(p=5/3\). Those are premises, not newly asserted results. Their main text does not provide this centered two-time covariance, positive relaxation-rate density, full-edge amplitude, or covariance-based parameter-recovery formulas. Majumdar and Oshanin [2] establish general renewal-based correlation and power-spectrum techniques for reset stochastic processes; the same renewal principle is explicitly credited here. Rose and collaborators [3] analyze how resetting shifts generator eigenvalues, without the specific continuous spectral-edge weight and static-response identity in the granular cooling model. The contribution here is a **joint, explicit, all-positive-parameter evaluation for the source's physical power-law cooling family**, including strict spectral positivity, the one-power covariance exponent shift, exact amplitude tied to a stationary reset-rate derivative, and covariance-based identification. The stationary generator's short-lag quadratic identity is a standard mechanism used as a consistency check, not claimed as a new general lemma.

## Limitations

The temperature trajectory is deterministic between globally synchronous Poisson reheatings. Particle-scale collision noise, non-Haff nonlinear corrections, clustering, finite-particle fluctuations, partial/intermittent heating, arbitrary renewal waiting times, and observation errors are outside the theorem. The positive relaxation-rate mixture is a representation of the stationary covariance, not a complete microscopic scattering spectrum. Exact mathematical identifiability does not imply stable numerical parameter estimation from finite observations. The proof establishes an asymptotic covariance and all strict finite-lag derivative signs, not any finite-sample confidence region. Comparison with broader renewal-process treatments may affect publication priority.

## References

[1] A. S. Bodrova, A. V. Chechkin and A. K. Dubey, *Granular gases under resetting*, arXiv:2403.18974 (first public 27 March 2024; full arXiv v5 available), subsequently *Physical Review E* **111**, 015405 (2025), DOI:10.1103/PhysRevE.111.015405. https://arxiv.org/html/2403.18974v5

[2] S. N. Majumdar and G. Oshanin, *Spectral content of fractional Brownian motion with stochastic reset*, arXiv:1806.03435 (2018), especially Sections II–III on reset correlation and frequency power spectra. https://arxiv.org/abs/1806.03435

[3] D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298 (2018), especially Sections II–III. https://arxiv.org/html/1806.01298v2
