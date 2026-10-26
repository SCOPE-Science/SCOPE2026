# Different universal coupling optima for peak and integrated time-asymmetric correlations of two thermostated Brownian particles

## Finding
In a pair of harmonically coupled overdamped Brownian particles connected to unequal-temperature reservoirs, optimizing the magnitude of the **largest delayed cross-covariance asymmetry** and optimizing its **integral over delay** selects two different, uniquely determined spring couplings. At fixed trap stiffness \(k>0\), the integrated optimum is \(u_{\mathrm{area}}=k/\sqrt{2}\). The peak optimum is \(u_{\mathrm{peak}}=(k/2)x_*\), where \(x_*>2\) is the unique positive solution of
\[
(x+2)\log(1+x)=x^2,
\qquad x_*=2.223254940100293\ldots.
\]
Thus \(u_{\mathrm{peak}}=1.111627470050146\ldots k>u_{\mathrm{area}}=0.707106781186547\ldots k\). Both ratios are independent of the two bath temperatures (provided they differ). In contrast, the infinitesimal-delay antisymmetric covariance slope increases strictly with coupling rather than possessing a finite optimum; this slope is the previously established mean-circulation observable, not a new result here.

## Assumptions and scope
Let \(Y_t=(Y_1(t),Y_2(t))^\top\) denote the mean-centered displacement along any fixed Cartesian axis of two particles in harmonic optical traps. The overdamped, unit-mobility SDE is
\[
 dY_t=-\begin{pmatrix}k+u&-u\\-u&k+u\end{pmatrix}Y_t\,dt
 +\begin{pmatrix}\sqrt{2T_1}&0\\0&\sqrt{2T_2}\end{pmatrix}dW_t,
\]
where \(k,u,T_1,T_2>0\), \(T_1\ne T_2\), and the Brownian drivers are independent. Initial data are sampled from the unique centered stationary Gaussian law. Shifting the locations of the trap centers changes only stationary means and therefore leaves all centered formulas below unchanged. For every \(t\ge0\), define
\[
\Delta_u(t)=\operatorname{Cov}(Y_1(t),Y_2(0))
-\operatorname{Cov}(Y_2(t),Y_1(0)),\quad
P(u)=\sup_{t\ge0}|\Delta_u(t)|,\quad
J(u)=\int_0^\infty|\Delta_u(t)|\,dt.
\]
No claim is made about hydrodynamic multiplicative-noise corrections, nonquadratic forces, unequal particle mobilities, or finite-sampling uncertainties. The two-dimensional particle model has two independent coordinate copies of the specified centered process.

## Proof
Write \(s=k+u\), \(A=\left(\begin{smallmatrix}s&-u\\-u&s\end{smallmatrix}\right)\), and \(\Theta=\operatorname{diag}(T_1,T_2)\). Since the eigenvalues of \(A\) are \(k\) and \(k+2u\), the stationary covariance \(C\) is the unique solution of \(AC+CA=2\Theta\). Its diagonal difference is
\[
C_{22}-C_{11}=\frac{T_2-T_1}{k+u};
\]
for completeness, \(C_{12}=u(T_1+T_2)/[2k(k+2u)]\) and \(C_{ii}=[T_i+u C_{12}]/(k+u)\). The two-time covariance matrix is \(\mathbb E[Y_tY_0^\top]=e^{-At}C\), where
\[
e^{-At}=\frac12\begin{pmatrix}e^{-kt}+e^{-(k+2u)t}&e^{-kt}-e^{-(k+2u)t}\\e^{-kt}-e^{-(k+2u)t}&e^{-kt}+e^{-(k+2u)t}\end{pmatrix}.
\]
Its off-diagonal antisymmetric part is therefore
\[
\boxed{\Delta_u(t)=\frac{T_2-T_1}{2(k+u)}\bigl(e^{-kt}-e^{-(k+2u)t}\bigr).}
\]
For all positive delays the sign is fixed by \(T_2-T_1\). Differentiation in delay gives the unique global maximizer
\[
 t_{\mathrm{peak}}(u)=\frac{\log(1+2u/k)}{2u}.
\]
Put \(x=2u/k\). Substitution and direct integration of the exponential difference give
\[
P(u)=\frac{|T_2-T_1|}{k}\,g(x),\quad
 g(x)=\frac{x}{(x+1)(x+2)}(1+x)^{-1/x},
\]
\[
J(u)=\frac{|T_2-T_1|}{k^2}\,h(x),\quad
 h(x)=\frac{x}{(x+1)(x+2)}.
\]
(The factor \((1+x)^{-1/x}\) means \(\exp[-\log(1+x)/x]\).)

To classify \(J\),
\[
h'(x)=\frac{2-x^2}{(x+1)^2(x+2)^2}.
\]
Hence the unique positive maximizer is \(x_{\mathrm{area}}=\sqrt2\), with \(h(\sqrt2)=3-2\sqrt2\). To classify \(P\), use
\[
\frac{d}{dx}\log g(x)=\frac{\log(1+x)}{x^2}-\frac1{x+2}
=\frac{F(x)}{x^2(x+2)},\qquad
 F(x)=(x+2)\log(1+x)-x^2.
\]
Here \(F(0)=0\), \(F'(0)=2\), and \(F''(x)=x/(1+x)^2-2<0\) for every \(x\ge0\), while \(F(x)\to-\infty\). Strict concavity implies that \(F\) crosses zero exactly once after zero: \(g\) rises and then falls. Since \(F(2)=4\log3-4>0\), its positive zero satisfies \(x_*>2>\sqrt2\), proving the strict ordering of the two optima. Further, \(g(x)\to0\) and \(h(x)\to0\) at both endpoints \(x\downarrow0\) and \(x\to\infty\), confirming they are global maxima.

Their optimal magnitudes are
\[
J(u_{\mathrm{area}})=(3-2\sqrt2)\frac{|T_2-T_1|}{k^2},\qquad
P(u_{\mathrm{peak}})=0.096476371815292\ldots\frac{|T_2-T_1|}{k}.
\]
Finally \(\Delta'_u(0+)=u(T_2-T_1)/(k+u)\). Its absolute value increases strictly from zero toward \(|T_2-T_1|\) as \(u\to\infty\), unlike \(P\) and \(J\), both of which vanish in that limit. This last short-time slope is a restatement of an already known circulation law.

## Verification
The included standalone `verify.py` checks the Lyapunov covariance equation, the matrix propagator, the exact delay formula, both optimized functions, all stationary-point derivatives, and rational/analytic root bounds. It also compares symbolic formulas and direct covariance propagation across 25 deterministic parameter draws, and tests each optimum under neighboring couplings. Running `python3 verify.py` with SymPy available produces the included `verification_output.txt`, reporting 113 passed assertions. These finite tests do not establish global uniqueness; the strict-concavity and derivative arguments above do.

## Relationship to prior work
Dotsenko, Imparato, Viot, and Oshanin [1] introduce and solve the two-particle, unequal-temperature optical-trap model, determining its stationary probability distribution, currents, and angular circulation. Their earlier related study [2] also finds nonmonotone **spatially integrated curl** as coupling changes. The observable studied here is different: **antisymmetry of two-time position cross-covariances**, with two experimentally distinguishable lag objectives. The generic two-thermostat Ornstein–Uhlenbeck covariance propagator is established prior theory [3]; the displayed formula for \(\Delta_u(t)\) follows from it, and is not asserted as independently novel. The contribution assessed here is the pair of exact distinct universal optimum couplings, their strict uniqueness, and their contrast with monotone short-lag circulation. More general thermodynamic bounds on cross-correlation asymmetry [4] do not supply these optimal-coupling ratios. A coincidence with an unlocated optimization of the same physical observable remains possible.

## Limitations
The result is an exact mathematical optimization within a Gaussian linear-response model, not a claim about measurements from a particular device or optimal statistical estimator. Temperatures must differ: for equal temperatures the asymmetry is identically zero and no unique optimizing coupling exists. The equal trap stiffnesses, uniform mobility, positive attractive coupling, and common stationary preparation are essential assumptions. A separate finite-sampling/noise analysis is needed before using the universal ratios as experimental design parameters. No claim of a previously unknown stationary distribution or a new mean circulation is made. No independent scholarly priority audit or independent proof audit has been performed.

## References
[1] V. S. Dotsenko, A. Imparato, P. Viot, G. Oshanin, *Out-of-equilibrium dynamics of two interacting optically-trapped particles*, arXiv:2302.07716 (first public version 2023-02-15), SciPost Physics Core 6, 056 (2023). https://arxiv.org/abs/2302.07716

[2] V. S. Dotsenko, P. Viot, A. Imparato, G. Oshanin, *Cooperative dynamics in two-component out-of-equilibrium systems: Molecular “spinning tops”*, arXiv:2208.12768 (2022). https://arxiv.org/abs/2208.12768

[3] A. Crisanti, A. Puglisi, D. Villamaina, *Non-equilibrium and information: the role of cross-correlations*, arXiv:1202.0508 (2012), Physical Review E 85, 061127. https://arxiv.org/abs/1202.0508

[4] T. Ohga, S. Ito, A. Kolchinsky, *Thermodynamic Bound on the Asymmetry of Cross-Correlations*, arXiv:2303.13116 (2023). https://arxiv.org/abs/2303.13116
