# Weighted-volume rigidity in the Petrzela–Gotthans conic-equilibrium flow
## Finding
Consider the autonomous polynomial system introduced by Petrzela and Gotthans,
\[
\dot x=z,\qquad
\dot y=-z(ay+bxz),\qquad
\dot z=x+y^2-r.
\]
Its divergence is
\[
\nabla\!\cdot f=-az.
\]
Because \(\dot x=z\), this is an exact trajectory derivative,
\[
\nabla\!\cdot f=-a\dot x=-\frac{d}{dt}(ax).
\]
Therefore the smooth positive density
\[
\rho(x,y,z)=e^{ax}
\]
is invariant:
\[
\nabla\!\cdot(\rho f)=0.
\]
Equivalently, the exact finite-time Euclidean Jacobian of the flow is
\[
\det D\phi_t(p)=\exp\!\left(\int_0^t\nabla\!\cdot f(\phi_s p)\,ds\right)
=\exp[-a(x(t)-x(0))].
\]
Thus the instantaneous Euclidean divergence can have either sign, but its time integral on a bounded recurrent trajectory is a boundary term rather than cumulative dissipation.

Three consequences follow. First, every bounded trajectory for which the Lyapunov-sum trace formula is defined has
\[
\lim_{t\to\infty}\frac1t\log|\det D\phi_t|=0.
\]
Second, every periodic orbit of period \(T\) satisfies \(x(T)=x(0)\), hence
\[
\det D\phi_T=1.
\]
Since an autonomous periodic orbit has the trivial Floquet multiplier \(1\), its two transverse multipliers \(\mu_1,\mu_2\) obey
\[
\mu_1\mu_2=1.
\]
No periodic orbit of the exact ODE can therefore be asymptotically attracting or asymptotically repelling.

Third, the invariant density rules out a compact asymptotically stable attractor with a bounded open trapping neighborhood. If a bounded open set \(U\) has compact closure and is strictly trapped after some time \(T>0\), so that \(\phi_T(\overline U)\subset U\), then preservation of the weighted measure
\[
m_\rho(E)=\int_E e^{ax}\,dx\,dy\,dz
\]
would give \(m_\rho(\phi_T(U))=m_\rho(U)\). But \(\phi_T(\overline U)\) is compactly contained in \(U\), so \(U\setminus\phi_T(\overline U)\) contains a nonempty open set and therefore has strictly positive \(m_\rho\)-measure, a contradiction. Hence the usual trapping-region notion of a compact strange attractor cannot apply to this exact flow.

## Assumptions and scope
The identities hold for all real parameters \(a,b,r\) on every interval on which the smooth flow is defined. The attractor obstruction concerns compact asymptotically stable invariant sets possessing a bounded open trapping neighborhood, the standard setting for a robust attracting set. It does not rule out bounded chaotic invariant sets without attraction, chaotic saddles, invariant sets with only measure-theoretic attraction, or numerical/circuit behavior altered by discretization, saturation, component drift, or other nonideal effects.

The source's reported chaotic parameter choice \(a=12\), \(b=0.4\), \(r=1\) is included. For a bounded trajectory at these parameters, the long-time Euclidean volume exponent is still exactly zero because the finite-time logarithmic Jacobian is \(-12(x(t)-x(0))\).

## Proof
Direct differentiation gives
\[
\nabla\!\cdot f
=\partial_x z+\partial_y[-z(ay+bxz)]+\partial_z(x+y^2-r)
=-az.
\]
For \(\rho=e^{ax}\),
\[
\nabla\!\cdot(\rho f)
=\rho\,\nabla\!\cdot f+\nabla\rho\cdot f
=e^{ax}(-az)+ae^{ax}\dot x
=0.
\]
This proves preservation of \(m_\rho\) wherever the flow map is defined and invertible. Liouville's formula gives
\[
\det D\phi_t
=\exp\!\left(\int_0^t -az(s)\,ds\right)
=\exp\!\left(-a\int_0^t\dot x(s)\,ds\right)
=\exp[-a(x(t)-x(0))].
\]
If \(x(t)\) is bounded, division of the logarithm by \(t\) and passage to the limit gives zero asymptotic volume rate. If the orbit is periodic, the boundary term vanishes exactly over one period. The Floquet product statement then follows from the determinant of the monodromy and the trivial flow-direction multiplier.

For the trapping-region obstruction, suppose \(U\) is bounded and open with \(\phi_T(\overline U)\subset U\). Since \(e^{ax}\) is continuous and strictly positive, \(m_\rho\) is finite on bounded sets and assigns positive measure to every nonempty open set. Invariance gives \(m_\rho(\phi_T(U))=m_\rho(U)\). Compact containment gives a nonempty open collar in \(U\) disjoint from \(\phi_T(\overline U)\), forcing \(m_\rho(\phi_T(U))<m_\rho(U)\), contradiction.

## Verification
The accompanying `verify_weighted_volume.py` symbolically reconstructs the vector field and checks all algebraic identities used in the proof. Its recorded execution returns

`VERIFY_WEIGHTED_VOLUME_OK`

and verifies exactly that \(\nabla\!\cdot f=-az\), \(\nabla\!\cdot f+a\dot x=0\), and \(\nabla\!\cdot(e^{ax}f)=0\).

The source article was inspected in full-text HTML. It gives the same vector field, labels the system dissipative, reports contraction using a state-dependent exponential expression, presents periodic solutions/limit cycles, and discusses a hidden strange attractor and basins of attraction. The exact Liouville calculation above replaces the state-dependent contraction expression by the endpoint formula \(\exp[-a(x(t)-x(0))]\).

## Relationship to prior work
Petrzela and Gotthans introduced the system in 2017 and numerically/experimentally described a hidden strange attractor, basins, and periodic motion. A later review by Petrzela, Gotthans, and Guzan surveys circuit realizations of systems with plane continua of equilibria. Searches by the exact title, DOI, vector-field terms, invariant-density terms, Liouville/volume-preservation terms, and Floquet consequences did not locate the identity \(\nabla\!\cdot(e^{ax}f)=0\) or its attractor obstruction for this specific system.

The closest published comparison found in the published-finding corpus corpus is a 2026 result on the trigonometric Nosé–Hoover flow where phase-space contraction is only cohomologous to a nonzero observable; there, zero integrated contraction requires additional symmetry. A second result uses reversibility to force reciprocal Floquet multipliers only for reversing-symmetric periodic orbits. Neither implies the present source-specific statement: here the entire divergence is an exact coboundary \(-a\dot x\), so every periodic orbit has unit monodromy determinant and the positive density \(e^{ax}\) is globally invariant on the flow domain.

## Limitations
The result corrects the dissipative/attracting interpretation of the exact continuous-time ODE, not the existence of sensitive dependence or bounded chaotic invariant dynamics. It does not prove that any particular numerical trajectory is a chaotic saddle, nor does it model finite-precision integration or nonideal electronic circuitry. The no-attractor conclusion is stated for the standard compact trapping-region/asymptotic-stability notion; broader terminology such as Milnor or statistical attractors can behave differently. Global completeness of all trajectories is not asserted, and is unnecessary for the local invariant-volume identity or for the contradiction inside a bounded trapping region.

## References
1. J. Petrzela and T. Gotthans, *New Chaotic Dynamical System with a Conic-Shaped Equilibrium Located on the Plane Structure*, Applied Sciences 7 (2017), 976. DOI: 10.3390/app7100976. https://doi.org/10.3390/app7100976
2. J. Petrzela, T. Gotthans, and M. Guzan, *Current-Mode Network Structures Dedicated for Simulation of Dynamical Systems with Plane Continuum of Equilibrium*, Journal of Circuits, Systems and Computers 27 (2018), 1830004. DOI: 10.1142/S0218126618300040. https://doi.org/10.1142/S0218126618300040
3. *Cohomological contraction and a Floquet edge in the trigonometric Nosé–Hoover flow*, published-finding corpus (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-cohomological-contraction-floquet-threshold-trigonometric-nose-hoover--0debb0e2ee19
4. *Reversible Floquet obstruction in the trigonometric Nosé–Hoover oscillator*, published-finding corpus (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-reversible-floquet-obstruction-trigonometric-nose-hoover--87f8866a2ffc
