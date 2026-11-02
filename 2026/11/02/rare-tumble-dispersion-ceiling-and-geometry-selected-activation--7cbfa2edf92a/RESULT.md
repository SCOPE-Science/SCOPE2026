# Rare-tumble dispersion ceiling and geometry-selected activation in periodic ratchets

## Finding
Consider an unwrapped one-dimensional diffusion driven by an independent symmetric two-state velocity with flip rate \(\gamma>0\):
\[
 dX_t=[-U'(X_t)+v\sigma_t]\,dt+\sqrt{2D}\,dB_t,
 \qquad \sigma_t\in\{-1,1\},\quad v,D>0.
\]
The potential \(U\) is periodic with period \(L>0\). Write \(D_{\mathrm{eff}}(\gamma,D)=\lim_{t\to\infty}\operatorname{Var}(X_t)/(2t)\) for the process started with its unique stationary distribution modulo \(L\). Define the velocity \(u(F;D)\) of a *non-switching* particle in the same potential with constant force \(F\), explicitly
\[
 u(F;D)=\frac{DL(1-e^{-FL/D})}{I(F;D)},\qquad
 I(F;D)=\int_0^L\!dx\int_0^L\!ds\,
 \exp\!\left(\frac{U(x+s)-U(x)-Fs}{D}\right).
\]
Then the exact rare-flip dispersion coefficient is
\[
 \boxed{\lim_{\gamma\downarrow0}\gamma D_{\mathrm{eff}}(\gamma,D)
 =K(D):=\frac{[u(v;D)-u(-v;D)]^2}{8}.}
\]
For every nonconstant periodic potential satisfying the assumptions and every \(D>0\), this coefficient obeys the strict, sharp ceiling
\[
 \boxed{0<K(D)<\frac{v^2}{2},\qquad
 \lim_{D\to\infty}K(D)=\frac{v^2}{2}.}
\]
For a flat potential, equality \(K(D)=v^2/2\) holds for every \(D>0\).

For the triangular ratchet with height \(h>0\), apex \(a\in(0,L)\), and potential \(U(x)=hx/a\) on \([0,a]\), \(U(x)=h(L-x)/(L-a)\) on \([a,L]\), extended periodically, impose the deterministic locking condition
\[
 0<v<\min\!\left\{\frac{h}{a},\frac{h}{L-a}\right\}.
\]
Set \(s_1=h/a\), \(s_2=h/(L-a)\), and
\[
 B_+=\frac1{s_1-v}+\frac1{s_2+v},\qquad
 B_-=\frac1{s_1+v}+\frac1{s_2-v}.
\]
The two fixed-force velocities have distinct, **sharp prefactors** as \(D\downarrow0\):
\[
 u(v;D)\sim\frac{L}{DB_+^2}e^{-(h-va)/D},\qquad
 u(-v;D)\sim-\frac{L}{DB_-^2}e^{-(h-v(L-a))/D}.
\]
Consequently, with \(K(D)\) as above,
\[
 \boxed{
 K(D)\sim\begin{cases}
 \displaystyle\frac{L^2}{8D^2B_+^4}e^{-2(h-va)/D},&a>L/2,\\[5pt]
 \displaystyle\frac{L^2}{8D^2B_-^4}e^{-2(h-v(L-a))/D},&a<L/2,\\[5pt]
 \displaystyle\frac{L^2}{2D^2B_+^4}e^{-2(h-va)/D},&a=L/2.
 \end{cases}}
\]
The selected small-temperature dispersion activation barrier is therefore \(2[h-v\max(a,L-a)]\); the symmetric apex has a separate fourfold prefactor relative to a single active branch with the same local amplitude. These asymptotics take \(\gamma\downarrow0\) **before** \(D\downarrow0\), with the geometry held fixed.

## Assumptions and scope
The first two assertions hold for any real nonconstant \(L\)-periodic \(U\in C^2\), and also for continuous, periodically piecewise \(C^2\) potentials with finitely many corners and bounded piecewise derivative. The Brownian motion and the stationary Markov flip clock are independent. For each \(\gamma,D>0\), the environment-position process on the compact periodic cell is ergodic, its unwrapped displacement has an asymptotic velocity and diffusivity, and its centered displacement satisfies a Gaussian central limit theorem. The sawtooth formulas require strictly positive slopes \(s_1-v\) and \(s_2-v\); equality at a depinning boundary is excluded. At \(D=0\) in that locked regime, with the natural sticking (Filippov) convention at the attracting cusps, every path remains confined to its original spatial period, so its asymptotic unwrapped diffusivity is zero for every positive flip rate.

## Proof
**1. Fixed-force velocity.** For fixed \(F\ne0\), the periodic Fokker–Planck equation has constant stationary probability flux \(j_F=(F-U')p_F-Dp_F'\). Multiplying by \(e^{(U-Fx)/D}\), integrating once, enforcing periodicity and normalization, and multiplying the flux by the period yields \(u(F;D)=Lj_F\) in the integral form above. This is the standard exact tilted-potential current formula; its use is not claimed as new. Since \(I(F;D)>0\), \(u(v;D)>0>u(-v;D)\).

**2. Rare-flip martingale corrector.** On \(\mathbb R/L\mathbb Z\times\{\pm1\}\) write \(b_\sigma=v\sigma-U'\) and
\[
 \mathcal L_\gamma f_\sigma=D f_\sigma''+b_\sigma f_\sigma'
 +\gamma(f_{-\sigma}-f_\sigma).
\]
Denote its invariant density by \(\pi_{\gamma,\sigma}\) (the two sector masses are each exactly \(1/2\)), and the averaged velocity by \(m_\gamma=\sum_\sigma\int b_\sigma\pi_{\gamma,\sigma}\). The unique zero-mean periodic Poisson solution \(\chi_\sigma\), up to a common additive constant, solves
\[
 \mathcal L_\gamma\chi_\sigma=m_\gamma-b_\sigma.
\]
The process \(X_t+\chi_{\sigma_t}(X_t\bmod L)-m_\gamma t\) is a martingale plus its initial constant, and the stationary bracket identity gives the **exact** formula
\[
 D_{\rm eff}=D\sum_\sigma\int_0^L \pi_{\gamma,\sigma}
 (1+\chi_\sigma')^2\,dx
 +\frac{\gamma}{2}\sum_\sigma\int_0^L\pi_{\gamma,\sigma}
 (\chi_{-\sigma}-\chi_\sigma)^2\,dx.
\]
As \(\gamma\downarrow0\), the invariant sector densities converge to \(p_\sigma/2\), where \(p_\sigma\) is the invariant density of \(D\partial_x^2+b_\sigma\partial_x\). Decompose \(\chi_\sigma=c_\sigma+\psi_\sigma\) with \(\int\psi_\sigma p_\sigma=0\). The fixed-state elliptic generators have bounded inverses on these centered subspaces; their kernel consists exactly of constants. Projecting the coupled Poisson equations onto those subspaces and using a Neumann-series perturbation at sufficiently small \(\gamma\) shows \(\sup_\sigma\|\psi_\sigma\|_{C^1}=O(1)\) and \(m_\gamma=(u(v;D)+u(-v;D))/2+O(\gamma)\). Integrating each equation against \(p_\sigma\) then gives
\[
 c_--c_+=\frac{u(-v;D)-u(v;D)}{2\gamma}+O(1).
\]
In the bracket formula, the thermal part stays \(O(1)\) and the flip part equals \([u(v;D)-u(-v;D)]^2/(8\gamma)+O(1)\). This proves the first boxed limit. Standard ergodic martingale arguments establish the asserted displacement variance rate and central limit theorem. For piecewise smooth potentials, the same bounded inverse argument uses the one-dimensional elliptic transmission conditions at the finitely many corners.

**3. Strict universal ceiling.** Let
\[
 Q_D(s)=\frac1L\int_0^L\exp\!\left(\frac{U(x+s)-U(x)}{D}\right)dx.
\]
Periodic averaging makes the mean exponent zero, so Jensen gives \(Q_D(s)\ge1\). For nonconstant \(U\), it is strictly greater than one for a positive-measure set of \(s\in(0,L)\). Consequently \(I(F;D)> L\int_0^L e^{-Fs/D}ds\) for every nonzero \(F\). Comparing with the flat-potential current formula yields \(0<u(v;D)<v\) and \(-v<u(-v;D)<0\), giving \(0<K(D)<v^2/2\). Uniform convergence \(Q_D(s)\to1\) as \(D\to\infty\) yields \(u(\pm v;D)\to\pm v\); hence the ceiling is sharp. The flat case has \(u(F;D)=F\) exactly; moreover, when \(U\) is flat the exact finite-rate law is \(D_{\mathrm{eff}}(\gamma,D)=D+v^2/(2\gamma)\), which also confirms the normalization of the rare-flip coefficient.

**4. Sharp cusp asymptotics.** In the locked sawtooth, the phase \(U(x+s)-U(x)-Fs\) in \(I(F;D)\) has its dominant corner at a potential minimum followed by the next maximum, for each \(F\in\{v,-v\}\). Linearizing this phase along the two sides of the minimum and maximum gives four one-sided exponential integrals, whose sums are \(DB_+\) at each corner for \(F=v\) and \(DB_-\) for \(F=-v\). Splitting the exact double integral into fixed neighborhoods of these corners and their complement yields by elementary one-sided Laplace estimates
\[
 I(v;D)\sim D^2B_+^2e^{(h-va)/D},\qquad
 I(-v;D)\sim D^2B_-^2e^{(h+va)/D}.
\]
The integrand on the complement is exponentially smaller because of the strict locking inequalities. Combining these with \(1-e^{-vL/D}\to1\) and \(1-e^{vL/D}\sim-e^{vL/D}\) proves the signed velocity asymptotics. Squaring their sum establishes all three regimes for \(K(D)\): the larger apex distance determines the smaller activation barrier, while at equal distances the two equally sized velocity contributions add before squaring.

**5. Zero-noise confinement.** When \(D=0\) and \(v<\min(s_1,s_2)\), both possible deterministic drifts are negative on every rising side and positive on every falling side, and the Filippov convention retains trajectories at attracting cusp minima. Therefore no switched trajectory can leave its original spatial period. Bounded displacement implies a zero variance growth rate at fixed \(\gamma>0\), without asserting any interchange of the small-noise and slow-flip limits.

## Verification
Run `python3 checker.py` from the package directory. It uses only the Python standard library and performs 93 passing diagnostic assertions: direct two-dimensional quadrature of the fixed-force current, strict ceiling checks, low-temperature comparison against both cusp prefactors, the exact flat-landscape finite-rate law, and an independent finite-grid two-state generator/Poisson-corrector calculation for the \(\gamma\downarrow0\) coefficient. In the last test the relative error in \(\gamma D_{\mathrm{eff}}/K(D)\) decreases from approximately \(0.432\) at \(\gamma=0.25\) to \(0.058\) at \(\gamma=0.03125\), at finite spatial resolution. These diagnostics do not replace the analytical uniform-in-\(\gamma\) Poisson argument or asymptotic Laplace proof.

## Relationship to prior work
Roberts and Zhen (2023) give the stationary densities, mean currents, entropy production, energetics and first-passage properties for this *same active ratchet*, but no long-time displacement diffusion law or slow-flip fluctuation coefficient. Kłosek and Cox (1999) consider the same **additive** dichotomous force with sharp periodic ratchets, but their calculations target steady currents and their main asymptotic analysis assumes driving amplitude exceeding both potential slopes, unlike the locked regime here. Spagnolo and Dubkov (2005) obtain diffusion results for *flipping the potential itself* (\(U\mapsto-U\)) in a symmetric supersymmetric landscape; they do not study the constant additive force \(\pm v\), nor the nonzero current contrast in this theorem. Reimann and collaborators (2002) provide exact fixed-tilt transport formulas; here those established formulas are used as input rather than presented as new. The assessed contribution is the combined sharp rare-flip fluctuation law, strict all-potential ceiling and geometry-selected low-temperature prefactors in a locked asymmetric ratchet.

## Limitations
The proof concerns \(\gamma\downarrow0\) with strictly positive fixed \(D\) first, and then the separate \(D\downarrow0\) asymptotic of its coefficient. It does not provide a closed form for \(D_{\mathrm{eff}}(\gamma,D)\) at arbitrary nonzero \(\gamma\) or justify interchanging the two limits. The sawtooth prefactors are pointwise in fixed \(a\); their scaling is not uniform as \(a\to L/2\). No claim is made for depinned deterministic regimes, correlated tumbling clocks, inertia or interacting particles. Unindexed prior coverage through broader switching-diffusion homogenization remains a possible publication-priority limitation. Independent mathematical verification has not been performed.

## References
1. C. Roberts and Z. Zhen, *Run-and-tumble motion in a linear ratchet potential: Analytic solution, power extraction, and first-passage properties* (2023), arXiv:2303.07880, first version 14 March 2023, https://arxiv.org/abs/2303.07880.
2. M. M. Kłosek and R. W. Cox, *Steady-state currents in sharp stochastic ratchets*, Physical Review E **60**, 3727–3735 (1999), https://doi.org/10.1103/PhysRevE.60.3727.
3. B. Spagnolo and A. Dubkov, *Diffusion in flashing periodic potentials* (2005), arXiv:cond-mat/0510170, https://arxiv.org/abs/cond-mat/0510170.
4. P. Reimann, C. Van den Broeck, H. Linke, P. Hänggi, J. M. Rubi and A. Pérez-Madrid, *Diffusion in tilted periodic potentials: Enhancement, universality, and scaling*, Physical Review E **65**, 031104 (2002), https://doi.org/10.1103/PhysRevE.65.031104.
