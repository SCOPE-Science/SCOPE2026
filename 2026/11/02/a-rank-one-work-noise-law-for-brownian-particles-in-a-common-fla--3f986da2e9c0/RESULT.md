# A rank-one work-noise law for Brownian particles in a common flashing harmonic trap

## Finding
Consider a stationary gas of \(N\geq2\) noninteracting overdamped Brownian particles under a *single shared* two-state, symmetrically switching harmonic potential. Although the thermal fluctuations of individual particles are independent, their accumulated switching-work fluctuations have a strictly positive, universal cross-covariance. Specifically, for distinct \(i,j\),
\[
\lim_{T\to\infty}\frac{\operatorname{Cov}(W_i(T),W_j(T))}{T}
=\frac{\kappa_iD_i\kappa_jD_j}{4q}
=\frac{\mu_i\mu_j}{q}>0,
\qquad \mu_i=\lim_{T\to\infty}\frac{\mathbb EW_i(T)}{T}=\frac{\kappa_iD_i}{2}.
\]
The entire work vector obeys a multivariate central limit theorem with the explicit *diagonal-plus-rank-one* covariance matrix
\[
\frac{W(T)-\mu T}{\sqrt T}\Longrightarrow\mathcal N_N(0,\Sigma),\qquad
\Sigma=\operatorname{diag}\left(2\kappa_iD_i^2\left(1+\frac{\kappa_i}{q}\right)\right)_{i=1}^N+\frac{aa^{\mathsf T}}{4q},
\quad a_i=\kappa_iD_i.
\]
Consequently, for any two distinct observed work streams, the common switching rate is exactly identifiable from mean and asymptotic cross-covariance rates by \(q=\mu_i\mu_j/\Sigma_{ij}\), regardless of unknown particle-wise diffusivities or trap stiffnesses. No trajectory-position measurements are required by this *ideal population-parameter identity*.

Moreover, the proof constructs corrected work martingales whose full covariance, at *every finite observation time* \(T\), is exactly \(T\Sigma\), rather than only asymptotic. For identical particles with \(\kappa_i=\kappa\) and \(D_i=D\), the uncorrected total work has the explicit leading collective variance rate
\[
\lim_{T\to\infty}\frac{\operatorname{Var}(\sum_{i=1}^NW_i(T))}{T}
=2N\kappa D^2+\frac{\kappa^2D^2}{4q}N(N+8).
\]
Thus a shared switching signal produces a quadratic-in-population term that would disappear from work cross-covariances if each particle had its own independent switching signal. In particular, for identical particles the precise non-self-averaging statement is
\[
\lim_{N\to\infty}\lim_{T\to\infty}\frac{1}{T}\operatorname{Var}\!\left(\frac{1}{N}\sum_{i=1}^{N}W_i(T)\right)=\frac{\kappa^2D^2}{4q}>0.
\]

## Assumptions and scope
Fix an integer \(N\ge2\) and real parameters \(q>0\), \(\kappa_i>0\), \(D_i>0\) for \(1\le i\le N\). Let \(S_t\in\{0,1\}\) be a continuous-time Markov chain that switches from either state to the other at rate \(q\), independent of independent standard Brownian motions \(B^1,\ldots,B^N\). All particles share the *same* \(S\), and
\[
dX_t^i=-\kappa_i S_tX_t^i\,dt+\sqrt{2D_i}\,dB_t^i.
\]
The joint system \((S,X^1,\ldots,X^N)\) is initialized in its stationary law. Here \(\kappa_i\) is the on-state relaxation rate (mobility times stiffness); the switching-work energy is normalized by choosing mobility one, so the on-state potential of particle \(i\) is \(\kappa_i(X_t^i)^2/2\). At switching instants \(X^i\) remains continuous. Define the signed injected switching work, allowing negative work at trap deactivation, by
\[
W_i(T)=\frac{\kappa_i}{2}\sum_{0<t\le T}\left(S_t-S_{t-}\right)(X_t^i)^2.
\]
All claims are for fixed finite \(N\) and then long observation time \(T\to\infty\). The number of particles may subsequently be varied in the *exact formula* for the covariance rate; no uniform-in-\(N\) functional limit is claimed. The \(N\)-dimensional joint process is a well-defined ergodic Markov process with stationary moments of every finite polynomial order.

## Proof
**1. Stationarity and moments.** On each interval with \(S=0\), each coordinate is free Brownian motion; on intervals with \(S=1\), it is an Ornstein–Uhlenbeck diffusion. Consider successive starts of on intervals. Over one off–on cycle the vector follows a random affine Gaussian recursion with coordinate-wise multipliers \(e^{-\kappa_i\tau_{\mathrm{on}}}\in(0,1)\), where \(\tau_{\mathrm{on}}\) is exponential with rate \(q\). The Gaussian increments have moments of every order because off and on residence times have exponential tails. The iid cycle recursion has strict contraction in every coordinate with \(\mathbb E e^{-p\kappa_i\tau_{\mathrm{on}}}<1\) for every \(p>0\). Iterating the recursion and applying standard moment estimates gives a unique stationary law, all polynomial moments, and ergodicity. The continuous-time stationary version is obtained by the usual equilibrium-age construction.

**2. State-conditioned moments and work means.** Write \(m_{i,s}=\mathbb E[(X_0^i)^2\mathbf1_{\{S_0=s\}}]\). The chain is stationary with \(\mathbb P(S_0=s)=1/2\). The generator acting on \((X^i)^2\) and \(S(X^i)^2\) gives
\[
0=2D_i-2\kappa_i m_{i,1},\qquad
0=D_i-2\kappa_i m_{i,1}+q(m_{i,0}-m_{i,1}),
\]
so \(m_{i,1}=D_i/\kappa_i\) and \(m_{i,0}=D_i/\kappa_i+D_i/q\). Predictable compensation of the signed jump work gives the local work-current rate \(g_i(s,x)=q\kappa_i(1-2s)x_i^2/2\). It follows that
\[
\mu_i=\mathbb E g_i(S_0,X_0)
=\frac{q\kappa_i}{2}(m_{i,0}-m_{i,1})=\frac{\kappa_iD_i}{2}.
\]
By stationarity this equality yields \(\mathbb EW_i(T)=\mu_iT\) exactly for every \(T>0\).

**3. Exact jump cancellation.** The Markov generator for smooth functions is
\[
\mathcal Lf(s,x)=\sum_{i=1}^N\left[D_i\partial^2_{x_i}f-\kappa_i sx_i\partial_{x_i}f\right]+q[f(1-s,x)-f(s,x)].
\]
For each coordinate define the explicit corrector
\[
h_i(0,x)=\frac{\kappa_i}{2}x_i^2,\qquad h_i(1,x)=-\frac{\kappa_iD_i}{2q}.
\]
Substitution into the generator verifies separately for both states that \(\mathcal Lh_i=\mu_i-g_i\). Therefore
\[
M_i(T):=W_i(T)-\mu_iT+h_i(S_T,X_T)-h_i(S_0,X_0)
\]
is a square-integrable martingale starting from zero. At a switch from \(0\) to \(1\), the work jump \(+\kappa_i x_i^2/2\) cancels the position-dependent part of the corrector jump, leaving \(-\kappa_iD_i/(2q)\). At a switch from \(1\) to \(0\), the corrected work jump is \(+\kappa_iD_i/(2q)\). This cancellation holds *simultaneously for every particle*, even if the \(\kappa_i,D_i\) differ.

**4. Full bracket and exact finite-time covariance.** The continuous martingale part of \(M_i\) is \(\int_0^T\kappa_iX_t^i\mathbf1_{\{S_t=0\}}\sqrt{2D_i}\,dB_t^i\), and the jump part has magnitude \(c_i=\kappa_iD_i/(2q)\) with a common sign across particles at every switch. Since the Brownian drivers are independent, the predictable cross-brackets are
\[
\langle M_i,M_j\rangle_T
=\delta_{ij}\,2D_i\kappa_i^2\int_0^T(X_t^i)^2\mathbf1_{\{S_t=0\}}\,dt+q\,c_ic_jT.
\]
The environmental jump contribution is **deterministic**, not merely an average. For stationary initialization, \(\mathbb E[(X_t^i)^2\mathbf1_{\{S_t=0\}}]=m_{i,0}\) at all \(t\), and martingale isometry gives, at every finite \(T>0\),
\[
\operatorname{Cov}(M_i(T),M_j(T))
=T\left[\delta_{ij}2D_i\kappa_i^2m_{i,0}+\frac{\kappa_iD_i\kappa_jD_j}{4q}\right]
=T\Sigma_{ij}.
\]
Replacing the explicit \(m_{i,0}\) proves the stated diagonal-plus-rank-one expression. Its off-diagonal entries are precisely \(\mu_i\mu_j/q\), so they remain strictly positive for every positive parameter choice and determine \(q\) from any pair of work-current means.

**5. Transfer to physical work and the joint CLT.** All correctors have finite second moment under the stationary distribution, so \(\mathbb E|h_i(S_T,X_T)-h_i(S_0,X_0)|^2=O(1)\). Since \(\mathbb E|M_i(T)|^2=O(T)\), Cauchy–Schwarz shows the difference between \(\operatorname{Cov}(W_i(T),W_j(T))\) and \(\operatorname{Cov}(M_i(T),M_j(T))\) is \(O(\sqrt T)\), proving the physical-work covariance-rate limit. The ergodic theorem applied to the bracket integrands yields almost-sure \(T^{-1}\langle M_i,M_j\rangle_T\to\Sigma_{ij}\). Martingale jumps are bounded (their magnitudes are the constants \(c_i\)), so the martingale Lindeberg condition holds; the continuous parts satisfy the corresponding martingale condition automatically. The multidimensional martingale central limit theorem yields \(T^{-1/2}M(T)\Rightarrow\mathcal N_N(0,\Sigma)\). The \(O(1)\) corrector boundary term divided by \(\sqrt T\) vanishes in \(L^2\), completing the claimed joint CLT. Summing the entries for identical \(\kappa_i,D_i\) proves the collective \(N(N+8)\) formula.

## Verification
The bundled `checker.py` verifies the generator–corrector identities and both switching-direction cancellations symbolically; checks the stationary on/off second moments and exact diagonal/off-diagonal bracket formula using rational arithmetic; verifies the collective identical-particle formula algebraically; and performs a seeded finite-trajectory simulation using exact free/Ornstein–Uhlenbeck Gaussian transitions between shared Poisson switches. The finite simulation is an independent numerical diagnostic and is **not** an infinite-time proof. The proof above supplies the exact all-parameter statements.

Execute `python checker.py` with Python, SymPy and NumPy. The checker has no nonstandard inputs, external data, network calls, or hidden dependencies. A passing diagnostic does not establish publication priority or independent mathematical validation.

## Relationship to prior work
Biroli, Kulkarni, Majumdar and Schehr (2023) establish the same physical mechanism of emergent many-particle correlations under one shared switching harmonic trap, but study stationary positions, extreme values, spacings and spatial counts; the present claim concerns **temporal switching-work cross-covariances** and joint work fluctuations. Alston, Cocconi and Bertrand (2022) and Frydel (2024; later 2026 extension) establish the fluctuating-potential model and stationary thermodynamic dissipation/mean injected power, not the stated many-particle covariance-rate law. The known one-particle work mean and variance for an on/off trap are not claimed as new ingredients; the diagonal terms reproduce that one-particle calculation. The distinct-particle cross-law, exact finite-time corrected-work cross-covariance, rank-one structure, identification consequence and quadratic collective scaling are the assessed contribution.

General resetting-work results involving full thermalization between cycles or first-passage-triggered return phases are not directly the same stochastic system: the current harmonic on intervals end at independent exponential times, generally before equilibration. A general martingale bracket theorem is used as a proof tool, but it does not itself supply this model-specific corrector, rank-one coefficient or inverse formula. The comparison does not establish absolute novelty; independent publication-priority verification remains necessary.

## Limitations
The result assumes an exactly common symmetric exponential two-state switch, one-dimensional overdamped particles, mutually independent thermal Brownian noises, positive stiffness and diffusivity parameters, stationary initialization, and the stated signed work convention. It does **not** cover independent/asymmetric switching, underdamped dynamics, correlated thermal drivers, partial reset, feedback, nonlinear potentials, an unknown state-dependent mobility convention, or full finite-noise statistical inference. In particular, \(q=\mu_i\mu_j/\Sigma_{ij}\) is an identity for exact asymptotic population quantities, not a finite-sample error bound. The diagonal work-variance formula is an existing one-particle result; it is included only to make the multivariate matrix complete. The finite-\(T\) exact matrix applies to corrected martingales \(M\), not directly to the raw switching work \(W\).

## References
1. M. Biroli, M. Kulkarni, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570v1 (first public 2023-12-05), https://arxiv.org/html/2312.02570v1.
2. H. Alston, L. Cocconi and T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, arXiv:2202.02630 (first public 2022-02-05), https://arxiv.org/abs/2202.02630.
3. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213v1 (first public 2024-07-16), https://arxiv.org/abs/2407.12213.
4. D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, arXiv:2607.05173 (2026), https://arxiv.org/abs/2607.05173.
5. *Thermodynamic cost of finite-time stochastic resetting*, arXiv:2310.11267 (2023), https://arxiv.org/abs/2310.11267; different full-thermalization resetting protocol.
