# A sharp two-reversal kurtosis phase diagram for an inertial telegraph-driven oscillator

## Finding

An inertial run-and-tumble particle in a one-dimensional harmonic trap has a **sharp damping threshold** below which its stationary position fourth cumulant changes sign *twice* as the tumble rate increases. Above the threshold it is always negative, including throughout the overdamped regime. This is a fourth-order fluctuation crossover, not a thermodynamic transition or a claim about the number of modes of the position density.

Set \(h=\eta/\sqrt{k}\) and \(g=\gamma/\sqrt{k}\). Define
\[
\begin{aligned}
P(h,g)={}&96g^5+384hg^4+(576h^2+208)g^3\\
&+(408h^3+448h)g^2+(138h^4+238h^2-18)g\\
&+18h^5+33h^3+12h,\\
Q(h,g)={}&h(3h^2+4)(1+2hg+4g^2)^2\\
&\quad\cdot(9+6hg+4g^2)(1+2h^2+6hg+4g^2).
\end{aligned}
\]
Then the stationary fourth cumulant is exactly
\[
\boxed{\kappa_4(X)=-\frac{6A^4}{k^4}\frac{P(h,g)}{Q(h,g)}.}
\]
Every factor in \(Q(h,g)\) is positive for \(h,g>0\). There exists exactly one pair \((h_*,g_*)\in(0,\infty)^2\) satisfying
\[
P(h_*,g_*)=0,\qquad \partial_g P(h_*,g_*)=0.
\]
Its numerically evaluated coordinates (not definitions by rounding) are
\[
h_*=0.08487853348854\ldots,\qquad
g_*=0.10961017659535\ldots.
\]
More precisely, \(21/250<h_*<17/200\) rigorously. For each \(0<h<h_*\) there are exactly two simple positive zeros \(g_-(h)<g_+(h)\) of \(P(h,\cdot)\). As \(g\) increases, \(\kappa_4(X)\) is negative for \(0<g<g_-\), positive for \(g_-<g<g_+\), and negative for \(g>g_+\). At \(h=h_*\) it vanishes only at \(g=g_*\) and is negative elsewhere. For \(h>h_*\), it is negative for every \(g>0\).

In particular, at \(h=1/50\), the exact sign pattern at \(g=1/100,1/10,1/3\) is respectively negative, positive, negative. All statements refer to the *stationary* position law.

## Assumptions and scope

Let \((X_t,V_t,\sigma_t)\) be the process
\[
\dot X_t=V_t,\qquad \dot V_t=-kX_t-\eta V_t+A\sigma_t,
\]
where \(k,\eta,A,\gamma>0\), and \(\sigma_t\in\{-1,+1\}\) flips sign at the jump times of a rate-\(\gamma\) Poisson process. The mass is one. The telegraph signal is stationary with equal sign probabilities. The linear drift matrix has negative-real-part eigenvalues, so the stationary solution is the unique bounded-input convolution over the infinite past. All stationary moments are finite. There is no additional translational noise in the main theorem. \(\kappa_4(X)=\mathbb E[X^4]-3(\mathbb E[X^2])^2\); symmetry gives \(\mathbb E[X]=0\).

The scales \(h=\eta/\sqrt{k}\), \(g=\gamma/\sqrt{k}\) follow from measuring time in units of the harmonic frequency and position in units of \(A/k\). The case \(h=0\) is excluded because the undamped oscillator need not possess a stationary state. The limits \(g\downarrow0\) and \(g\to\infty\) are only one-sided limits within \(g>0\).

## Proof

**1. Stationarity and finite moments.** For \(Z_t=(X_t,V_t)\), the homogeneous drift is \(\dot Z=MZ\) with \(M=\left(\begin{smallmatrix}0&1\\-k&-\eta\end{smallmatrix}\right)\). Its eigenvalues have strictly negative real part for \(k,\eta>0\). Thus \(Z_t=\int_{-\infty}^t e^{M(t-s)}(0,A\sigma_s)^\top\,ds\) is a stationary bounded random variable; exponential contraction proves uniqueness of its stationary law and justifies applying the generator to polynomials. Symmetry under \((X,V,\sigma)\mapsto(-X,-V,-\sigma)\) annihilates the odd unflagged moments.

**2. Fourth moment computed by a finite linear system.** Write \(M^{(p)}_{ij}=\mathbb E[X^iV^j\sigma^p]\) for \(p\in\{0,1\}\), with \(\sigma^2=1\). Stationarity of the polynomial generator gives, for \(i,j\ge0\),
\[
\begin{aligned}
0={}&iM^{(p)}_{i-1,j+1}-jkM^{(p)}_{i+1,j-1}-j\eta M^{(p)}_{i,j}\\
&+jA M^{(1-p)}_{i,j-1}-2\gamma p M^{(p)}_{i,j}.
\end{aligned}
\]
Terms with a negative index are absent. In degree \(d\), symmetry leaves the \(d+1\) variables with \(p\equiv d\pmod2\); the forcing term on the right has degree \(d-1\), already computed. The coefficient matrix is invertible because it is the generator's stable diagonal action on homogeneous degree-\(d\) polynomials, with an additional \(-2\gamma\) decay on the flagged sector. Starting from \(M^{(0)}_{00}=1\), solving degrees 1 to 4 (or equivalently eliminating the finite generator equations directly) gives
\[
\mathbb E[X^2]=\frac{A^2}{k^2}\frac{h+2g}{h(1+2hg+4g^2)},
\]
and subtracting three times its square from \(\mathbb E[X^4]\) gives the stated factored \(\kappa_4(X)\). The complete equations and the exact rational-function comparison appear in `checker.py`. This is an identity of rational functions, not an interpolation from parameter samples.

**3. Sharp sign classification.** For every \(h>0\), \(P(h,0)=3h(3h^2+4)(2h^2+1)>0\), and \(P(h,g)\to+\infty\) as \(g\to\infty\). Furthermore,
\[
\begin{aligned}
\partial^2_g P(h,g)&=16(120g^3+288hg^2+216h^2g+78g+51h^3+56h)>0,\\
\partial_h P(h,g)&=384g^4+1152hg^3+(1224h^2+448)g^2\\
&\quad +(552h^3+476h)g+90h^4+99h^2+12\ge12.
\end{aligned}
\]
Therefore each section \(g\mapsto P(h,g)\) is strictly convex on \([0,\infty)\), and \(m(h)=\min_{g\ge0}P(h,g)\) is continuous and strictly increasing in \(h\) (indeed \(m(h_2)\ge m(h_1)+12(h_2-h_1)\) when \(h_2>h_1\)). Continuity follows from uniform coercivity on compact \(h\)-intervals. For \(h=21/250\), direct rational substitution at \(g=11/100\) yields a negative value. For \(h=17/200\), using global lower bound \(\partial^2_g P(h,g)\ge \partial^2_gP(h,0)>0\) and a quadratic supporting inequality about \(g_0=11/100\) yields
\[
\min_{g\ge0}P(17/200,g)\ge P(17/200,g_0)-\frac{[\partial_gP(17/200,g_0)]^2}{2\partial^2_gP(17/200,0)}
=\frac{267767843389081879}{98126241280000000000}>0.
\]
Hence there is a **unique** \(h_*\in(21/250,17/200)\) with \(m(h_*)=0\). The minimizer at that \(h_*\) lies strictly inside \(g>0\), since the value at \(g=0\) is positive; strict convexity gives its uniqueness and \(\partial_gP(h_*,g_*)=0\). For smaller \(h\) the strictly convex graph with positive endpoint and positive limit has exactly two positive simple zeros; for larger \(h\) none. As \(Q>0\), the sign pattern of the cumulant is exactly opposite to that of \(P\). There can be no further roots or disconnected positive regions.

**4. Oscillatory-filter mechanism.** The telegraph signal has two-point covariance \(\mathbb E[\sigma_s\sigma_t]=e^{-2\gamma|t-s|}\). At four ordered times \(t_1<t_2<t_3<t_4\), its connected fourth cumulant equals
\[
\operatorname{cum}(\sigma_{t_1},\sigma_{t_2},\sigma_{t_3},\sigma_{t_4})
=-2e^{-2\gamma[(t_3-t_1)+(t_4-t_2)]}<0.
\]
A second-order oscillator filters this signal through its impulse response. In the overdamped regime the response is nonnegative, forcing a negative displacement fourth cumulant. Only an underdamped sign-changing response can produce the positive middle regime, which the explicit sharp threshold proves occurs. The rate of response decay, not merely the underdamped/overdamped classification, governs its appearance.

## Verification

The included standalone `checker.py` requires Python 3, SymPy, and mpmath. Running `python checker.py` reconstructs the stationary polynomial-moment generator through degree four, verifies symbolically the variance and fourth-cumulant factorization, proves the derivative polynomial identities and rational threshold-bracket witness, and tests 48 exact rational parameter triples across all 14 nontrivial moment equations. Its recorded replay passed **683** assertions; `CHECKS.txt` contains the recorded output. The analytic strict-convexity and parameter-monotonicity argument, not numerical root finding or finite tests, proves uniqueness and sign changes.

## Relationship to prior work

Dutta, Kundu, Sabhapandit, and Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension*, arXiv:2406.06120 (initially public 2024-06-10), formulate this **same physical model** and provide a general polynomial moment recursion, the stationary second moments, and qualitative stationary-distribution shape regimes. Their moment recursion can in principle generate the fourth moment, so the calculation technique and the existence of a fourth-moment expression are not asserted to be new. The targeted distinction is the exact factored sign polynomial and **complete sharp two-reversal versus no-reversal phase classification with a unique damping cusp**, absent from the material inspected (their main text, moment section and appendices).

Sun, Ye, and Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578 (initially public 2024-09-01), study first-order overdamped dynamics with a run/stop state, not the second-order inertial model; their high-order moments therefore do not imply this damping boundary. Pawula, *Dichotomous-noise-driven oscillators*, Phys. Rev. A **35**, 3102 (1987), presents a general output-moment method for dichotomous-driven filters and numerical second-order results. Its abstract is available but the plausible full paper was inaccessible during comparison; it remains a priority risk, not evidence of noncoverage. The sharp phase statement is offered subject to independent scholarly priority review.

## Limitations

The boundary concerns stationary **fourth cumulant sign**, not a proven unimodality threshold, ergodic-rate transition, particle interactions, spatial thermodynamic limit, or observed finite-sample estimator. Strongly underdamped parameters \(0<h<h_*\) are required for two reversals. No claim is made that the general moment recursion itself is new. Existing general dichotomous-filter literature may contain equivalent fourth-moment expressions or phase descriptions not obtained for full-text comparison. Numerical values for \(h_*\) and \(g_*\) are approximations; the rigorous definition is the unique positive solution of the displayed double-root equations and exact rational bracket.

## References

1. Debraj Dutta, Anupam Kundu, Sanjib Sabhapandit, Urna Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension*, arXiv:2406.06120, initial submission 2024-06-10, https://arxiv.org/abs/2406.06120.
2. Aoran Sun, Fangfu Ye, Rudolf Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578, initial submission 2024-09-01, https://arxiv.org/abs/2409.00578.
3. R. F. Pawula, *Dichotomous-noise-driven oscillators*, Phys. Rev. A 35, 3102–3108 (1987), https://doi.org/10.1103/PhysRevA.35.3102.
