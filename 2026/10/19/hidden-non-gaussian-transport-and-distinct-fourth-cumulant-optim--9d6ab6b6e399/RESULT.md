# Hidden non-Gaussian transport and distinct fourth-cumulant optima under Maxwellian velocity refresh

## Finding
Consider an inertial particle whose velocity undergoes thermal Ornstein–Uhlenbeck relaxation and is independently refreshed to a Maxwellian at Poisson times, while its position is **never** reset. Although its stationary velocity law is Gaussian and its entire two-time velocity covariance equals that of an ordinary Gaussian Ornstein–Uhlenbeck process, the particle's integrated displacement is strictly non-Gaussian at every positive time. Its long-time fourth-cumulant growth rate is strictly positive and reaches a unique maximum at a different refresh rate from the large-time standardized excess-kurtosis coefficient.

Specifically, for \(\gamma,r,\sigma^2>0\), with \(X_t=\int_0^t V_s\,ds\),
\[
\lim_{t\to\infty}\frac{\operatorname{cum}_4(X_t)}t
 =\frac{24\sigma^4r}{(\gamma+r)^3(2\gamma+r)},
\qquad
\lim_{t\to\infty}t\,\frac{\operatorname{cum}_4(X_t)}{\operatorname{Var}(X_t)^2}
 =\frac{6r}{(\gamma+r)(2\gamma+r)}.
\]
The two rates maximizing these respective observables over \(r>0\), with \(\gamma\) and \(\sigma^2\) fixed, are uniquely
\[
 r_{\mathrm{absolute}}=\frac{\sqrt{10}-2}{3}\gamma,
\qquad r_{\mathrm{standardized}}=\sqrt2\,\gamma.
\]
Furthermore, \(\operatorname{Cov}(V_0^2,V_t^2)=2\sigma^4e^{-(2\gamma+r)t}\) for \(t\ge0\). Together with the velocity covariance decay rate \(\gamma+r\), this identifies both \(\gamma\) and \(r\) from ideal second- and fourth-order stationary lag measurements.

## Assumptions and scope
For every \(\gamma,r,\sigma^2>0\), take a rate-\(r\) Poisson clock, independent Brownian noise, and independent samples from \(N(0,\sigma^2)\). Between clock times let
\[
 dV_t=-\gamma V_t\,dt+\sqrt{2\gamma\sigma^2}\,dB_t,
 \qquad dX_t=V_t\,dt.
\]
At every clock time replace \(V\) by a fresh \(N(0,\sigma^2)\) sample, leave \(X\) unchanged, and start with independent \(V_0\sim N(0,\sigma^2)\), \(X_0=0\). The fourth cumulant is \(\operatorname{cum}_4(X)=\mathbb EX^4-3(\mathbb EX^2)^2\); all expectations refer to this law. The position is unbounded and has no stationary marginal distribution; only velocity is stationary. The word Maxwellian means the one-dimensional centered thermal Gaussian. The inequalities and maximizers concern strictly positive refresh and relaxation rates.

## Proof
**1. Exact Gaussian marginal and two-time disguise.** Both the thermal Ornstein–Uhlenbeck propagator and the refresh law preserve \(N(0,\sigma^2)\), so the stationary velocity marginal is Gaussian. Conditional on no refresh between \(0\) and \(t\), its covariance is \(\sigma^2e^{-\gamma t}\); a refresh kills correlation with the past. Hence
\[
 \mathbb E[V_0V_t]=\sigma^2e^{-(\gamma+r)t}.
\]
An ordinary Gaussian Ornstein–Uhlenbeck process with relaxation \(\gamma+r\) and invariant variance \(\sigma^2\) has precisely the same velocity covariance and therefore gives precisely the same mean-square displacement at every time. However, for a Gaussian pair without an intervening refresh, Wick's identity gives a squared-velocity covariance \(2\sigma^4e^{-2\gamma t}\). If at least one refresh occurs, past and future velocities are independent, and their squared covariance vanishes. Consequently
\[
 \operatorname{Cov}(V_0^2,V_t^2)=2\sigma^4e^{-(2\gamma+r)t},
\]
whereas the covariance-matched Gaussian process gives \(2\sigma^4e^{-2(\gamma+r)t}\). For each \(t>0\) their difference is strictly positive. If the measured positive decay rates are \(a_1=\gamma+r\) and \(a_2=2\gamma+r\), then \(\gamma=a_2-a_1\), \(r=2a_1-a_2\), and \(\sigma^2=\operatorname{Var}(V_0)\).

**2. Strict finite-time non-Gaussianity.** Conditional on all refresh times in \((0,t)\), the velocity trajectory is jointly Gaussian and its independent refresh-separated pieces have covariance kernel \(\sigma^2e^{-\gamma|u-v|}\) within each piece and zero covariance between pieces. The integrated displacement is thus centered normal with random conditional variance
\[
 Q_t=\sum_{I\in\mathcal P_t}q(|I|),\qquad
 q(s)=2\sigma^2\left(\frac{s}{\gamma}-\frac{1-e^{-\gamma s}}{\gamma^2}\right),
\]
where \(\mathcal P_t\) is the partition of \([0,t]\) formed by refresh epochs. Conditioning gives \(\mathbb EX_t^2=\mathbb EQ_t\), \(\mathbb EX_t^4=3\mathbb EQ_t^2\), hence
\[
 \operatorname{cum}_4(X_t)=3\operatorname{Var}(Q_t).
\]
For \(0<s<t\), the strict inequality \(q(s)+q(t-s)<q(t)\) follows from the positive double covariance integral over opposite sides of the cut. The no-refresh event and the exactly-one-refresh event both have positive probability and give different values of \(Q_t\). Therefore \(\operatorname{Var}(Q_t)>0\), proving strict positivity at **every** \(t>0\), not just asymptotically.

**3. Exact long-time coefficient by moment equations.** Put \(a_1=\gamma+r\), \(a_2=2\gamma+r\). The generator acts on centered velocity Hermite polynomials by
\[
 \mathcal LV=-a_1V,\quad
 \mathcal L(V^2-\sigma^2)=-a_2(V^2-\sigma^2),\quad
 \mathcal L(V^3-3\sigma^2V)=-(3\gamma+r)(V^3-3\sigma^2V).
\]
Let \(A=\mathbb E[XV]\), \(B=\mathbb E[X^2(V^2-\sigma^2)]\), \(M=\mathbb E[X^2]\), and \(D_3=\mathbb E[X^3V]\). Stationarity of the velocity marginal and the cubic Hermite equation give \(\mathbb E[X(V^3-3\sigma^2V)]=0\). The generator identities therefore yield the closed system
\[
 A'=\sigma^2-a_1A,\qquad B'=4\sigma^2A-a_2B,
 \qquad M'=2A,\qquad D_3'=3\sigma^2M+3B-a_1D_3.
\]
All four quantities vanish initially. For \(W=D_3-3MA\), direct differentiation yields \(W'=3B-6A^2-a_1W\) and \(\operatorname{cum}_4(X_t)'=4W(t)\). Since
\[
 A(t)\longrightarrow\frac{\sigma^2}{a_1},\quad
 B(t)\longrightarrow\frac{4\sigma^4}{a_1a_2},\quad
 W(t)\longrightarrow\frac{6\sigma^4(2a_1-a_2)}{a_1^3a_2}
 =\frac{6\sigma^4r}{a_1^3a_2},
\]
the asserted fourth-cumulant growth rate follows by time averaging. Also the exact second moment is
\[
 M(t)=2\sigma^2\left(\frac{t}{a_1}-\frac{1-e^{-a_1t}}{a_1^2}\right),
\]
so \(M(t)/t\to2\sigma^2/a_1\); this gives the standardized coefficient as stated. All these ODEs are polynomial moment identities and require no unproved spectral approximation.

**4. Regenerative cross-check.** A complete refresh-to-refresh excursion of duration \(T\sim\operatorname{Exp}(r)\) has conditional normal displacement variance \(q(T)\). The renewal cumulant exponent \(\lambda(z)\) near zero is determined by
\[
 \mathbb E\exp\left(\frac{z^2q(T)}2-\lambda(z)T\right)=1.
\]
This identity follows by conditioning on complete iid excursions; the incomplete terminal piece affects no limiting linear-in-time cumulant rate. Analyticity near zero follows since \(q(T)\) grows at most linearly in \(T\). Writing \(\lambda(z)=c_2z^2+c_4z^4+O(z^6)\), we obtain
\[
 c_2=\frac{\mathbb Eq(T)}{2\mathbb ET}=\frac{\sigma^2}{a_1},\qquad
 c_4=\frac{\mathbb E\left[(q(T)/2-c_2T)^2\right]}{2\mathbb ET}.
\]
The exponential identities \(\mathbb ET^2=2/r^2\), \(\mathbb Ee^{-\gamma T}=r/(r+\gamma)\), and \(\mathbb E[Te^{-\gamma T}]=r/(r+\gamma)^2\) give
\[
 \mathbb E\left[(q(T)/2-c_2T)^2\right]
 =\frac{2\sigma^4}{a_1^3a_2}.
\]
Thus \(24c_4=24\sigma^4r/(a_1^3a_2)\), independently confirming the moment-ODE result.

**5. Unique and separated optima.** Differentiation of the strictly positive fourth-cumulant rate as a function of \(r>0\) gives a derivative whose sign is that of \(2\gamma^2-4\gamma r-3r^2\). This polynomial decreases strictly from positive to negative and has the unique positive zero \(r_{\mathrm{absolute}}=(\sqrt{10}-2)\gamma/3\). The standardized large-time coefficient has derivative with sign \(2\gamma^2-r^2\), giving the unique positive maximizer \(r_{\mathrm{standardized}}=\sqrt2\gamma\). Both objectives tend to zero as \(r\downarrow0\) or \(r\to\infty\), and the two optimum rates are distinct.

## Verification
The standalone `verify.py` recomputes the exponential-cycle squared expectation algebraically, independently matches the coefficient through the centered-Hermite recursion, differentiates both rational objectives symbolically, integrates the cycle identity numerically for four parameter triples, independently integrates the finite-time polynomial-moment ODE system, and checks conditional-variance splitting. It reports 64 passing assertions when executed with Python, SymPy, and SciPy. Numerical checks support the calculation but are not substitutes for the all-parameter analytic proof above.

## Relationship to prior work
Olsen and Löwen (2024) developed a general partial-resetting theory for inertial transport, including Fourier–Laplace transforms and moment recursions. Velocity resetting, renewal methods, and effective diffusivity are not claimed as new. Standard Andersen thermostat protocols already draw new velocities from a Maxwell–Boltzmann distribution; GROMACS documents this and cautions that such collisions modify dynamical transport properties. Franke and Sokolov (2026) studied underdamped Brownian particles whose **position and velocity are both reset** (with Maxwellian velocity in one protocol), and analyzed the stationary displacement distribution between full resets. Their position-reset model is not the unbounded accumulated displacement considered here.

The separate assessed contribution is the complete fourth-order identifiability/displacement-fluctuation theorem for **velocity-only Maxwellian refresh with ongoing OU relaxation**, and the proof of two distinct, exact interior rate optima. An inaccessible full text of Olsen and Löwen's closely related 2024 work leaves a genuine priority risk: their general transform machinery might implicitly specialize to part of this model. No independent claim is made that these formulas cannot be inferred from prior general renewal or kinetic theory.

## Limitations
The setting is one-dimensional, linear thermal velocity relaxation, independent exponential refreshes, and exactly equilibrium-Gaussian refresh velocities. Position is never reset. The results do not establish optimal finite-time kurtosis, finite-sample inference accuracy, or extensions to heavy-tailed, coupled, non-Maxwellian, or state-dependent collisions. The fourth-cumulant rate is not a stationary position cumulant, and no claim about energy dissipation or thermodynamic entropy production is made. Independent literature-priority assessment remains necessary.

## References
1. K. Stølevik Olsen and H. Löwen, “Dynamics of inertial particles under velocity resetting,” *Journal of Statistical Mechanics* 033210 (2024), arXiv:2401.12685, doi:10.1088/1742-5468/ad319a (first publicly posted 2024-01-23).
2. GROMACS Development Team, “Molecular Dynamics,” GROMACS 2024.1 reference documentation, subsection “Andersen thermostat,” https://gromacs-manual.biophysics.kth.se/2024.1/reference-manual/algorithms/molecular-dynamics.html.
3. H. Franke and I. M. Sokolov, “Resetting of underdamped Brownian motion,” *Physical Review E* **113**, 064125 (2026), doi:10.1103/qyl8-6q9h.
4. D. Frenkel and B. Smit, *Understanding Molecular Simulation*, 2nd edition, chapter on thermostats (2002), for classical Andersen collision context.
