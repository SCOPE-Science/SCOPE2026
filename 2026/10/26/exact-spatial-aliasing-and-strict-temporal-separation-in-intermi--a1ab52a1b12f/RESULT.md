# Exact spatial aliasing and strict temporal separation in intermittent resetting transport

## Finding

A diffusive–ballistic intermittent search process can have **exactly the same stationary position distribution** under two different complete-reset protocols, while the two stationary position autocovariances are **strictly ordered at every positive time lag**. This phenomenon occurs on one sharp, nondegenerate parameter surface and provides a precise way to distinguish resetting mechanisms that cannot be distinguished by any stationary one-time position statistic.

For the dynamics specified below, put \(L=\beta+\rho\) and \(S=\alpha+\beta+\rho\). Let protocols \(\mathcal D\) and \(\mathcal B\) restart the particle, respectively, in the diffusive mode and in an equiprobable ballistic direction. Their stationary position distributions coincide **if and only if**
\[
v^2=D(\beta+\rho).
\]
On this surface, both are exactly the symmetric Laplace distribution of an ordinary Brownian particle reset to the origin at rate \(\rho\):
\[
p(x)=\frac12\sqrt{\frac{\rho}{D}}\,e^{-\sqrt{\rho/D}|x|},\qquad x\in\mathbb R.
\]

Despite this equality of all stationary position marginals, writing \(C_{\mathcal D}(t)\), \(C_{\mathcal B}(t)\), and \(C_{\mathrm{BM}}(t)\) for the stationary covariances of position at times separated by \(t\), one has, for every \(t>0\),
\[
C_{\mathcal B}(t)>C_{\mathcal D}(t)>C_{\mathrm{BM}}(t),
\]
with the exact formulas
\[
\begin{aligned}
C_{\mathcal D}(t)&=e^{-\rho t}\left[\frac{2D}{\rho}+\frac{D\alpha}{\beta S}(1-e^{-\beta t})\right],\\
C_{\mathcal B}(t)&=e^{-\rho t}\left[\frac{2D}{\rho}+\frac{D(\alpha+\rho)}{\beta S}(1-e^{-\beta t})\right],\\
C_{\mathrm{BM}}(t)&=\frac{2D}{\rho}e^{-\rho t}.
\end{aligned}
\]
Consequently the two intermittently moving systems have an exact positive temporal difference
\[
C_{\mathcal B}(t)-C_{\mathcal D}(t)=\frac{D\rho}{\beta S}e^{-\rho t}(1-e^{-\beta t}),
\]
and a nonzero integrated covariance gap
\[
\int_0^{\infty}\bigl[C_{\mathcal B}(t)-C_{\mathcal D}(t)\bigr]dt
=\frac{D}{S(\beta+\rho)}.
\]
Thus their asymptotic integrated-time-average variance coefficients differ by \(2D/[S(\beta+\rho)]\), although all stationary one-time position distributions agree.

## Assumptions and scope

Fix \(\alpha,\beta,\rho,D,v>0\). The state is \((X_t,J_t)\) with \(X_t\in\mathbb R\) and \(J_t\in\{0,+,-\}\). In state \(0\), \(dX_t=\sqrt{2D}\,dW_t\), with no drift. In state \(+\) (respectively \(-\)), \(dX_t=v\,dt\) (respectively \(dX_t=-v\,dt\)), without Brownian noise. Internal switches \(0\to\pm\) occur at rate \(\alpha/2\) each, and \(\pm\to0\) at rate \(\beta\). Independently, a Poisson clock of rate \(\rho\) resets \(X_t\) to zero and resets \(J_t\) to state \(0\) for \(\mathcal D\), or independently to equiprobable \(+,-\) for \(\mathcal B\). Every reset fully renews the state. For comparison, \(\mathrm{BM}\) has diffusion coefficient \(D\) and position resetting to zero at rate \(\rho\).

All distributions and covariances are evaluated in their unique stationary laws, and the process is defined on the whole real line. Each resetting protocol is symmetric, so \(\mathbb E[X_t]=0\). The statements are exact at fixed positive rates; no singular limits or finite-target first-passage claims are required.

## Proof

**1. Stationary laws and the unique spatial-aliasing surface.** Complete resetting gives a regenerative process with cycle lengths exponentially distributed with parameter \(\rho\); its unique stationary law is the exponentially weighted occupation measure over a fresh cycle. Exponential tails of the cycle length and finite Brownian moments imply all polynomial position moments exist.

Set \(L=\beta+\rho\), \(S=\alpha+\beta+\rho\), and write \(k\in\mathbb R\) for the Fourier variable. Solving the three stationary forward Fourier equations, with the reset injection to \(0\) or equally to \(+,-\), yields the characteristic functions
\[
\Phi_{\mathcal D}(k)=\frac{\rho(LS+v^2k^2)}{Q(k)},\qquad
\Phi_{\mathcal B}(k)=\frac{\rho L(S+Dk^2)}{Q(k)},
\]
where
\[
Q(k)=(\rho+Dk^2)(L^2+v^2k^2)+\alpha(\rho L+v^2k^2)>0.
\]
The difference is
\[
\Phi_{\mathcal D}(k)-\Phi_{\mathcal B}(k)
=\frac{\rho k^2[v^2-DL]}{Q(k)}.
\]
For any nonzero real \(k\), this vanishes exactly when \(v^2=DL\); thus that balance is necessary and sufficient for equality of the two complete position distributions. At balance, the denominator factorizes as \(Q(k)=L(\rho+Dk^2)(S+Dk^2)\), and both numerators become \(\rho L(S+Dk^2)\). Therefore
\[
\Phi_{\mathcal D}(k)=\Phi_{\mathcal B}(k)=\frac{\rho}{\rho+Dk^2}.
\]
Fourier inversion gives the stated symmetric Laplace density, identical to the stationary resetting-Brownian law.

**2. Hidden modes and cross position–heading moment.** Let \(\eta(J)\) be \(0,+1,-1\) on states \(0,+,-\), and let \(\pi_{\mathrm{bal}}\) denote total stationary probability of a ballistic state. The stationary two-state balance immediately gives
\[
\pi_{\mathrm{bal}}^{\mathcal D}=\frac{\alpha}{S},\qquad
\pi_{\mathrm{bal}}^{\mathcal B}=\frac{\alpha+\rho}{S}.
\]
For \(H=\mathbb E[X\eta(J)]\), the stationary generator applied to \(X\eta(J)\) gives
\[
0=v\pi_{\mathrm{bal}}-(\beta+\rho)H,
\qquad H=\frac{v\pi_{\mathrm{bal}}}{L}.
\]
Indeed, a transition out of \(+\) or \(-\) erases heading memory at rate \(\beta\), resetting erases the product at rate \(\rho\), and a \(0\to\pm\) switch has zero mean heading. Applying the generator to \(X^2\) gives
\[
0=2D(1-\pi_{\mathrm{bal}})+2vH-\rho\mathbb E[X^2].
\]
On the balancing surface, \(v^2=DL\), this reduces to \(\mathbb E[X^2]=2D/\rho\) for both protocols, as also follows from the common characteristic function.

**3. Full two-time covariance and strict separation.** Conditional on current position \(x\) and heading \(\eta\), the mean after a positive lag \(t\) is
\[
\mathbb E[X_t\mid X_0=x,J_0]
=e^{-\rho t}\left[x+\frac{v\eta}{\beta}(1-e^{-\beta t})\right].
\]
This follows by conditioning on no reset during the lag; after any reset the subsequent conditional mean is zero by sign symmetry. Without resetting, the initial heading persists in mean as \(\eta e^{-\beta s}\); later headings generated from a diffusive state have zero conditional mean. Multiplying by \(X_0\), then averaging the stationary state, proves for either protocol
\[
C(t)=e^{-\rho t}\left[\mathbb E[X^2]+\frac{v^2\pi_{\mathrm{bal}}}{\beta(\beta+\rho)}(1-e^{-\beta t})\right].
\]
Substituting the common variance and the two different ballistic fractions gives both stated exact covariance formulas. Since \(\alpha,\beta,\rho,D>0\), the strict all-positive-lag ordering follows. Integrating the difference term by term proves the stated integrated gap. For an ergodic stationary process with integrable covariance, \(T\operatorname{Var}(T^{-1}\int_0^T X_tdt)\to2\int_0^\infty C(s)ds\); the covariance formula gives exponential decay, so this application is justified.

The temporal gap has a unique maximum at \(t_*=\beta^{-1}\log(1+\beta/\rho)\), obtained by differentiating the strictly positive explicit function.

## Verification

`CHECK.py` uses independent stationary mode and moment linear systems, a six-dimensional lagged cross-moment matrix semigroup, a separate complex Fourier stationary solve, and symbolic factorization. Executing `python CHECK.py` with Python, NumPy, SciPy, and SymPy installed returns `PASS: 622 exact symbolic / independent matrix-generator assertions`. Its numerical grids include both balancing and off-balance parameters; no finite numerical check is treated as proof of the all-parameter assertions.

For example, with \(\alpha=2\), \(\beta=3\), \(\rho=1\), \(D=2\), \(v=2\sqrt 2\), all three stationary position densities equal \(e^{-|x|/\sqrt2}/(2\sqrt2)\), but
\[
\begin{aligned}
C_{\mathcal D}(t)&=e^{-t}\left[4+\frac29(1-e^{-3t})\right],\\
C_{\mathcal B}(t)&=e^{-t}\left[4+\frac13(1-e^{-3t})\right],\\
C_{\mathcal B}(t)-C_{\mathcal D}(t)&=\frac19 e^{-t}(1-e^{-3t}).
\end{aligned}
\]
The integrated covariance difference is \(1/12\), corresponding to a time-average asymptotic variance coefficient difference of \(1/6\).

## Relationship to prior work

Flaquer-Galmés, Campos, and Méndez derive precisely this diffusive/ballistic switching model, its two fully renewed resetting protocols, its Fourier–Laplace propagators, its separate stationary spatial density formulas, and mean-square displacements (Physical Review E 109, 034103, 2024, particularly equations (1)–(8), (26)–(32) and Appendix B). **The equality of the two stationary spatial laws on a tuned parameter surface is an algebraic specialization of their existing stationary formulas and is not presented here as independently original.** The present mathematical finding is the exact joint statement that this spatial aliasing occurs if and only if the stated balance holds, while *all* positive-lag stationary position correlations remain strictly separated with an explicit integrated discrepancy. Their paper does not derive stationary two-time position covariances.

Santra, Olsen, and Gupta (Soft Matter 20, 9360–9372, 2024) derive transform and cumulant methods for intermittently active motion, without establishing this complete-reset stationary two-time contrast. Datta, Beta, and Großmann (Physical Review Research 6, 043281, 2024) analyze autocorrelation and transport in intermittently propelled particles without the present competing resetting protocols. Gupta (Frontiers in Physics 10, 789097, 2022) reviews the classical resetting-Brownian law and renewal framework, which supply the exact comparison law but not the new hybrid all-lag comparison.

## Limitations

The system requires positive switching, diffusion, speed, and resetting rates, symmetric choice of ballistic directions, complete resetting of position and motion state, and Poisson clocks. The equality is of one-time stationary *position* laws only; full stationary joint states and time-dependent laws are different. In particular, equality of the stationary marginals must not be interpreted as process-level equivalence. The result does not cover incomplete resets, asymmetric ballistic switching, non-Poisson renewal clocks, target-detection statistics, or higher-dimensional motion. An equivalent specialization of broader switching-process theory remains a possible priority risk; the mathematical novelty is assessed only against the inspected sources and not independently certified.

## References

1. R. Flaquer-Galmés, D. Campos, and V. Méndez, *Intermittent random walks under stochastic resetting*, Physical Review E 109, 034103 (2024). arXiv:2401.16849, doi:10.1103/PhysRevE.109.034103. First arXiv submission: 2024-01-30. Public full text: https://webs.uab.cat/vmendez/wp-content/uploads/sites/97/2024/03/127.pdf.
2. I. Santra, K. S. Olsen, and D. Gupta, *Dynamics of switching processes: general results and applications in intermittent active motion*, Soft Matter 20, 9360–9372 (2024), doi:10.1039/D4SM01054J.
3. A. Datta, C. Beta, and R. Großmann, *Random walks of intermittently self-propelled particles*, Physical Review Research 6, 043281 (2024), doi:10.1103/PhysRevResearch.6.043281.
4. S. Gupta, *Stochastic Resetting: A (Very) Brief Review*, Frontiers in Physics 10, 789097 (2022), doi:10.3389/fphy.2022.789097.
