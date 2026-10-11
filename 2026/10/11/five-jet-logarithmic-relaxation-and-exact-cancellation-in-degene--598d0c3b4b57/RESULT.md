# Five-jet logarithmic relaxation and exact cancellation in degenerate Liénard damping

## Finding
For the restoring-force oscillator
\[
\dot x=v,\qquad \dot v=-g(x)v-f(x),
\]
all non-equilibrium trajectories converge to the origin. Outside its one-dimensional global strong-stable set, the inverse-square displacement has a **two-term asymptotic expansion with a finite remainder limit**:
\[
\boxed{x(t)^{-2}=\frac{2c}{a}t+\Gamma\log t+C+o(1),\qquad
\Gamma=\frac{d}{c}-\frac{b}{a}+\frac{3c}{a^2}.}
\]
Here \(C\in\mathbb R\) depends on the initial state and the origin of time; the slope and logarithmic coefficient do not. Every slow trajectory has an eventually constant sign of \(x\). Every nonzero trajectory in the strong-stable set instead satisfies
\[x(t)=K e^{-at}(1+o(1)),\qquad v(t)=-aK e^{-at}(1+o(1)),\qquad K\ne0.\]
The coefficient \(\Gamma\) vanishes if and only if \(b=ad/c+3c/a\). Thus its sign may be positive, zero, or negative while the origin remains globally attracting.

For the polynomial subclass \(f(x)=cx^3+dx^5\), \(g(x)=a+bx^2\), with \(a,c>0\), \(b,d\ge0\), the zero-logarithm relation is exactly the condition for the **cubic slow graph** \(v=-(c/a)x^3\) to be invariant. On this relation, every orbit obeys the exact deviation law
\[
W(t)=W(0)\exp\!\left(-at-\frac{ad}{c}\int_0^t x(s)^2\,ds\right),\quad W=v+\frac{c}{a}x^3.
\]
Consequently this graph is transversely exponentially attracting. The existence of algebraic invariant curves in tuned Liénard equations is established in earlier integrability literature; the new assertion concerns the **global, initial-data-independent two-term relaxation coefficient**, including its identification with this invariance defect.

## Assumptions and scope
Assume \(f,g\in C^\infty(\mathbb R)\), \(f(-x)=-f(x)\), \(g(-x)=g(x)\), and the following, for every real \(x\):
\[
g(x)\ge g_0>0,\qquad xf(x)>0\text{ for }x\ne0,\qquad
U(x):=\int_0^x f(s)\,ds\longrightarrow+\infty\text{ as }|x|\to\infty.
\]
Locally at zero, for constants \(a,c>0\) and arbitrary real \(b,d\),
\[
f(x)=cx^3+dx^5+O(x^7),\qquad g(x)=a+bx^2+O(x^4).
\]
All time limits are \(t\to+\infty\), and every finite real initial condition \((x(0),v(0))\) is admitted. The global strong-stable set is the union of the backward flow images of the local one-dimensional stable manifold tangent at zero to \((1,-a)\). The invariant-cubic-graph statement is restricted to the displayed polynomial subfamily; no exact polynomial graph is asserted for general \(f,g\).

## Proof
**Global convergence.** With \(E(x,v)=v^2/2+U(x)\), differentiation along a solution gives \(\dot E=-g(x)v^2\le -g_0v^2\). The coercive energy bounds both state variables and gives forward completeness. Any forward limit set lies in \(v=0\); a whole orbit stays there only if \(f(x)=0\), which by the sign hypothesis means \(x=0\). LaSalle's invariance principle, or the same omega-limit argument, yields \((x(t),v(t))\to(0,0)\). The linearization has eigenvalues \(0,-a\).

**Slow-graph jet.** Smooth center-manifold theory supplies a local smooth graph \(v=h(x)\), tangent to \(v=0\). Since the vector field is odd under \((x,v)\mapsto(-x,-v)\), its finite Taylor jet can be chosen odd. Invariance is the scalar identity
\[
h'(x)h(x)+g(x)h(x)+f(x)=0.
\]
Insert \(h(x)=A x^3+B x^5+O(x^7)\). The cubic and quintic coefficients yield
\[
A=-\frac ca,\qquad B=-\frac da+\frac{bc}{a^2}-\frac{3c^2}{a^3}.
\]
Write \(\alpha=c/a>0\) and \(\beta=B\). Then on the center graph
\[\dot z=-\alpha z^3+\beta z^5+O(z^7).\]
The remainder order is justified by the smoothness and odd parity assumptions, not inferred from a finite numerical experiment.

**Reduction of every orbit to a center orbit.** Once a trajectory has entered the graph's domain, put \(w=v-h(x)\). The invariance identity gives the **exact** differential equation
\[\dot w=-[g(x)+h'(x)]w.\]
As \(x\to0\), its bracket tends to \(a>0\), hence \(w(t)=O(e^{-\eta t})\) for some \(\eta>0\). Therefore \(\dot x=h(x)+w(t)\). An exponentially tracked solution \(z(t)\) of \(\dot z=h(z)\) exists on a tail: for sufficiently large \(T\), solve
\[
\delta(t)=-\int_t^\infty\left[h(x(s))-h(x(s)-\delta(s))+w(s)\right]ds,
\]
in an exponentially weighted sup-norm ball. Because \(h'(x)=O(x^2)\), the integral map is a contraction when \(T\) is large. Set \(z=x-\delta\). Then \(\dot z=h(z)\), and \(x(t)-z(t)=O(e^{-\eta' t})\) for some \(\eta'>0\). The zero tracked center orbit singles out the local strong-stable curve; its nonzero trajectories have the stated simple-eigenvalue exponential asymptotic by the smooth stable manifold theorem. Every other orbit tracks a nonzero \(z\), whose sign is fixed by uniqueness and whose magnitude approaches zero algebraically.

**Exact second asymptotic order.** On a nonzero center orbit let \(u=z^{-2}\). For large time,
\[
\dot u=2\alpha-\frac{2\beta}{u}+O(u^{-2}).
\]
First \(u=2\alpha t+O(\log t)\). Consequently
\[
\frac1u=\frac1{2\alpha t}+O\!\left(\frac{\log t}{t^2}\right),
\]
and the derivative of \(u-2\alpha t+(\beta/\alpha)\log t\) is \(O((\log t)/t^2)\), which is absolutely integrable. It therefore tends to a finite constant. As \(z\asymp t^{-1/2}\) and \(x-z\) is exponentially small, \(x^{-2}-z^{-2}\to0\). Since \(-\beta/\alpha=d/c-b/a+3c/a^2\), the displayed expansion follows with a true \(C+o(1)\) remainder. It implies the first-passage-time correction for a slow orbit reaching small \(\varepsilon>0\):
\[
T_\varepsilon=\frac{a}{2c}\varepsilon^{-2}-\frac{a\Gamma}{2c}\log(\varepsilon^{-2})+O(1),
\]
for crossing levels after its eventual monotone regime; the \(O(1)\) depends on the initial condition.

**Algebraic-curve comparison.** In the polynomial subclass set \(W=v+(c/a)x^3\). Direct differentiation, without any asymptotic approximation, gives
\[
\dot W=-\left[a+\left(b-\frac{3c}{a}\right)x^2\right]W
+\left(\frac{bc}{a}-\frac{3c^2}{a^2}-d\right)x^5.
\]
The last term vanishes identically precisely at \(b=ad/c+3c/a\), equivalent to \(\Gamma=0\). On that locus the remaining linear equation integrates to the stated exact transverse formula. For \(W=0\), \(\dot x=-(c/a)x^3\), which integrates explicitly to \(x(t)=x(0)/\sqrt{1+2(c/a)x(0)^2t}\) for all \(t\ge0\).

## Verification
Symbolic expansion of the center invariance equation fixes \(A\), \(B\), and \(\Gamma\) exactly. The associated reproducibility script `lienard_critical_checker.py` checks the polynomial graph deviation identity, the iff cancellation condition, and positive/zero/negative coefficient examples. A direct numerical check of the exact polynomial system, for instance \((a,c,d)=(1,1,0)\) and \(b=0,3,6\), exhibits approximate logarithmic slopes \(3,0,-3\) as predicted. These numerical observations are supplementary, not substitutes for the smooth invariant-manifold and integral estimates above.

## Relationship to prior work
Llibre and Valls prove global asymptotic stability for much broader polynomial planar systems, including generalized Liénard equations, in their 2023 primary-MSC-34C05 paper; their theorem does not specify this degenerate two-term rate. Bárta develops the slow/fast alternative and polynomial decay estimates for degenerate potential oscillators, with velocity-dependent damping, not the present state-dependent-damping logarithmic coefficient. Demina studies Liouvillian integrability and invariant algebraic curves for general polynomial Liénard systems. In particular the general identity connecting a polynomial graph \(v=q(x)\) to \(f(x)=-q(x)[g(x)+q'(x)]\) already implies the cubic invariant graph on the tuned surface; that graph is not proposed here as an independently novel integrability result. The difference is the exact global inverse-square law with its three-term coefficient, applicable also to smooth nonpolynomial systems and to coefficients *off* the algebraically invariant surface.

## Limitations
The theorem treats one-degree-of-freedom autonomous oscillators with positive damping, sign-restoring force, coercive potential, and odd/even smooth symmetry. It does not apply without these hypotheses, does not classify limit cycles when damping changes sign, and does not give an elementary formula for the initial-data constant \(C\). The explicitly solvable cubic graph covers only a tuned polynomial subfamily. The claimed novelty of the asymptotic law is assessed relative to the inspected literature and is not an independence certificate.

## References
1. J. Llibre and C. Valls, *A weakened Markus–Yamabe condition for planar polynomial differential systems of degree \((1,n)\)*, Proceedings of the Edinburgh Mathematical Society 66 (2023), 1110–1118. DOI: 10.1017/S0013091523000615. First verified public appearance: 2023-10-17.
2. T. Bárta, *Exact rate of decay for solutions to damped second order ODE's with a degenerate potential*, Evolution Equations and Control Theory (2018). DOI: 10.3934/eect.2018025.
3. M. V. Demina, *Integrability and solvability of polynomial Liénard differential systems*, arXiv:2110.14306 (first posted 2021), later Studies in Applied Mathematics 150 (2023), 755–817.
4. M. V. Demina and D. I. Sinelshchikov, *Darboux first integrals and linearizability of quadratic–quintic Duffing–van der Pol oscillators*, Journal of Geometry and Physics 165 (2021), 104215. DOI: 10.1016/j.geomphys.2021.104215.
