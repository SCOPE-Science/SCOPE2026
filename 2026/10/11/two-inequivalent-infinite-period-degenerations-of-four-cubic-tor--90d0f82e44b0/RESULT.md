# Two inequivalent infinite-period degenerations of four cubic torus cycles

## Finding
Consider the cubic polynomial flow on the smooth algebraic torus
\[
\mathcal T_a=\{(x,y,z)\in\mathbb R^3:(x^2+y^2-a^2)^2+z^2=1\},\qquad a>1,
\]
with real parameters \(c>0\), \(\eta>0\), and \(\lambda>0\):
\[
\begin{aligned}
\dot x&=\tfrac14(\lambda+\eta z)zx+cxy^2,\\
\dot y&=\tfrac14(\lambda+\eta z)zy-cx^2y,\\
\dot z&=\tfrac12(\lambda+\eta z)[-a^2(x^2+y^2)+z^2+a^4-1].
\end{aligned}
\tag{1}
\]
For \(\lambda>\eta\), exactly four periodic orbits lie on \(\mathcal T_a\): the four meridians with polar angle \(\theta=0,\pi/2,\pi,3\pi/2\). All four have the same **minimal original-time period**
\[
\boxed{T=\frac{4\pi}{\lambda^2+(a^4-1)\eta^2}
\left(\frac{\lambda}{\sqrt{a^4-1}}+
\frac{a^2\eta^2}{\sqrt{\lambda^2-\eta^2}}\right).}
\tag{2}
\]
There are no other periodic orbits on the torus. The two meridians \(\theta=0,\pi\) are attracting **relative to the torus**, with nontrivial torus-transverse Floquet multiplier
\[
\boxed{\rho_{\mathrm s}=\exp\!\left(-\frac{4\pi c}{\sqrt{\lambda^2-\eta^2}}\right),}
\tag{3}
\]
while the other two are repelling, with multiplier \(\rho_{\mathrm u}=\rho_{\mathrm s}^{-1}\). The exact return map, on each angular quadrant with \(\tan\theta\) finite, is
\[
\boxed{\tan\theta_{\rm next}=\rho_{\rm s}\tan\theta_{\rm now}.}
\tag{4}
\]
The multiplier in (3) is independent of the torus-shape parameter \(a\). It refers to dynamics **on the invariant torus**; no claim is made about the second normal multiplier in ambient three-space.

Two geometrically distinct boundaries both produce square-root period divergence but have opposite transverse stability behavior:

**Velocity-arrest boundary.** Fix \(a>1\), \(c>0\), \(\eta>0\), put \(\delta=\lambda-\eta\), and let \(\delta\downarrow0\). Then
\[
\boxed{\lim_{\delta\downarrow0}\sqrt\delta\,T
=\frac{4\pi}{a^2\sqrt{2\eta}},\qquad
\lim_{\delta\downarrow0}\sqrt\delta(-\log\rho_{\rm s})
=\frac{4\pi c}{\sqrt{2\eta}},\qquad
\lim_{\delta\downarrow0}\frac{\log\rho_{\rm s}}{T}=-ca^2.}
\tag{5}
\]
At \(\lambda=\eta\), each meridian becomes a single equilibrium plus a homoclinic orbit with infinite flight time. For \(0<\lambda<\eta\), there are no periodic orbits on the torus; instead, the meridian direction has two stationary phases.

**Geometric pinching boundary.** Fix \(\lambda>\eta>0\), \(c>0\), and let \(a\downarrow1\) through smooth tori. Then
\[
\boxed{\lim_{a\downarrow1}\sqrt{a^4-1}\,T=\frac{4\pi}{\lambda},\qquad
\rho_{\rm s}=\exp\!\left(-\frac{4\pi c}{\sqrt{\lambda^2-\eta^2}}\right),\qquad
\lim_{a\downarrow1}\frac{\log\rho_{\rm s}}{T}=0.}
\tag{6}
\]
Thus divergence caused by vanishing angular speed drives the stable return multiplier to zero, whereas divergence caused by geometric pinching leaves the multiplier fixed. The endpoint \(a=1\) is a singular horn torus and is **not** included in the smooth-torus theorem.

## Assumptions and scope
The independent variable of (1) is the original physical time \(t\). All conclusions concern the restriction of the three-dimensional cubic flow (1) to its invariant smooth embedded torus \(\mathcal T_a\), with \(a>1\), \(c,\eta,\lambda>0\). There are no assertions about all trajectories of (1) outside the torus. The parameter regimes \(\lambda>\eta\), \(\lambda=\eta\), and \(0<\lambda<\eta\) are separate statements. The limiting expressions in (5) hold with \(a,c,\eta\) fixed; those in (6) hold with \(c,\eta,\lambda\) fixed.

## Proof
Write \(r^2=x^2+y^2\), and \(F=(r^2-a^2)^2+z^2-1\). Direct polynomial differentiation yields
\[
\dot F=(\lambda+\eta z)zF,
\]
so \(\mathcal T_a\) is invariant. Since \(a>1\), \(r>0\) everywhere on the torus and there are global angular coordinates (each modulo \(2\pi\))
\[
\begin{aligned}
r^2&=a^2+\cos\varphi,\\
z&=\sin\varphi,\\
x&=r\cos\theta,\quad y=r\sin\theta.
\end{aligned}
\]
Using \(2r\dot r=(\lambda+\eta z)zr^2/2\) and \(r^2\dot\theta=x\dot y-y\dot x=-cxyr^2\) gives the exact **original-time** equations
\[
\dot\varphi=-\tfrac12(a^2+\cos\varphi)(\lambda+\eta\sin\varphi),
\qquad
\dot\theta=-\tfrac c2(a^2+\cos\varphi)\sin2\theta.
\tag{7}
\]
The derivation of the first equality initially away from \(\sin\varphi=0\) extends there by smoothness. This also verifies the normalization of time in all following formulas.

For \(\lambda>\eta\), \(\dot\varphi<0\) everywhere. Every return to a section \(\varphi=\varphi_0\) therefore occurs after one negative circuit of \(\varphi\). Dividing (7) gives
\[
\frac{d\theta}{d\varphi}=\frac{c\sin2\theta}{\lambda+\eta\sin\varphi},\qquad
\frac{d\log|\tan\theta|}{d\varphi}=\frac{2c}{\lambda+\eta\sin\varphi}.
\]
This identity is valid inside each quadrant; endpoints are invariant by uniqueness. Since
\[
\int_0^{2\pi}\frac{d\varphi}{\lambda+\eta\sin\varphi}
=\frac{2\pi}{\sqrt{\lambda^2-\eta^2}},
\]
integration over the **negatively oriented** return circuit proves (4). Its only fixed angular values are the four quadrant endpoints. Linearizing (4) at \(\theta=0,\pi\) gives (3), and using the reciprocal cotangent coordinate at \(\theta=\pi/2,3\pi/2\) gives \(\rho_{\rm s}^{-1}\). Hence the four cycles are isolated among periodic trajectories on the torus and have the stated relative stability.

The return time is independent of \(\theta\), with
\[
T=2\int_0^{2\pi}\frac{d\varphi}{(a^2+\cos\varphi)(\lambda+\eta\sin\varphi)}.
\tag{8}
\]
Put \(A=a^2>1\), and \(D=\lambda^2+(A^2-1)\eta^2\). The exact identity
\[
\frac1{(A+\cos\varphi)(\lambda+\eta\sin\varphi)}
=\frac{\lambda-\eta\sin\varphi}{D(A+\cos\varphi)}
+\frac{\eta^2(A-\cos\varphi)}{D(\lambda+\eta\sin\varphi)}
\tag{9}
\]
follows on multiplying by both denominators and using \(\sin^2\varphi+\cos^2\varphi=1\). The integrals of \(\sin\varphi/(A+\cos\varphi)\) and \(\cos\varphi/(\lambda+\eta\sin\varphi)\) over a full circle vanish as logarithmic derivatives. With
\[
\int_0^{2\pi}\frac{d\varphi}{A+\cos\varphi}=\frac{2\pi}{\sqrt{A^2-1}},
\]
(8) and (9) establish the exact formula (2). Positivity of the speed and monotone winding imply that this is the **minimal** period on any invariant meridian.

For \(\lambda=\eta\), the angular speed \(\dot\varphi\) is strictly negative except at \(\varphi=3\pi/2\); the equilibrium at that phase belongs to each invariant meridian, and each remaining meridian arc is asymptotic to that same point in both time directions. For \(0<\lambda<\eta\), \(\dot\varphi\) has two stationary phases; one-dimensional uniqueness prevents a nonconstant periodic \(\varphi\). A periodic orbit would have to lie at one of those stationary phases, but the remaining scalar equation for \(\theta\) in (7) has no nonconstant periodic solution. Thus no periodic orbit remains in either of these regimes.

Finally, for \(\lambda=\eta+\delta\), \(\sqrt{\lambda^2-\eta^2}\sim\sqrt{2\eta\delta}\), while \(D\to a^4\eta^2\). The second term in (2) dominates, yielding the first limit in (5); equation (3) yields the second and their quotient yields the third. For \(a\downarrow1\) with \(\lambda>\eta\) fixed, \(D\to\lambda^2\), and the first term in (2) dominates; (3) does not depend on \(a\), proving (6).

## Verification
All equalities in (1)–(9) follow from exact polynomial algebra, elementary separable return dynamics, and standard one-dimensional trigonometric integrals. `checker.py` verifies the invariant-torus cofactor identity numerically at multiple points, compares the closed period formula with a high-resolution composite Simpson quadrature, and checks the return multiplier and both asymptotic scales at representative admissible parameters. Run using `python3 checker.py`; it has no third-party dependencies. Such finite numerical checks are corroboration, **not** proofs of the global or limiting statements; the proof above supplies those.

## Relationship to prior work
Jana, *Characterization and dynamics of certain classes of polynomial vector fields on the torus*, arXiv:2401.07843 (first public version January 15, 2024), Theorem 2.1 parametrizes cubic torus-tangent polynomial fields by a cofactor, and Theorem 2.4 gives the existence and alternating stability of four invariant meridians. Example 5.5 uses the constant cofactor \(K'=1\) and \(f=xy\). Equation (1) specializes this geometric setting to a nonconstant affine cofactor \(K'=\lambda+\eta z\), retaining its natural four-meridian configuration and making the critical cofactor-zero boundary accessible. The existence/stability classification is **not** presented here as original. The claims here are the exact global holonomy and physical-time period **together with** the two different sharp limiting regimes and the vanishing versus nonvanishing limiting multiplier. None is stated in the inspected theorem, example, or proof of arXiv:2401.07843v3.

Medrado and Llibre (2011) and Llibre and Rebollo-Perdomo (2013) previously treated configurations of invariant meridians and parallels on algebraic tori. Their stated classification and existence objectives are acknowledged; a complete relevant full-text comparison could not be completed. General saddle-node infinite-period normal forms explain the square-root *type* but do not alone determine the exact coefficient, projective holonomy or distinction between smooth-torus velocity arrest and geometric torus pinching in this polynomial family.

## Limitations
The conclusion is confined to the invariant torus; ambient normal attraction, persistence under arbitrary perturbations, and robustness of the simultaneous four-cycle degeneration are not established. At the horn-torus endpoint \(a=1\), smooth-torus coordinates degenerate. Publication priority beyond the specifically inspected literature is not certified, particularly regarding older works on polynomial torus meridians and possible alternative expressions of the same return map. The example is algebraically special: its exact solvability need not hold for arbitrary cubic vector fields tangent to a torus.

## References
1. S. Jana, *Characterization and dynamics of certain classes of polynomial vector fields on the torus*, arXiv:2401.07843 (v1 posted 2024-01-15, v3 posted 2024-09-10); J. Math. Anal. Appl. 542 (2025), 128875. https://arxiv.org/abs/2401.07843
2. J. Llibre and J. C. Medrado, *Limit cycles, invariant meridians and parallels for polynomial vector fields on the torus*, Bull. Sci. Math. 135 (2011), 1–9. https://doi.org/10.1016/j.bulsci.2010.06.005
3. J. Llibre and S. Rebollo-Perdomo, *Invariant parallels, invariant meridians and limit cycles of polynomial vector fields on some 2-dimensional algebraic tori in* \(\mathbb R^3\), J. Dyn. Differ. Equ. 25 (2013), 777–793. https://doi.org/10.1007/s10884-013-9315-4
