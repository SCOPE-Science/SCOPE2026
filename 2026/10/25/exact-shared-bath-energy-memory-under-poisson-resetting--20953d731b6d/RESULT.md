# Exact shared-bath energy memory under Poisson resetting

## Finding
For each integer \(d\ge 1\), a particle with \(d\) independently driven Cartesian coordinates but one common Brownian diffusivity, reset jointly with its diffusivity at Poisson rate \(r>0\), has an exactly solvable stationary *squared-position* autocovariance matrix. Let \(\Lambda>0\) be the diffusivity-noise amplitude and \(Q_t=\sum_{i=1}^d X_i(t)^2\). For every \(s\ge0\) and \(1\le i,j\le d\),
\[
\operatorname{Cov}(X_i(0)^2,X_j(s)^2)
=\frac{16\Lambda^4}{r^4}\,e^{-rs}\left(13+6rs+28\mathbf 1_{\{i=j\}}\right).
\]
Consequently,
\[
\mathbb E Q_t=\frac{4d\Lambda^2}{r^2},\qquad
\operatorname{Cov}(Q_0,Q_s)=\frac{16\Lambda^4d}{r^4}(13d+28+6drs)e^{-rs},
\]
and the exact long-time variance coefficient of the stationary temporal mean is
\[
\lim_{T\to\infty}T\,\operatorname{Var}\!\left(\frac1T\int_0^T Q_t\,dt\right)
=\frac{32\Lambda^4}{r^5}d(19d+28).
\]
In particular, with energy normalized by its stationary expectation, the sequential dimension and time limits yield
\[
\lim_{d\to\infty}\lim_{T\to\infty}T\,\operatorname{Var}\!\left(\frac1T\int_0^T\frac{Q_t}{\mathbb E Q_t}\,dt\right)
=\frac{38}{r}>0.
\]
Thus averaging over arbitrarily many coordinates does **not** suppress the long-time measurement variance when their stochastic diffusivity and reset clock are common. The same one-coordinate model with *independent* diffusivities and resetting clocks for each coordinate has normalized coefficient \(94/(rd)\), which vanishes as \(d\to\infty\).

## Assumptions and scope
Fix integer \(d\ge1\), constants \(r,\Lambda>0\), independent standard Brownian motions \(B_0,B_1,\ldots,B_d\), and one independent homogeneous Poisson clock of rate \(r\). Between events,
\[
 d\omega_t=\sqrt2\Lambda\,dB_{0,t},\qquad
 dX_i(t)=\sqrt2\,\omega_t\,dB_{i,t},\quad 1\le i\le d.
\]
At **each common** Poisson event, \((\omega,X_1,\ldots,X_d)\) is set to zero. The signed coefficient \(\omega\) has the same conditional coordinate distribution as the physical nonnegative amplitude \(|\omega|\) when multiplying independent Brownian noises; thus the instantaneous diffusivity is \(\omega^2\). All stationary and lagged quantities in the theorem are taken in the unique stationary regenerative version, and \(s\) is a nonnegative time lag. No claim is made about unequal or partially coordinated resets, non-Brownian diffusivity environments, or interchange of the time and dimension limits.

## Proof
**Stationarity and moment legitimacy.** Two versions driven by the same Poisson clock become identical after the next reset, giving a unique regenerative stationary law. The elapsed time since the previous reset has the exponential distribution with rate \(r\), independent of the Brownian increments of the current cycle. Conditional on that age, the Brownian-functionals defining each coordinate have moments of all orders; the exponential age has all moments, so the polynomial generator moment identities below are legitimate.

**Polynomial generator and fourth moments.** For smooth polynomials of the state, the generator is
\[
\mathcal Lf=\omega^2\sum_{i=1}^d\partial_{x_i}^2f
+\Lambda^2\partial_\omega^2f+r[f(0,\boldsymbol0)-f(\omega,\boldsymbol x)].
\]
Writing \(\langle\cdot\rangle\) for a stationary expectation, applying \(\langle\mathcal Lf\rangle=0\) successively to \(\omega^2,\omega^4,X_i^2,X_i^2\omega^2,X_i^2X_j^2\) (for \(i\ne j\)) and \(X_i^4\) gives
\[
\begin{aligned}
\langle\omega^2\rangle&=2\Lambda^2/r,&
\langle\omega^4\rangle&=24\Lambda^4/r^2,\\
\langle X_i^2\rangle&=4\Lambda^2/r^2,&
\langle X_i^2\omega^2\rangle&=56\Lambda^4/r^3,\\
\langle X_i^2X_j^2\rangle&=224\Lambda^4/r^4\quad(i\ne j),&
\langle X_i^4\rangle&=672\Lambda^4/r^4.
\end{aligned}
\]
For example, \(\mathcal L(X_i^2\omega^2)=2\omega^4+2\Lambda^2 X_i^2-rX_i^2\omega^2\), while \(\mathcal L(X_i^2X_j^2)=2\omega^2(X_i^2+X_j^2)-rX_i^2X_j^2\) for distinct indices. It follows that
\[
\operatorname{Cov}(X_i^2,X_j^2)=\frac{\Lambda^4}{r^4}(208+448\mathbf1_{\{i=j\}}),\qquad
\operatorname{Cov}(X_i^2,\omega^2)=\frac{48\Lambda^4}{r^3}.
\]

**Full temporal covariance.** Put \(g_j=X_j^2-4\Lambda^2/r^2\) and \(h=\omega^2-2\Lambda^2/r\). These centered observables form a closed generator block:
\[
\mathcal Lh=-rh,\qquad \mathcal Lg_j=2h-rg_j.
\]
The backward semigroup on this invariant polynomial subspace therefore satisfies, for every \(s\ge0\),
\[
P_sg_j=e^{-rs}(g_j+2sh).
\]
Stationarity and the Markov property give
\[
\begin{aligned}
\operatorname{Cov}(X_i(0)^2,X_j(s)^2)
&=\langle g_iP_sg_j\rangle\\
&=e^{-rs}\left[\frac{\Lambda^4}{r^4}(208+448\mathbf1_{\{i=j\}})+\frac{96s\Lambda^4}{r^3}\right],
\end{aligned}
\]
which is the stated formula. Summing over the \(d\) diagonal and \(d(d-1)\) off-diagonal entries yields the covariance of \(Q\).

**Temporal measurement limit and persistence at large dimension.** For a stationary real process with absolutely integrable autocovariance \(C_Q(s)\),
\[
T\operatorname{Var}\!\left(\frac1T\int_0^TQ_t\,dt\right)
=2\int_0^T(1-s/T)C_Q(s)\,ds
\longrightarrow 2\int_0^\infty C_Q(s)\,ds.
\]
Absolute integrability follows from the explicit exponential-polynomial formula. Using \(\int_0^\infty e^{-rs}ds=1/r\) and \(\int_0^\infty rs\,e^{-rs}ds=1/r\) gives exactly \(32\Lambda^4d(19d+28)/r^5\). Divide by \((4d\Lambda^2/r^2)^2\) to obtain the normalized coefficient
\[
\frac{2}{r}\left(19+\frac{28}{d}\right).
\]
Its limit as \(d\to\infty\) is \(38/r\), whereas with \(d\) independent reset diffusivity systems the total variance coefficient is \(d\) times the one-coordinate coefficient \(32\Lambda^4(19+28)/r^5\), giving \(94/(rd)\) after normalization. This proves the complete claim.

## Verification
Run `python checker.py` with Python, SymPy and SciPy installed. The included checker independently reconstructs the triangular stationary generator recurrences, diagonal and off-diagonal covariances, semigroup identities, Green–Kubo integral and dimension normalization. It also independently computes single-cycle moments using the Brownian diffusivity functional and performs 15 numerical quadrature comparisons over different dimensions, reset rates and amplitudes. The executable is a cross-check; the proof is the analytic stationary-generator and semigroup argument above.

## Relationship to prior work
Santra, Basu and Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient* (arXiv:2205.00549v1; first public 2022-05-01), define the common-diffusivity, common-reset process and derive unreset position laws, resetting stationary position laws and the relaxation of one-time densities. Its stationary one-time law supplies no lag-resolved energy covariance or evaluated temporal-mean variance coefficient. The calculation above uses their physical model but adds a time-lag and non-self-averaging observable.

Mesquita, Majumdar and Sabhapandit, *Dynamically emergent correlations in a Brownian gas with diffusing diffusivity* (arXiv:2506.20859v2), compute correlations of squared positions in an **unreset**, nonstationary shared-diffusivity gas; their time-dependent equal-time correlation does not imply the stationary two-time response of the jointly reset process. Both treatments provide helpful context for the role of a common bath, but the explicit finite-lag reset formula and integrated time-average law are different results.

## Limitations
The result holds for a common resetting clock that resets both all positions and the diffusivity, a Brownian squared-diffusivity environment and every **fixed finite** integer dimension. No joint scaling limit with observation time and dimension is asserted; the dimension limit above is taken **after** the time-asymptotic coefficient. A general stationary renewal formula or the already-known static radial distribution alone does not establish mathematical uniqueness or publication priority of this new evaluated formula. Independent scholarly checking is not part of this result.

## References
1. I. Santra, U. Basu and S. Sabhapandit, “Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient,” arXiv:2205.00549v1 (2022-05-01). https://arxiv.org/html/2205.00549v1
2. A. C. Mesquita, S. N. Majumdar and S. Sabhapandit, “Dynamically emergent correlations in a Brownian gas with diffusing diffusivity,” arXiv:2506.20859v2 (2025). https://arxiv.org/html/2506.20859v2
