# Critical thermal-noise crossover and angular tails in inertial active resetting

## Finding

Consider a two-dimensional inertial active Brownian particle completely reset at independent Poisson rate \(r\) to \((X,V,\Theta)=(0,0,0)\). Its stationary position and velocity are denoted by \((X_r,V_r)\). With fixed \(\gamma,v,D_\theta>0\), allow the translational velocity-noise intensity \(\kappa_r\geq0\) to depend on \(r\). Put \(a=\gamma v/2\), \(e=(1,0)\), and \(\eta_r=r\kappa_r\).

**High-reset crossover theorem.** If \(\eta_r\to\eta\in[0,\infty)\), then jointly
\[
(r^2X_r,rV_r)\ \Longrightarrow\ (Z_\eta,U_\eta)
=\left(aE^2e+\sqrt{2\eta}\int_0^E(E-s)\,dB_s,\quad 2aEe+\sqrt{2\eta}B_E\right),
\]
where \(E\sim\operatorname{Exp}(1)\) and the standard planar Brownian motion \(B\) are independent. Convergence holds for every finite polynomial moment of these vectors. Given \(E=u\), the limiting pair is Gaussian with means \((au^2e,2aue)\) and coordinatewise covariance block
\[
\eta\begin{pmatrix}2u^3/3&u^2\\u^2&2u\end{pmatrix}.
\]
At \(\eta=0\), \(Z_0=aE^2e\) lies on one directed ray and \(\Pr(e\cdot Z_0>x)=\exp(-\sqrt{x/a})\) for every \(x\geq0\). When instead \(\eta_r\to\infty\), the noise-normalized limit is
\[
\left(\frac{r^{3/2}X_r}{\sqrt{\kappa_r}},\frac{r^{1/2}V_r}{\sqrt{\kappa_r}}\right)
\Longrightarrow\left(\sqrt2\int_0^E(E-s)\,dB_s,\sqrt2 B_E\right).
\]
Thus \(\kappa_r\asymp r^{-1}\) is the critical thermal-noise scale separating directional propulsion and noise-dominated random acceleration.

For every fixed \(\eta>0\), \(Z_\eta\) has an integrable planar density, finite at every nonzero point, given by
\[
f_\eta(x)=\frac{3}{4\pi\eta}\int_0^\infty u^{-3}\exp\!\left[-u-\frac{3|x-au^2e|^2}{4\eta u^3}\right]du,\qquad x\ne0.
\]
For a unit direction \(n\) with \(z=n\cdot e\), put
\[
b=\frac3{4\eta},\quad c=1+\frac{3a^2}{4\eta},\quad d_z=\frac{3az}{2\eta},\quad
q_z=\frac{-d_z+\sqrt{d_z^2+12bc}}{2c},\quad t_z=\sqrt{q_z},
\]
\[
\Phi_z(t)=ct+bt^{-3}-d_zt^{-1},\qquad I_\eta(z)=\Phi_z(t_z),\qquad H_\eta(z)=\Phi_z''(t_z)>0.
\]
The exact directional far-field asymptotic of the **limiting** density is
\[
\boxed{\ f_\eta(\rho n)\sim
\frac{3t_z^{-3}}{4\pi\eta}\sqrt{\frac{2\pi}{H_\eta(z)}}\,
\rho^{-5/4}\exp[-I_\eta(z)\sqrt\rho]\ },\qquad \rho\to\infty.
\]
The rate \(I_\eta(z)\) is strictly decreasing in \(z\in[-1,1]\). In particular the rear direction \(n=-e\) has a strictly faster stretched-exponential decay than the forward direction \(n=e\). This tail limit is taken **after** the high-reset scaling, not uniformly over finite resetting rates.

## Assumptions and scope

For each \(r>0\), between full resets the Itô system is
\[
dX_t=V_t\,dt,\qquad dV_t=-\gamma V_t\,dt+\gamma v(\cos\Theta_t,\sin\Theta_t)\,dt+\sqrt{2\kappa_r}\,dB_t,\qquad d\Theta_t=\sqrt{2D_\theta}\,dW_t.
\]
Here \(B\) is standard planar Brownian motion, \(W\) is independent scalar Brownian motion, and both are independent of the reset clock. Every reset restores position, velocity and orientation to \((0,0,0)\); the same \(\kappa_r\) is used throughout an excursion. All fixed parameters are finite and strictly positive except \(\kappa_r\ge0\). For the case \(r\kappa_r\to\infty\), \(\kappa_r>0\) eventually. Stationary laws exist uniquely for each \(r>0\) by full renewal. The theorem is in primary mathematical-physics/stochastic-process scope (MSC2020 82C31).

## Proof

**1. Stationary renewal representation.** Sample an independent \(E\sim\operatorname{Exp}(1)\). Since the backward recurrence age of a stationary Poisson reset process has distribution \(E/r\), the stationary \((X_r,V_r)\) has the law of a fresh reset-free excursion evaluated at time \(E/r\).

**2. Rescaled exact excursion.** Variation of constants gives, at time \(t\),
\[
V_t=\gamma v\int_0^t e^{-\gamma(t-s)}n(\Theta_s)\,ds+\sqrt{2\kappa_r}\int_0^t e^{-\gamma(t-s)}\,dB_s,
\]
\[
X_t=v\int_0^t[1-e^{-\gamma(t-s)}]n(\Theta_s)\,ds+\frac{\sqrt{2\kappa_r}}\gamma\int_0^t[1-e^{-\gamma(t-s)}]dB_s,
\]
where \(n(\theta)=(\cos\theta,\sin\theta)\). Coupling Brownian motions by \(\Theta_{s/r}=\sqrt{2D_\theta/r}\,W_s\), \(dB_{s/r}=r^{-1/2}dB_s\), after multiplying velocity by \(r\) and position by \(r^2\) the deterministic kernels tend respectively to \(\gamma v\) and \(\gamma v(E-s)\); the noise multipliers become \(\sqrt{2r\kappa_r}\). Uniform convergence of the kernels and \(n(\Theta_{s/r})\to e\) on every compact rescaled time interval holds almost surely. Hence, conditional on any finite \(E=u\), the stated joint limit follows in \(L^p\) for every finite \(p\), using the Itô isometry and Gaussian moment bounds. The exponential law of \(E\) has all polynomial moments, and the kernel bounds \(|1-e^{-\gamma t}|\le\gamma t\), \(|n|=1\) give a uniform integrable polynomial bound if \(r\kappa_r\) is bounded. This upgrades conditional convergence to joint weak convergence and all polynomial moments. If \(r\kappa_r\to\infty\), division by \(\sqrt{r\kappa_r}\) removes the uniformly bounded propulsion terms and gives the indicated noise-only limit and its polynomial moments.

**3. Conditional covariance and boundary.** Itô isometry gives \(\operatorname{Var}(\sqrt{2\eta}\int_0^u(u-s)dB_s)=2\eta u^3/3\), \(\operatorname{Var}(\sqrt{2\eta}B_u)=2\eta u\), and \(\operatorname{Cov}=\eta u^2\), per coordinate. The determinant of this block is \(\eta^2u^4/3\), strictly positive for \(\eta,u>0\). For \(\eta=0\), \(e\cdot Z_0=aE^2\); its Rayleigh-type tail follows by evaluating the exponential survival function at \(\sqrt{x/a}\).

**4. Density and direction-dependent saddle.** Integrating the conditional planar Gaussian density (covariance \((2\eta u^3/3)I_2\)) against \(e^{-u}du\) gives \(f_\eta\) for \(x\ne0\). Substituting \(x=\rho n\), \(u=\sqrt\rho\,t\) yields exactly
\[
f_\eta(\rho n)=\frac3{4\pi\eta\rho}\int_0^\infty t^{-3}\exp[-\sqrt\rho\,\Phi_z(t)]\,dt.
\]
The derivative equation \(\Phi_z'(t)=0\) is \(cq^2+d_zq-3b=0\) for \(q=t^2\), and has one positive solution \(q_z\). Because \(\Phi_z\to\infty\) at both endpoints and
\[
\Phi_z''(t_z)=\frac{2ct_z^4+6b}{t_z^5}>0,
\]
this solution is the unique global nondegenerate minimizer. Standard one-dimensional Laplace asymptotics prove the stated \(\rho^{-5/4}\) prefactor and exponential rate. Finally, for \(z_1>z_2\), \(\Phi_{z_1}(t)<\Phi_{z_2}(t)\) at all \(t>0\); evaluating at the minimizer for \(z_2\) proves \(I_\eta(z_1)<I_\eta(z_2)\). No numerical extrapolation establishes these infinite-domain statements.

## Verification

Run `python3 verify.py` from the same directory. It performs deterministic positive-definiteness checks of the conditional Gaussian covariance, exact saddle identities, strict angular ordering, stationary-mean and thermal-covariance comparisons against finite-reset OU formulas, and direct Simpson-quadrature checks of the leading far-field Laplace formula. The supplied run passes 650 checks. These finite tests supplement, but do not replace, the analytic proof above.

Additional exact consistency checks: \(\mathbb E[Z_\eta]=2ae\); its covariance is \(\operatorname{diag}(20a^2+4\eta,4\eta)\), so \(\mathbb E|Z_\eta|^2=24a^2+8\eta\). In the noise-dominated limit \(\mathbb E|Z_\infty|^2=8\), matching the known high-rate mean-squared-displacement exponent and amplitude when noise is held fixed.

## Relationship to prior work

Patel and Shee (2026, arXiv:2602.21134, first submitted 24 February 2026) derive exact second/fourth scalar moments for inertial active particles under resetting, including the fixed-positive-temperature \(r^{-3}\) displacement-variance regime; their Sec. VII identifies full position-distribution analysis as unresolved. Their source supplies the physical model, not this moving-temperature joint law or angular asymptotic. Singh (2020, arXiv:2007.05576) gives exact renewal distributions for one-dimensional zero-force random acceleration under resetting: its noise-only limit is recovered here, and is not newly claimed. Kumar, Sadekar and Basu (2020, arXiv:2008.03294) study spatial densities of **overdamped** active Brownian resetting; their high-rate anisotropy differs in both power scaling and propulsion/thermal competition. The new mathematical content is the critical joint scaling with a nonzero propulsion-induced quadratic mean, coupled with the exact angular tail coefficient across the finite-noise crossover.

## Limitations

This theorem treats independent Poisson **complete** resets, zero reset velocity, fixed reset heading, finite positive inertial relaxation and rotational diffusivity, and a chosen dependence of velocity thermal forcing on resetting rate. It does not assert corresponding results for partial resets, finite-rate far-field tails, correlated thermal/rotational noise, or non-Poisson resets. The density tail is an iterated limit: first the stationary high-rate weak-noise scaling, then large radius in its limiting law. Directional monotonicity is for \(\eta>0\), not for the singular ray-supported case \(\eta=0\). Existing broader theorems on forced random-acceleration renewal mixtures could possibly subsume this result; no independent originality or correctness review is claimed.

## References

1. M. Patel and A. Shee, *Controlling inertial active Brownian motion via stochastic resetting*, arXiv:2602.21134v2 (2026), https://arxiv.org/html/2602.21134v2. Earliest public version: 2026-02-24.
2. P. Singh, *Random acceleration process under stochastic resetting*, arXiv:2007.05576 (2020), https://arxiv.org/abs/2007.05576.
3. V. Kumar, O. Sadekar and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294 (2020), https://arxiv.org/html/2008.03294v1.
4. M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic Resetting and Applications*, J. Phys. A 53 (2020) 193001, arXiv:1910.07993, https://arxiv.org/abs/1910.07993.
