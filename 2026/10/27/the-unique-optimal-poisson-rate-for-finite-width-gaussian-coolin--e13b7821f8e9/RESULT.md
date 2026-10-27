# The unique optimal Poisson rate for finite-width Gaussian cooling cycles

## Finding
For a harmonically confined Brownian particle reset to a **nondegenerate Gaussian position law**, the Poisson-reset rate maximizing the cycle-averaged symmetric endpoint Kullback–Leibler divergence has a **unique global optimum at every cooling contrast**. In particular, for weak cooling the optimal resetting rate approaches \(2\sqrt2\lambda\), with an explicit first correction. This sharpens a thermodynamically motivated finite-width regularization beyond qualitative low/high reset-frequency behavior; the observable is expressly an endpoint-divergence proxy, not the full entropy production of arbitrary reset machinery.

## Assumptions and scope
Fix \(D,\lambda>0\) and \(0<\sigma_0^2<D/\lambda\). Between renewal events \(dX_t=-\lambda X_t\,dt+\sqrt{2D}\,dB_t\). At independently occurring Poisson events of rate \(r>0\), completely replace the particle position with a fresh sample from \(P_0=\mathcal N(0,\sigma_0^2)\). The reset variable is independent of the Brownian increments and waiting times. The inter-reset equilibrium variance is \(\sigma_\infty^2=D/\lambda\). Conditional on an interval of duration \(t\), its ending distribution is \(P_t=\mathcal N(0,v_t)\), where \(v_t=\sigma_\infty^2[1-ce^{-ut}]\), \(c=1-\sigma_0^2/\sigma_\infty^2\in(0,1)\), and \(u=2\lambda\).

The single-cycle observable is the *Jeffreys divergence* \(\Phi(t)=\mathrm{KL}(P_t\Vert P_0)+\mathrm{KL}(P_0\Vert P_t)\). The time-averaged reward rate is exactly \(\mathcal J(r)=r\mathbb E[\Phi(T)]\) for iid cycle intervals \(T\sim\mathrm{Exp}(r)\). It is not identified with total stochastic entropy production; even when endpoint KL bounds dissipation, implementation-dependent and trajectory-level terms may be additional.

## Proof
**Step 1: exact cycle divergence.** Set \(a=1-c\), \(s(t)=1-ce^{-ut}\). The Gaussian KL identity gives
\[
\Phi(t)=\frac12\left[\frac{s(t)}a+\frac a{s(t)}-2\right]
=\frac{c^2}{2a}\frac{(1-e^{-ut})^2}{1-ce^{-ut}}.
\]
Put \(z=r/u\) and \(h_c(t)=(1-e^{-t})^2/(1-ce^{-t})\). Integration against the exponential waiting law and the geometric expansion (absolutely convergent because \(c<1\)) give
\[
\mathcal J(r)=\frac{uc^2}{2a}z^2\int_0^\infty e^{-zt}h_c(t)\,dt
=\frac{uc^2}{a}z^2\sum_{n=0}^\infty\frac{c^n}{(z+n)(z+n+1)(z+n+2)}.
\]
This formula is valid for each \(r>0\), and its derivative may be taken under the integral.

**Step 2: a single curvature crossing.** Put \(x=e^{-t}\). Direct differentiation yields
\[
h_c''(t)=\frac{xP_c(x)}{(1-cx)^3},\qquad
P_c(x)=c-2+(4-2c+c^2)x-3cx^2+c^2x^3.
\]
The derivative \(P_c'(x)=4-2c+c^2-6cx+3c^2x^2\) is strictly positive on \([0,1]\): it decreases throughout this interval and its minimum is \(P_c'(1)=4(1-c)^2>0\). Since \(P_c(0)=c-2<0\) and \(P_c(1)=2(1-c)^2>0\), there is exactly one \(t_c>0\) where \(h_c''\) switches from positive on \((0,t_c)\) to negative on \((t_c,\infty)\).

**Step 3: exactly one optimum.** Two integrations by parts (using \(h_c(0)=h_c'(0)=0\), exponential decay of \(h_c'\), and \(h_c(\infty)=1\)) give
\[
\frac{d\mathcal J}{dz}=-\frac{uc^2}{2a}\int_0^\infty t e^{-zt}h_c''(t)\,dt.
\]
Let \(A(z)\) integrate its positive integrand contribution over \((0,t_c)\), and \(B(z)\) the absolute value of its negative contribution over \((t_c,\infty)\). Both are strictly positive. The derivative of \(\log[A(z)/B(z)]\) is the difference between the tilted means of \(t\) over the second and first intervals, and hence is strictly positive. Therefore \(A(z)-B(z)\) can vanish **at most once**. At \(z\downarrow0\), \(\mathcal J\sim uc^2z/(2a)\), so \(\mathcal J'>0\) for small \(z\); at \(z\to\infty\), \(\mathcal J\sim uc^2/(a^2z)\), so \(\mathcal J'<0\) for large \(z\). Hence it has exactly one critical point and this point is the unique global maximum.

**Step 4: weak-cooling expansion.** Expand the convergent series uniformly for \(z\) in a neighborhood of \(\sqrt2\) as
\[
\frac{2a}{uc^2}\mathcal J=J_0(z)+cJ_1(z)+O(c^2),\quad
J_0(z)=\frac{2z}{(z+1)(z+2)},\quad
J_1(z)=\frac{2z^2}{(z+1)(z+2)(z+3)}.
\]
The unique maximum of \(J_0\) is at \(z_0=\sqrt2\), with strictly negative second derivative there. Implicit differentiation of the stationary equation gives
\[
 z_*(c)=z_0-c\frac{J_1'(z_0)}{J_0''(z_0)}+O(c^2)
=\sqrt2+\frac{24+27\sqrt2}{98}c+O(c^2).
\]
Since \(J_0(\sqrt2)=2(3-2\sqrt2)\), \(\max_r\mathcal J(r)=u(3-2\sqrt2)c^2+O(c^3)\). The global uniqueness just proved identifies this local implicit branch with the global optimizer.

**Step 5: both rate extremes.** For \(r\downarrow0\), the duration diverges in probability and \(\Phi(t)\to c^2/(2a)\); bounded convergence gives \(\mathcal J(r)\sim rc^2/(2a)\). For \(r\to\infty\), Taylor expansion of the exact Gaussian expression gives \(\Phi(t)=c^2u^2t^2/(2a^2)+O(t^3)\). Exponential moments yield \(\mathcal J(r)\sim c^2u^2/(a^2r)\). Here and throughout, the asymptotics are for fixed \(D,\lambda,c\), except in the explicitly stated separate weak-cooling limit.

## Verification
The standalone program `check.py` integrates the positive-kernel formula independently of its convergent partial-fraction series across 25 \((c,z)\) configurations, calculates the critical point via the signed-curvature integral at five cooling contrasts, and tests the weak-cooling optimizer coefficient at three small contrasts. Its assertions pass. Finite numerical tests corroborate, but do not establish, global uniqueness or infinite-series identities, which are proved above.

## Relationship to prior work
Farago, arXiv:2605.28445v1, develops the harmonic Gaussian-endpoint KL cycle framework, including the symmetric-KL formula, and reports qualitative low- and high-frequency behavior and teleportation-limit expressions. Its source analysis does not state or prove uniqueness of the full finite-width Poisson optimizer, or its weak-cooling expansion. The present theorem relies on the established endpoint-KL motivation while treating a precisely specified nondegenerate Gaussian-redraw reset and retaining the **exact** finite-width term which cannot be dropped in the fast-reset limit.

Mori, Olsen, and Krishnamurthy, arXiv:2211.15372v1, analyze random-location resetting and total thermodynamic entropy production. Their steady-state symmetrized divergence between the **stationary mixture** and the reset law is not this work's cycle-average divergence between a **conditional Gaussian after time \(T\)** and the reset law. In general the two quantities differ by nonlinear mixing. General finite-time resetting work and its optimization are also studied in Phys. Rev. Research 6, 033343 (2024), for a distinct cost functional and physical reset protocol.

## Limitations
This is a theorem about a symmetric **endpoint probability divergence per unit time**, not a theorem about the total entropy produced by a physical reset device or a universal optimal engine. It assumes a centered Gaussian redraw, time-homogeneous Poisson resets, an exactly harmonic potential, and strict finite positive reset variance smaller than equilibrium variance. The degenerate zero-width reset, a reset distribution warmer than equilibrium, finite-duration experimental reset machinery, and non-Poisson renewal clocks are not covered. Broader general optimization principles could imply the unimodality argument after a suitable reduction; independent originality checking remains advisable.

## References
1. O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression*, arXiv:2605.28445v1 (public 2026-05-27).
2. F. Mori, K. Stølevik Olsen, and S. Krishnamurthy, *Entropy production of resetting processes*, arXiv:2211.15372v1 (2022).
3. K. Olsen et al., *Thermodynamic cost of finite-time stochastic resetting*, Phys. Rev. Research **6**, 033343 (2024), DOI:10.1103/PhysRevResearch.6.033343.
