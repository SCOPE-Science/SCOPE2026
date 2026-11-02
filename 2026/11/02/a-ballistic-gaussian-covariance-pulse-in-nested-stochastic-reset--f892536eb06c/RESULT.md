# A ballistic Gaussian covariance pulse in nested stochastic resetting

## Finding
Consider the stationary hierarchy of independent Brownian particles with one-sided copying resets defined below. Write \(V=2D/r\), \(n\ge2\), \(m=n-1\), and \(z=rt\). Its **forward** and **reverse** first-to-\(n\)-th time-lagged covariances are exactly
\[
F_n(t):=\mathbb E[X_1(0)X_n(t)]
 = V2^{-m}e^{-z}\sum_{k=0}^{m}\frac{(2z)^k}{k!},
\qquad
R_n(t):=\mathbb E[X_n(0)X_1(t)]
 =V2^{-m}e^{-z}.
\]
In particular, \(F_n(t)>R_n(t)\) for every \(t>0\), whereas the equal-time covariance is \(V2^{-m}\). The forward covariance has precisely one global maximum at \(t=t_n^*=z_m/r>0\), where \(z_m\) is the unique positive root of
\[
\sum_{j=1}^{m}\frac{m!}{(m-j)!(2z_m)^j}=1.
\]
At that maximum,
\[
F_n(t_n^*)=\frac{2V e^{-z_m}z_m^m}{m!},\qquad
z_m=m-1+O(m^{-1}),\qquad
F_n(t_n^*)\sim V\sqrt{\frac{2}{\pi m}}.
\]
More precisely, for every fixed \(s\in\mathbb R\), uniformly over \(s\) in compact sets,
\[
F_n\!\left(\frac{m+s\sqrt m}{r}\right)
 =\frac{2V}{\sqrt{2\pi m}}e^{-s^2/2}(1+o(1))
\qquad(m\to\infty).
\]
The first and \(n\)-th stationary variances are \(V\) and \(nV\). Hence the maximum **Pearson correlation** has the algebraic law
\[
\max_{t\ge0}\operatorname{Corr}(X_1(0),X_n(t))
\sim \sqrt{\frac{2}{\pi}}\frac{1}{n},
\]
although its equal-time value is the exponentially smaller \(2^{-m}/\sqrt n\). A delayed Gaussian pulse carries first-particle information down the reset chain even after equal-time correlations have become exponentially small.

## Assumptions and scope
For each finite integer \(N\ge2\), the coordinates \(X_1,\ldots,X_N\) evolve on the real line with independent Brownian drivers of generator \(D\partial_x^2\), with \(D>0\). Each coordinate has an independent rate-\(r\) Poisson clock, with the same \(r>0\). At its event, \(X_1\) jumps to zero; for \(i\ge2\), \(X_i\) jumps instantaneously to the contemporaneous value \(X_{i-1}\). No other coordinate jumps. All clocks and Brownian drivers are independent, and simultaneous clock events have probability zero. The expectations refer to the unique stationary joint law. The asymptotic statements use the consistent sequence of these systems with \(N\ge n\to\infty\), holding \(D,r\) fixed. The lag \(t\) is physical time, not resetting-event count. No unreset drift, interaction, shared noise, or randomly distributed copy target is assumed.

## Proof
**1. Existence, uniqueness, and moments.** Trace a coordinate backward from time zero to the most recent reset of its index, then trace the predecessor recursively. After at most \(i\) ancestral resets, the lineage of coordinate \(i\) reaches the fixed coordinate zero. Two-sided independent Poisson clocks supply almost surely finite exponential waiting times; independent Brownian increments supply a pathwise stationary construction with finite moments. Applying the same backward construction to a process started in the distant past erases every finite-dimensional initial state almost surely; this gives uniqueness and convergence to stationarity for each finite \(N\). Symmetry gives zero coordinate means. The generator yields
\[
0=\mathbb E[\mathcal L X_1^2]=2D-r\mathbb E[X_1^2],
\quad
0=\mathbb E[\mathcal L X_i^2]=2D+r(\mathbb E[X_{i-1}^2]-\mathbb E[X_i^2])
\]
for \(i\ge2\). Consequently \(\mathbb E[X_1^2]=V\) and \(\mathbb E[X_i^2]=iV\). For \(j\ge2\), independent Brownian coordinates have zero cross-quadratic variation, and only resets of coordinates \(1\) and \(j\) change their product; therefore
\[
0=\mathbb E[\mathcal L(X_1X_j)]
 =r\mathbb E[X_1X_{j-1}]-2r\mathbb E[X_1X_j].
\]
Induction gives the exact stationary covariance \(\mathbb E[X_1X_j]=V2^{-(j-1)}\).

**2. Temporal covariance and directionality.** Conditional on the full stationary starting vector \(X(0)\), the coordinate means solve
\[
\frac{d}{dt}M_1=-rM_1,\qquad
\frac{d}{dt}M_j=r(M_{j-1}-M_j),\quad j\ge2,
\]
where \(M_j(t)=\mathbb E[X_j(t)\mid X(0)]\). The finite triangular system has the exact solution
\[
M_j(t)=e^{-rt}\sum_{k=0}^{j-1}\frac{(rt)^k}{k!}X_{j-k}(0).
\]
Multiplying by \(X_1(0)\), averaging, and inserting the stationary covariances proves \(F_n\). The analogous identity \(M_1(t)=e^{-rt}X_1(0)\) proves \(R_n\). Their difference is strictly positive for \(m\ge1,z>0\), because all nonconstant coefficients in the finite sum are positive. The lag asymmetry is an explicit stationarity-compatible witness of time irreversibility.

**3. Unique peak.** Write \(P_m(z)=\sum_{k=0}^m(2z)^k/k!\). Direct differentiation gives
\[
\frac{d}{dz}[e^{-z}P_m(z)]
=e^{-z}\left[\sum_{k=0}^{m-1}\frac{(2z)^k}{k!}-\frac{(2z)^m}{m!}\right].
\]
Dividing the bracket by its positive last term yields \(Q_m(z)-1\), where
\[
Q_m(z)=\sum_{j=1}^{m}\frac{(m)_j}{(2z)^j},\qquad
(m)_j=\frac{m!}{(m-j)!}.
\]
Every term decreases strictly in \(z>0\). Moreover, \(Q_m(z)\to\infty\) as \(z\downarrow0\) and \(Q_m(z)\to0\) as \(z\to\infty\). Thus there is exactly one critical point, a global maximum. At its root \(Q_m(z_m)=1\), the preceding sum equals the last term; substituting yields \(F_n(t_n^*)=2Ve^{-z_m}z_m^m/m!\).

**4. Peak location.** For bounded real \(a\), expansion of the falling factorial and denominator, followed by a geometrically dominated summation, gives
\[
Q_m(m+a)
=\sum_{j\ge1}2^{-j}
\left[1-\frac{j(j-1)/2+ja}{m}\right]+O(m^{-2})
=1-\frac{2+2a}{m}+O(m^{-2}),
\]
uniformly for \(a\) in compact sets. The extension of the finite sum to infinity changes it by an exponentially small amount. Indeed \(\sum_{j\ge1}j2^{-j}=2\) and \(\sum_{j\ge1}j(j-1)2^{-j}=4\). At \(a=-2\) the expansion exceeds one and at \(a=0\) it falls below one for large \(m\). Monotonicity first traps \(z_m\) between \(m-2\) and \(m\), and the same expansion at the root yields \(z_m=m-1+O(m^{-1})\). Stirling's formula then gives the stated peak height.

**5. Gaussian pulse.** Rewrite the exact covariance at any positive \(z\) as
\[
F_n(z/r)=V\frac{e^{-z}z^m}{m!}[1+Q_m(z)].
\]
When \(z=m+s\sqrt m\), the ratios \((m)_j/(2z)^j\) converge termwise to \(2^{-j}\), and a common geometric majorant applies uniformly on compact sets of \(s\). Thus \(Q_m(m+s\sqrt m)\to1\). Stirling's local expansion yields
\[
\frac{e^{-(m+s\sqrt m)}(m+s\sqrt m)^m}{m!}
=\frac{e^{-s^2/2}}{\sqrt{2\pi m}}(1+o(1)).
\]
Combining these formulas proves the Gaussian pulse. Finally dividing by \(\sqrt{\mathbb E[X_1^2]\mathbb E[X_n^2]}=V\sqrt n\) proves the Pearson law. All limits are for fixed \(D,r>0\); the result is not a claim of uniformity in those parameters.

## Verification
`verify_pulse.py` uses the independent stationary second-moment recursion and the matrix exponential of the conditional-mean generator to check the exact formulas. For multiple chain sizes, diffusion constants, reset rates, and lags it independently compares forward and reversed covariances. It also checks the exact maximizing-value identity and numerically samples the scaled Gaussian-pulse asymptotics. The script completed **728 deterministic finite checks** with no failures. Run it using Python with NumPy and SciPy; see `requirements.txt`. These computations do not certify the infinite-size limits, which follow from the analytical argument above.

## Relationship to prior work
Alston, Britton and Bertrand (2025) introduced the nested Brownian copying-reset chain and computed its stationary marginal distributions, moments, and **equal-time** correlations. Those known ingredients, including the static first-to-depth decay, are not claimed as new. Britton, Le Jeune, Alston, Bressloff and Bertrand (2026) studied relaxation and accumulation times with equal and heterogeneous resetting rates, including a linear-in-depth relaxation delay; their Discussion explicitly identifies **time-dependent interparticle correlations** as a further question. The finding here addresses a different observable: the noncommuting forward/reverse **stationary two-time** covariances and their moving, asymptotically Gaussian optimum, with algebraic peak strength. Classical Markov semigroup identities and Stirling asymptotics underlie the proof; the model-specific exact formulas and sharp depth asymptotics are the asserted contribution.

## Limitations
Only the first-to-depth covariance in the equal-rate, independently reset Brownian chain is analyzed. No full distribution of the transmitted signal, nonlinear response, heterogeneous-rate pulse classification, pathwise propagation front, finite-size uniform remainder, thermodynamic entropy-production value, or empirical information-channel capacity is established. A generic semigroup argument may imply the finite-time algebraic identities once the model and static moments are specified; the claimed mathematical content includes the strict global optimum, its location and amplitude, and the universal Gaussian deep-chain pulse. Independent literature-wide priority adjudication remains open.

## References
1. H. Alston, C. Britton and T. Bertrand, *Nested stochastic resetting: nonequilibrium steady states and exact correlations*, arXiv:2502.03225v1 (first public 2025-02-05); *Physical Review Letters* **135**, 167101 (2025), DOI 10.1103/ccjj-6ksn. Primary full text: https://arxiv.org/html/2502.03225v1.
2. C. Britton, B. Le Jeune, H. Alston, P. C. Bressloff and T. Bertrand, *Approach to steady-state in nested resetting processes*, arXiv:2609.25252v1 (first public 2026-09-21), especially Sections 2, 4, and 5: https://arxiv.org/html/2609.25252.
