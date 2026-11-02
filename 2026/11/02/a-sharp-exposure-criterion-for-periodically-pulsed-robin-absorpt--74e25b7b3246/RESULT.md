# A sharp exposure criterion for periodically pulsed Robin absorption

## Finding

For a Brownian reactant confined to a finite reflecting interval, intermittent reactions at one endpoint exhibit an exact **diffusion-limited exposure criterion**. Let the surface be reactive only during successive nonoverlapping time windows of lengths \(\delta_n>0\), separated by uniform positive gaps, with finite, constant reactivity \(\kappa_n>0\) during window \(n\). Suppose each window is shorter than a fixed fraction of both the diffusion crossing time and the gap period. Starting from the uniform spatial distribution, the probability of **never reacting** is positive if and only if

\[
\sum_{n=1}^{\infty}\min\!\left\{\frac{\kappa_n\delta_n}{L},\frac{\sqrt{D\delta_n}}{L}\right\}<\infty.
\]

Here \(L>0\) is the interval length and \(D>0\) is the diffusivity. If this series diverges, reaction occurs almost surely. In particular, the total integrated surface reactivity \(\sum_n\kappa_n\delta_n\) can diverge while a positive fraction of particles survive indefinitely: the pulse durations impose an independent, sharp diffusion-limited cap.

For the normalized system \(L=D=1\) and pulses \([n,n+\delta_n)\), \(0<\delta_n\le1/4\), write \(k_n=\kappa_n\). If \(p(\delta,k)\) is the reaction probability in one isolated pulse of duration \(\delta\) and rate \(k\), starting from a uniform distribution, then the universal quantitative estimate is

\[
\frac14\min\{k\delta,\sqrt\delta\}\;\le\;p(\delta,k)\;\le\;4\min\{k\delta,\sqrt\delta\}.
\]

The diffusion-limited pulse law also has an explicit sharp crossover:

\[
p(\delta,k)=\sqrt\delta\,F(k\sqrt\delta)+O\!\left(e^{-1/(4\delta)}\right),\qquad
F(z)=\frac{2}{\sqrt\pi}-\frac{1-e^{z^2}\operatorname{erfc}(z)}{z},\quad z>0,
\]

where the error constant is independent of the reaction rate \(k>0\) for \(0<\delta\le1/4\). The function satisfies \(F(z)\sim z\) for \(z\downarrow0\) and \(F(z)\to2/\sqrt\pi\) for \(z\to\infty\). Both the series criterion and the crossover are assertions about the same time-dependent Robin absorption problem.

For power-law windows \(\delta_n=c\,n^{-p}\) and rates \(k_n=n^q\), with \(p>0\), \(q\in\mathbb R\), and fixed \(0<c\le1/4\), reaction is almost sure exactly when \(p\le2\) and \(q\ge p-1\). Thus \(p>2\) precludes almost-sure absorption, even at arbitrarily high polynomial reaction rates.

## Assumptions and scope

Let \(X_t\) be reflected Brownian motion on \([0,L]\) with generator \(D\partial_{xx}\), \(D>0\), and initially uniform position. Only the left endpoint is reactive; the right endpoint always reflects. Pulses start at times \(nT\), for positive integer \(n\), where \(T>0\). The left endpoint has time-dependent Robin reactivity

\[
\kappa(t)=\sum_{n\ge1}\kappa_n\mathbf1_{[nT,nT+\delta_n)}(t),\qquad
0<\delta_n\le\min\{T/4,L^2/(4D)\},\quad 0<\kappa_n<\infty.
\]

The time-dependent diffusion density has \(\partial_tu=D\partial_{xx}u\) in the interior, \(D\partial_xu(0,t)=\kappa(t)u(0,t)\), \(\partial_xu(L,t)=0\), and uniform initial density. Equivalently, write \(\ell^0_t=D\lim_{\varepsilon\downarrow0}\varepsilon^{-1}\int_0^t\mathbf1_{[0,\varepsilon)}(X_s)ds\), the left-endpoint boundary local time, and let \(E\) be an independent mean-one exponential random variable. The reaction time is

\[
\tau=\inf\!\left\{t\ge0:\frac1D\int_0^t\kappa(s)\,d\ell^0_s\ge E\right\}.
\]

The finite rate on each finite-duration window gives a well-defined locally bounded reactivity, even if the rates grow without bound as the window index tends to infinity. The statements apply to this deterministic pulsing model, not to arbitrary overlapping windows, general nonperiodic clocking without a uniform mixing gap, unbounded spatial domains, or nonlinear reactive boundary laws.

## Proof

**1. Nondimensionalization.** Put \(y=x/L\) and \(s=Dt/L^2\). The diffusion generator becomes \(\partial_{yy}\), the dimensionless Robin parameter during pulse \(n\) becomes \(k_n=\kappa_nL/D\), and its length becomes \(d_n=D\delta_n/L^2\). The dimensionless spacing is \(DT/L^2\), and each gap is at least three quarters of this period. Hence it suffices to prove the series criterion on \([0,1]\) for pulse starts separated by a fixed positive period and \(0<d_n\le1/4\); the special unit-period form is used to state explicit constants.

**2. One-pulse upper bound.** Let \(L_d\) denote local time accumulated at the left endpoint by the stationary reflected diffusion over duration \(d\). Normalize it by

\[
L_d=\lim_{\varepsilon\downarrow0}\frac1\varepsilon\int_0^d\mathbf1_{[0,\varepsilon)}(X_s)ds,
\quad \mathbb E_{\mathrm{unif}}L_d=d.
\]

For constant pulse rate \(k\), the uniform-start removal probability is \(p(d,k)=\mathbb E[1-e^{-kL_d}]\). The elementary inequality \(1-e^{-z}\le z\) gives \(p(d,k)\le kd\). It also satisfies \(p(d,k)\le\mathbb P(L_d>0)\). Unfold reflected Brownian motion into \(x+\sqrt2 B_t\) with reflecting folds at the integer boundaries. Reaching the left boundary before time \(d\) requires the unfolded process to hit either \(0\) or \(2\); hence the reflection principle and uniform initial position give

\[
\mathbb P(L_d>0)\le\int_0^1 2\Phi\!\left(-\frac{x}{\sqrt{2d}}\right)+2\Phi\!\left(-\frac{2-x}{\sqrt{2d}}\right)dx
\le\frac4{\sqrt\pi}\sqrt d.
\]

Consequently \(p(d,k)\le4\min\{kd,\sqrt d\}\).

**3. One-pulse lower bound.** The Neumann kernel of \(\partial_{xx}\) on \([0,1]\) is

\[
H_s(x,y)=1+2\sum_{j\ge1}e^{-j^2\pi^2s}\cos(j\pi x)\cos(j\pi y).
\]

The boundary local-time occupation formula and stationarity give the exact two-moment identities

\[
\mathbb E L_d=d,\qquad
\mathbb E L_d^2=2\int_0^d(d-s)H_s(0,0)\,ds.
\]

For \(0<s\le1/4\), monotone comparison with a Gaussian integral yields

\[
H_s(0,0)\le1+\frac1{\sqrt{\pi s}}
\le\left(\frac12+\frac1{\sqrt\pi}\right)s^{-1/2}.
\]

Integrating gives \(\mathbb E L_d^2\le 3d^{3/2}\). The inequalities \(1-e^{-z}\ge z/(1+z)\) and Cauchy–Schwarz, applied to the two factors \(\sqrt{L_d/(1+kL_d)}\) and \(\sqrt{L_d(1+kL_d)}\), imply

\[
\begin{aligned}
p(d,k)&\ge k\mathbb E\frac{L_d}{1+kL_d}\\
&\ge\frac{k(\mathbb E L_d)^2}{\mathbb E L_d+k\mathbb E L_d^2}
\ge\frac{kd}{1+3k\sqrt d}
\ge\frac14\min\{kd,\sqrt d\}.
\end{aligned}
\]

This proves the uniform crossover estimate without any asymptotic assumption about the pulse strengths.

**4. Mixing gaps turn one-pulse probabilities into an exact infinite-horizon criterion.** The Neumann heat kernel for any gap length \(g\ge g_0>0\) satisfies \(0<m\le H_g(x,y)\le M<\infty\), with constants depending only on \(g_0\). For instance, if \(g_0=3/4\), take

\[
m=1-2\sum_{j\ge1}e^{-3j^2\pi^2/4}>0,\qquad
M=1+2\sum_{j\ge1}e^{-3j^2\pi^2/4}.
\]

Let \(S_n\) be the probability of surviving through the end of pulse \(n\), and let \(p_n=p(d_n,k_n)\). Before each pulse, conditional on survival, the position distribution has a density bounded between \(m\) and \(M\): the preceding freely reflecting gap applies the Neumann kernel to a probability measure. The first pulse starts from the uniform measure, for which the same comparison is valid after enlarging the constants if necessary. Since the probability of reaction during a pulse, conditional on starting position \(x\), is a nonnegative function, we obtain

\[
m p_n\le1-\frac{S_n}{S_{n-1}}\le M p_n.
\]

If \(\sum p_n=\infty\), the left inequality implies \(S_n\le\prod_{j\le n}(1-mp_j)\to0\). If \(\sum p_n<\infty\), then \(Mp_n<1/2\) in the tail and the right inequality gives a positive lower bound \(S_n\ge S_N\prod_{j>N}(1-Mp_j)>0\), because any finite number of pulses with finite rates leaves positive survival probability. Thus \(\mathbb P(\tau=\infty)>0\) if and only if \(\sum_np_n<\infty\). Step 3 turns this into the stated series, and step 1 restores \(D\) and \(L\).

**5. Sharp one-pulse crossover.** For the half-line with constant initial density \(1\), reflecting/partially absorbing Robin boundary of parameter \(k\), and generator \(\partial_{xx}\), the boundary density \(v(0,s)\) has Laplace transform \(1/[\sqrt z(\sqrt z+k)]\), hence

\[
v(0,s)=e^{k^2s}\operatorname{erfc}(k\sqrt s).
\]

The total mass lost from the half-line, which is finite despite its infinite initial mass, is

\[
k\int_0^d v(0,s)\,ds
=\frac{2\sqrt d}{\sqrt\pi}-\frac{1-e^{k^2d}\operatorname{erfc}(k\sqrt d)}k
=\sqrt d\,F(k\sqrt d).
\]

For the interval, couple the half-line and twice-reflected processes with the same Brownian motion and same exponential local-time reaction threshold until their first visit to the right endpoint. For their absorption decisions to differ before time \(d\), one of them must subsequently traverse the full distance back to the left endpoint. The reflection principle bounds this by \(C e^{-1/(4d)}\), uniformly in \(k\). The extra half-line initial population at \(x>1\) contributes at most \(2\int_1^\infty\Phi(-x/\sqrt{2d})dx=O(e^{-1/(4d)})\). This proves the claimed uniform exponentially small correction. Standard complementary-error-function expansions give the two limits of \(F\).

**6. Power-law phase boundary.** For \(d_n=c n^{-p}\), \(k_n=n^q\), the decisive terms are comparable to \(\min\{n^{q-p},n^{-p/2}\}\). If \(p>2\), the second branch is summable regardless of \(q\). If \(0<p\le2\), the series diverges exactly when \(q\ge p-1\), including the harmonic-series boundaries. For example, \(d_n=n^{-4}/4\), \(k_n=n^6\) yield \(\sum_n k_nd_n=\infty\) but positive survival, whereas \(d_n=n^{-2}/4\), \(k_n=n\) yield almost-sure absorption despite \(\sum_nd_n<\infty\).

## Verification

The standalone `verify.py` reproduces the exact Robin–Neumann Sturm–Liouville spectral one-pulse mass formula, checks its independent half-line short-pulse limit across several rates, verifies the spectral boundary residuals and monotonicity in pulse strength, and checks the proved moment-envelope inequalities and power-law phase-boundary cases. Run with `python3 verify.py`; it uses only the Python standard library. Finite numerical checks are supplementary; the infinite-horizon equivalence is proved in Steps 2–4 and does not follow from finite pulse enumeration.

## Relationship to prior work

Grebenkov and Ye (2026) introduce time-dependent Robin surface reactivity, the corresponding weighted local-time reaction functional, and a five-regime adiabatic analysis for smoothly varying power-law reactivities; they give the sufficient condition that finite time-integrated reactivity permits nonreaction. The present result concerns *nonadiabatic isolated pulses*: their sharp width-dependent exposure cap, necessary-and-sufficient full-horizon series, and failure of the converse integrated-reactivity rule. These statements are not asserted in that paper.

Grebenkov (2019) develops the general spectral and probabilistic theory of boundary local time, and Bressloff (2022) studies *stochastically* switching partially reactive surfaces; both provide useful ingredients but neither supplies the deterministic-pulse sharp series criterion. Guillaume (2024) studies finite-horizon *perfectly absorbing* intermittent step barriers rather than an infinite succession of finite-rate Robin pulses. The claimed originality concerns the completed criterion and crossover in the specified model, not the known local-time representation, Neumann spectral expansion, Robin heat equation, or standard mixing estimates.

## Limitations

The proof requires a compact interval and a uniform positive free-diffusion gap between pulses; it does not classify pulses accumulating in finite time, schedules with vanishing mixing gaps, higher-dimensional domains, or reactive sites that are not well modeled by Robin killing. The universal constants in the one-pulse envelope are not asserted optimal, while the series threshold itself is exact. Rates must be finite in each pulse. The result is a mathematical statement about a standard idealized diffusion-reaction model, not direct experimental validation. Publication priority remains subject to further expert literature review, particularly more general parabolic boundary-potential and capacitary criteria.

## References

1. D. S. Grebenkov and Y. Ye, *Diffusion-controlled reactions with time-dependent surface reactivity*, arXiv:2610.23017 (first posted 2026-10-16), https://arxiv.org/abs/2610.23017 .
2. D. S. Grebenkov, *Probability distribution of the boundary local time of reflected Brownian motion in Euclidean domains*, arXiv:1909.07677; Phys. Rev. E **100**, 062110 (2019), https://arxiv.org/html/1909.07677v2 .
3. P. C. Bressloff, *Stochastically switching diffusion with partially reactive surfaces*, arXiv:2205.13985; Phys. Rev. E **106**, 034108 (2022), https://arxiv.org/abs/2205.13985 .
4. T. Guillaume, *Computation of the Survival Probability of Brownian Motion with Drift Subject to an Intermittent Step Barrier*, AppliedMath **4**, 1080–1097 (2024), https://doi.org/10.3390/appliedmath4030058 .
