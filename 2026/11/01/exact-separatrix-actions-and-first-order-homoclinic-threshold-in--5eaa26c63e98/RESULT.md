# Exact separatrix actions and first-order homoclinic threshold in an equal-depth sextic triple well

## Finding

Fix arbitrary real \(a>0\) and \(\kappa>0\). Consider the reversible polynomial differential system
\[
\dot x=y,\qquad \dot y=-V'(x)+(b_0x+b_1x^3)y,\qquad V(x)=\kappa x^2(x^2-a^2)^2,
\]
with real parameters \(b_0,b_1\). Its Hamiltonian member at \(b_0=b_1=0\) has three equal-depth potential wells at \(x=0,\pm a\), two hyperbolic saddles at \(x=\pm a/\sqrt3\), and common saddle energy \(h=4\kappa a^6/27\). The saddle-energy graph contains one central heteroclinic two-saddle contour and exactly two symmetric outer homoclinic contours. Their bounded Euclidean phase-plane areas, equivalently their unsigned Hamiltonian actions, satisfy the **exact partition**
\[
\mathcal A_{\mathrm{central}}=\frac{\sqrt{6\kappa}}3a^4,\qquad
\mathcal A_{\mathrm{right}}=\mathcal A_{\mathrm{left}}=\frac{\sqrt{6\kappa}}6a^4,
\]
so the area ratio is exactly \(2:1:1\).

For all sufficiently small \(|b_0|+|b_1|\), the two central heteroclinic connections persist by reversibility. In a neighborhood of \((b_0,b_1)=(0,0)\), **both outer homoclinic loops persist exactly on a unique smooth curve** \(b_0=g(b_1)\), with \(g(0)=0\) and
\[
\boxed{g'(0)=-\frac{19}{21}a^2},\qquad
 g(b_1)=-\frac{19}{21}a^2b_1+O(b_1^2).
\]
The leading invariant-manifold energy splitting for the right outer loop is
\[
D(b_0,b_1)=\frac{4\sqrt{2\kappa}}{15}a^5
\left(b_0+\frac{19}{21}a^2b_1\right)
+O\big((|b_0|+|b_1|)^2\big).
\]
For small \(b_1<0\), the homoclinic curve lies below the exact outer-well Hopf line \(b_0=-a^2b_1\) by a parameter interval of length
\[
(-a^2b_1)-g(b_1)=\frac{2a^2}{21}|b_1|+O(b_1^2).
\]
This is the leading width of the one-limit-cycle region identified qualitatively for the five-equilibrium quintic Liénard class by Cao–Sadri–Tang–Wang.

## Assumptions and scope

The coefficients \(a,\kappa\) are fixed strictly positive real numbers. Every assertion about persistence is local in the two real damping parameters \((b_0,b_1)\), whose neighborhood can depend on \(a,\kappa\). No global assertion at finite damping or about nonlocal cycles is made. The outer homoclinic loops are based separately at the two saddles; they are not a figure-eight orbit through a common saddle. The central contour consists of two distinct saddle-to-saddle heteroclinic trajectories.

## Proof

**1. The three critical contours.** At zero damping let \(H=y^2/2+V(x)\). Direct differentiation gives \(V'(x)=2\kappa x(x^2-a^2)(3x^2-a^2)\). Thus the five critical points are \(0,\pm a/\sqrt3,\pm a\); the two interior nonzero ones are saddles since \(V''(a/\sqrt3)=-8\kappa a^4/3<0\). At their common energy,
\[
h-V(x)=\kappa\left(x^2-\frac{a^2}{3}\right)^2\left(\frac{4a^2}{3}-x^2\right).
\]
Setting \(r=a/\sqrt3\), the upper energy branch is therefore
\[
y_+(x)=\sqrt{2\kappa}\,|x^2-r^2|\sqrt{4r^2-x^2},\qquad -2r\le x\le2r.
\]
The bounded contours have consecutive turning intervals \([-r,r]\), \([r,2r]\), and \([-2r,-r]\). The central contour closes through both saddles; each exterior contour returns to one saddle.

**2. Exact action areas.** Phase-plane area enclosed by each contour equals \(2\int y_+(x)\,dx\) over its turning interval. Two elementary integrals are
\[
\int_0^r(r^2-x^2)\sqrt{4r^2-x^2}\,dx=\frac{3\sqrt3}{4}r^4,\qquad
\int_r^{2r}(x^2-r^2)\sqrt{4r^2-x^2}\,dx=\frac{3\sqrt3}{4}r^4.
\]
The equalities follow by setting \(x=2r\sin\theta\), integrating a trigonometric polynomial and evaluating at \(\theta=0,\pi/6,\pi/2\). The central contour has two half-intervals \([-r,0]\) and \([0,r]\), while each exterior contour has only one interval of the same action integral. Multiplication by \(2\sqrt{2\kappa}\) proves the three stated areas and their exact ratio.

**3. Persistence of the central saddle connections.** Reversibility follows directly from \(V'(-x)=-V'(x)\) and \(b_0(-x)+b_1(-x)^3=-(b_0x+b_1x^3)\): the involution \(R(x,y)=(-x,y)\) sends forward trajectories to reversed trajectories. At zero damping each saddle unstable branch directed toward the central well crosses the fixed line \(x=0\) transversely, once with \(y>0\) and once with \(y<0\). Hyperbolic invariant manifolds depend smoothly on parameters. Both crossings persist for sufficiently small parameters, and reversible reflection of an unstable branch at a fixed-line crossing is a stable branch of the reflected saddle. Thus both central connections persist, without tuning \(b_0\) or \(b_1\).

**4. Homoclinic splitting.** Fix the right saddle \((r,0)\). At zero damping its outer unstable and stable separatrix branches meet the transverse line \(y=0\) at \((2r,0)\). The relevant branches have nearby intersections \(p_u(b_0,b_1)\) and \(p_s(b_0,b_1)\) on that same line, depending smoothly on parameters. Set \(D=H(p_u)-H(p_s)\), with the unchanged Hamiltonian \(H\) evaluated even for nonzero damping. Near the turning point, \(H|_{y=0}=V(x)\) is strictly increasing, so \(D=0\) holds exactly when the intersections agree and the homoclinic connection is restored.

Along any perturbed trajectory,
\[\dot H=(b_0x+b_1x^3)y^2.\]
Integrate this identity from the fixed saddle to the two transverse intersections along unstable and stable branches. Exponential approach to the hyperbolic saddle justifies differentiation under these improper integrals at zero damping; the first derivatives of \(D\) are the integrals of \(xy^2\) and \(x^3y^2\) over the unperturbed outer homoclinic orbit. Since \(dt=dx/y\) on either upper or lower segment,
\[
\partial_{b_0}D(0,0)=2\sqrt{2\kappa}\int_r^{2r}x(x^2-r^2)\sqrt{4r^2-x^2}\,dx,\quad
\partial_{b_1}D(0,0)=2\sqrt{2\kappa}\int_r^{2r}x^3(x^2-r^2)\sqrt{4r^2-x^2}\,dx.
\]
With \(x=au\), direct substitutions \(w=4/3-u^2\) yield the exact integrals
\[
\int_{1/\sqrt3}^{2/\sqrt3}u\left(u^2-\frac13\right)\sqrt{\frac43-u^2}\,du=\frac{2}{15},\quad
\int_{1/\sqrt3}^{2/\sqrt3}u^3\left(u^2-\frac13\right)\sqrt{\frac43-u^2}\,du=\frac{38}{315}.
\]
Therefore \(\partial_{b_0}D(0,0)=4\sqrt{2\kappa}a^5/15>0\), and \(\partial_{b_1}D(0,0)=76\sqrt{2\kappa}a^7/315\), proving the splitting expansion. The implicit-function theorem yields a unique smooth graph \(b_0=g(b_1)\) on which the right outer homoclinic orbit exists, and
\[
g'(0)=-\frac{\partial_{b_1}D}{\partial_{b_0}D}=-\frac{19}{21}a^2.\]
By the same reversible symmetry the left outer homoclinic exists on exactly that graph.

**5. Exact leading Hopf gap.** At either outer equilibrium \(x=\pm a\), the Jacobian trace is \(\pm a(b_0+a^2b_1)\) and its determinant is \(V''(a)>0\). The common Hopf trace-zero line is thus exactly \(b_0=-a^2b_1\). For small \(b_1<0\), subtracting the homoclinic expansion gives the width \((2a^2/21)|b_1|+O(b_1^2)\), which is positive. The identification of that intervening region with one outer-well limit cycle is supplied by the cited global five-equilibrium classification; the present calculation determines its quantitative leading width.

## Verification

The polynomial potential factorization, exact action integrals, both odd-weighted Melnikov integrals, and the strict inequality between the Hopf and homoclinic slopes are reproduced by the supplied standalone symbolic script `verify_separatrix.py`. This checks algebraic and integral identities. The smooth-manifold persistence statements follow from the proof, not from finite arithmetic or numerical evidence.

## Relationship to prior work

Cao, Sadri, Tang and Wang (2026), arXiv:2610.26699v1, characterize this reversible quintic Liénard family globally. Their Section 5.12 gives a uniquely defined continuous homoclinic surface in the five-equilibrium regime \(\Omega_{15}\), and Section 6.13 identifies the qualitative parameter strips between it and the Hopf line. They also compute a different first-order resonance slope in the distinct \(\Omega_{14}\) saddle configuration. Their results establish the existence and relative ordering of the loops and limit cycles, **not** the present equal-depth triple-well symplectic area partition, explicit homoclinic derivative \(-19a^2/21\), or exact leading Hopf–homoclinic gap \(2a^2|b_1|/21\).

Siewe and collaborators (2005) studied the sextic three-well Van der Pol oscillator using Melnikov theory, but with **even-position damping** \(\mu(1-x^2)y\) and external/parametric periodic forcing. Their symmetry class and splitting coefficients therefore differ from the odd-position damping considered here. The hyperbolic invariant-manifold and Melnikov differentiation principles are classical and are not claimed as new.

## Limitations

Only the leading tangent and width near vanishing damping are found; no claim is made about the entire nonlinear global homoclinic surface or higher-order coefficients. The signed energy-splitting function depends on the chosen section and orientation, although its zero set and tangent are intrinsic. The three area values concern the Hamiltonian system exactly at zero damping and the specified physical \((x,y)\) coordinates. The region's limit-cycle multiplicity uses the cited prior classification, not a new global proof. Historical-priority assessment is necessarily bounded by the inspected relevant sources; independent mathematical validation has not been performed.

## References

1. C. Cao, N. Sadri, Y. Tang, and Z. Wang, *Global Dynamics and Periodic-Annulus Bifurcations in a Reversible Quintic Liénard System*, arXiv:2610.26699v1 (first public 19 October 2026), https://arxiv.org/html/2610.26699v1.
2. M. S. Siewe et al., *Bifurcations and chaos in the triple-well Van der Pol oscillator driven by external and parametric excitations*, Physica A 357 (2005), 383–396, https://www.academia.edu/130359903/Bifurcations_and_chaos_in_the_triple_well_Van_der_Pol_oscillator_driven_by_external_and_parametric_excitations.
3. H. Chen, X. Chen, M. Jia, and Y. Tang, *A quintic Z2-equivariant Liénard system arising from the complex Ginzburg–Landau equation (II)*, arXiv:2409.04024 (2024), https://arxiv.org/abs/2409.04024. The earlier family has damping even in position.
