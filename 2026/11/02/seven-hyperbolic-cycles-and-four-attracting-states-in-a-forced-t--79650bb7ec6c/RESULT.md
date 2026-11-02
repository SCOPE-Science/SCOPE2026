# Seven hyperbolic cycles and four attracting states in a forced three-zone oscillator

## Finding
For the scalar forced oscillator
\[
\dot x=-9x+\frac{21}{2}\operatorname{sat}(x)+\frac{181363}{100000}\sin t,
\qquad
\operatorname{sat}(x)=\begin{cases}-1&x<-1,\\x&-1\le x\le1,\\1&x>1,\end{cases}
\]
there are **at least seven distinct hyperbolic forcing-periodic solutions**, with **four exponentially attracting** and **three repelling**. In particular, there are four disjoint open attraction basins, and this seven-orbit configuration persists under sufficiently small forcing-periodic, continuous piecewise-\(C^1\) perturbations preserving transversality of the switching crossings. The theorem concerns period \(2\pi\) and does not assert that seven is the total number of periodic solutions.

The three nonsymmetric representatives at time zero lie in the exact rational intervals
\[
J_1=(-0.569205,-0.569203),\quad
J_2=(-0.556761,-0.556759),\quad
J_3=(-0.555157,-0.555155).
\]
They are respectively attracting, repelling, and attracting. The unique half-period antisymmetric solution lies in \((-0.579022471,-0.579022470)\) and is repelling. Each nonsymmetric solution has a distinct symmetry partner with the **same** Floquet multiplier. Valid bounds for the multipliers are
\[
0.99<P'_1<1,\qquad 1.5<P'_2<1.53,\qquad
0.33<P'_3<0.34,\qquad 1.003<P'_{\rm c}<1.006.
\]

## Assumptions and scope
The forcing amplitude and both slopes are the displayed exact rationals. Initial data are arbitrary real numbers; we make existence and stability assertions only for the seven indicated periodic solutions. The source paper [1, Section 4 and Appendix A.3] proves the transverse switching itineraries on the larger shooting intervals \([-0.571,-0.567]\), \([-0.55677,-0.55675]\), and \([-0.55517,-0.55514]\). We use those independently published itinerary results as premises; all new narrower displacement and Floquet inequalities are reproduced by the standalone directed-interval calculation supplied here.

## Proof
Write \(P(y)=x(2\pi;y)\) and \(D(y)=P(y)-y\). For a segment governed by \(\dot x=ax+b+\mu\sin t\), its exact flow is
\[
\Phi_{a,b}(t;t_0,x_0)=e^{a(t-t_0)}x_0+\frac b a\bigl(e^{a(t-t_0)}-1\bigr)
+\frac{\mu}{a^2+1}\bigl[-a\sin t-\cos t
-e^{a(t-t_0)}(-a\sin t_0-\cos t_0)\bigr],
\]
with \(\mu=181363/100000\). In the middle zone \((a,b)=(3/2,0)\); in the upper and lower zones they are \((-9,21/2)\) and \((-9,-21/2)\). Since the vector field is continuous, a transverse crossing has no nontrivial saltation factor. If \(E(y)\) is the total time spent outside \([-1,1]\) over one forcing period, then
\[
P'(y)=\exp\left(3\pi-\frac{21}{2}E(y)\right).
\]
The neutral multiplier threshold is therefore exactly \(E_*=2\pi/7\).

Directed interval evaluation of the exact segment flow at the six rational endpoints shows \(D(\inf J_1)>0>D(\sup J_1)\), \(D(\inf J_2)<0<D(\sup J_2)\), and \(D(\inf J_3)>0>D(\sup J_3)\). Explicitly the endpoint displacements, in the same order, lie respectively in
\[
(8.92,8.94)10^{-9},\ (-8.16,-8.14)10^{-9},\quad
(-4.16,-4.13)10^{-7},\ (6.19,6.21)10^{-7},\quad
(6.72,6.75)10^{-7},\ (-6.62,-6.59)10^{-7}.
\]
Each endpoint itinerary is a special case of the transverse intervals verified in [1].

Scalar order gives \(\partial_yx(t;y)>0\). Differentiating the transverse crossing equations shows that the duration of the lower exterior excursion is strictly decreasing in \(y\), whereas that of the upper exterior excursion is increasing. Consequently the **entire** exterior residence time on each small interval is enclosed using only endpoint excursion durations. The directed interval calculation gives
\[
\begin{aligned}
0.8983943&<E(J_1)<0.8984349,\\
0.8575513&<E(J_2)<0.8582154,\\
1.0022125&<E(J_3)<1.0024041.
\end{aligned}
\]
Comparison with \(2\pi/7\) establishes \(P'<1\) on \(J_1,J_3\) and \(P'>1\) on \(J_2\). The intermediate-value theorem supplies a fixed point in each interval, and strict monotonicity of \(D\) there proves uniqueness within each and hyperbolicity, with the multiplier bounds stated above.

Set \(H(y)=x(\pi;y)\) and \(Q(y)=-H(y)\). The identity \(F(t+\pi,-x)=-F(t,x)\) gives \(P=Q\circ Q\). The map \(Q\) is strictly decreasing, hence has a unique fixed point, which is the half-period antisymmetric solution. Evaluating its half-period equation \(H(y)+y=0\) encloses it in \((-0.579022471,-0.579022470)\). The lower exterior visit of this central solution has duration \(s<0.448589954<\pi/7\); antisymmetry gives total exterior residence \(E=2s<2\pi/7\), hence its multiplier exceeds one. Each of the three other fixed points lies to the right of this central fixed point, and therefore has a distinct partner \(Q(y)\) to its left. By the chain rule \(P'(Q(y))=Q'(y)Q'(Q(y))=P'(y)\), so both partners inherit the corresponding strict stability classification. This yields four attracting and three repelling cycles among seven distinct hyperbolic ones.

Finally, on each transverse itinerary the return map depends continuously and differentiably on the initial value and on sufficiently small piecewise-\(C^1\), forcing-periodic perturbations. Since all seven return multipliers avoid one, the implicit-function theorem continues each fixed point uniquely locally, preserving its stability and the separation of the seven orbits.

## Verification
Run `python verify_hyperbolic.py` alongside `centers.json` with Python 3 and `mpmath` 1.3 or newer. The code evaluates the exact affine flows using outward-rounded interval arithmetic, verifies signed endpoint return displacements, isolates transverse switching times and their velocity signs, bounds the exterior residence duration on whole rational shooting intervals, and checks the central half-period multiplier. It reports `PASS` only after every inequality is strict. The event-order premise for the broader shooting intervals is taken from [1, Appendix A.3], not inferred from finite sampling.

## Relationship to prior work
Hu and Chen [1] establish at least seven **isolated** periodic solutions and rigorous sign brackets; they also bound the central antisymmetric orbit. Isolation and endpoint sign changes do not establish that the six nonsymmetric periodic solutions are hyperbolic. The new content is strict multiplier control for all six, leading to a complete hyperbolic stability split and persistence of a seven-cycle configuration. Bravo, Carmona, Fernández, and Ojeda [2] establish finiteness and analyze one-, three-, and five-cycle regimes; their hypotheses and conclusions do not imply the claimed stability of these seven fixed-parameter orbits. No general maximum-of-seven theorem is asserted.

## Limitations
The result relies on the source's published proof of transverse itineraries over the larger intervals. It provides a **lower bound** of seven periodic orbits and a stability classification only for those seven; other periodic solutions or global attractors are neither excluded nor classified. The persistence assertion is local and does not provide a numerical perturbation radius. Independent verification and historical-priority assessment have not been performed.

## References
[1] C. Hu and J. Chen, *Seven Limit Cycles in a Periodically Forced Three-Zone Equation*, arXiv:2610.19586v1 (first posted 2026-10-14), Sections 1–4 and Appendix A.

[2] J. L. Bravo, V. Carmona, M. Fernández and I. Ojeda, *Upper bound for the number of limit cycles for symmetric piecewise linear differential equations with three zones*, arXiv:2507.06705v2 (revision 2026-10-09; first posted 2025-07-09), Sections 2–6.
