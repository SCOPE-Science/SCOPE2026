# Sharp dwell-time noise bounds and trap-spectroscopic recovery for alternating-renewal propulsion

## Finding

The stationary position variance of a one-dimensional harmonically confined, symmetric alternating-renewal active particle determines the **entire distribution of the switching durations** from a stiffness scan, even when propulsion speed and mean duration are unknown. At a prescribed positive mean run duration, completely periodic sign reversals uniquely minimize the variance for *every* trap stiffness, whereas the supremum is the ballistic value and is not attained. In a weak trap, periodic reversals leave a finite variance but any nonzero finite run-duration variance produces a universal inverse-stiffness divergence.

Precisely, with the definitions below and \(\phi(k)=\mathbb E e^{-kL}\), for all \(k>0\),
\[
V_L(k)=\operatorname{Var}(X_0)=\frac{v^2}{k^2}\left[1-\frac{2(1-\phi(k))}{k\tau(1+\phi(k))}\right].
\]
Fix \(v,\tau,k>0\). Over **all probability laws** on \((0,\infty)\) with mean \(\tau\), the sharp bounds are
\[
\frac{v^2}{k^2}\left[1-\frac{2}{k\tau}\tanh\left(\frac{k\tau}{2}\right)\right]
\ \le\ V_L(k)\ <\ \frac{v^2}{k^2}.
\]
Equality on the left holds exactly when \(L=\tau\) almost surely; the right supremum is approached by positive two-point laws of mean \(\tau\). More generally, if two waiting-time laws have the same mean and \(L_1\preceq_{\rm cx}L_2\) (convex order), then \(V_{L_1}(k)\le V_{L_2}(k)\) simultaneously for every \(k>0\), strictly when the two laws differ.

A complete stationary-variance scan over all \(k>0\) identifies \(v\), \(\tau\), and the whole law of \(L\):
\[
v^2=\lim_{k\to\infty}k^2V_L(k),\qquad
\frac2\tau=\lim_{k\to\infty}k\left(1-\frac{k^2V_L(k)}{v^2}\right),
\]
\[
q(k)=\frac{k\tau}{2}\left(1-\frac{k^2 V_L(k)}{v^2}\right),
\qquad \phi(k)=\frac{1-q(k)}{1+q(k)}.
\]
For fixed \(v,\tau\) and any \(L\) with finite second moment, the weak-trap dichotomy is
\[
\lim_{k\downarrow0} V_L(k)=\frac{v^2\tau^2}{12}\quad (L=\tau\text{ almost surely}),
\]
\[
\lim_{k\downarrow0} k V_L(k)=\frac{v^2\operatorname{Var}(L)}{2\tau}
\quad(\operatorname{Var}(L)>0).
\]
In the deterministic case the full stationary position law converges to the uniform distribution on \([-v\tau/2,v\tau/2]\) as \(k\downarrow0\). For a law of nonzero finite switching-duration variance, \(V_L(k)\) instead diverges like the displayed positive constant divided by \(k\).

## Assumptions and scope

Let \(k,v>0\). Let \((L_n)_{n\in\mathbb Z}\) be independent identically distributed durations with \(0<L_n<\infty\) almost surely and \(\mathbb E L_n=\tau\in(0,\infty)\). The propulsion orientation \(S_t\in\{-1,+1\}\) **flips sign at every renewal**. Its equilibrium version is formed by the size-biased interval, a uniform observation point within it, and a fair orientation sign; no density or exponential law is assumed. The particle satisfies
\[
\dot X_t=-kX_t+vS_t
\]
without translational thermal noise, independent resets, inertia, or an additional resting state. The unique stationary bounded response is
\[
X_t=v\int_{-\infty}^{t}e^{-k(t-u)}S_u\,du,\qquad |X_t|\le v/k.
\]
All assertions about stationary variance concern this stationary joint construction. The inversion result assumes access to **exact** variance values at all positive stiffnesses; it does not claim stable inference from finite noisy data. The weak-trap divergence assumes finite second moment and takes the stationary limit at fixed \(k>0\) before \(k\downarrow0\).

## Proof

**1. Renewal orientation correlations.** Write \(\phi(s)=\mathbb E e^{-sL}\) for \(s>0\). Let \(f(t)\) be the mean orientation at elapsed time \(t\) given that a fresh positive interval begins at time zero. At its first reversal the sign changes; conditioning on its duration gives the ordinary renewal identity
\[
f(t)=\mathbb P(L>t)-\int_{(0,t]} f(t-u)\,dF_L(u).
\]
The Laplace transform is \(\widehat f(s)=(1-\phi(s))/[s(1+\phi(s))]\). In the stationary process the forward recurrence time \(R\) has transform \(\mathbb E e^{-sR}=(1-\phi(s))/(s\tau)\). If \(C(t)=\mathbb E[S_0S_t]\), its first-reversal decomposition is
\[
C(t)=\mathbb P(R>t)-\mathbb E[\mathbf1_{\{R\le t\}}f(t-R)].
\]
Taking Laplace transforms yields exactly
\[
\widehat C(s)=\frac1s-\frac{2[1-\phi(s)]}{\tau s^2[1+\phi(s)]}.
\]
No Markov assumption was used. The deterministic periodic case follows from the same renewal equations with Stieltjes integrals.

**2. Variance as a resolvent of orientation correlation.** The stationary orientation is symmetric, so \(\mathbb E X_0=0\). The exponentially weighted double integral is absolutely convergent because \(|C(t)|\le1\). By stationarity and symmetry of \(C\),
\[
\mathbb E X_0^2
=v^2\int_0^\infty\!\int_0^\infty e^{-k(a+b)}C(a-b)\,da\,db
=\frac{v^2}{k}\widehat C(k).
\]
Substitution proves the variance formula. Its positivity and all boundaries also follow from this expression as an actual variance; the strict inequalities in Step 3 give positive lower and finite strict upper values.

**3. Sharp optimization and convex order.** For fixed \(k,\tau\), \(V_L(k)\) is strictly increasing as a function of \(\phi(k)\), because \((1-\phi)/(1+\phi)\) is strictly decreasing. Strict Jensen for the strictly convex function \(u\mapsto e^{-ku}\) gives \(\phi(k)\ge e^{-k\tau}\), equality only for constant \(L\). Since \((1-e^{-z})/(1+e^{-z})=\tanh(z/2)\), this proves the left bound with its uniqueness. The same convexity proves monotonicity under convex order; if two laws differ in convex order, strictness follows from any martingale coupling and strict conditional Jensen.

As \(L>0\) almost surely, \(\phi(k)<1\), proving the strict upper bound. To prove sharpness, choose for \(0<\eta<1\) the positive two-point law
\[
\mathbb P(L=\eta\tau)=1-\eta,\qquad
\mathbb P\left(L=\frac{\tau(1-\eta+\eta^2)}{\eta}\right)=\eta.
\]
Its mean is exactly \(\tau\), and its Laplace transform tends to \(1\) at each fixed \(k>0\) as \(\eta\downarrow0\). Consequently \(V_L(k)\uparrow v^2/k^2\) along this family. There is no maximizer among positive finite-mean durations.

**4. Complete inverse spectroscopy.** Because \(L>0\), dominated convergence gives \(\phi(k)\to0\) as \(k\to\infty\). Insert this into the variance expression to obtain both large-\(k\) formulas in the Finding. The recovered \(v\) is positive and \(\tau\) is finite positive. The rational inversion then recovers \(\phi(k)\) at every positive \(k\). Uniqueness of Laplace transforms of finite measures on \([0,\infty)\) identifies the full waiting-time law. Exact spectra with arbitrary different \(v\), \(\tau\), or switching-duration laws cannot coincide.

**5. Singular weak-trap boundary.** When \(\operatorname{Var}(L)\in(0,\infty)\), finite \(\mathbb E L^2\) gives the second-order expansion \(\phi(k)=1-\tau k+(\mathbb E L^2)k^2/2+o(k^2)\). Therefore
\[
\frac{2(1-\phi(k))}{k\tau(1+\phi(k))}
=1-\frac{\operatorname{Var}(L)}{2\tau}k+o(k).
\]
This proves the inverse-\(k\) divergence. When \(L=\tau\) almost surely, the exact expression reduces to
\[
V_L(k)=\frac{v^2}{k^2}\left[1-\frac{2}{k\tau}\tanh(k\tau/2)\right]
\longrightarrow v^2\tau^2/12.
\]
For the stronger distributional statement, every deterministic half-period evolves toward the target equilibrium \(\pm v/k\) exponentially; stationarity cycles between opposite extrema \(\pm (v/k)\tanh(k\tau/2)\). Its traversal speed uniformly tends to \(v\) as \(k\downarrow0\), while these extrema tend to \(\pm v\tau/2\). Uniform stationary phase hence yields the uniform limit law.

## Verification

The standalone `verification.py` uses two algebraically independent routes to the variance: (i) the renewal-autocorrelation transform above and (ii) the moment equations of the alternating affine reversal-epoch recursion \(Y_{n+1}=-e^{-kL_n}Y_n-(v/k)(1-e^{-kL_n})\), integrated over entire runs by renewal reward. It tests 48 parameter-law combinations across deterministic, exponential, Erlang-2, and equal-mass two-point durations. It also performs exact event-driven integrations of the position-square reward along simulated runs for twelve configurations, direct comparisons of the Jensen bounds, the weak-trap leading constants, and the unattained upper envelope. Full reproducibility: from the same directory as this document execute `python3 verification.py`. No external package is required. Simulation checks are finite and not the proof of any universal claim.

## Relationship to prior work

Farago and Smith, *Confined run and tumble particles with non-Markovian tumbling statistics* (arXiv:2401.01576, first public January 3, 2024), introduce the alternating nonexponential-duration trapped active-particle model and develop position-current integral equations and a numerical scheme for steady spatial densities; their worked nonlinear potential is sinusoidal. Their published results are not claimed as new. The result above instead exploits the harmonic filter to obtain a closed second moment for arbitrary positive waiting-time laws, proving a sharp **all-stiffness optimization** and recovering the waiting law, speed, and mean from a stationary-variance scan. Its weak-trap localization/delocalization boundary does not follow simply from the paper's fixed-potential numerical density profiles.

Sun, Ye, and Podgornik (arXiv:2409.00578) derive exact moments for **exponentially timed** runs with an additional finite-time tumble state, not this symmetric iid non-Markovian sign-flip process. Sarkar, Santra, and Basu (arXiv:2210.09035) examine harmonic chains with exponentially correlated active boundary reservoirs, not waiting-law optimization. General stationary renewal transform identities are established background and not asserted as new. Another published confined switching model with non-Poisson wall residence obtains a convex-order diffusivity bound and a Laplace-spectrum inverse; that slit-wall observable is mathematically distinct and does not imply the two-state harmonic variance formula, its critical weak-trap divergence, or inversion with unknown speed and mean. Identifiability here specifically requires *the same* run-time law in both alternating orientations; when those two laws differ, stationary two-time-law aliasing is a known possibility.

## Limitations

These are exact statements for an idealized overdamped harmonic model with iid strictly positive equal-law alternating durations and no translational Brownian noise. The inverse map is theoretically injective, not necessarily well-conditioned under finite experimental sampling. The weak-trap coefficient requires finite second moment; heavy-tailed infinite-variance waiting laws are outside that asymptotic statement. Equal-law sign flips are essential to the stated reconstruction. The result does not cover interacting particles, partially random direction redraws, finite-duration resting states, arbitrary external forces, or finite-data inference guarantees. The published priority of related broader linear-filter/renewal results cannot be completely excluded; the exact specialization, global optimization, inverse recovery, and weak-trap split were the subjects of the scientific comparison.

## References

1. O. Farago and N. R. Smith, *Confined run and tumble particles with non-Markovian tumbling statistics*, arXiv:2401.01576 (first public 2024-01-03); *Physical Review E* **109**, 044121 (2024), DOI 10.1103/PhysRevE.109.044121.
2. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578 (first public 2024-09-01).
3. R. Sarkar, I. Santra and U. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035 (first public 2022-10-17); *Physical Review E* **107**, 014123 (2023).
4. M. O. Cáceres and A. A. Budini, *The generalized Ornstein–Uhlenbeck process*, *Journal of Physics A* **30** (1997), DOI 10.1088/0305-4470/30/24/009, as background on linear filtering of non-Markovian forcing.
