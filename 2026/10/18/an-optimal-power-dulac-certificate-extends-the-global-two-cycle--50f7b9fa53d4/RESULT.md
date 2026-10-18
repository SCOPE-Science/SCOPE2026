# An optimal power-Dulac certificate extends the global two-cycle regime of a polynomial three-flow

## Finding
For the polynomial vector field of Castañeda and Rebollo-Perdomo [1], the global two-cycle classification remains valid on the larger exact interval
\[
0<\mu\le \mu_*:=\frac{1764}{15625}=0.112896.
\]
The source proves its corresponding no-extra-cycles assertion only for \(0<\mu\le588/6575\) using ordinary planar divergence. The new certificate enlarges that interval by \(26.24\%\), and is **optimal within the full family of power Dulac weights** on the squared-radius half-plane. No dynamical sharpness beyond \(\mu_*\) is claimed.

Specifically, all forward solutions are bounded. Exactly two nonconstant periodic orbits exist: the saddle circle \(\gamma_1:\ x^2+y^2=1,\ z=-1/10\) and the attracting circle \(\gamma_2:\ x^2+y^2=4,\ z=-2/5\), both of minimal period \(2\pi\). Every forward orbit tends either to the origin, to \(\gamma_1\) along its stable manifold, or to \(\gamma_2\). In either nonzero case, its continuously lifted angle satisfies \(\theta(t)-t\to\theta_\infty\in\mathbb R\). Thus convergence to a circle has a finite asymptotic phase shift.

## Assumptions and scope
Take any \(\mu\in(0,\mu_*]\), any \(\varepsilon>0\), and any initial \((x,y,z)\in\mathbb R^3\). Put \(u=x^2+y^2\) and
\[
B(u,z)=(u-5)\left(\frac{20}{21}-u\right)-\frac{400}{21}z^2.
\]
The equations of [1], including the angular coupling, are
\[
\dot x=\mu xB(u,z)-\left[1+\varepsilon\left(z+\frac u{10}\right)\right]y,\quad
\dot y=\mu yB(u,z)+\left[1+\varepsilon\left(z+\frac u{10}\right)\right]x,\quad
\dot z=-z-\frac u{10}.
\]
On the invariant half-plane \(u>0\) they reduce, exactly, to
\[
\dot u=P(u,z)=2\mu u B(u,z),\qquad
\dot z=Q(u,z)=-z-u/10,\qquad
\dot\theta=1+\varepsilon(z+u/10).
\]
The axis \(u=0\) is invariant, and its forward solutions approach the origin. The statement concerns dynamical behavior, **not** pointwise Hurwitzness of the Cartesian Jacobian throughout the enlarged parameter interval.

## Proof
**1. Forward completeness and equilibria.** For \(u\ge5\), \(B(u,z)\le0\), so \(u(t)\le\max\{u(0),5\}\). The linear equation for \(z\) then implies boundedness. In Cartesian coordinates this also bounds \(x,y\), and the smooth polynomial vector field is forward complete. In the interior half-plane, \(Q=0\) forces \(z=-u/10\); the exact identity
\[
B(u,-u/10)=-\frac{25}{21}(u-1)(u-4)
\]
shows there are precisely two equilibria \(q_1=(1,-1/10)\) and \(q_2=(4,-2/5)\). Their reduced Jacobians are
\[
J_1=\begin{pmatrix}166\mu/21&160\mu/21\\-1/10&-1\end{pmatrix},\qquad
J_2=\begin{pmatrix}-344\mu/21&2560\mu/21\\-1/10&-1\end{pmatrix}.
\]
The determinants are respectively \(-150\mu/21<0\) and \(600\mu/21>0\), and \(\operatorname{tr}J_2=-1-344\mu/21<0\). Hence \(q_1\) is a hyperbolic saddle and \(q_2\) a hyperbolic sink. The boundary equilibrium \(q_0=(0,0)\) is also a sink in the closed half-plane, with linear eigenvalues \(-200\mu/21\) and \(-1\). Each \(q_i\) for \(i=1,2\) lifts to the stated circle: at the equilibrium \(z+u/10=0\), so \(\dot\theta=1\).

**2. A weighted Bendixson–Dulac identity.** On the simply connected half-plane \(H=(0,\infty)\times\mathbb R\), the positive smooth Dulac weight \(D(u,z)=1/u\) gives
\[
\begin{aligned}
\operatorname{div}(D(P,Q))
&=\partial_u(2\mu B)+\partial_z\left(\frac{-z-u/10}{u}\right)\\
&=\frac{250\mu}{21}-4\mu u-\frac1u.
\end{aligned}
\]
For \(u>0\), the last two terms obey \(4\mu u+u^{-1}\ge4\sqrt\mu\). Thus the weighted divergence is everywhere nonpositive whenever \(\frac{250}{21}\mu\le4\sqrt\mu\), or precisely \(0<\mu\le1764/15625\). At the endpoint,
\[
\operatorname{div}(D(P,Q))=-\frac{(84u-125)^2}{15625u}.
\]
It vanishes only on one vertical line, and its integral over any planar region of positive area is strictly negative. Bendixson–Dulac excludes all nonconstant periodic orbits in \(H\). The same Green-theorem argument excludes any homoclinic polygon bounding a planar region in \(H\); here the only saddle is \(q_1\), so every possible saddle polycycle would be homoclinic.

**3. Full forward classification and asymptotic phase.** All projected positive-half-plane orbits have nonempty compact omega-limit sets. If an omega-limit set meets the boundary \(u=0\), it must contain the boundary equilibrium \(q_0\); because \(q_0\) is a sink, the whole orbit converges to \(q_0\). Otherwise its omega-limit set is compactly contained in \(H\). The Poincaré–Bendixson alternative for a bounded planar orbit with finitely many equilibria then forces a single equilibrium unless the omega-limit set contains a periodic orbit or a connecting polycycle. Both alternatives are excluded by step 2 and the source/sink types of \(q_1,q_2\). Therefore every projected orbit approaches exactly one of \(q_0,q_1,q_2\). The set of data converging to \(q_1\) is exactly the stable set of the saddle; the other two attraction basins are nonempty and open. Hyperbolicity gives exponential approach near the destination along every converging orbit. Consequently \(z(t)+u(t)/10\) is integrable on \([0,\infty)\); integrating the exact angular equation yields the finite phase shift \(\theta_\infty=\theta(0)+\varepsilon\int_0^\infty(z(s)+u(s)/10)\,ds\) whenever \(u(0)>0\). No additional periodic orbit of the three-flow is possible because its planar projection would be a periodic orbit or a fixed point, with only the two fixed-point circles above.

**4. Optimality among power weights (certificate sharpness only).** For any \(\alpha\in\mathbb R\), apply the weight \(D_\alpha=u^{-\alpha}\). Direct differentiation yields
\[
\operatorname{div}(D_\alpha(P,Q))
=u^{-\alpha}\left(2\mu\left[(1-\alpha)B+u\,\partial_uB\right]-1\right).
\]
If \(\alpha>1\), the bracket has a positive coefficient of \(z^2\), so this divergence becomes positive for sufficiently large \(|z|\) and cannot be globally nonpositive. If \(\alpha\le1\), the maximum over \(z\) is at \(z=0\). The remaining concave quadratic in \(u\) reaches its maximum at
\[
u_\alpha=\frac{125(2-\alpha)}{42(3-\alpha)}>0,
\quad M(\alpha)=\frac{15625}{1764}\frac{(2-\alpha)^2}{3-\alpha}-\frac{100}{21}(1-\alpha).
\]
Its derivative is
\[
M'(\alpha)=-\frac{25(17\alpha-76)(17\alpha-26)}{1764(\alpha-3)^2}<0\qquad(\alpha\le1).
\]
Thus \(M(\alpha)\ge M(1)=15625/3528\), and global nonpositive divergence for a power weight is possible only when \(2\mu M(1)\le1\), precisely \(\mu\le1764/15625\). Equality is achieved by \(\alpha=1\) as in step 2. This proves **only** optimality of the method within the stated weight family, not a sharp dynamical bifurcation threshold.

## Verification
The standalone `verify.py` reproduces the exact divergence, squared-radius reduction, endpoint perfect-square identity, stationary-type Jacobians, maximizer of the power-weight envelope, and its derivative factorization using rational symbolic arithmetic. It also integrates nine representative projected trajectories with \(\mu=0.09,0.10,0.112\); these finite experiments illustrate, but do not establish, the global theorem. Run `python verify.py` with Python 3, SymPy, NumPy and SciPy. No finite sample is used to exclude additional recurrent sets.

## Relationship to prior work
Castañeda and Rebollo-Perdomo [1, Lemma 1, pp. 4 and 8–9] identify the same two periodic circles and prove absence of others for \(\mu\le588/6575\), using *unweighted* divergence in \((r,z)\). The present result shares those circles and their local types; it does **not** claim rediscovery. Its new statement is the rigorously enlarged interval and the power-family-optimal weighted certificate, with a global classification valid there. Established planar Bendixson–Dulac and Poincaré–Bendixson theorems supply general methods; neither alone supplies the parameter-specific cutoff. An earlier global classification on the smaller published parameter interval likewise does not imply the extension.

## Limitations
The number \(\mu_*\) is sharp for globally nonpositive divergence among weights \(u^{-\alpha}\), not proven sharp for actual existence of extra cycles. The enlarged interval need not preserve the global Hurwitz-Jacobian condition, which is established in [1] only for a much smaller positive parameter neighborhood. The result is limited to the exact polynomial family, not its perturbations. Full independent scholarly verification has not been performed.

## References
[1] Álvaro Castañeda and Salomón Rebollo-Perdomo, *A family of Hurwitz polynomial vector fields in \(\mathbb R^3\) having non-constant periodic orbits*, arXiv:2610.09176v1, first posted October 6, 2026, especially Lemma 1 and its proof, pp. 4, 8–9; https://arxiv.org/abs/2610.09176.
