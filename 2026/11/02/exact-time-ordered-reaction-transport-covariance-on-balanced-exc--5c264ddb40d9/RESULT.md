# Exact time-ordered reaction–transport covariance on balanced exclusion networks

## Finding
Consider an exclusion process on any finite connected loopless graph with fixed orientations of its edges, with asymmetric particle hops and homogeneous Langmuir attachment and detachment. Under the vertexwise circulation-balance assumption below, the **stationary time-ordered chemical–transport covariance densities** are exactly

\[
\begin{aligned}
 K_{A,J}(t)&=\lambda B(1-\rho)^2(1-2\rho)e^{-\omega t},\\
 K_{J,A}(t)&=-\lambda B\rho(1-\rho)(1-2\rho)e^{-\omega t},\\
 K_{D,J}(t)&=-\delta B\rho^2(1-2\rho)e^{-\omega t},\\
 K_{J,D}(t)&=\delta B\rho(1-\rho)(1-2\rho)e^{-\omega t},\qquad t>0.
\end{aligned}
\]

Here \(A\), \(D\), and \(J\) are the attachment count, detachment count, and signed count of hops across any selected collection of oriented edges; \(B\) is the sum of the corresponding forward-minus-backward hop rates; \(\omega=\lambda+\delta\); and \(\rho=\lambda/\omega\). In particular, attaching a particle before measuring transport and measuring transport before an attachment have opposite covariance signs whenever \(B(1-2\rho)\ne0\). Detachment reverses the signs. For all observation times \(T>0\), the **integrated** covariances instead coincide:

\[
\boxed{\operatorname{Cov}(A_T,J_T)=\operatorname{Cov}(D_T,J_T)
=\omega B\rho(1-\rho)(1-2\rho)^2
\left[\frac{T}{\omega}-\frac{1-e^{-\omega T}}{\omega^2}\right].}
\]

Thus for \(B>0\) both are strictly positive except at half filling, where all four time-ordered cross-covariances and both integrated covariances vanish, even though \(\mathbb E J_T=TB/4\) need not vanish. The theorem holds at every finite system size. Periodic two-dimensional ASEP with lane-dependent hopping and uniform Langmuir kinetics is an included case.

## Assumptions and scope
Let \(V\) be a finite set of \(S\ge2\) vertices, and choose one orientation \(e=(u_e,v_e)\) of each edge of a connected simple graph. The state \(\eta\in\{0,1\}^{V}\) has at most one particle per vertex. For each edge, a particle at \(u_e\) jumps to vacant \(v_e\) at rate \(p_e\ge0\), and a particle at \(v_e\) jumps to vacant \(u_e\) at rate \(q_e\ge0\). The rates satisfy the circulation-balance identity, for every \(i\in V\),

\[
\sum_{e:u_e=i}(p_e-q_e)=\sum_{e:v_e=i}(p_e-q_e).
\]

At each empty site a particle attaches independently at rate \(\lambda>0\), and at each occupied site it detaches at rate \(\delta>0\). The system is initialized in its unique stationary law. Let \(F\) be any subset of the oriented edges, and define

\[
B=\sum_{e\in F}(p_e-q_e).
\]

The signed counting process \(J_T\) adds \(+1\) for a hop along the chosen orientation of an edge in \(F\), and \(-1\) for its reverse; hops on other edges add zero. The counting processes \(A_T,D_T\) record attachments and detachments. The rates and parameter \(F\) are fixed as \(T\) and all time lags vary. For \(U,W\in\{A,D,J\}\), the ordered covariance density is defined for \(t>0\) by

\[
K_{U,W}(t)=\lim_{h\downarrow0}h^{-2}\operatorname{Cov}
\big(U_h-U_0,\,W_{t+h}-W_t\big).
\]

This is a statement about distinct event types at distinct times; it does not assert a same-event delta term. Because the state space is finite and jump intensities are bounded, the limits exist. We use \(\rho=\lambda/(\lambda+\delta)\), \(\omega=\lambda+\delta\), and denote \(N(\eta)=\sum_{i\in V}\eta_i\).

## Proof
**1. Invariance of uniform particle-number sectors.** For fixed \(n\), let \(u_n\) be the uniform probability distribution on configurations with exactly \(n\) particles. For a configuration \(\eta\), the difference between influx and outflux of the exclusion-hopping generator under constant configuration weights is

\[
-\sum_{e}(p_e-q_e)(\eta_{u_e}-\eta_{v_e})=0
\]

by the vertexwise circulation balance. Thus hopping preserves every \(u_n\). Homogeneous births send \(u_n\) to \(u_{n+1}\) with total rate \(\lambda(S-n)\), and deaths send \(u_n\) to \(u_{n-1}\) with total rate \(\delta n\). Hence the space of mixtures of the \(u_n\) is invariant, and on this space the particle number follows the Ehrenfest birth–death chain. Its invariant law is \(\operatorname{Binomial}(S,\rho)\), giving the product Bernoulli law \(\pi_\rho\) as the unique stationary law (uniqueness follows from the strictly positive attachment and detachment rates).

The total instantaneous signed hop-current intensity is

\[
j(\eta)=\sum_{e\in F}\left[p_e\eta_{u_e}(1-\eta_{v_e})-q_e\eta_{v_e}(1-\eta_{u_e})\right].
\]

Conditional on \(N=n\) and uniform position sector, its mean is

\[
\bar j(n)=B\frac{n(S-n)}{S(S-1)}.
\]

Therefore \(\mathbb E_\pi j=B\rho(1-\rho)\) and, by a two-site Bernoulli computation,

\[
\operatorname{Cov}_\pi(j,N)=B\rho(1-\rho)(1-2\rho).
\]

**2. A reaction event before transport.** Stationarity and the uniform sitewise birth rate imply that the distribution immediately after a typical attachment event is obtained by choosing a vertex uniformly, forcing its occupation to one, and independently drawing the other \(S-1\) occupations from Bernoulli \(\rho\). Immediately after a typical detachment, one uniformly chosen vertex is instead forced vacant. These laws are mixtures of the \(u_n\) and remain in that mixture class at all later times.

For the Ehrenfest chain, one forced bit relaxes its occupation mean toward \(\rho\) at rate \(\omega\); the other \(S-1\) bits are initially stationary. Comparing the two-site factors in \(\bar j(N)\) gives the exact conditional mean current intensity at time \(t>0\):

\[
\begin{aligned}
\mathbb E[j(\eta_t)\mid\text{attachment at }0]
&=B\rho(1-\rho)+\frac{B}{S}(1-\rho)(1-2\rho)e^{-\omega t},\\
\mathbb E[j(\eta_t)\mid\text{detachment at }0]
&=B\rho(1-\rho)-\frac{B}{S}\rho(1-2\rho)e^{-\omega t}.
\end{aligned}
\]

The stationary attachment and detachment intensities are \(\lambda S(1-\rho)\) and \(\delta S\rho\), respectively. Multiplication of these event rates by the conditional-mean differences proves \(K_{A,J}\) and \(K_{D,J}\).

**3. Transport before a reaction.** A hop preserves \(N\). Starting from any configuration with \(N=n\), the conditional number mean at time \(t\) is \(S\rho+(n-S\rho)e^{-\omega t}\), independently of the subsequent spatial hopping. Therefore the conditional future attachment and detachment intensities are

\[
\lambda\big[S(1-\rho)-(n-S\rho)e^{-\omega t}\big],\qquad
\delta\big[S\rho+(n-S\rho)e^{-\omega t}\big].
\]

The signed instantaneous hop intensity is \(j(\eta)\). Taking stationary covariances and applying the expression for \(\operatorname{Cov}_\pi(j,N)\) in step 1 gives \(K_{J,A}\) and \(K_{J,D}\). The calculation is valid for signed hops because positive and negative events are treated as separate jump transitions with their signs in the current observable.

**4. Integrated counts and phase structure.** Cross-event types have no common jumps. Stationarity and Fubini's theorem yield

\[
\operatorname{Cov}(U_T,J_T)=\int_0^T(T-t)\big(K_{U,J}(t)+K_{J,U}(t)\big)\,dt,
\qquad U\in\{A,D\}.
\]

In each case, the sum of the two kernels simplifies to

\[
\omega B\rho(1-\rho)(1-2\rho)^2e^{-\omega t},
\]

using \(\lambda=\omega\rho\) and \(\delta=\omega(1-\rho)\). Elementary integration proves the displayed formula. Its bracket is strictly positive for \(T>0\), so the sign and half-filling statements follow. The equality of the integrated covariances also agrees with the pathwise identity \(A_T-D_T=N_T-N_0\), although that identity alone does not prove their common value.

## Verification
A standalone verification program, `verify.py`, constructs the **complete finite-state generator and marked jump matrices**, and evaluates ordered event covariances by sparse matrix exponentiation rather than by the sector-mixture formulas used in the proof. It checks a \(3\times3\) periodic lattice with lane-dependent rates, a balanced nonrectangular cycle network, three filling regimes including half filling, and two positive time lags. Its 40 numerical covariance comparisons and stationarity checks pass. Reproduce with `python verify.py` (Python 3, NumPy, SciPy). These finite-state computations corroborate but do not replace the proof for arbitrary finite balanced networks.

## Relationship to prior work
Ishiguro and Sato (2024, arXiv:2405.09261, Sections 3–4) constructed the torus stationary product distribution and the mean cross-section current of the two-dimensional ASEP with Langmuir kinetics. Those results are **premises**, not new claims here. Ishiguro and Sato (2024, arXiv:2403.01934) supplied the sectorwise stationary structure of multi-dimensional ASEP. Sato and Nishinari (2016, arXiv:1601.02651) studied one-dimensional ring relaxation, low-lying eigenmodes and equal-time occupation correlations from an empty initial state. These sources do not state the four time-ordered **reaction-event versus signed hopping-event** covariance kernels or the exact integrated covariance equality for arbitrary balanced finite networks. The present proof uses post-event Palm laws and a current–number regression, not just the static current formula.

## Limitations
The theorem requires homogeneous positive attachment and detachment rates, circulation-balanced hopping on a finite graph, stationary initialization, and current measured on fixed oriented edges. It does not extend directly to open-boundary injection, spatially varying Langmuir rates, or graphs lacking the balance condition. It characterizes only mixed second-order reaction–transport counting statistics, not the variance or full large-deviation law of the hopping current alone. Although the evaluated identities were not found in the inspected sources, a more general Markov-process covariance theorem may subsume them; publication priority is not independently established.

## References
1. Y. Ishiguro and J. Sato, *Exact analysis of the two-dimensional asymmetric simple exclusion process with attachment and detachment of particles*, arXiv:2405.09261v1 (first posted 2024-05-15), https://arxiv.org/html/2405.09261v1 .
2. Y. Ishiguro and J. Sato, *Exact steady states in the asymmetric simple exclusion process beyond one dimension*, arXiv:2403.01934v1 (2024), https://arxiv.org/html/2403.01934v1 .
3. J. Sato and K. Nishinari, *Relaxation dynamics of the asymmetric simple exclusion process with Langmuir kinetics on a ring*, Physical Review E **93**, 042113 (2016), arXiv:1601.02651v3, https://arxiv.org/html/1601.02651v3 .
4. I. Neri, N. Kern, and A. Parmeggiani, *Exclusion processes on networks as models for cytoskeletal transport*, New Journal of Physics **15**, 085005 (2013), https://doi.org/10.1088/1367-2630/15/8/085005 .
