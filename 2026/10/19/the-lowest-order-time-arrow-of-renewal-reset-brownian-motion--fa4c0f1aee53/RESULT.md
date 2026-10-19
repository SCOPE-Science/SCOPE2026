# The lowest-order time arrow of renewal-reset Brownian motion

## Finding

Let \(X\) be the stationary, one-dimensional Brownian diffusion with independent, complete instantaneous resets to zero at renewal epochs, with \(dX=\sqrt{2D}\,dB\) between resets. Every reset renews the Brownian noise. The independent and identically distributed inter-reset duration \(T\) satisfies \(T>0\) almost surely, \(D>0\), \(0<\mu=\mathbb E T<\infty\), and \(\mathbb E T^3<\infty\). No density or nonlattice assumption is imposed on \(T\).

For every \(t>0\), define the time-oriented fourth-moment difference
\[
\Delta(t)=\mathbb E[X_0X_t^3]-\mathbb E[X_0^3X_t].
\]
Then the exact, distribution-free renewal identity is
\[
\boxed{\Delta(t)=\frac{6D^2t}{\mu}\,\mathbb E[(T-t)_+^2],\qquad t>0.}
\]
Consequently \(\Delta(t)>0\) exactly when \(\mathbb P(T>t)>0\), and \(\Delta(t)=0\) otherwise. Thus a fourth-order two-time statistic detects the direction of time for every lag below the essential maximum of the reset duration. Every two-time polynomial moment of total degree at most three is invariant under interchanging the two observation times: fourth order is minimal for this statistic-based detection under spatial sign symmetry.

Write \(H(t)=\Delta(t)/t\) for \(t>0\), extending continuously at zero. Its right second derivative exists at every \(t\ge0\), including reset-duration atoms, and
\[
\boxed{H''_+(t)=\frac{12D^2}{\mu}\,\mathbb P(T>t).}
\]
Here \(H''_+(t)\) denotes the right derivative of \(H'(t)\). In particular
\[
\boxed{\mathbb P(T>t)=\frac{H''_+(t)}{H''_+(0)}\quad(t\ge0),\qquad
D=\left(\frac{\mu\,\Delta'(0+)}{6\mathbb E[T^2]}\right)^{1/2}.}
\]
Therefore the full *physical-time* lag curve \(\Delta\) identifies both the complete inter-reset duration law and the unknown diffusion coefficient \(D\), without recording resets. This is exact identifiability from an ideal noiseless population-level function, not a numerical stability guarantee for empirical second differentiation.

The same reset-age calculation yields a positive hierarchy: for every integer \(m\ge1\) with \(\mathbb E[T^{m+2}]<\infty\),
\[
\begin{aligned}
\Delta_m(t)&=\mathbb E[X_0X_t^{2m+1}]-\mathbb E[X_0^{2m+1}X_t]\\
&=\frac{2(2m+1)!D^{m+1}}{\mu}
\sum_{j=1}^{m}\frac{m+1-j}{j!(m+1-j)!(m+2-j)}
 t^j\,\mathbb E[(T-t)_+^{m+2-j}].
\end{aligned}
\]
Every summand is nonnegative; when \(\mathbb P(T>t)>0\), every such \(\Delta_m(t)\) is strictly positive. The inversion uses only \(m=1\); the higher identities exhibit the same time orientation at all admissible even total moment orders.

## Assumptions and scope

Construct a two-sided stationary equilibrium renewal point process with strictly positive independent inter-event times distributed as \(T\). Sample a cycle by length-biasing \(T\), then choose the observation origin uniformly within that cycle. Each cycle carries an independent standard Brownian path beginning at the reset point zero; a complete reset discards previous displacement and starts independent noise. In this construction \(X_t\) is strictly stationary. Define the age \(A\ge0\) and forward residual duration \(R\ge0\) at time zero. For all Borel \(E\subseteq[0,\infty)\) and \(t\ge0\), their equilibrium joint law implies
\[
\mathbb E[\mathbf1_{\{A\in E,\,R>t\}}]
=\frac1\mu\int_E\mathbb P(T>a+t)\,da.
\]
The hypothesis \(\mathbb E T^3<\infty\) makes all mixed fourth moments finite, since \(\mathbb E[A^2]=\mathbb E[T^3]/(3\mu)\). The hierarchy requires \(\mathbb E T^{m+2}<\infty\) for finiteness of the two mixed moments of total degree \(2m+2\). All derivatives are ordinary in the interior when smooth and are interpreted as right derivatives at atoms. \((x)_+=\max\{0,x\}\).

## Proof

**1. Renewal separation.** Fix \(t>0\) and condition on the complete renewal schedule. If one or more resets lie in \((0,t]\), then \(X_0\) and \(X_t\) are independent centered Gaussian random variables conditional on the schedule, because they belong to independent Brownian excursions. Consequently both crossed odd mixed moments vanish. The probability that a reset occurs exactly at an observation time does not affect this conclusion: a stationary renewal origin has no renewal atom at deterministic time zero, and the event of renewal at fixed lag likewise has probability zero after the cycle's uniform time shift.

**2. Gaussian expansion without a reset.** Conditional on an age \(A=a\) and no reset before \(t\), write \(X_0=U\), \(X_t=U+V\), where \(U\) and \(V\) are independent centered Gaussians of variances \(2Da\) and \(2Dt\). Wick's identity gives
\[
\mathbb E[U(U+V)^3-U^3(U+V)]=3(2Da)(2Dt)=12D^2at.
\]
Integrating against the equilibrium age/residual law produces
\[
\Delta(t)=\frac{12D^2t}{\mu}\int_0^\infty a\,\mathbb P(T>a+t)\,da
=\frac{6D^2t}{\mu}\,\mathbb E[(T-t)_+^2].
\]
The last equality follows from Tonelli and \(\int_0^{(T-t)_+}a\,da=(T-t)_+^2/2\). Positive lag, positive diffusivity and the positivity of a squared positive part yield the strict sign criterion.

**3. Inversion and the boundary.** Define \(f(t)=\mathbb E[(T-t)_+^2]\), \(t\ge0\). By dominated convergence, \(f'(t)=-2\mathbb E[(T-t)_+]\), and its right derivative satisfies \(f''_+(t)=2\mathbb P(T>t)\) at every \(t\ge0\), including atoms. Thus \(H(t)=6D^2f(t)/\mu\) gives \(H''_+(t)=12D^2\mathbb P(T>t)/\mu\). As \(T>0\) almost surely, \(H''_+(0)=12D^2/\mu>0\), and division recovers the entire right-continuous survival function. The small-lag slope is \(\Delta'(0+)=H(0)=6D^2\mathbb E[T^2]/\mu\). Since the recovered survival function fixes \(\mu\) and \(\mathbb E T^2\), this slope fixes the positive \(D\) uniquely.

**4. Minimal degree of time asymmetry.** Stationarity makes all one-time moments at times zero and \(t\) equal. Spatial reflection invariance of the Brownian excursions makes every joint moment of odd total degree zero. At total degree two the only mixed moment \(\mathbb E[X_0X_t]\) is unchanged on exchange. Thus all polynomial two-time moments of total degree at most three are exchange-symmetric. The displayed fourth-order statistic is strictly asymmetric whenever \(\mathbb P(T>t)>0\).

**5. Higher moments.** For integer \(m\ge1\), the two mixed terms differ on a no-reset interval by
\[
\sum_{j=1}^{m}\binom{2m+1}{2j}\mathbb E[U^{2m+2-2j}]\mathbb E[V^{2j}].
\]
Using Gaussian double-factorial moments, the summand equals
\[
\frac{2(2m+1)!(m+1-j)}{j!(m+1-j)!}
D^{m+1}a^{m+1-j}t^j.
\]
The equilibrium renewal integral of \(a^{m+1-j}\mathbf1_{\{R>t\}}\) is \(\mathbb E[(T-t)_+^{m+2-j}]/[\mu(m+2-j)]\). Substitution gives the stated hierarchy, with all terms positive whenever \(\mathbb P(T>t)>0\).

## Verification

A standalone standard-library Python program, `verify.py`, independently computes the hierarchy using (i) Gaussian pair-moment expansion integrated over the cycle age and (ii) the positive-part moment formula. These were compared at exact rational arithmetic for deterministic, two-point, and three-point inter-reset distributions over multiple lags, diffusion coefficients, and orders through the tenth total moment. It additionally tests the fourth-order collapse and the normalized inverse by exact second finite differences away from interarrival atoms. Execution reports 899 passing checks. Tests confirm finite parameter cases only; the analytic proof supplies the arbitrary-law, arbitrary-lag quantifiers.

For an exponential reset time with rate \(r>0\),
\[
\Delta(t)=\frac{12D^2}{r}t e^{-rt},
\]
whose maximum is at \(t=1/r\). For periodic resets with duration \(b>0\),
\[
\Delta(t)=\frac{6D^2}{b}t(b-t)_+^2,
\]
whose unique positive maximum is at \(t=b/3\). Both examples are immediate exact checks of the theorem.

## Relationship to prior work

Singh, Górska and Sandev (2022), *General approach to stochastic resetting*, establish renewal formulations, time-one propagators and mean-square displacement for arbitrary reset-time laws. Masó-Puigdellosas, Campos and Méndez (2022), *Conditioned backward and forward times of diffusion with stochastic resetting*, derive the renewal age/residual structure and position-conditioned renewal times. Those ingredients explain the stationary construction here. The inspected full-text statements concern one-time or conditioned-age quantities, rather than the oriented fourth-order two-time difference or recovery of both parameters from it.

Sokolov (2023), *Linear Response and Fluctuation-Dissipation Relations for Brownian Motion under Resetting*, studies renewal Brownian response and second-order fluctuation–dissipation relations. The publicly accessible abstract was checked, but the article's complete text was unavailable under the available legitimate access conditions. Second-order covariance can already encode the reset law, and the present formula itself obeys the exact identity \(\Delta(t)=6Dt\,\mathbb E[X_0X_t]\). Hence the reset-law identification is **not** claimed to be independent information beyond the full covariance if \(D\) is known. The distinct evaluated contribution is the least-order *time-antisymmetric* statistic, its positive renewal stop-loss representation and all-order positive hierarchy. These differences do not establish priority over inaccessible more general treatments.

Colantoni, D'Ovidio and Pagnini (2025), *Time reversal of Brownian motion with Poissonian resetting*, investigate a reflected half-line process and its reverse semigroup under exponential resetting. That later setting is different from arbitrary-renewal, unreflected Brownian excursions and does not assert the above moment-contrast inversion in the inspected article.

## Limitations

This is a theoretical exact, noise-free stationary identification theorem. Differentiating empirical temporal correlations twice can severely amplify observation noise; no rates, stable estimator, finite-record identifiability or confidence regions are proved. Independent complete resets, stationary renewal initialization, scalar zero-drift free Brownian excursions, strict positivity of inter-reset durations and the stated moment assumptions are necessary parts of the result. The argument does not treat partial position resets, correlated driving noise, drifts, observation errors or interacting particles. The fourth-order identity is proportional to covariance; any existing general theorem implying the same conditional Gaussian renewal structure may also imply it. The accessible primary comparisons do not certify absolute novelty, and a relevant response-theory full text remains an explicit priority risk. No independent mathematical assessment has been performed.

## References

1. R. K. Singh, K. Górska and T. Sandev, *General approach to stochastic resetting* (first public 2022-03-08), arXiv:2203.04046, https://arxiv.org/abs/2203.04046 .
2. A. Masó-Puigdellosas, D. Campos and V. Méndez, *Conditioned backward and forward times of diffusion with stochastic resetting: a renewal theory approach* (first public 2022-05-03), arXiv:2205.01613, https://arxiv.org/abs/2205.01613 .
3. I. M. Sokolov, *Linear Response and Fluctuation-Dissipation Relations for Brownian Motion under Resetting*, Phys. Rev. Lett. 130, 067101 (2023), https://doi.org/10.1103/PhysRevLett.130.067101 .
4. F. Colantoni, M. D'Ovidio and G. Pagnini, *Time reversal of Brownian motion with Poissonian resetting* (2025), arXiv:2505.15639, https://arxiv.org/abs/2505.15639 .
