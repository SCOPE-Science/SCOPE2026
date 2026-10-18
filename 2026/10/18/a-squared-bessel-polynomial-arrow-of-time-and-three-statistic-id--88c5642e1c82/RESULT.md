# A squared-Bessel polynomial arrow of time and three-statistic identification in reset heterogeneous planar diffusion

## Finding
For the canonical radial diffusion with diffusivity \(D(\rho)=D_0/\rho^2\), stochastic-calculus prescription \(\alpha\in[0,1]\), and independent Poisson returns to the origin at rate \(r>0\), the quartic radial observable \(Q_t=R_t^4/(8D_0)\) is exactly a squared-Bessel diffusion of dimension \(\delta=2-\alpha\), restarted from zero at rate \(r\). This conjugacy supplies an exact stationary two-time Laplace transform and an infinite triangular hierarchy of stationary polynomial correlations. In particular, two centered, mutually orthogonal radial polynomial observables have a strictly positive time-lag cross-correlation in one temporal direction and identically zero correlation in the other. Three population measurements—the stationary mean and normalized variance of the fourth radial power, and one positive-lag autocorrelation—determine \(\alpha\), \(r\), and \(D_0\) uniquely without prior calibration.

## Assumptions and scope
Fix \(D_0>0\), \(r>0\), \(0\le\alpha\le1\), and a lag \(t>0\). Use the radial zero-flux Markov extension at the singular origin determined by the source's radial propagator. Between resets, the backward generator on \(\rho>0\) is
\[
L_0f(\rho)=\frac{D_0}{\rho^2}f''(\rho)+\frac{(1-2\alpha)D_0}{\rho^3}f'(\rho).
\]
An independent Poisson clock at rate \(r\) sets \(R\) exactly to zero; the process immediately resumes with the same canonical radial extension. All population moments are evaluated in the unique stationary resetting regime. The result concerns radial observables, not the planar angular trajectory or fractional-memory extensions. The parameter \(\alpha=0\) gives Itô, \(\alpha=1/2\) Stratonovich, and \(\alpha=1\) Hänggi–Klimontovich conventions. Put \(\delta=2-\alpha\in[1,2]\) and \(\nu=\delta/2\in[1/2,1]\).

## Proof
**1. Exact generator conjugacy.** Define \(q=\rho^4/(8D_0)\). The chain rule yields \(L_0q=2-\alpha=\delta\) and \(L_0(q^2)=2(\delta+2)q\). More generally, for smooth \(h\), \(L_0h(q)=\delta h'(q)+2qh''(q)\). Consequently \(Q\) is the unique nonnegative squared-Bessel diffusion with generator \(\mathscr B=\delta\partial_q+2q\partial_q^2\), dimension \(\delta>0\), and instantaneous return to zero at rate \(r\). Its full reset generator is \(\mathscr G h=\mathscr B h+r(h(0)-h(q))\). The standard squared-Bessel transition identity, which can also be checked by substitution in the backward equation, is
\[
\mathbb E_q[e^{-vQ_t^0}]=(1+2vt)^{-\nu}\exp\!\left(-\frac{vq}{1+2vt}\right),\qquad v\ge0.
\]
Here superscript \(0\) means no resetting. In particular \(Q_a^0\) started from zero is \(2aG\) with \(G\) gamma distributed with shape \(\nu\), unit scale.

**2. Stationary joint law.** The age since the last reset at a stationary observation is an independent \(A\sim\operatorname{Exp}(r)\). Hence \(Q_0\overset{d}=2AG\) and its Laplace transform is
\[
\Phi(s)=r\int_0^\infty e^{-ra}(1+2as)^{-\nu}\,da,\quad s\ge0.
\]
Condition on whether the observation interval \((0,t]\) contains a reset. With no reset (probability \(e^{-rt}\)), use the squared-Bessel transition identity; if a reset occurs, the most recent reset has backward age density \(re^{-ra}\,da\) on \(0<a<t\) and the post-reset radial coordinate is independent of \(Q_0\). Therefore, for every \(u,v\ge0\) and \(t\ge0\),
\[
\boxed{\mathbb E[e^{-uQ_0-vQ_t}]
=e^{-rt}(1+2vt)^{-\nu}\Phi\!\left(u+\frac{v}{1+2vt}\right)
+\Phi(u)\int_0^t re^{-ra}(1+2va)^{-\nu}\,da.}
\]
For \(t=0\) the second integral vanishes and the first term reduces to \(\Phi(u+v)\). This is the complete bivariate Laplace law; it identifies the joint distribution on \([0,\infty)^2\).

**3. Triangular polynomial time correlations.** The stationary law has support \((0,\infty)\) and moments of every finite order,
\[
M_k:=\mathbb E[Q_0^k]=\frac{2^k k!(\nu)_k}{r^k},\quad k\in\{0,1,2,\ldots\}.
\]
Thus there is a unique monic orthogonal polynomial \(P_n\) of each degree \(n\), for this stationary measure, with \(P_0=1\). The squared-Bessel generator satisfies \(\mathscr B q^n=n(\delta+2n-2)q^{n-1}\), so its semigroup preserves degree and acts as identity on the highest coefficient. For arbitrary centered polynomial observables \(f,g\), any shared reset in \((0,t]\) destroys their correlation. Therefore
\[
\operatorname{Cov}(f(Q_0),g(Q_t))
=e^{-rt}\operatorname{Cov}_\pi(f,\exp(t\mathscr B)g).
\]
Orthogonality and degree preservation prove the exact triangular hierarchy, for every \(t\ge0\):
\[
\mathbb E[P_m(Q_0)P_n(Q_t)]=0\ (m>n\ge1),\qquad
\mathbb E[P_n(Q_0)P_n(Q_t)]=e^{-rt}\,\mathbb E[P_n(Q_0)^2]\ (n\ge1).
\]
The upper-triangular terms need not vanish, so identical individual normalized correlations do not imply reversible joint dynamics.

Explicitly put \(\mu_Q=\delta/r\), \(V_Q=\delta(\delta+4)/r^2\),
\[
P_1(q)=q-\mu_Q,\quad
P_2(q)=q^2-aq-b,\quad
a=\frac{4(\delta+2)(\delta+6)}{r(\delta+4)},\quad
b=-\frac{2\delta(\delta+2)(\delta+8)}{r^2(\delta+4)}.
\]
These polynomials are centered and orthogonal. The two conditional polynomial identities are
\[
\mathbb E_q[Q_t^0]=q+\delta t,\qquad
\mathbb E_q[(Q_t^0)^2]=q^2+(2\delta+4)tq+\delta(\delta+2)t^2.
\]
They yield the **strictly one-way lag correlation**
\[
\boxed{\begin{aligned}
\mathbb E[P_2(Q_0)P_1(Q_t)]&=0,\\
\mathbb E[P_1(Q_0)P_2(Q_t)]&=\frac{2\delta(\delta+2)(\delta+4)}{r^2}\,t e^{-rt}>0
\end{aligned}\quad(t>0).}
\]
The difference changes sign when time is reversed. This is a direct witness of failure of detailed balance of the stationary radial path, despite the common normalized autocorrelation \(e^{-rt}\) for **every** nonconstant orthogonal polynomial mode.

**4. Exactly three-quantity parameter recovery.** Let \(S_t=R_t^4=8D_0Q_t\), and suppose its stationary mean \(M=\mathbb E[S]\), normalized variance \(H=\operatorname{Var}(S)/M^2\), and normalized autocorrelation \(c_t=\operatorname{Corr}(S_0,S_t)\) at one known \(t>0\) are measured exactly. The moment formula and preceding hierarchy give
\[
M=\frac{8D_0\delta}{r},\quad H=1+\frac4\delta,\quad c_t=e^{-rt}.
\]
Consequently
\[
\boxed{\delta=\frac4{H-1},\quad
\alpha=2-\frac4{H-1},\quad
r=-\frac{\log c_t}{t},\quad
D_0=\frac{Mr}{8\delta}.}
\]
The complete range of the normalized shape diagnostic is \(3\le H\le5\): Itô gives \(H=3\), Stratonovich \(H=11/3\), and Hänggi–Klimontovich \(H=5\). All three quantities are needed for *this three-statistic inversion*: omitting \(M\), \(H\), or \(c_t\), respectively, leaves a continuous free parameter among \(D_0\), \(\alpha\), or \(r\). No universal lower bound against arbitrary alternative experimental observables is asserted.

## Verification
A standalone reproducibility script `check_bessel_reset.py` checks the two generator identities and the polynomial correlation directions symbolically; independently verifies the bivariate Laplace formula using stationary-age gamma samples and noncentral-chi-square squared-Bessel transitions for all three stochastic prescriptions, two reset-rate/lag parameter combinations each, and tests the stationary Bessel-density representation against direct reset-age integration. It also checks the analytic parameter-reconstruction formulas, with **54 assertions** overall. Run with `python check_bessel_reset.py` after installing Python with `numpy`, `scipy`, and `sympy`. Sampling and quadrature are supporting finite checks, not replacements for the derivation above.

## Relationship to prior work
Sandev, Fumeron, Henkel and Lenzi (2026) introduce exactly the planar singular-diffusion model, its stochastic-prescription dependence, the reset renewal framework, explicit one-time stationary densities, MSD and first-passage laws. Their source establishes the forward model and single-time laws; none is claimed new here. Stojkoski, Sandev, Kocarev and Pal (2021) establish autocorrelation formulas for diffusion under resetting, including exponential stationary Brownian correlations. The mere exponential decay \(e^{-rt}\) and the general reset renewal decomposition are not new. Liu et al. (2026) investigate interpretation identification in related **non-resetting** planar heterogeneous diffusion; generic interpretation identification is not new either. The contribution assessed here is the exact quartic-radius squared-Bessel reduction, its full stationary two-time law, triangular orthogonal-polynomial correlations and strict one-way cross-mode asymmetry, and parameter recovery with the stated three radial measurements. These specialized implications are not presented in the inspected relevant portions of those works; general squared-Bessel semigroups and renewal decompositions remain established tools.

## Limitations
The process uses the canonical radial entrance extension at the singular origin and genuinely Poisson resetting **to that same origin**. The analysis is not for arbitrary resetting sites, an unknown radial profile, finite-mass regularization near the origin, non-Markovian memory, interactions, finite ensembles or measurement noise. Identification is population-level and ideal; no statistical confidence intervals or conditioning/stability analysis is given. The squared-Bessel identity follows from the specific radial generator and is not a claim of novel Bessel-process theory. Some parts may be implicit in broader results on reset Markov semigroups and orthogonal polynomial bases, an acknowledged novelty risk; the present assertion is limited to this combined physically specified theorem.

## References
1. Sandev, T., Fumeron, S., Henkel, M., and Lenzi, E. K., *Heterogeneous planar diffusion with axisymmetric power-law decaying diffusion coefficient under stochastic resetting* (2026), arXiv:2609.24427v1, first publicly submitted 2026-09-21.
2. Stojkoski, V., Sandev, T., Kocarev, L., and Pal, A., *Autocorrelation functions and ergodicity in diffusion with stochastic resetting* (2021), arXiv:2107.11686.
3. Liu et al., *Identifying the interpretation in two-dimensional diffusion processes with power-law spatially dependent diffusivity*, Physical Review Research 8, 013143 (2026), DOI:10.1103/xz7y-n8w2.
4. Evans, M. R., Majumdar, S. N., and Schehr, G., *Stochastic resetting and applications*, Journal of Physics A 53, 193001 (2020), arXiv:1910.07993.
