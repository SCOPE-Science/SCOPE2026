# A sharp dimension-five kurtosis transition for run-and-tumble particles with refreshed speeds

## Finding
Let a particle move in \(\mathbb R^d\) through independent ballistic runs separated by a rate-\(\gamma>0\) Poisson process. Initially and after each tumble its velocity is resampled as \(V\Theta\), with \(\Theta\) uniform on the unit sphere, \(V\ge0\) independent of \(\Theta\), and successive pairs independent. Assume \(d\) is a positive integer, \(0<\mathbb E V^2<\infty\) and \(\mathbb E V^4<\infty\). Let \(X_t\) be the first Cartesian displacement and set
\[
m_2=\frac{\mathbb E V^2}{d},\qquad m_4=\frac{3\mathbb E V^4}{d(d+2)},\qquad R=\frac{m_4}{m_2^2},\qquad x=\gamma t.
\]
The exact variance and fourth cumulant are
\[
\operatorname{Var}(X_t)=\frac{2m_2}{\gamma^2}(x-1+e^{-x}),\qquad
\kappa_4(X_t)=\frac{12m_2^2}{\gamma^4}[R A(x)+B(x)],
\]
where
\[
A(x)=e^{-x}(x^2+4x+6)+2x-6,
\qquad B(x)=-e^{-x}(x^2+8x+10)-e^{-2x}-4x+11.
\]
For every \(x>0\), \(A(x)>0\), and the threshold \(R_*(x)=-B(x)/A(x)\) decreases **strictly** from \(3\) to \(2\). Hence:

- \(R\le2\): \(\kappa_4(X_t)<0\) for every \(t>0\).
- \(2<R<3\): a unique \(t_*>0\) has zero fourth cumulant, negative before and positive after.
- \(R\ge3\): \(\kappa_4(X_t)>0\) for every \(t>0\).

Writing the speed-moment ratio as \(Q=\mathbb EV^4/(\mathbb EV^2)^2\ge1\), the thresholds are \(Q_{\mathrm{low}}=2(d+2)/(3d)\) and \(Q_{\mathrm{high}}=(d+2)/d\). In particular, **constant speed** has \(R=3d/(d+2)\), and the unique sign switch occurs exactly in dimensions \(d\ge5\). For \(d=5\), it is located at \(\gamma t_*\approx6.12239214208656\). In \(d=2\), equal probabilities of speeds \(1\) and \(3\) give \(R=123/50\) and \(\gamma t_*\approx2.08102085125232\).

## Assumptions and scope
The initial velocity is freshly sampled from the same i.i.d. run law as all later velocities. The tumble rate is independent of speed and direction; a tumble instantaneously redraws both speed and direction isotropically. There is no spatial diffusion or rotational diffusion between tumbles. The process starts at the origin. The statements hold for every positive observation time and finite fourth speed moment. A zero speed may have positive mass, but \(\mathbb EV^2>0\). The fourth cumulant means \(\mathbb E X_t^4-3(\mathbb E X_t^2)^2\); the projection has mean zero.

## Proof
**1. A Poisson–Dirichlet formula.** Condition on exactly \(n\ge0\) tumbles in \([0,t]\). The \(n+1\) normalized run durations have a uniform Dirichlet law. If \(S_j\) denote their unnormalized lengths and \(U_j\) are independent fresh Cartesian velocities, \(X_t=\sum_j S_jU_j\). Isotropy gives \(\mathbb E U_j=0\), \(\mathbb E U_j^2=m_2\), and \(\mathbb E U_j^4=m_4\). Dirichlet moments and independence give the exact conditional equations
\[
\mathbb E[X_t^2\mid N_t=n]=\frac{2m_2t^2}{n+2},\quad
\mathbb E[X_t^4\mid N_t=n]=\frac{t^4(24m_4+12nm_2^2)}{(n+2)(n+3)(n+4)}.
\]
Averaging with the Poisson weights \(e^{-x}x^n/n!\), summing these absolutely convergent series and subtracting three times the squared variance yields the displayed closed forms for the variance and fourth cumulant. Independently, applying the velocity-refresh generator to polynomial moments gives
\[
\mathcal L\{\mathbb E X_t^2\}(s)=\frac{2m_2}{s^2(s+\gamma)},\qquad
\mathcal L\{\mathbb E X_t^4\}(s)=\frac{24m_4}{s^2(s+\gamma)^3}+\frac{24\gamma m_2^2}{s^3(s+\gamma)^3}.
\]
These Laplace transforms invert to the same expressions. All interchanges use bounded time intervals and the assumed finite fourth moment.

**2. Strict positivity of \(A\).** In the exact fourth-moment formula the coefficient of \(m_4\) is \(\mathbb E\sum_j S_j^4=12A(x)/\gamma^4\). It is strictly positive at every \(t>0\); hence \(A(x)>0\) for all \(x>0\).

**3. A global sign certificate.** Differentiation shows that \(R_*'(x)=(B A'-B'A)/A^2\). Defining \(F(x)=-e^{3x}(B A'-B'A)\), exact algebra gives
\[
F(x)=2e^{3x}+(-2x^3+7x^2-18x+6)e^{2x}+(4x^2+12x-18)e^x+x^2+6x+10.
\]
Write \(F(x)=\sum_{n\ge0}c_nx^n/n!\). Its first eight coefficients \(c_0,\dots,c_7\) vanish, and \(c_8=112>0\). For every integer \(n\ge8\), direct coefficient calculation gives
\[
c_{n+1}-3c_n=\frac{2^n}{4}(n^3-16n^2+79n-96)-8(n-2)(n+3).
\]
The cubic divided by four equals \(6\) at \(n=8\) and increases strictly thereafter: its derivative \((3n^2-32n+79)/4\) is positive for \(n\ge8\). Also \(6\cdot2^n>8(n-2)(n+3)\) at \(n=8\), and the left-hand side doubles at each subsequent integer while the right-hand side increases by a factor less than two. Thus \(c_{n+1}>3c_n>0\) by induction. Consequently \(F(x)>0\) at every \(x>0\), and \(R_*'(x)<0\).

**4. Endpoints and phase diagram.** The Taylor expansion \(A(x)=x^4/12+O(x^5)\) and its counterpart for \(B\) give \(R_*(x)\to3\) as \(x\downarrow0\). The leading terms \(A(x)=2x-6+o(1)\) and \(B(x)=-4x+11+o(1)\) give \(R_*(x)\to2\) as \(x\to\infty\). Strict decrease then proves all three alternatives and uniqueness. For constant speed \(R=3d/(d+2)\) lies above \(2\) exactly when \(d>4\), and remains below \(3\) at every finite dimension. This gives the sharp dimension-five threshold.

## Verification
The standalone standard-library Python script `rtp_velocity_kurtosis_checks.py` calculates 1,136 finite checks. It independently sums the conditional Dirichlet–Poisson moment series for different dimensions, speed moments and observation times; checks the exact exponential-series coefficient recurrence through order \(120\); reconstructs transition times at arbitrary precision; and checks the dimension-four strict sign. The universal strict monotonicity is established by the induction above, not by finite computation. Running `python3 rtp_velocity_kurtosis_checks.py` requires no external packages.

For an additional asymptotic diagnostic, \(\kappa_4(X_t)=(m_4-3m_2^2)t^4+O(t^5)\) as \(t\downarrow0\), whereas for \(R\ne2\), \(\kappa_4(X_t)\sim24m_2^2(R-2)t/\gamma^3\) as \(t\to\infty\). At the boundary \(R=2\), the cumulant converges to the strictly negative constant \(-12m_2^2/\gamma^4\).

## Relationship to prior work
Mori, Le Doussal, Majumdar and Schehr (2020, arXiv:2001.01492; expanded arXiv:2006.06989) examine arbitrary-dimensional run-and-tumble processes including i.i.d. speeds redrawn after tumbling; their explicit central results are persistence, time of maximum and record statistics rather than the fourth-cumulant sign diagram. Mori and collaborators (arXiv:2103.04637 and 2107.00338) analyze rare displacements and condensation, not this finite-time zero-crossing classification. Santra, Basu and Sabhapandit (arXiv:2211.07337) compute higher moments in two-dimensional fixed-speed active-particle variants; these formulas do not establish the all-dimensional random-speed single-crossing theorem. The Dirichlet moment identities are elementary existing probability tools; novelty is not claimed for these ingredients. Earlier general velocity-jump process theory could contain an implicit higher-cumulant identity, and a further priority examination is warranted.

## Limitations
The theorem concerns a single free, noninteracting particle and a fixed Cartesian displacement from the origin. It does not describe tumbling kernels with directional memory, run-duration-dependent speeds, a fixed particle-to-particle random speed, translational Brownian noise, heavy-tailed speed laws without fourth moments, confinement, or interactions. The dimension-five crossover is a sign change of the **unnormalized fourth cumulant**, not a thermodynamic phase transition, and the central-limit Gaussian long-time law remains valid for each finite fourth-moment speed law. Exact published priority is not independently certified.

## References
1. F. Mori, P. Le Doussal, S. N. Majumdar and G. Schehr, *Universal survival probability for a d-dimensional run-and-tumble particle*, arXiv:2001.01492, first posted 6 January 2020. https://arxiv.org/abs/2001.01492
2. F. Mori, P. Le Doussal, S. N. Majumdar and G. Schehr, *Universal Properties of a Run-and-Tumble Particle in Arbitrary Dimension*, arXiv:2006.06989, first posted 12 June 2020. https://arxiv.org/abs/2006.06989
3. F. Mori, P. Le Doussal, S. N. Majumdar and G. Schehr, *Condensation transition in the late-time position of a Run-and-Tumble particle*, arXiv:2103.04637, 2021. https://arxiv.org/abs/2103.04637
4. F. Mori, D. S. P. Gradenigo and S. N. Majumdar, *First-order condensation transition in the late-time position of a run-and-tumble particle in one dimension*, arXiv:2107.00338, 2021. https://arxiv.org/abs/2107.00338
5. I. Santra, U. Basu and S. Sabhapandit, *Long time behavior of run-and-tumble particles in two dimensions*, arXiv:2211.07337, 2022. https://arxiv.org/abs/2211.07337
