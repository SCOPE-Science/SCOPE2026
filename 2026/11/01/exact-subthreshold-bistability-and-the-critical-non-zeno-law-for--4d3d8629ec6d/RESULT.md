# Exact subthreshold bistability and the critical non-Zeno law for an exponentially reset impact oscillator

## Finding

A single-wall impact oscillator with exponentially renewed drive has a sharp restitution-dependent transition between unique periodic motion and a region of coexisting rest and sustained bouncing. In the original physical time, the same threshold separates finite-time impact accumulation from infinite-time accumulation with an exact logarithmic rate.

Consider the free-flight equation and impact rule
\[
\ddot z(s)=A e^{-s/\tau}-g,\qquad
(z,\dot z,s)\big|_{\mathrm{impact}}=(0,-\eta\dot z^-,0),
\]
where a flight begins with \(z(0)=0\) and \(\dot z(0)=v>0\), the next impact occurs at the first return to \(z=0\), and \(A,g,\tau>0\), \(0<\eta<1\). There is no upper wall. Put \(r=A/g\). If \(r\le1\), the zero-speed contact state is allowed as an absorbing resting state after impact accumulation; this does not impose any external upward kick.

For \(u>0\), define the positive function
\[
I_\eta(u)=\int_0^1[1-(1+\eta)t]e^{-ut}\,dt
=\frac{1+\eta e^{-u}-(1+\eta)(1-e^{-u})/u}{u},
\qquad I_\eta(0)=\frac{1-\eta}{2}.
\]
A positive one-impact periodic orbit of physical period \(T=\tau u\) exists **if and only if**
\[
 r=\frac{1-\eta}{2 I_\eta(u)}.
\tag{1}
\]
Each solution determines a genuine first-return flight, and no prime multi-impact periodic orbit exists.

**Exact census.** If \(0<\eta\le 1/2\), there is exactly one positive periodic orbit for \(r>1\), and none for \(r\le1\). The positive orbit, whenever it exists, attracts every initial positive launch speed.

If \(1/2<\eta<1\), \(I_\eta\) has a unique strict maximum at \(u_*(\eta)>0\). Define
\[
 r_*(\eta)=\frac{1-\eta}{2I_\eta(u_*(\eta))}<1.
\]
For \(r<r_*\), there are no positive periodic orbits. At \(r=r_*\), there is one neutral, one-sided attracting orbit (an ordinary fold). For \(r_*<r<1\), there are exactly two: the smaller-period orbit is repelling and the larger-period orbit is attracting, coexisting with the attracting resting contact. At \(r\ge1\), there is exactly one positive periodic orbit, attracting every positive launch speed. The positive orbit at \(r=1\) has strictly positive period for \(\eta>1/2\).

The fold approaches the critical point with the **sharp quadratic cusp**
\[
 u_*(1/2+\delta)=8\delta+O(\delta^2),\qquad
 r_*(1/2+\delta)=1-\frac{16}{3}\delta^2+O(\delta^3)
 \quad (\delta\downarrow0).
\tag{2}
\]

**Critical impact clock.** Precisely at \(r=1\) and \(\eta=1/2\), every strictly positive initial launch speed yields an infinite sequence of impacts whose speeds \(v_n\) and intervening flight times \(T_n\) obey
\[
\lim_{n\to\infty}\frac{n^2v_n}{g\tau}=\frac{128}{3},\qquad
\lim_{n\to\infty}\frac{nT_n}{\tau}=16,\qquad
\sum_{k=1}^{n} T_k=16\tau\log n+C+o(1).
\tag{3}
\]
Here the finite constant \(C\) depends on initial speed (and clock origin). Hence impacts cannot accumulate at finite physical time. In contrast, at \(r=1\) and \(0<\eta<1/2\), every positive launch speed decays geometrically and the total remaining flight time is finite (a Zeno sequence). This distinction concerns the ideal reset dynamics and its chosen resting continuation; it does not assert that a real particle undergoes an infinite number of resolved physical collisions.

## Assumptions and scope

The theorem applies to one isolated inertial particle on the half-line, with gravitational acceleration \(g>0\), an exponentially relaxing upward acceleration renewed after every impact, constant coefficient of restitution \(\eta\in(0,1)\), and no viscous damping or upper electrode. Only physically positive departing velocities and first positive-altitude return crossings define flights. At a contact with no positive departing velocity and \(A\le g\), remaining at rest is an explicit unilateral-contact convention. All orbit counts concern the full one-dimensional impact-return map over strictly positive kick velocities, not merely a small-oscillation approximation. Physical time is measured along the flights, not by counting impacts.

## Proof

**1. Exact flight and monotonically increasing return map.** Integrating the acceleration from a positive departing speed \(v\) gives
\[
 z(s)=vs+A\tau s-A\tau^2(1-e^{-s/\tau})-\frac g2s^2.
\]
Because \(z''(s)\) is strictly decreasing and tends to \(-g\), the particle first rises and then returns exactly once to \(z=0\), with negative incoming velocity \(w(v)\). Write \(T(v)\) for this first return. Implicit differentiation gives
\[
 T'(v)=-\frac{T(v)}{w(v)}>0.
\]
The return map is \(P(v)=-\eta w(v)\). With \(a(s)=A e^{-s/\tau}-g\), integration by parts using \(z(T)=0\) yields
\[
 w(v)=\frac1T\int_0^T s a(s)\,ds<0,
 \qquad w(v)\ge \frac12 T a(T),\quad a(T)<0.
\]
Consequently
\[
 P'(v)=\eta\left(\frac{T a(T)}{w(v)}-1\right)\ge\eta>0.
\tag{4}
\]
Thus the entire positive-impact dynamics is a strictly increasing scalar map, which cannot possess any period greater than one. Also \(P(v)=\eta v+O(1)\) as \(v\to\infty\), so large speeds decrease.

**2. Exact fixed-point equation and physicality.** Put \(u=T/\tau\) and \(V=v/(g\tau)\). The return height and incoming speed are
\[
 V=\frac u2-r+r\frac{1-e^{-u}}u,\qquad
\frac{w}{g\tau}=V+r(1-e^{-u})-u.
\]
Direct substitution into the impact map yields the exact sign identity
\[
 P(v)-v=g\tau u\left[r I_\eta(u)-\frac{1-\eta}{2}\right].
\tag{5}
\]
This proves the necessary fixed-point equation (1). Conversely, a root of (1) satisfies
\[
 v=\frac{\eta g\tau}{1+\eta}\,[u-r(1-e^{-u})].
\]
The bracket is strictly positive: after substituting (1), its positivity is equivalent to
\[
 (1+\eta)\left[1+e^{-u}-\frac{2(1-e^{-u})}{u}\right]>0,
\]
which is the strict trapezoid inequality for the strictly convex function \(e^{-s}\) on \([0,u]\). Thus each root produces a positive launch and a genuine, unique first return. The integral \(I_\eta(u)\) is strictly positive: its linear factor and the exponential weight are both decreasing, so Chebyshev's integral inequality yields
\[
 I_\eta(u)\ge \left(\int_0^1[1-(1+\eta)t]\,dt\right)
\left(\int_0^1e^{-ut}\,dt\right)>0.
\]

**3. Unimodality and global orbit count.** The derivative is
\[
 I_\eta'(u)=-\int_0^1 t[1-(1+\eta)t]e^{-ut}\,dt,
\qquad I_\eta'(0)=\frac{2\eta-1}{6}.
\]
Let \(b=1/(1+\eta)\). Split the integral at \(b\) into its strictly positive part on \((0,b)\) and the absolute value of its negative part on \((b,1)\). As \(u\) increases, the ratio of the latter to the former decreases strictly: differentiating its logarithm gives minus the difference of two exponentially weighted means of \(t\), the latter lying strictly above \(b\) and the former strictly below. This ratio tends to zero. Therefore \(I_\eta\) is strictly decreasing on \((0,\infty)\) for \(\eta\le1/2\); for \(\eta>1/2\) it strictly increases to one nondegenerate maximum and then strictly decreases. Since \(I_\eta(u)\to0\) as \(u\to\infty\), the level equation (1) has exactly the counts asserted above. At a simple root, the sign of (5) across the root determines attraction or repulsion, using monotonicity (4). At the maximum the sign is negative on both sides and tangential at the root, giving the stated semistability.

For \(r<1\), a small kick sees initial acceleration \(-g(1-r)<0\), so \(P(v)/v\to\eta\) and \(T(v)\sim2v/[g(1-r)]\) as \(v\downarrow0\). Therefore the basin below the repelling root reaches the resting contact in finite cumulative time. At \(r=1\), \(P(v)/v\to2\eta\). For \(r>1\), a zero-speed release lifts off spontaneously and the positive attracting fixed point attracts all positive speeds. The other global basins follow from (4), (5), and the large-speed bound.

**4. Cusp expansion.** Expansion under the integral gives, uniformly near \((u,\eta)=(0,1/2)\),
\[
 I_\eta(u)=\frac{1-\eta}{2}+\frac{2\eta-1}{6}u+
\frac{1-3\eta}{24}u^2+O(u^3).
\]
The implicit function theorem for \(I_\eta'(u)=0\) gives \(u_*(1/2+\delta)=8\delta+O(\delta^2)\). Substitution into (1) proves (2).

**5. Critical non-Zeno clock.** At \(r=1\), let \(u=T/\tau\). Explicit Taylor series for the departing and impact-updated dimensionless speeds at \(\eta=1/2\) are
\[
 \frac{v}{g\tau}=\frac{u^2}{6}-\frac{u^3}{24}+O(u^4),\qquad
 \frac{P(v)}{g\tau}=\frac{u^2}{6}-\frac{u^3}{16}+O(u^4).
\]
Eliminating \(u\) gives the exact leading map asymptotic
\[
 P(v)=v-\frac{\sqrt6}{8\sqrt{g\tau}}\,v^{3/2}+O(v^2).
\tag{6}
\]
Here \(I_{1/2}\) is strictly decreasing and (5) ensures \(0<P(v)<v\) for every \(v>0\); thus all positive iterates tend to zero. Set \(y_n=\sqrt{g\tau/v_n}\). Equation (6) yields \(y_{n+1}-y_n=\sqrt6/16+O(1/y_n)\), hence
\[
 y_n=\frac{\sqrt6}{16}n+O(\log n),\quad
 \frac{v_n}{g\tau}=\frac{128}{3n^2}+O\!\left(\frac{\log n}{n^3}\right),\quad
 \frac{T_n}{\tau}=\frac{16}{n}+O\!\left(\frac{\log n}{n^2}\right).
\]
Summing the summable error proves the finite-constant logarithmic law (3). For \(\eta<1/2\) at \(r=1\), \(P(v)/v\to2\eta<1\), so speeds decrease geometrically and \(T(v)\asymp\sqrt v\); impact times have a finite accumulation point. This proves the sharp boundary.

## Verification

The included standalone Python program `checks/return_map_verify.py` checks the exact flight/impact identities over multiple positive parameters, solves the fold equation and the two subthreshold period roots by bisection, verifies their opposite stability multipliers, and tests the critical map coefficient and \(n^2v_n\), \(nT_n\) scalings through 30,000 impacts. All assertions passed in the recorded execution; the universal results follow from the proof above, not finite testing. Reproduce with `python checks/return_map_verify.py` from the extraction root.

## Relationship to prior work

Saldi and Morin, *Phase-locking of hybrid oscillators* (arXiv:2608.02926v1, first posted 2026-08-03), introduce the identical exponentially relaxing free-flight law and velocity reset in their Section II.1. Their principal single-oscillator period expression concerns the long-flight regime \(T\gg\tau\) and assumes drive initially exceeds gravity to lift from rest. The exact return-map census, persistence of kicked oscillations for subgravity drive, cusp threshold, and critical impact-time law are not established in the inspected main text or its Appendix A. As \(u\to\infty\), equation (1) recovers their asymptotic \(T\sim2r\tau/(1-\eta)\), consistently with their formula (6). The present theorem concerns one uncoupled oscillator, so it does not alter their coupled-oscillator phase-locking conclusions.

Classical impact studies include Luck and Mehta, *Bouncing ball with a finite restitution: Chattering, locking, and chaos* (1993), and Naylor, Sánchez and Swift, *Chaotic dynamics of an air-damped bouncing ball* (2002). Those publications investigate bouncing against periodically moving platforms or air damping, not the precisely reset exponentially decaying upward acceleration considered here. This comparison does not establish historical uniqueness against every hybrid-impact model; uninspected supplementary materials and specialized earlier analyses remain a priority risk.

## Limitations

The result concerns an ideal, noise-free one-wall model and excludes upper-wall collisions, contact-compliance effects, velocity-dependent restitution, interactions between oscillators, and secondary forces. Continuation after a finite-time Zeno accumulation uses an explicit absorbing-contact rule and is not deduced from classical free-flight ODE evolution. The algebraic critical law describes the model's exact impact sequence; real microscale collision regularization can change its ultimate behavior. Originality is assessed against inspected accessible material, not independently audited.

## References

1. Joshua H. K. Saldi and Alexandre Morin, *Phase-locking of hybrid oscillators*, arXiv:2608.02926v1 (first public version, August 3, 2026). https://arxiv.org/abs/2608.02926
2. J. M. Luck and A. Mehta, *Bouncing ball with a finite restitution: Chattering, locking, and chaos*, Physical Review E **48** (1993), 3988–3997. https://doi.org/10.1103/PhysRevE.48.3988
3. M. A. Naylor, P. Sánchez, and M. R. Swift, *Chaotic dynamics of an air-damped bouncing ball*, Physical Review E **66** (2002), 057201. https://doi.org/10.1103/PhysRevE.66.057201
