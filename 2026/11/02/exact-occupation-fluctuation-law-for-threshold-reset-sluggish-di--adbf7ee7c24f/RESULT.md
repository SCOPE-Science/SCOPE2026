# Exact occupation-fluctuation law for threshold-reset sluggish diffusion

## Finding

For one-dimensional driftless diffusion with position-dependent mobility \(\kappa |x|^{-\alpha}\), instantaneously returned to \(\rho L\) after first hitting either endpoint of \((-L,L)\), the positive-side occupation fraction has an exact Gaussian central limit theorem. For every \(\alpha\ge0\), \(\kappa,L>0\), and \(0\le\rho<1\), put
\[
\vartheta_{\alpha,\rho}=1-\frac{1-\rho}{2(1-\rho^{\alpha+2})},\qquad
Q_\alpha(\rho)=\frac{3(\alpha+1)(1-\rho^2)}{4(\alpha+2)(\alpha+3)(2\alpha+3)(1-\rho^{\alpha+2})}.
\]
For \(\Xi_T=T^{-1}\int_0^T\mathbf1_{\{X_t>0\}}\,dt\),
\[
\Xi_T\longrightarrow\vartheta_{\alpha,\rho}\quad\text{a.s.},\qquad
\sqrt{T}(\Xi_T-\vartheta_{\alpha,\rho})\Longrightarrow
\mathcal N\!\left(0,\frac{L^{\alpha+2}}{\kappa}Q_\alpha(\rho)\right),
\]
and
\[
\lim_{T\to\infty}T\operatorname{Var}(\Xi_T)
=\frac{L^{\alpha+2}}{\kappa}Q_\alpha(\rho).
\]
At \(\alpha=0\), \(Q_0(\rho)=1/24\) for **every** reset point \(0\le\rho<1\), despite the nonconstant occupation mean. For every \(\alpha>0\), \(Q_\alpha(\rho)\) is strictly decreasing in \(\rho\), from
\[
Q_\alpha(0)=\frac{3(\alpha+1)}{4(\alpha+2)(\alpha+3)(2\alpha+3)}
\]
to the endpoint limit \(Q_\alpha(1-)=\frac{2}{\alpha+2}Q_\alpha(0)\). The endpoint value is a one-sided limit of interior reset positions, not a process reset at an absorbing endpoint.

## Assumptions and scope

Fix \(\alpha\ge0\), \(\kappa>0\), \(L>0\) and \(b=\rho L\in[0,L)\). Between resets the process is the **nonsticky natural-scale diffusion** with backward generator
\[
\mathcal L f(x)=\kappa |x|^{-\alpha}f''(x),\qquad -L<x<L,\ x\ne0.
\]
At \(\alpha>0\) this is specified without ambiguity by the continuous time change of Brownian motion with generator \(\kappa\partial_x^2\): if \(B_s\) is such a Brownian motion, the physical time is \(t(s)=\int_0^s|B_u|^\alpha du\). Brownian hitting \(\pm L\) completes an excursion in physical time and is followed by an instantaneous reset to \(b\), with an independent new Brownian path. The time change fixes the gluing rule at the singular point \(x=0\), excluding sticky solutions. At \(\alpha=0\) the diffusion is ordinary Brownian motion of diffusivity \(\kappa\). Occupancy at \(x=0\) has zero Lebesgue time.

All limits are for fixed parameters as \(T\to\infty\), and the initial condition is a fresh reset at \(b\). The same asymptotic variance holds for stationary initiation. No dependence on a microscopic lattice cutoff is asserted.

## Proof

**1. Regeneration, exit moments and the mean.** It suffices first to take \(L=\kappa=1\) by scaling time with \(L^{\alpha+2}/\kappa\). Let \(\tau\) be the first exit from \((-1,1)\) started at \(\rho\), and \(R=\int_0^\tau\mathbf1_{\{X_s>0\}}ds\). The time-changed Brownian realization has \(\tau\le\sigma\), with \(\sigma\) the ordinary Brownian exit time from \((-1,1)\); hence \(\tau\) and \(R\) have exponential moments in a neighborhood of zero and the successive pairs \((\tau_i,R_i)\) are iid.

The Dirichlet equation \(m''=-|x|^\alpha\), \(m(\pm1)=0\), gives
\[
\mathbb E_\rho\tau=m(\rho)=\frac{1-\rho^{\alpha+2}}{(\alpha+1)(\alpha+2)}.
\]
Write \(\vartheta=\mathbb E_\rho R/\mathbb E_\rho\tau\). The Dirichlet equation for the centered reward \(Z=R-\vartheta\tau\) gives \(g(x)=\mathbb E_x\int_0^\tau(\mathbf1_{\{X_s>0\}}-\vartheta)ds\), where \(h=(\alpha+1)(\alpha+2)\) and
\[
\begin{aligned}
g(y)&=h^{-1}\left(\tfrac12-\vartheta+\tfrac y2-(1-\vartheta)y^{\alpha+2}\right),&&0\le y\le1,\\
g(y)&=h^{-1}\left(\tfrac12-\vartheta+\tfrac y2+\vartheta(-y)^{\alpha+2}\right),&&-1\le y\le0.
\end{aligned}
\]
Both \(g\) and \(g'\) match at zero. The requirement \(g(\rho)=\mathbb E_\rho Z=0\) gives exactly \(\vartheta=\vartheta_{\alpha,\rho}\) as stated. The strong renewal-reward law proves the almost-sure occupation limit.

**2. Exact centered excursion variance.** By the Markov property, \(v(x)=\mathbb E_x[\big(\int_0^\tau f(X_s)ds\big)^2]\), where \(f=\mathbf1_{\{x>0\}}-\vartheta\), solves \(v''=-2|x|^\alpha f(x)g(x)\), \(v(\pm1)=0\). The Green kernel for \(-\partial_x^2\) with Dirichlet endpoints is
\[
G(x,y)=\frac{(1+\min\{x,y\})(1-\max\{x,y\})}{2},
\]
so \(v(\rho)=2\int_{-1}^1G(\rho,y)|y|^\alpha f(y)g(y)dy\).

To evaluate the integral, use \(\vartheta=1-\frac{1-\rho}{2(1-\rho^{\alpha+2})}\) and the monomial Green moments
\[
\begin{aligned}
I_n^+(\rho)&=\int_0^1 2G(\rho,y)y^n\,dy
=\frac{1+\rho-2\rho^{n+2}}{(n+1)(n+2)},\\
I_n^-(\rho)&=\int_{-1}^0 2G(\rho,y)|y|^n\,dy
=\frac{1-\rho}{(n+1)(n+2)}.
\end{aligned}
\]
Substitute the three powers \(n=\alpha,\alpha+1,2\alpha+2\). Direct simplification (valid for all real \(\alpha\ge0\)) yields
\[
\boxed{\mathbb E_\rho Z^2=v(\rho)=
\frac{3(1-\rho^2)}{4(\alpha+2)^2(\alpha+3)(2\alpha+3)}.}
\]
This is a centered **cycle-reward** second moment, not the long-time occupation variance. In general \(R\) and \(\tau\) are correlated and must not be treated as independent.

**3. Limit law and physical-time variance.** The regenerative reward central limit theorem applies to bounded rewards and cycles with exponential moments. Its asymptotic variance is \(\mathbb E_\rho Z^2/\mathbb E_\rho\tau=Q_\alpha(\rho)\). The final incomplete cycle contributes \(o_{\mathbb P}(\sqrt T)\); exponential cycle moments also give uniform integrability of the normalized squared deviations, implying the variance limit displayed above. Scaling time back by \(L^{\alpha+2}/\kappa\) proves the general assertions.

**4. A Brownian rigidity and its strict breakdown.** For \(\alpha=0\), the ratio \((1-\rho^2)/(1-\rho^{\alpha+2})\) is identically one. For \(\alpha>0\), set \(m=\alpha+2>2\). The derivative of \(F(\rho)=(1-\rho^2)/(1-\rho^m)\) has the sign of \(-2+m\rho^{m-2}-(m-2)\rho^m\). Its negative has derivative \(-m(m-2)\rho^{m-3}(1-\rho^2)<0\), is zero at \(\rho=1\), and is therefore positive for \(0<\rho<1\). Thus \(F\) decreases strictly. L'Hôpital's rule gives \(F(1-)=2/m\).

## Verification

The accompanying `verify.py` uses exact rational arithmetic to integrate the two Dirichlet Green-kernel moment families for seven integer sluggishness indices and six reset locations, comparing the resulting centered cycle moment and central-limit variance with the closed formulas. It also independently integrates the original piecewise Green convolution by cusp-smoothed quadrature for five noninteger indices and four locations, tests positivity and reset-location ordering, and checks the Brownian location invariance. It passes **158** tests. The analytic proof, not a finite list of tests, establishes the all-parameter theorem.

Run: `python verify.py` (Python 3.10 or later; no third-party packages).

## Relationship to prior work

Frimpong, Bresque and Roldán (arXiv:2610.21962, first public version dated 2026-10-15) formulate the spatial-threshold-reset sluggish diffusion, derive its occupation mean \(\vartheta_{\alpha,\rho}\), and identify concentration on that deterministic value, with qualitative \(T^{-1/2}\) fluctuations. The closed second-order fluctuation coefficient, its exact \(\rho\)-dependence, and Brownian-location rigidity are the contributions evaluated here. The renewal-reward central limit theorem, Brownian Green kernels, and elementary Dirichlet/Feynman–Kac moment recursions are standard prior tools rather than novel general theorems.

Den Hollander, Majumdar, Meylahn and Touchette (arXiv:1801.09909) derive positive-occupation fluctuations for **Poisson-clock** Brownian resetting on the whole line, a distinct reset protocol. Bressloff (arXiv:2009.01968) studies positive occupation of **Poisson-reset run-and-tumble particles**, not the spatial-boundary reset of a heterogeneous diffusion. Bressloff (arXiv:2205.13989) studies a different threshold, an **occupation-triggered absorption** mechanism with Poisson position resets. Those works motivate the methods but do not state the new closed coefficient for the present model.

## Limitations

This is a continuum nonsticky diffusion theorem. Finite-lattice sluggish walks with site-wise retention are not covered exactly. Resetting happens immediately upon reaching one of two symmetric spatial boundaries; no Poisson reset clock, asymmetric boundaries, drift, or random post-reset positions are included. The theorem concerns a fixed-parameter long-time Gaussian limit and variance, not the full finite-time occupation law or a complete large-deviation rate function. The literature comparison is a best-knowledge statement; broader general regenerative-diffusion results could imply the coefficient without displaying it in this form.

## References

- T. D. Frimpong, L. Bresque, E. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962 (first public version 2026-10-15), https://arxiv.org/abs/2610.21962 . Section 6.1.2 gives the deterministic threshold-reset occupation limit.
- F. den Hollander, S. N. Majumdar, J. M. Meylahn, H. Touchette, *Properties of additive functionals of Brownian motion with resetting*, arXiv:1801.09909 (2018), https://arxiv.org/abs/1801.09909 . Section IV treats the different Poisson-clock protocol.
- P. C. Bressloff, *Occupation time of a run-and-tumble particle with resetting*, arXiv:2009.01968 (2020), https://arxiv.org/abs/2009.01968 . Section IV treats Poisson-resets and ballistic orientation dynamics.
- P. C. Bressloff, *Diffusion in a partially absorbing medium with position and occupation time resetting*, arXiv:2205.13989 (2022), https://arxiv.org/abs/2205.13989 . Sections 3–4 treat occupation-dependent absorption and Poisson restarting.
