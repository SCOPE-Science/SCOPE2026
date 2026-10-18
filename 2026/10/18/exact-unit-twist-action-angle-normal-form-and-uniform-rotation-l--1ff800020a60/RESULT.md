# Exact unit-twist action–angle normal form and uniform rotation law for a genus-zero birational map

## Finding
For every \(a>1/4\) define
\[
F_a(x,y)=\left(y,\frac{a-y+y^2}{x}\right),\qquad V_a(x,y)=\frac{x^2+y^2-x-y+a}{xy},\qquad \omega=\frac{dx\wedge dy}{xy}.
\]
Write \(h_c=2-1/a\), \(\phi_a=\arccos(h_c/2)\), and \(\mathcal E_a=\{(x,y)\in(0,\infty)^2:h_c<V_a(x,y)<2\}\). Then a global smooth symplectic chart \((I,\theta):\mathcal E_a\to(0,\phi_a)\times\mathbb R/(2\pi\mathbb Z)\) exists with
\[
I=\phi_a-\arccos(V_a/2),\quad \omega=dI\wedge d\theta,\quad (I,\theta)\circ F_a=(I,\theta+I-\phi_a).
\]
The rotation-angle derivative with respect to canonical action is **exactly one at every elliptic level**, independently of \(a\). The enclosed logarithmic symplectic area at energy \(h\in(h_c,2)\) is
\[
A_a(h)=2\pi\left(\phi_a-\arccos(h/2)\right),
\qquad \omega(\mathcal E_a)=2\pi\phi_a.
\]
Under normalized \(\omega\)-area on \(\mathcal E_a\), both \(I\) and the rotation-angle deficit \(\arccos(V_a/2)=\phi_a-I\) are uniform on \((0,\phi_a)\). These statements form one action–angle theorem and its exact measure consequences.

## Assumptions and scope
The parameter \(a\) is any fixed real number greater than \(1/4\), and the state space is the positive quadrant. The numerator \(a-y+y^2=(y-1/2)^2+a-1/4\) is positive, so the map preserves this quadrant and is a smooth diffeomorphism there. The level \(h_c\) is the unique positive-quadrant minimum of \(V_a\), at \((a,a)\). For every \(h_c<h<2\), the conic \(V_a=h\) is a smooth simple ellipse lying wholly in the positive quadrant. The excluded central equilibrium and the parabolic limiting level are not part of the asserted smooth annular chart.

## Proof
**First integral and natural symplectic form.** Direct substitution yields \(V_a\circ F_a=V_a\). Writing \(F_a=(y,z)\) with \(z=(a-y+y^2)/x\), its Jacobian satisfies
\[
\det DF_a=\frac{a-y+y^2}{x^2},\qquad \frac{\det DF_a}{yz}=\frac1{xy}.
\]
Thus \(F_a^*\omega=\omega\). Introduce logarithmic Cartesian coordinates \(u=\log x,v=\log y\), so \(\omega=du\wedge dv\). The Lie-symmetry field already explicitly identified in the cited 2015 study is
\[
X_a=\left(\frac{x^2-y^2+a-x}{y},\frac{x^2-y^2-a+y}{x}\right)
=xy\left(-\frac{\partial V_a}{\partial y},\frac{\partial V_a}{\partial x}\right).
\]
In \((u,v)\) coordinates this means \(\dot u=-\partial_vV_a\), \(\dot v=\partial_uV_a\), and hence \(\iota_{X_a}\omega=-dV_a\). Its orbits are the elliptic level circles, and its time coordinate \(t\) is canonically dual to energy \(h=V_a\).

**Exact period of the Hamiltonian flow.** The same source proves that on each smooth conic a proper real projective parametrization conjugates this very field to
\[
\dot z=1-hz+z^2,
\]
not merely a time-rescaled vector field. For \(-2<h<2\), the quadratic is \((z-h/2)^2+(4-h^2)/4\). Completing a full real projective circuit gives the exact flow period
\[
T_a(h)=\int_{-\infty}^{\infty}\frac{dz}{z^2-hz+1}
=\frac{2\pi}{\sqrt{4-h^2}}.
\]
The condition \(h_c<h<2\) implies \(-2<h<2\) because \(a>1/4\).

**Global smooth canonical chart and area.** Every ellipse has two diagonal intersections. The greater one is a smooth transversal section
\[
\sigma(h)=\bigl(z_+(h),z_+(h)\bigr),\qquad
z_+(h)=\frac{1+\sqrt{1-a(2-h)}}{2-h}.
\]
It intersects each orbit once, and its derivative is transverse to the Hamiltonian flow. If \(p=\Phi_{X_a}^{t}(\sigma(h))\), with \(t\) taken modulo \(T_a(h)\), define \(\theta=2\pi t/T_a(h)\pmod{2\pi}\). In these coordinates \(\omega=dh\wedge dt\), because \(\omega(\partial_h,\partial_t)=dV_a(\partial_h)=1\). Therefore
\[
\omega=\frac{T_a(h)}{2\pi}\,dh\wedge d\theta
=\frac{dh\wedge d\theta}{\sqrt{4-h^2}}.
\]
Normalize the action to vanish at the central equilibrium. Integrating \(dI/dh=T_a(h)/(2\pi)\) gives
\[
I(h)=\int_{h_c}^{h}\frac{ds}{\sqrt{4-s^2}}
=\arcsin(h/2)-\arcsin(h_c/2)
=\phi_a-\arccos(h/2).
\]
It increases smoothly from \(0\) to \(\phi_a\). The preceding formula proves \(\omega=dI\wedge d\theta\), establishing the global symplectomorphism and, by integration, the enclosed and full area formulas.

**Exact unit twist.** The cited source computes the same map's orientation-preserving rotation angle on \(V_a=h\) as \(-\arccos(h/2)\) modulo \(2\pi\). Its conjugating projective coordinate also intertwines the actual flow of \(X_a\), so this angle is measured in the positive-flow \(\theta\) coordinate, not merely up to unoriented circle conjugacy. Independently, with the source's Möbius model \(M_h(z)=((h+1)z-1)/(z+1)\), the flow time of the transition from \(z=0\) to \(z=-1\) is
\[
\tau(h)=\int_0^{-1}\frac{dz}{z^2-hz+1}
=-\frac{\arccos(h/2)}{\sqrt{4-h^2}}.
\]
Multiplying by \(2\pi/T_a(h)=\sqrt{4-h^2}\) confirms signed displacement \(-\arccos(h/2)\). Substitution of the action gives \(\theta' = \theta+I-\phi_a\pmod{2\pi}\). Differentiating yields the constant twist \(\partial_I(\theta'-\theta)=1\).

**Uniform rotation law.** Since the chart is canonical, the normalized area law is \(dI\,d\theta/(2\pi\phi_a)\). Thus \(I\) is uniform on its action interval, and so is \(\phi_a-I=\arccos(h/2)\). For every \(0<r<s<\phi_a\), the set with rotation-angle deficit in \((r,s)\) has unnormalized area \(2\pi(s-r)\).

## Verification
The accompanying standalone `verify.py` checks the invariant, symplectic Jacobian, and Lie/Hamiltonian formulas symbolically. Independent high-precision integration of \(\int\! \log(y_+(x)/y_-(x))\,dx/x\) on four distinct conic interiors reproduces \(A_a(h)\); six further Riccati integrals reproduce the signed map shift. Run with Python, SymPy, and mpmath by executing `python verify.py`. These finite checks test algebra and numerical normalizations; the proof above establishes the continuum assertions.

## Relationship to prior work
Bastien and Rogalski (2004) introduced the recurrence and characterized its periodic structure. Llorens and Mañosa (first public manuscript 2015-02-12, arXiv:1502.03737), particularly Propositions 8 and 10, established the invariant conics, their individual-oval rotation angles, a Lie symmetry, and the invariant density \(1/(xy)\). None of those ingredients is presented here as new. The additional assertion is their exact synthesis into one **global canonical** action–angle chart, the parameter-independent unit twist, the finite total logarithmic area, and the corresponding uniform frequency-deficit distribution. These are stronger quantitative statements than pointwise rotation angles or invariance of a nonnormalized density.

## Limitations
The theorem is for the positive-quadrant elliptic component of this specified genus-zero recurrence. The center and the parabolic boundary are excluded from the smooth chart. The outer parabolic/hyperbolic region has no asserted finite invariant area or action–angle description. Any smooth perturbation, KAM persistence, or stochastic limit would require separate hypotheses and proof. Earlier unindexed results and the inaccessible full 2004 article create a residual historical-priority uncertainty. The analysis does not assert independent validation.

## References
Llorens, M., and Mañosa, V., *Lie Symmetries of Birational Maps Preserving Genus 0 Fibrations*, arXiv:1502.03737 (first posted 2015-02-12), especially §3.1, Propositions 8 and 10. https://arxiv.org/abs/1502.03737

Bastien, G., and Rogalski, M., *On some algebraic difference equations related to families of conics or cubics: generalization of the Lyness sequences*, Journal of Mathematical Analysis and Applications 300 (2004), 303–333, DOI:10.1016/j.jmaa.2004.06.035 (original recurrence and periodic structure; only bibliographic record and abstract available for comparison).
