# Finite backward escape and endpoint profiles of a saddle basin boundary

## Finding

For the Castañeda–Rebollo-Perdomo polynomial flow, at every \(0<\mu\le588/6575\) and every real angular coefficient \(e\), both complete branches of the planar stable separatrix of the inner periodic orbit have a **finite backward endpoint** \(t_*\) at which \(r\to\infty\). For each branch, put \(\Delta=t-t_*\); then as \(\Delta\downarrow0\),
\[
 r(t)=(4\mu\Delta)^{-1/4}(1+O(\Delta^{1/2})),\qquad
 z(t)=z_*-\frac{\Delta^{1/2}}{10\sqrt\mu}+O(\Delta),\qquad
 \theta(t)=\theta_*+\frac{e\Delta^{1/2}}{10\sqrt\mu}+O(\Delta).
\]
Here \(\theta\) is a continuous real lift along the trajectory, and \(z_*\) and \(\theta_*\) are finite. In particular the whole stable manifold of the inner periodic orbit is properly embedded as a smooth cylinder, with these endpoint profiles along its two radial–height branches. It is the common boundary of the origin's and outer circle's basins. The global forward classification into the two basins and the saddle stable set is background, not a separate originality claim.

## Assumptions and scope

Put \(s=x^2+y^2\) and
\[
B(s,z)=(s-5)(20/21-s)-400z^2/21.
\]
The equations are
\[
\begin{aligned}
 \dot x&=\mu xB(s,z)-[1+e(z+s/10)]y,\\
 \dot y&=\mu yB(s,z)+[1+e(z+s/10)]x,\\
 \dot z&=-z-s/10.
\end{aligned}
\]
Writing \(r=\sqrt{s}>0\), the exact equations on the punctured cylindrical chart are
\[
 \dot r=-\frac{\mu r}{21}P(r,z),\quad
 \dot z=-z-r^2/10,\quad \dot\theta=1-e\dot z,\qquad
 P(r,z)=(r^2-5)(21r^2-20)+400z^2.
\]
The closed half-plane \(r\ge0\) is invariant. The equilibria in that half-plane are \(q_0=(0,0)\), \(q_1=(1,-1/10)\), \(q_2=(2,-2/5)\). The latter two lift to period-\(2\pi\) orbits \(\gamma_1,\gamma_2\). A branch means a component of \(W^s(q_1)\setminus\{q_1\}\). The claims concern the dynamics, not pointwise Hurwitzness for all real \(e\) or over the full \(\mu\) interval.

## Proof

**Planar preliminaries.** The factorization shows \(\dot r<0\) for \(r>\sqrt5\). Thus \(r\) is bounded in forward time, and variation of constants for \(\dot z=-z-r^2/10\) bounds \(z\); the Cartesian flow is forward complete. On the axis it approaches the origin. Substitution of \(z=-r^2/10\) in \(P\) gives \(25(r^2-1)(r^2-4)\). At \(q_1,q_2\) the planar determinants are respectively \(-150\mu/21\) and \(600\mu/21\); at \(q_2\) the trace is \(-1-344\mu/21\). Hence \(q_1\) is a saddle, \(q_2\) a sink, and the linearization at \(q_0\), with eigenvalues \(-100\mu/21,-1\), is also a sink.

The planar divergence is
\[
-1-\mu\bigl[5(r^2-25/14)^2+400z^2/21-6575/588\bigr].
\]
It is strictly negative in the half-plane except possibly at an isolated point when \(\mu=588/6575\). Green's theorem excludes periodic orbits and saddle homoclinic loops: the bounded interior of any such loop has strictly negative divergence integral, whereas the normal flux across a trajectory is zero. The hyperbolic saddle corner of a homoclinic loop does not affect the flux identity. There is no other saddle in the half-plane; the invariant axis admits no nonconstant compact recurrent set. The Poincaré–Bendixson alternatives therefore imply that any bounded forward or backward semiorbit in the half-plane has a single equilibrium as its limit in the bounded time direction. In particular all forward orbits have this classification in planar projection.

**Both branches enter the large-radius region backward.** Use reversed time \(\tau=-t\) and start at any nonstationary point of a stable branch. Suppose \(r\le\sqrt5\) throughout the maximal backward continuation. The equation \(dz/d\tau=z+r^2/10\) prevents finite-time height blow-up under this bound, so the continuation is infinite. If \(z\) is unbounded, then \(|z|>1\) at some time and remains so: above 1 the derivative is positive and below \(-1\) it is less than \(-1/2\). On \(0\le r\le\sqrt5\) with \(|z|>1\), \(P\) is bounded below by a positive constant, since \(21r^4-125r^2+100\ge100-125^2/84>-400\). Thus \(dr/d\tau\ge c\mu r\) for an absolute \(c>0\), contradicting the bound. Otherwise both coordinates are bounded, so the backward limit is a single equilibrium by the planar preliminaries. A nonstationary trajectory cannot be backward-asymptotic to either forward sink. Backward convergence to \(q_1\) would produce an excluded saddle homoclinic loop. This proves that each branch attains \(r>\sqrt5\) backward.

**Finite backward time and finite height.** For \(r>\sqrt5\) the reversed radius is strictly increasing. It reaches \(\sqrt{10}\) because its derivative has a positive lower bound on every compact radial interval above \(\sqrt5\); a maximal trajectory cannot end at finite time while \(r\) is bounded, since bounded forcing then keeps \(z\) finite. Once \(r\ge\sqrt{10}\), the factorization gives \(dr/d\tau\ge(19\mu/42)r^5\). Integrating \(d\tau/dr\le(42/19\mu)r^{-5}\) shows that \(r\to\infty\) at a finite endpoint and that \(\int^{\tau_*}r^2\,d\tau<\infty\). The linear height formula then gives \(z\to z_*\in\mathbb R\). The exact identity \(\theta+ez-t=\mathrm{constant}\) along lifted trajectories gives a finite \(\theta_*\).

**Profiles.** Since \(z\) remains bounded, \(h=r^{-4}\) satisfies \(\dot h=4\mu+O(r^{-2})\) and \(h\to0\) at \(t_*\). First \(h\asymp\Delta\), and then integration gives \(h=4\mu\Delta+O(\Delta^{3/2})\). It follows that \(r^2=(4\mu\Delta)^{-1/2}+O(1)\). Integration of the height equation now gives the coefficient \(-1/(10\sqrt\mu)\) of \(\Delta^{1/2}\); the angle follows from \(\theta-\theta_*=\Delta-e(z-z_*)\). If \(e=0\) the latter is exactly \(\Delta\).

**Geometry of the two ends.** The global stable manifold of the planar saddle is a smooth injectively immersed line. Since \(r\to\infty\) along both of its ends, this line is proper and embedded. The open half-plane is homeomorphic to the plane; one-point compactification sends the proper line to a Jordan curve. Thus the complementary regions are two and have the line as their common boundary. The forward alternatives above and openness of the two sink basins identify the regions with those basins (both occur already at positive radius). Rotating the line gives a proper embedded cylinder \(W^s(\gamma_1)\) in space. Every point on the axis tends to the origin and is interior to its basin, so no axis point is added to the common boundary.

## Verification

The proof is analytic over the entire stated parameter range. The algebraic identities follow by differentiation and substitution. The accompanying `verify.py` records symbolic checks and finite radius-100 integration tests at four parameter values. Those tests are corroboration, not evidence of a finite endpoint at infinite radius or of the stated profiles; these follow from the reversed-time inequalities and integrations above.

## Relationship to prior work

Castañeda and Rebollo-Perdomo [1, Lemma 1] give the two hyperbolic cycles and exclude additional periodic orbits over the displayed interval. Their numerical illustration [1, Section 4] describes the saddle stable separatrix as the basin separator. A power-Dulac theorem [2] already gives boundedness, global forward classification and phase convergence over the larger interval \(0<\mu\le1764/15625\) for positive angular parameter. The planar classification does not depend on that parameter; the angle identity extends phase convergence to real \(e\). Neither the general forward classification nor this real-parameter extension is claimed here as new. The endpoint theorem uses backward continuation of both full branches and the large-radius estimate, and provides the radius, height and phase expansions at the two backward endpoints. The small-\(\mu\) separatrix graph in [3] is a different asymptotic result on bounded windows of rescaled height, not an infinite-radius time profile.

## Limitations

The estimates are for fixed \(\mu,e\) and a fixed branch, without a uniform error bound as \(\mu\to0\). The endpoint heights, phases and times are not given in closed form. The upper bound on \(\mu\) is not asserted to be dynamically sharp. No forward blow-up or extension of a Cartesian Hurwitz theorem is claimed.

## References

1. Á. Castañeda and S. Rebollo-Perdomo, *A family of Hurwitz polynomial vector fields in \(\mathbb R^3\) having non-constant periodic orbits*, [arXiv:2610.09176v1](https://arxiv.org/abs/2610.09176v1), Lemma 1 and Section 4.
2. [*An optimal power-Dulac certificate extends the global two-cycle regime of a polynomial three-flow*](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-an-optimal-power-dulac-certificate-extends-the-global-two-cycle--50f7b9fa53d4/RESULT.md), Finding and Proof §§1–3.
3. [*Gaussian high-altitude basin boundary and asymmetric correction*](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-gaussian-high-altitude-basin-boundary-and-asymmetric-correction--03361c09e75e/RESULT.md), Finding and Assumptions and scope.
