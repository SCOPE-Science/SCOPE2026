# A weighted-Dulac global phase portrait for a three-dimensional Hurwitz counterexample family

## Finding
Consider the polynomial vector field specified below. Set
\[
\mu_{\mathrm D}=\frac{1764}{15625}=0.112896.
\]
For every \(0<\mu\leq\mu_{\mathrm D}\) and every real \(e\), every forward solution is global and bounded. Exactly three distinct asymptotic outcomes are possible: convergence to the origin, orbital convergence with an asymptotic phase to the circle \(\gamma_1\) of radius one, and orbital convergence with an asymptotic phase to the circle \(\gamma_2\) of radius two. The first circle is a saddle periodic orbit, the second an attracting periodic orbit, and the origin an attracting equilibrium. The basin of the saddle circle is a codimension-one immersed stable manifold; outside that zero-volume set, each orbit tends to one of the two attracting invariant sets.

Every invariant Borel probability measure is a convex combination of the point mass at the origin and the uniform-time probabilities on the two circles. These three measures are exactly the ergodic invariant probabilities; only the origin measure and radius-two circle measure are physical (have a positive-volume time-average basin).

The number \(\mu_{\mathrm D}\) is the largest parameter for which **any radial power multiplier** \(B(r)=r^\alpha\), with \(\alpha\in\mathbb R\), makes the divergence of the weighted planar field nonpositive everywhere in the open half-plane \(r>0\). This optimality concerns this specified multiplier family, **not** the actual onset of further limit cycles. Relative to the previously proved unweighted-divergence range \(0<\mu\leq588/6575\), the certified parameter upper endpoint increases by exactly the factor \(789/625\).

## Assumptions and scope
Let \(x,y,z\in\mathbb R\), \(s=x^2+y^2\), \(0<\mu\leq1764/15625\), and \(e\in\mathbb R\). Define
\[
\begin{aligned}
\dot x&=-\frac{\mu x}{21}\bigl(21s^2-125s+400z^2+100\bigr)-\bigl(1+e(z+s/10)\bigr)y,\\
\dot y&=-\frac{\mu y}{21}\bigl(21s^2-125s+400z^2+100\bigr)+\bigl(1+e(z+s/10)\bigr)x,\\
\dot z&=-z-s/10.
\end{aligned}
\]
The invariant circles (each of least period \(2\pi\)) are
\[
\gamma_1=\{x^2+y^2=1,z=-1/10\},\qquad
\gamma_2=\{x^2+y^2=4,z=-2/5\}.
\]
Each circle is equipped with the normalized arclength/time measure. An invariant Borel probability means invariance under the forward semiflow at every nonnegative time; forward completeness holds for all starting states. An asymptotic phase means that for each orbit approaching \(\gamma_j\) there exists \(\theta_\infty\) such that the orbit differs by a vector tending exponentially to zero from \((j\cos(t+\theta_\infty),j\sin(t+\theta_\infty),-j^2/10)\). The two circles and the origin were already identified and locally classified in the motivating work; their existence and local stability are not claimed as new.

## Proof
**Bounded global flow and reduction.** Set \(r=\sqrt{x^2+y^2}\), and for \(r>0\) write \(x+iy=re^{i\theta}\). Then
\[
\begin{aligned}
\dot r&=-\frac{\mu r}{21}P(r,z),\\
\dot z&=-z-r^2/10,\\
\dot\theta&=1+e(z+r^2/10),
\end{aligned}\qquad
P(r,z)=21r^4-125r^2+400z^2+100.
\]
The axis \(r=0\) is invariant and supports only the scalar equation \(\dot z=-z\). Because
\[
P(r,z)=(r^2-5)(21r^2-20)+400z^2\geq0\quad\text{when }r^2\geq5,
\]
we have \(r(t)^2\leq R^2:=\max\{5,r(0)^2\}\). The explicit variation-of-constants formula
\[
z(t)=e^{-t}z(0)-\frac1{10}\int_0^t e^{-(t-u)}r(u)^2\,du
\]
gives \(|z(t)|\leq |z(0)|+R^2/10\). The polynomial vector field therefore remains in a compact set for every finite positive time and has global bounded forward trajectories.

**Weighted Bendixson exclusion.** On the simply connected half-plane \(r>0\), put \(B(r)=r^{-1}\) and let \(X=(\dot r,\dot z)\). Direct differentiation gives the exact square identity
\[
\operatorname{div}(BX)
=\frac1r\left[
\frac{15625\mu-1764}{1764}
-4\mu\left(r^2-\frac{125}{84}\right)^2\right].
\]
For \(0<\mu\leq\mu_{\mathrm D}\), this is nonpositive and strictly negative almost everywhere in \(r>0\), including at equality where its zero locus is a single vertical line. Green's theorem forbids a closed periodic trajectory or a homoclinic Jordan loop: the vector field is tangent to the enclosing piecewise-smooth boundary, forcing zero flux, contrary to the strictly negative area integral. The \(r>0\) reduced field has exactly two critical points, \(q_1=(1,-1/10)\) and \(q_2=(2,-2/5)\); the axis contains only \(q_0=(0,0)\). Indeed, at an equilibrium \(z=-r^2/10\), and
\[
P(r,-r^2/10)=25(r^2-1)(r^2-4).
\]
The reduced Jacobians at \(q_0,q_1,q_2\) have, respectively, diagonal eigenvalues \((-100\mu/21,-1)\), determinant \(-50\mu/7\) at \(q_1\), and trace \(-1-344\mu/21\) with determinant \(200\mu/7\) at \(q_2\). Thus \(q_0,q_2\) are sinks and \(q_1\) is a hyperbolic saddle.

**Exhaustive omega limits.** Every reduced forward orbit has nonempty compact connected omega limit by boundedness. If it includes a sink, that sink attracts the whole forward trajectory. Otherwise, a nontrivial omega limit would, by the planar Poincaré–Bendixson classification with finitely many hyperbolic equilibria, contain either a periodic orbit or a separatrix circuit. A circuit in this reduced field can only be a homoclinic loop at the unique saddle: the other two equilibria are sinks. Both options are excluded by the weighted divergence. Hence every reduced forward orbit converges to exactly one of \(q_0,q_1,q_2\). Hyperbolicity yields exponential convergence after the orbit enters a local stable manifold. For \(q_1,q_2\), it follows that
\[
\int_0^\infty\left|z(t)+r(t)^2/10\right|\,dt<\infty.
\]
The identity \(\frac{d}{dt}(\theta+ez)=1\) gives the exact formula \(\theta(t)=t+\theta(0)+e(z(0)-z(t))\), and hence the asserted phase-selected convergence. This angular identity is not claimed as a new contribution. The three-dimensional origin is a hyperbolic sink, the two circles have the types stated by the reduced Jacobian and one neutral flow-direction multiplier.

**Statistical and basin consequences.** No point outside the origin or the two circles is positively recurrent: its forward orbit tends to one of those invariant sets and cannot return arbitrarily close to its distinct starting point. Poincaré recurrence for a finite invariant Borel probability therefore puts full measure on their union. A circle with unit-speed rotation has exactly one invariant probability, its uniform measure; the origin has its point mass. The invariant-probability simplex and its three extreme ergodic points follow. The stable-manifold theorem gives the radius-one circle a two-dimensional immersed stable manifold in three-dimensional phase space (one stable reduced direction plus phase), which has zero three-dimensional Lebesgue measure. Both attracting basins are nonempty open sets, so precisely their two associated ergodic measures are physical.

**Optimality within radial powers.** For arbitrary real \(\alpha\), a second exact differentiation yields
\[
\frac{\operatorname{div}(r^\alpha X)}{r^\alpha}
=-1-\frac{\mu}{21}\left[
21(\alpha+5)r^4-125(\alpha+3)r^2
+400(\alpha+1)z^2+100(\alpha+1)
\right].
\]
If \(\alpha<-1\), this expression becomes positive for sufficiently large \(|z|\) with fixed \(r>0\). If \(\alpha\geq-1\), the bracket is minimized over \(r>0,z\in\mathbb R\) at \(z=0\) (or arbitrary \(z\) if \(\alpha=-1\)) and \(r^2=125(\alpha+3)/[42(\alpha+5)]\), with minimum
\[
Q_{\min}(\alpha)
=-\frac{25(289\alpha^2+1734\alpha+3945)}{84(\alpha+5)}.
\]
Its derivative is
\[
Q'_{\min}(\alpha)
=-\frac{25(17\alpha+35)(17\alpha+135)}{84(\alpha+5)^2}<0
\quad (\alpha\geq-1).
\]
Thus the globally largest possible allowable \(\mu\) within \(r^\alpha\) is attained at \(\alpha=-1\), where the sign condition becomes exactly \(\mu\leq1764/15625\). This proves the restricted optimality statement and makes no assertion about what happens at larger \(\mu\).

## Verification
The symbolic reconstruction of the planar reduction, inverse-radius divergence, squared form, all three reduced Jacobians, the power-weight identity, and the power-weight minimization is reproducible by running \(\texttt{python3 verify.py}\) with Python 3 and SymPy. The verification program uses exact symbolic expressions and rational coefficients; it does not certify the global Poincaré–Bendixson argument, which is established above analytically. The endpoint quotient is exactly \(789/625\). The code is supplementary; finite checks are not substituted for the global proof.

## Relationship to prior work
Castañeda and Rebollo-Perdomo (2026, arXiv:2610.09176v1), Lemma 1, prove the existence and local stability of the two periodic circles and exclude additional periodic orbits via the **unweighted** planar divergence for \(\mu\leq588/6575\). Its Section 4 depicts the basin-separating saddle stable manifold at the particular parameter \(\mu=1/1000\); such qualitative separation at that example is not claimed here as new. The present result supplies an explicitly larger uniform no-cycle domain, its optimality within radial power multipliers, an all-initial-state convergence theorem throughout that domain, and a full invariant-probability classification. The use of the classical Bendixson–Dulac and Poincaré–Bendixson theorems is not itself novel.

An earlier analysis of this same polynomial family gives a parameter-conjugacy and an exact angular isochron formula but does not provide the weighted-Dulac parameter endpoint or this global invariant-measure classification. The authors' earlier nilpotent-Jacobian work studies a different class; general global convergence results for other polynomial systems do not specialize to this three-dimensional vector field without additional hypotheses.

## Limitations
The bound \(1764/15625\) is **not** claimed to be the actual threshold for extra periodic orbits or any global bifurcation. It is sharp only among the radial power Dulac multipliers \(r^\alpha\) required to have globally nonpositive weighted divergence on \(r>0\). The conclusions about full global dynamics do not imply that every parameter in the stated range yields an everywhere-Hurwitz Cartesian Jacobian: the previously established global-Hurwitz property applies on a much smaller parameter set. No independent scientific audit has been performed, and historic priority remains subject to unindexed literature.

## References
1. Á. Castañeda and S. Rebollo-Perdomo, *A family of Hurwitz polynomial vector fields in R3 having non-constant periodic orbits*, arXiv:2610.09176v1 (first public version 2026-10-06), especially Lemma 1 and Section 4. https://arxiv.org/abs/2610.09176
2. Á. Castañeda and S. Rebollo-Perdomo, *Discrete and continuous dynamics of real 3-dimensional nilpotent polynomial vector fields*, arXiv:2209.06986 (2022); different nilpotent-Jacobian family. https://arxiv.org/abs/2209.06986
3. Classical Bendixson–Dulac criterion, Poincaré–Bendixson theorem, stable-manifold theorem, and Poincaré recurrence theorem, used in their standard forms.
