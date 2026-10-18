# Finite-backward-time ends of the basin separatrix in a Hurwitz polynomial flow

## Finding
For the Castañeda–Rebollo-Perdomo polynomial family, both ends of the stable separatrix of the inner saddle periodic orbit escape to infinite radius in **finite backward time**. For every \(0<\mu\le 588/6575\) and every real angular parameter \(e\), this yields a parameter-uniform, rigorous global basin classification. At each backward endpoint \(t_*\), with \(\Delta=t-t_*\downarrow0\), the radius, height, and angular phase have the asymptotic laws
\[
 r(t)=(4\mu\Delta)^{-1/4}\bigl(1+O(\Delta^{1/2})\bigr),\qquad
 z(t)=z_*-\frac{\Delta^{1/2}}{10\sqrt\mu}+O(\Delta),\qquad
 \theta(t)=\theta_*+\frac{e\Delta^{1/2}}{10\sqrt\mu}+O(\Delta).
\]
Here \(z_*\) and \(\theta_*\) are finite and may depend on the separatrix branch. The two exponents and displayed coefficients are universal. Every forward orbit converges to the origin, the inner saddle circle, or the outer attracting circle; the exact common boundary of the two open basins is a proper smooth cylinder.

## Assumptions and scope
Set \(s=x^2+y^2\), and consider the polynomial differential equations
\[
\begin{aligned}
 \dot x&=\mu x\left[(s-5)(20/21-s)-400z^2/21\right]-\left[1+e(z+s/10)\right]y,\\
 \dot y&=\mu y\left[(s-5)(20/21-s)-400z^2/21\right]+\left[1+e(z+s/10)\right]x,\\
 \dot z&=-z-s/10,
\end{aligned}
\]
with \(0<\mu\le588/6575\), \(e\in\mathbb R\). The motivating paper takes positive \(e\); permitting real \(e\) concerns the dynamics only, **not** the Hurwitz property of the Cartesian Jacobian. We assert the Hurwitz condition only on the source's established parameter region.

For positive radius \(r=\sqrt{s}\), write \(x=r\cos\theta\), \(y=r\sin\theta\). The radius–height subsystem and angular equation are exactly
\[
\dot r=-\frac{\mu r}{21}P(r,z),\quad
\dot z=-z-r^2/10,\quad
\dot\theta=1+e(z+r^2/10),\qquad
P(r,z)=21r^4-125r^2+400z^2+100.
\]
In the closed half-plane \(r\ge0\), the equilibria are \(q_0=(0,0)\), \(q_1=(1,-1/10)\), and \(q_2=(2,-2/5)\). The corresponding spatial objects are the equilibrium \(O=(0,0,0)\), the inner circle \(\gamma_1=\{r=1,z=-1/10\}\), and outer circle \(\gamma_2=\{r=2,z=-2/5\}\). For \(r>0\), \(W^s(q_1)\) is the set of points converging to \(q_1\) in positive time; its two branches are the connected components after deleting \(q_1\).

## Proof
**1. Forward completeness and equilibria.** The polynomial factorization
\[
P(r,z)=(r^2-5)(21r^2-20)+400z^2
\]
shows that \(\dot r<0\) for \(r>\sqrt5\). Thus \(r(t)\le\max\{r(0),\sqrt5\}\) for positive time. Variation of constants gives
\[
z(t)=e^{-t}z(0)-\frac1{10}\int_0^t e^{-(t-u)}r(u)^2\,du,
\]
so the height remains bounded. Angular velocity is bounded along every forward orbit; hence the full polynomial system is forward complete. The axis \(r=0\) converges to \(O\). For positive radius, substituting \(z=-r^2/10\) in \(P=0\) gives \(25(r^2-1)(r^2-4)=0\), which proves the stated equilibrium list.

**2. Hyperbolic types and planar recurrence.** The Jacobians of the planar system at \(q_1\) and \(q_2\) are respectively
\[
J_1=\begin{pmatrix}166\mu/21&80\mu/21\\-1/5&-1\end{pmatrix},\qquad
J_2=\begin{pmatrix}-344\mu/21&640\mu/21\\-2/5&-1\end{pmatrix}.
\]
They satisfy \(\det J_1=-150\mu/21<0\), and \(\det J_2=600\mu/21>0\), \(\operatorname{tr}J_2=-1-344\mu/21<0\). The origin is a sink in the half-plane; \(q_1\) is a saddle, and \(q_2\) a sink. The planar divergence is
\[
\operatorname{div}X_\mu=-1-\mu\left[5(r^2-25/14)^2+400z^2/21-6575/588\right].
\]
It is strictly negative throughout the half-plane if \(0<\mu<588/6575\); at the endpoint it is negative except at one point. Therefore its integral over any nonempty bounded planar domain is strictly negative. Green's theorem excludes both nonconstant periodic orbits and any saddle homoclinic loop. No other saddle exists, so there are no heteroclinic cycles. Every bounded forward orbit has an equilibrium as its sole omega-limit by the planar Poincaré–Bendixson classification. In particular, every forward orbit in \(r>0\) converges to exactly one of \(q_0,q_1,q_2\).

**3. The global saddle stable branches cannot remain at bounded radius backward.** Fix a nonstationary point on either branch of \(W^s(q_1)\), and reverse time \(\tau=-t\). Suppose \(r(\tau)\le\sqrt5\) throughout its maximal backward continuation. Then the equation \(dz/d\tau=z+r^2/10\), with bounded forcing, precludes finite-\(\tau\) height blow-up. If \(z\) becomes unbounded as \(\tau\to\infty\), then at some instant \(|z|>1\). For \(z>1\), \(dz/d\tau>0\); for \(z<-1\), \(dz/d\tau<-1/2\). Consequently \(|z|>1\) persists, and
\[
\frac{dr}{d\tau}=\frac{\mu r}{21}P(r,z)\ge c\mu r
\]
for an absolute \(c>0\), because \(0\le r^2\le5\) and \(400z^2>400\). This contradicts bounded radius. If instead \(z\) is bounded, the backward orbit has a nonempty compact alpha-limit in the closed half-plane. Applying the same planar recurrence classification to reversed time, its alpha-limit is an equilibrium: it cannot be either sink \(q_0\) or \(q_2\), which has no nontrivial backward-asymptotic orbit, and it cannot be \(q_1\), which would give an excluded homoclinic loop. This contradiction proves that both branches cross \(r=\sqrt5\) in backward time.

**4. Finite-time escape.** As soon as a backward branch has \(r>\sqrt5\), its backward radial derivative is positive. From the displayed factorization, it remains positive and eventually \(r\ge\sqrt{10}\), since \(dr/d\tau\) is bounded below by a positive multiple of \(r\) away from \(\sqrt5\). For \(r\ge\sqrt{10}\), the leading quartic factor gives \(dr/d\tau\ge c_\mu r^5\). Hence the backward maximal time \(\tau_*\) is finite and \(r(\tau)\uparrow\infty\) as \(\tau\uparrow\tau_*\). The same differential inequality implies \(\int^{\tau_*}r(\tau)^2\,d\tau<\infty\), since \(d\tau/dr\le C_\mu r^{-5}\) for large radius. Variation of constants in the linear height equation therefore shows that \(z\to z_*\in\mathbb R\) at that endpoint. The angular integral also converges because \(|\dot\theta|\le C(1+r^2+|z|)\), giving a finite limiting phase \(\theta_*\).

**5. Universal singular profiles.** Along each endpoint with \(\Delta=t-t_*>0\), bounded height yields \(\dot r=-\mu r^5+O(r^3)\). Set \(h=r^{-4}\), so \(\dot h=4\mu(1+O(r^{-2}))\) and \(h(t_*)=0\). Since \(h\asymp\Delta\), this improves to \(h=4\mu\Delta+O(\Delta^{3/2})\), giving the stated radius expansion. Then \(r^2=(4\mu\Delta)^{-1/2}+O(1)\), and integrating \(\dot z=-z-r^2/10\) and \(\dot\theta=1+e(z+r^2/10)\) from the finite endpoint yields the two remaining expansions with the displayed exact coefficients.

**6. Global basin boundary and convergence.** Each end of \(W^s(q_1)\) tends to unbounded radius, hence its complete stable manifold is a proper injectively immersed smooth line in \(\{r>0\}\); uniqueness of ODE trajectories makes it an embedding. The proper-arc separation theorem gives exactly two connected complementary regions in this half-plane. Every point in either region tends to one of the two sinks, and sink basins are open. Because both sink basins occur, the two regions are precisely their basins. Rotation about the invariant axis produces the proper cylinder \(W^s(\gamma_1)\cong S^1\times\mathbb R\), the exact common boundary of the basin of \(O\) and that of \(\gamma_2\). Exponential hyperbolic relaxation at either circular orbit makes \(z+r^2/10\) integrable in positive time, hence the angular phase approaches a translate of \(t\). Thus every forward orbit approaches the corresponding stationary object or phase-locked periodic orbit.

## Verification
Run `python verify.py` with Python, SymPy, NumPy, and SciPy. The script symbolically verifies the reduced divergence identity, the factorization, and the two equilibrium Jacobian determinants and traces. As noncertifying stress tests it integrates both stable eigen-directions backward for \(\mu=0.001,0.02,0.07,0.089\) and confirms that each reaches radius 100. These computations are finite checks; steps 1–6 above are the proof of the statements for all parameters and both full branches.

## Relationship to prior work
Castañeda and Rebollo-Perdomo, *A family of Hurwitz polynomial vector fields in \(\mathbb R^3\) having non-constant periodic orbits*, arXiv:2610.09176v1 (public October 6, 2026), introduce exactly this polynomial family. Their Lemma 1 proves the two hyperbolic circles and excludes other periodic orbits throughout the displayed \(\mu\) range. Their Section 4 explicitly **describes** the stable separatrix splitting the two basins for the illustrated parameter \(\mu=0.001\). Those conclusions and the algebraic reduction are prior work. The additional result proved here is the parameter-uniform global forward basin theorem together with the finite-backward-time existence and sharp three-coordinate asymptotics of **both entire saddle stable-manifold ends**. Standard Bendixson–Dulac, Poincaré–Bendixson, and proper planar-arc separation facts are used without claims of novelty.

## Limitations
The flow is not asserted Hurwitz for all \(\mu,e\); only the source establishes that property on a smaller open parameter region. The theorem does not give closed forms for the branch-specific endpoint heights, phases, or blow-up times, nor any uniform estimates as \(\mu\to0\). The quoted \(O(\cdot)\) constants may depend on \(\mu,e\) and the branch. All stated blow-ups are **backward**; no forward trajectory escapes. The secondary source search does not exclude a previously published equivalent proof. This result has not received independent scientific validation.

## References
1. Álvaro Castañeda and Salomón Rebollo-Perdomo, *A family of Hurwitz polynomial vector fields in \(\mathbb R^3\) having non-constant periodic orbits*, arXiv:2610.09176v1 (2026), https://arxiv.org/html/2610.09176v1, especially Lemma 1, its proof, and Section 4.
2. Poincaré–Bendixson theorem, classical planar omega-limit classification.
3. Bendixson–Dulac criterion and Green's theorem, classical planar integral obstruction.
4. Proper planar-arc separation theorem, a consequence of the Jordan–Schoenflies theory.
