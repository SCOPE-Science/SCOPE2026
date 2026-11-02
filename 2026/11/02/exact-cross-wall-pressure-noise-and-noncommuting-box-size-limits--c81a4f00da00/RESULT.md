# Exact cross-wall pressure noise and noncommuting box-size limits for run-and-tumble swimmers

## Finding

Consider an ideal gas of independent, identical, symmetric, one-dimensional run-and-tumble particles between two hard, sticky walls at distance \(L>0\). For one particle, let \(v>0\) be the running speed, \(\gamma>0\) the rate of each orientation flip (including while stuck), and \(\mu>0\) the mechanical mobility. The particle sticks to a wall only while its orientation points outward, and detaches instantaneously at its next flip. There is no translational Brownian noise or interparticle interaction.

Let \(B_-(t)\) and \(B_+(t)\) indicate outward-pointing adhesion at the left and right walls. The instantaneous force magnitude on wall \(i\) is \(F_i(t)=(v/\mu)B_i(t)\), and \(J_i(T)=\int_0^T F_i(t)\,dt\). Write

\[
k=\frac{\gamma L}{v},\qquad F_0=\frac v\mu,\qquad R(k)=\frac{k^2(k+3)}{3(1+k)^3}.
\]

Under the unique stationary initial law, the mean force on either wall is \(F_0/[2(1+k)]\), and the full asymptotic integrated-force covariance matrix exists, with rows and columns in left/right order:

\[
\boxed{\lim_{T\to\infty}\frac{\operatorname{Cov}(J_i(T),J_j(T))}{T}=\frac{F_0^2}{4\gamma}
\begin{pmatrix}1+R(k)&R(k)-1\\R(k)-1&1+R(k)\end{pmatrix}_{ij}.}
\]

For every finite \(k>0\), \(0<R(k)<1/3\), so the two wall forces have strictly negative long-time covariance. Their asymptotic Pearson correlation is

\[
\rho(k)=\frac{R(k)-1}{R(k)+1}\in(-1,-1/2),
\]

and increases strictly with \(k\). The difference in accumulated wall impulses has the exactly box-size-independent variance rate \(F_0^2/\gamma\), whereas the sum has variance rate \(F_0^2 Lk(k+3)/[3v(1+k)^3]\).

There is a noncommutation of the infinite-observation and infinite-box limits. At fixed \(v,\gamma,\mu>0\),

\[
\begin{aligned}
\lim_{L\to\infty}\lim_{T\to\infty}\frac{\operatorname{Cov}(J_-(T),J_+(T))}{T}
&=-\frac{F_0^2}{6\gamma},\\
\lim_{T\to\infty}\lim_{L\to\infty}\frac{\operatorname{Cov}(J_-(T),J_+(T))}{T}
&=0.
\end{aligned}
\]

The same order-of-limits phenomenon holds for each wall's variance rate: the first order gives \(F_0^2/(3\gamma)\) and the reversed order gives zero. Here \(L\to\infty\) always starts the process from its \(L\)-dependent stationary law. For \(N\) independent particles, all mean forces and all entries of the covariance-rate matrix multiply by \(N\).

## Assumptions and scope

The state is \((X,S)\), with \(0\le X\le L\) and orientation \(S\in\{-1,+1\}\). In the interior, \(\dot X=vS\); \(S\) flips sign according to an independent Poisson clock of rate \(\gamma\). At \((0,-1)\) and \((L,+1)\), the coordinate stays pinned until the next flip, at which instant the particle runs inward. The one-dimensional walls are mechanically hard; \(F_0=v/\mu\) is the propulsive force scale, or a pressure scale per unit transverse cross-section. There is no absorption, resetting, translational thermal diffusion, orientational bias, or finite wall residence after an inward flip.

The invariant measure has constant interior orientation densities

\[
\pi(dx,+)=\pi(dx,-)=\frac{\gamma\,dx}{2(v+\gamma L)}\quad(0<x<L),
\]

and wall masses \(\pi\{(0,-1)\}=\pi\{(L,+1)\}=v/[2(v+\gamma L)]\). In particular the total stationary pinned fraction is \(m=1/(1+k)\). The covariance limit is for the centered stationary integrated forces; it is not a statement that the instantaneous pointwise forces remain nonzero as the box grows.

## Proof

**1. Invariant law.** In the interior the forward equations admit equal constant densities \(c=\gamma/[2(v+\gamma L)]\) in both orientations. Balancing incoming ballistic flux \(vc\) at each wall against the detachment flux \(\gamma q\) gives wall mass \(q=vc/\gamma=v/[2(v+\gamma L)]\). Normalization is \(2cL+2q=1\). Positivity of both flip and ballistic transport makes the process irreducible with a unique stationary probability law. Its regeneration via successive wall hits provides exponential return-time tails on every fixed finite interval.

**2. Sum observable.** Let \(B=B_-+B_+\), so \(\pi B=m=1/(1+k)\). To compute the asymptotic variance of \(\int_0^T B(t)dt\), solve the centered Poisson equation \(-\mathcal Lg=B-m\) with \(\pi g=0\). On the open interval, the backward generator acts by

\[
\mathcal Lg_+=vg'_++\gamma(g_--g_+),\qquad
\mathcal Lg_-=-vg'_-+\gamma(g_+-g_-).
\]

At outward-pointing wall states it acts only by flipping: \(\mathcal Lg_+(L)=\gamma(g_-(L)-g_+(L))\) and \(\mathcal Lg_-(0)=\gamma(g_+(0)-g_-(0))\). In the interior \(B=0\), whereas at either outward wall \(B=1\). Put \(w=g_+-g_-\) and \(u=g_++g_-\). The interior equations give

\[
w(x)=\frac{2m}{v}\left(x-\frac L2\right),\qquad
u(x)=C+\frac{2\gamma m}{v^2}\left(x-\frac L2\right)^2,
\]

where symmetry fixes the additive constant of \(w\) and \(\pi g=0\) fixes

\[
C=-\frac{m^2L}{v}\left(1+\frac{k(k+3)}6\right).
\]

Consequently, at both outward-pointing wall states,

\[
g_-(0)=g_+(L)=\frac{L}{v}\frac{m^2k(k+3)}6.
\]

The wall Poisson equations hold because \(\gamma mL/v=1-m\). The zero-mean condition is verified directly by integrating \(u\) against the two constant interior orientation densities and adding the two wall masses. The finite-state regenerative-martingale argument for this bounded piecewise-smooth solution yields

\[
\lim_{T\to\infty}\frac{\operatorname{Var}(\int_0^T B(t)dt)}T
=2\langle B-m,g\rangle_\pi
=2m g_+(L)
=\frac Lv\frac{k(k+3)}{3(1+k)^3}.
\]

In more detail, Dynkin's martingale for \(g\) differs from the centered integrated occupation by the bounded endpoint term \(g(X_T,S_T)-g(X_0,S_0)\); the quadratic-variation identity under stationarity has stationary mean \(2\langle B-m,g\rangle_\pi\). Exponentially mixing regenerative returns control the endpoint covariance and give the variance-rate limit. The exact identity also follows from stationarity and integration of the covariance function.

**3. Difference observable.** The position obeys the exact pathwise balance

\[
X_T-X_0=v\int_0^T[S(t)-B_+(t)+B_-(t)]\,dt.
\]

Thus

\[
\int_0^T(B_+(t)-B_-(t))dt
=\int_0^T S(t)dt-\frac{X_T-X_0}{v}.
\]

The orientation is an autonomous symmetric telegraph process whose stationary covariance is \(\mathbb E[S(t)S(0)]=e^{-2\gamma|t|}\). Consequently \(\operatorname{Var}(\int_0^T S(t)dt)/T\to1/\gamma\). The bounded endpoint displacement has negligible variance on the \(T\) scale and negligible cross term by Cauchy–Schwarz. Therefore the left/right occupation difference has asymptotic variance rate \(1/\gamma\), independently of \(L\).

**4. Covariance matrix.** Reflection \((X,S)\mapsto(L-X,-S)\) preserves the stationary law. It leaves the sum invariant and changes the sign of the difference, so their covariance is exactly zero at each finite observation time. Applying the preceding two variance rates to their sum and difference gives the displayed matrix after multiplication by \(F_0^2\).

**5. Signs, monotonicity, and limits.** Direct differentiation gives \(R'(k)=2k/(1+k)^4>0\); furthermore \(R(0+)=0\) and \(R(+\infty)=1/3\). The signs and strict correlation interval follow. For the reversed large-box limit, the stationary mean pinned time at either wall satisfies \(\mathbb E I_i(T)=T/[2(1+k)]\), where \(I_i(T)=\int_0^T B_i(t)dt\) lies in \([0,T]\). Therefore \(\mathbb E I_i(T)^2\le T^2/[2(1+k)]\to0\) for fixed \(T\) as \(L\to\infty\), and all finite-time force covariances tend to zero. Taking \(T\to\infty\) first instead gives \(R(k)\to1/3\) in the matrix, proving both noncommutations.

## Verification

The accompanying standalone \(\texttt{verify\_pressure\_noise.py}\) uses only the Python standard library. Running \(\texttt{python verify\_pressure\_noise.py}\) returns \(\texttt{PASS: 117 exact-arithmetic assertions}\). It checks the analytic Poisson solution, centering, boundary equations, the derivative and correlation bounds using rational parameters; it independently constructs discrete persistent-walk Markov generators and solves stationary and two Poisson systems by exact rational elimination at three lattice resolutions. For each of three rate ratios, finite-lattice discrepancy decreases with lattice resolution. These numerical approximations are not an infinite-dimensional proof; Steps 1–5 above supply the analytical argument.

## Relationship to prior work

Angelani's confined run-and-tumble analysis (2017, arXiv manuscript publicly uploaded 2022) already establishes the same sticky hard-wall model, its time-dependent one-point distribution, stationary wall population, and wall pressure. Its transition parameter \(\alpha\) is twice the present orientation-flip rate \(\gamma\), so the corresponding stationary force agrees after this conversion. The 2026 work of Li, Eichhorn and Dabelow develops an exact active ideal-gas law and one-dimensional RTP mean pressure; those mean-pressure results are prior art. The 2024 work of Mukherjee, Le Doussal and Smith develops general RTP local-/occupation-time fluctuations in a different, non-sticky geometry, providing relevant methodology rather than the displayed two-wall covariance. The present claim concerns the explicit joint integrated wall-force covariance, its strict anticorrelation, and the noncommuting large-box/time limits. Inspection of accessible primary full texts did not identify this formula, but the October 2026 motivating work's complete PDF and supplement were not accessible for full-text comparison; the novelty assessment is correspondingly qualified and requires independent publication-priority verification.

## Limitations

The result is exact only for a symmetric, noninteracting, athermal one-dimensional model with independent exponential orientation flips at the same rate in the bulk and at walls. The singular box-size limit is a statement about the order of limits in stationary ensembles, not persistence of an ordinary thermodynamic pressure in an infinite volume. No full-time force distribution, unequal wall parameters, interaction correction, higher-dimensional law, or finite-population pressure large-deviation principle is established. General stochastic-process methods may recover the displayed rates after additional model-specific calculation. The closest 2026 article's inaccessible supplement remains a specific originality risk; there has been no independent audit.

## References

1. S. Li, R. Eichhorn, and L. Dabelow, *Ideal gas of active particles in a box*, arXiv:2610.01287v1 (first public October 1, 2026), https://arxiv.org/abs/2610.01287 .
2. L. Angelani, *Confined run-and-tumble swimmers in one dimension*, Journal of Physics A 50 (2017); manuscript https://arxiv.org/abs/2206.03123 .
3. L. Angelani, *One-dimensional run-and-tumble motions with generic boundary conditions*, Journal of Physics A (2023), https://doi.org/10.1088/1751-8121/ad009e .
4. S. Mukherjee, P. Le Doussal, and N. R. Smith, *Large deviations in statistics of the local time and occupation time for a run and tumble particle*, arXiv:2405.07032, https://arxiv.org/abs/2405.07032 .
5. P. C. Bressloff and S. Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary*, Physical Review E 113, 054122 (2026), https://doi.org/10.1103/dcnh-bhwc .
