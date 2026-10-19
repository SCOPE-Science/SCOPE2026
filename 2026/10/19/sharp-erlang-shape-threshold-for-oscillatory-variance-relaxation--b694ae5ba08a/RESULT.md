# Sharp Erlang-shape threshold for oscillatory variance relaxation in a reset harmonic diffusion

## Finding
An Ornstein–Uhlenbeck particle reset to the trap center at independent integer-shape Erlang renewal times need not approach its stationary variance monotonically. There is an exact and complete dichotomy. For Erlang shape \(m\ge4\), its time-dependent variance crosses its stationary value infinitely often for **every** positive trap stiffness and reset-stage rate. For shape \(m=3\), infinitely many crossings occur **exactly when** the stage rate \(r\) is smaller than \(4\kappa\), where \(\kappa\) is the harmonic relaxation rate. For shapes \(m=1,2\), and for \(m=3\) with \(r\ge4\kappa\), only finitely many crossings occur. At and above the shape-three threshold, convergence is eventually from below. The infinite-crossing phase has an explicit leading exponentially damped sinusoid, whereas the eventually-one-sided phase at shape three has an explicit positive polynomial–exponential leading term.

## Assumptions and scope
Fix \(m\in\{1,2,\ldots\}\) and \(\kappa,D,r>0\). Start with \(X_0=0\) and a reset at time zero. Successive inter-reset durations are independent, each with Erlang density
\[
 f_m(t)=\frac{r^m t^{m-1}e^{-rt}}{(m-1)!},\qquad t>0.
\]
Independent of these durations, during each inter-reset excursion the position solves \(dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dW_t\); at every reset set \(X_t=0\) instantaneously. Define the variance \(V_m(t)=\operatorname{Var}(X_t)=\mathbb E[X_t^2]\), its stationary limit \(V_{m,\infty}\), and \(a=2\kappa\). All sign changes and asymptotics below refer to the deterministic function \(V_m(t)-V_{m,\infty}\) at physical observation times \(t\to\infty\), not to any phase-averaged initial renewal law.

The stationary variance is
\[
V_{m,\infty}=\frac D\kappa\left[1-\frac{r}{ma}\left(1-\left(\frac r{r+a}\right)^m\right)\right].
\]
For \(m\ge3\), set \(z_m=e^{2\pi i/m}\), \(b_m=r[1-\cos(2\pi/m)]\), \(\omega_m=r\sin(2\pi/m)\), and
\[
 C_m(a,r)=\frac{rz_m}{m}\,\frac{1-[r/(a+rz_m)]^m}{a+r(z_m-1)}.
\]
If \(m\ge4\), or if \(m=3\) and \(r<2a=4\kappa\), then \(C_m(a,r)\ne0\) and
\[
V_m(t)-V_{m,\infty}=-\frac{2D}{\kappa}e^{-b_mt}\operatorname{Re}\big(C_m(a,r)e^{i\omega_mt}\big)+o(e^{-b_mt}).
\]
In particular it assumes both strict signs infinitely many times. In the remaining shape-three regime, \(r\ge2a\),
\[
V_m(t)-V_{m,\infty}\sim-\frac D\kappa\,\frac{r^2a^3}{2(a^3+r^3)}\,t^2e^{-(a+r)t}<0.
\]
For \(m=1,2\) the relaxation is a nonzero finite combination of real exponential–polynomial terms and therefore has only finitely many zeros. This is a statement about crossing **infinitely often**, not about monotonicity at all earlier times or the exact number of finite-time crossings.

## Proof
**1. Conditional variance and renewal equation.** Let \(A_t\) be the elapsed time since the latest reset, with the initial event at \(t=0\). The OU excursion launched at zero has conditional second moment \((D/\kappa)(1-e^{-aA_t})\), and conditional mean zero. Thus
\[
 V_m(t)=\frac D\kappa[1-u_m(t)],\qquad u_m(t)=\mathbb E[e^{-aA_t}].
\]
The Erlang survival function is \(S_m(t)=e^{-rt}\sum_{j=0}^{m-1}(rt)^j/j!\). Splitting by the first reset time gives the exact renewal equation
\[
 u_m(t)=e^{-at}S_m(t)+\int_0^t f_m(s)u_m(t-s)\,ds.
\]
The Laplace transform initially defined for \(\operatorname{Re}s>0\) is
\[
 \widehat u_m(s)=\frac{[(s+a+r)^m-r^m](s+r)^m}
 {(s+a)(s+a+r)^m[(s+r)^m-r^m]}.
\tag{1}
\]
Here the apparent singularity at \(s=-a\) is removable since the numerator also vanishes. Standard positive-recurrent renewal theory applies because the waiting law is nonlattice with finite positive mean \(m/r\), so \(A_t\) converges in law to the equilibrium age having density \(rS_m(t)/m\). Consequently
\[
 u_{m,\infty}=\frac r m\int_0^\infty e^{-at}S_m(t)\,dt
 =\frac r{ma}\left[1-\left(\frac r{r+a}\right)^m\right],
\]
which proves the stationary expression and gives \(0<u_{m,\infty}<1\).

**2. All possible decay exponents.** After cancelling removable factors, (1) is rational. Its possible nonzero poles are \(s=-(a+r)\), of order at most \(m\), and
\[
 s_j=r(e^{2\pi i j/m}-1),\qquad 1\le j<m.
\]
The root at \(j=0\) corresponds to the stationary pole at \(s=0\). For \(m\ge3\) the rightmost nonreal reset-root pair is \(s_1=-b_m+i\omega_m\) and its conjugate \(s_{m-1}\); all other reset roots have strictly smaller real parts. The residue at \(s_1\) equals
\[
\operatorname{Res}_{s=s_1}\widehat u_m(s)
 =\frac{rz_m}{m}\frac{1-[r/(a+rz_m)]^m}{a+r(z_m-1)}=C_m(a,r).
\]
It is never zero: the denominator is nonzero because \(\operatorname{Im}z_m>0\). If the numerator vanished, \(a+rz_m\) would equal \(rz_j\) for some \(m\)-th root \(z_j\). Equal imaginary parts would force \(z_j=z_m\), or a root with strictly smaller real part than \(z_m\), since \(2\pi/m\in(0,2\pi/3]\) and \(z_m\) has the maximal real part among roots with that positive imaginary part. Either possibility contradicts \(a>0\). Thus the least-damped complex pair survives.

**3. Sharp competition between poles.** For \(m\ge4\), \(\cos(2\pi/m)\ge0\), so \(b_m\le r<a+r\); the pair from step 2 strictly dominates the real OU pole. For \(m=3\), \(b_3=3r/2\), so the same dominance holds exactly when \(3r/2<a+r\), equivalently \(r<2a=4\kappa\). Partial fractions of the rational function (1) therefore give \(u_m(t)-u_{m,\infty}=2e^{-b_mt}\operatorname{Re}(C_me^{i\omega_mt})+o(e^{-b_mt})\) in these regimes. Since \(C_m\ne0\) and \(\omega_m>0\), there are arbitrarily late times at which the leading sinusoid is respectively positive and negative; the little-o remainder cannot remove those alternating strict signs. Continuity forces infinitely many intervening crossings of the stationary variance.

If \(m=3\) and \(r\ge2a\), the order-three pole at \(s=-(a+r)\) is at least as far right as the oscillatory pair and has a nonzero coefficient:
\[
\lim_{s\to-(a+r)}(s+a+r)^3\widehat u_3(s)
 =\frac{r^2a^3}{a^3+r^3}>0.
\]
The inverse transform of its principal cubic pole is \(r^2a^3t^2e^{-(a+r)t}/[2(a^3+r^3)]\). At the boundary \(r=2a\) this polynomial factor still dominates any pure sinusoid at the same exponential decay. Below the boundary in the nonoscillatory region it dominates exponentially. Hence \(u_3(t)-u_{3,\infty}>0\) eventually, giving the claimed negative asymptotic for the variance difference.

For \(m=1\), there are no nonzero reset roots; for \(m=2\), the only reset root is real \(-2r\). The remaining pole is real \(-(a+r)\), including any coincidences. Their inverse transforms are real exponential–polynomial combinations. Such a nonzero combination has only finitely many zeros on \([0,\infty)\), because its slowest nonvanishing real exponent times its leading polynomial determines an eventual fixed sign (with analyticity excluding infinitely many zeros in a compact interval). It is not identically zero because \(V_m(0)=0<V_{m,\infty}\). This finishes all parameter cases.

## Verification
A standalone reproducibility program, `proofcheck.py`, checks the exact resolvent identity by two independent constructions: the renewal Laplace transform and a \(2m\)-dimensional Erlang-stage linear system. It checks stationary limits, the shape-three cubic-pole coefficient, renewal-convolution integrals versus matrix exponentiation, complex-mode noncancellation at sample parameters, and explicit alternating-crossing witnesses. The recorded run passed 730 assertions. These finite checks are corroboration; the complete parameter-domain proof uses the pole and root arguments above. Execute with `python proofcheck.py` using Python 3, SymPy, NumPy and SciPy.

## Relationship to prior work
Eule and Metzger (2015) established a general renewal-resetting propagator and derived temporal moments for free diffusion and constant advection with Gamma resetting. Their general representation is the mathematical starting point here and can recover the Laplace-transform construction; the claimed additional result is the explicit necessary-and-sufficient shape/stiffness classification of infinitely many late-time stationary-variance crossings for **harmonically confined** diffusion, including a sharp threshold at shape three and the mode amplitudes. Trajanovski et al. (2023) treat harmonic Ornstein–Uhlenbeck motion with Poissonian resets, for which the Erlang shape is one and the oscillatory regime is absent. Radice (2022) treats Gamma renewal durations with non-instantaneous returns but free inter-reset diffusion. Bodrova and Serdyukov (2023) study generalized OU confinement with exponential reset waiting times. The reusable general-renewal formulas are prior art; the sharp spectral phase diagram is the assessed contribution, subject to independent priority review.

## Limitations
The result requires **integer** Erlang shape, strictly positive trap stiffness, diffusivity and stage rate, instantaneous reset to zero, and initialization at a reset event. The existence of infinitely many sign changes does not imply a large measurable amplitude: crossing magnitudes decay exponentially. The proof does not assert the same criterion for noninteger Gamma shapes, delayed returns, nonlinear confinement, or renewal-equilibrium initialization. Earlier general renewal-response formulas may imply parts of the classification once specialized; an exhaustive independent priority determination has not been performed.

## References
1. S. Eule and J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, arXiv:1510.07876 (first public 2015-10-27). https://arxiv.org/abs/1510.07876
2. P. Trajanovski et al., *Ornstein-Uhlenbeck process and generalizations: particle's dynamics under comb constraints and stochastic resetting*, arXiv:2301.12304 (first public 2023-01-28). https://arxiv.org/abs/2301.12304
3. M. Radice, *Diffusion processes with Gamma-distributed resetting and non-instantaneous returns*, arXiv:2201.01829 (first public 2022-01-05). https://arxiv.org/abs/2201.01829
4. A. S. Bodrova and S. I. Serdyukov, *Non-equilibrium and first-passage properties of generalized Ornstein-Uhlenbeck processes under stochastic resetting*, arXiv:2310.14357 (first public 2023-10-22). https://arxiv.org/abs/2310.14357
