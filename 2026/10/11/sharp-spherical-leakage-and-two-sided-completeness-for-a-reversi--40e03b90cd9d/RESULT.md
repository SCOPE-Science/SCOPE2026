# Sharp spherical leakage and two-sided completeness for a reversible quadratic flow

## Finding
For the three-dimensional flow
\[
\dot x=y+2xy+xz,\qquad \dot y=1-2x^2+yz,\qquad \dot z=x-x^2-y^2,
\]
let \(V=(x-1)^2+y^2+(z+1)^2\) and \(q=x^2+xy+y^2-x\). The **radial balance theorem** is the exact identity
\[
\dot V=-2q,
\qquad
q=(x-2/3)^2+(x-2/3)(y+1/3)+(y+1/3)^2-1/3.
\]
For every \(R\ge2\), the region on the centered sphere \(S_R=\{V=R^2\}\) where the field points strictly outward is a pair of graphs over the **same** planar ellipse \(E=\{(x,y):q(x,y)<0\}\). Its spherical surface-area fraction \(f_R\) and total positive outward flux \(J_R\) satisfy
\[
 f_R=\frac{1}{3\sqrt3\,R^2}+O(R^{-4}),
 \qquad J_R=\frac{2\pi}{9\sqrt3\,R}+O(R^{-3}).
\]
In particular, every such centered sphere has a nonempty outward-pointing patch, yet the patch occupies a vanishing \(R^{-2}\) fraction and carries a vanishing \(R^{-1}\) positive flux. The same identity proves that **all maximal solutions are defined for every real time** and obey \(\|(x(t),y(t),z(t))\|=O(\sqrt{1+|t|})\) for each initial condition. Any compactly supported invariant probability measure \(\mu\) obeys the two exact constraints
\[
\int xy\,d\mu=0,
\qquad \int\left[(x-1/2)^2+y^2\right]d\mu=1/4.
\]

## Assumptions and scope
The differential equations above have exactly the fixed coefficients displayed, without a varying parameter. The state space is \(\mathbb R^3\) and initial conditions are arbitrary finite real triples. Sphere radius \(R\) is Euclidean distance from \((1,0,-1)\). The normal flux is \(J_R=\int_{S_R}\max(F\cdot n,0)\,dA\) with outward unit normal \(n\). Area fraction is the area of \(\{F\cdot n>0\}\) divided by \(4\pi R^2\). Constants implicit in large-radius error terms are absolute. Statements about invariant probability measures assume compact support and invariance under this exact complete flow; no existence of a particular chaotic attractor is assumed.

## Proof
**Radial identity and ellipse.** Direct differentiation gives
\[
\frac{d}{dt}\big[(x-1)^2+y^2+(z+1)^2\big]
=-2(x^2+xy+y^2-x).
\]
With \(X=x-2/3\) and \(Y=y+1/3\), the quadratic \(q=X^2+XY+Y^2-1/3\). Its quadratic matrix is \(A=\bigl(\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}\bigr)\), with eigenvalues \(1/2\) and \(3/2\). Thus the positivity region for \(-q\) is the bounded ellipse \(E=\{X^2+XY+Y^2<1/3\}\), whose area is
\[
 |E|=\frac{\pi/3}{\sqrt{\det A}}=\frac{2\pi}{3\sqrt3}.
\]
The elementary coordinate bounds \(0\le x\le4/3\), \(-1\le y\le1/3\) on its closure imply \((x-1)^2+y^2\le2\). Hence for every \(R\ge2\), above each point of \(E\) the sphere has exactly two points
\[
 z=-1\pm\sqrt{R^2-(x-1)^2-y^2}.
\]
At either point its outward normal is \(n=((x-1),y,z+1)/R\), so the normal speed is \(F\cdot n=-q/R\). This proves the exact outward-region assertion.

**Area and positive flux.** Put \(\rho^2=(x-1)^2+y^2\). On either spherical graph the area element is \(R(R^2-\rho^2)^{-1/2}\,dx\,dy\). Consequently the exact expressions, valid for \(R\ge2\), are
\[
 f_R=\frac{1}{2\pi R^2}\int_E\frac{R}{\sqrt{R^2-\rho^2}}\,dx\,dy,
\qquad
 J_R=2\int_E\frac{-q(x,y)}{\sqrt{R^2-\rho^2}}\,dx\,dy.
\]
The integrands can be uniformly expanded for large \(R\) since \(\rho^2\le2\) on \(E\). The linear transformation \((X,Y)\mapsto A^{1/2}(X,Y)\) maps \(E\) to a disk of squared radius \(1/3\); its mean quadratic radius \(X^2+XY+Y^2\) is \(1/6\). Thus
\[
 \int_E(-q)\,dx\,dy=|E|/6=\pi/(9\sqrt3).
\]
Substituting these two integrals into the expansions gives the claimed \(f_R\) and \(J_R\), with errors \(O(R^{-4})\) and \(O(R^{-3})\), respectively. These are exact limits, not Monte Carlo estimates. In particular the area coefficient and flux coefficient cannot be lowered in the stated asymptotics.

**Global solutions and time averages.** Since \(q\ge-1/3\), the exact balance yields \(\dot V\le2/3\) and therefore
\[
0\le V(t)\le V(0)+2t/3\qquad(t\ge0).
\]
For a polynomial locally Lipschitz vector field, finite-time failure of a maximal solution entails its norm becoming unbounded. The displayed proper quadratic bound excludes such failure in positive time. The vector field is reversible under \(\mathcal R(x,y,z)=(x,-y,-z)\): \(\mathcal R F(u)=-F(\mathcal R u)\). Applying the positive-time conclusion to \(\mathcal R u(-t)\) proves negative-time completeness and the analogous bound \((x(t)-1)^2+y(t)^2+(z(t)-1)^2\le (x(0)-1)^2+y(0)^2+(z(0)-1)^2+2|t|/3\) for \(t\le0\). The asserted two-sided square-root growth follows.

The exact time-integrated form is
\[
\int_0^T\!\big[X(t)^2+X(t)Y(t)+Y(t)^2\big]dt
=\frac{T}{3}+\frac{V(0)-V(T)}{2}
\le \frac{T}{3}+\frac{V(0)}{2}
\quad(T>0).
\]
This uniformly controls the transverse quadratic time average even without assuming a bounded orbit.

**Stationary identities.** For any compactly supported invariant probability \(\mu\), invariance and smoothness imply \(\int\dot V\,d\mu=\int\dot z\,d\mu=0\). Thus
\[
\int(x^2+xy+y^2-x)\,d\mu=0,
\qquad\int(x^2+y^2-x)\,d\mu=0.
\]
Their difference is \(\int xy\,d\mu=0\), and completing the square in the second yields \(\int[(x-1/2)^2+y^2]d\mu=1/4\). Moreover \(0<\int x\,d\mu<1\): equality at either endpoint would force \(\mu\) onto \(x=y=0\) or \(x=1,y=0\), neither an invariant set because \(\dot y=1\) or \(\dot y=-1\), respectively.

## Verification
The standalone script `radial_flux_check.py` uses exact rational symbolic algebra to test the radial derivative, ellipse completion, determinant and area, mean projected squared radius, outgoing-flux integral coefficient, reversibility, and divergence. It was executed successfully using SymPy. The global-continuation and area-expansion steps are proved above; the checker does not replace these infinite-time arguments. An independent derivation via the divergence theorem gives \(\int_{S_R}F\cdot n\,dA=-8\pi R^3/3\) because \(\nabla\cdot F=2(y+z)\) and the ball is centered at \((1,0,-1)\), consistent with small positive leakage and much larger inward flux.

## Relationship to prior work
Sprott's original 2014 article supplies precisely this vector field and describes an inward-pointing vector field on large centered spheres except for small polar holes, based on numerical observations rather than an exact outgoing-area or flux coefficient. It also gives numerical evidence for boundedness. The present theorem computes the entire outward-pointing spherical region and its leading area and flux constants analytically, while proving two-sided global existence without asserting global boundedness. Sprott's 2015 paper reprises the flow and discusses symmetry and attractor geometry. Algaba, Merino, Qin and Rodríguez-Luis (2019) analyze Hopf-zero bifurcations and KAM dynamics in an embedding family; their publicly accessible material concerns a different question. Their full text could not be conclusively inspected, so overlap with an unlocated observation remains a residual priority risk.

## Limitations
The outgoing patches measure **instantaneous normal orientation**, not the set of initial conditions escaping to infinity. A sphere having outward points need not exclude a globally absorbing region of another shape. The \(O(\sqrt{|t|})\) growth estimate excludes finite-time explosion but does **not** prove that all trajectories remain uniformly bounded for infinite time, nor that any chaotic invariant set exists. A higher-order area or flux expansion is possible but is not needed here. Historical novelty is supported by source comparisons and searches, not formally certified by them; the 2019 full text remained inaccessible during this review. No independent audit has been performed.

## References
1. J. C. Sprott, “A dynamical system with a strange attractor and invariant tori,” *Physics Letters A* 378 (2014), 1361–1363. DOI: `10.1016/j.physleta.2014.03.028`. Author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper423.pdf. First verified public availability: 2014-03-21.
2. J. C. Sprott, “Symmetric Time-Reversible Flows with a Strange Attractor,” *International Journal of Bifurcation and Chaos* 25 (2015), 1550078. DOI: `10.1142/S0218127415500789`. Author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper433.pdf.
3. A. Algaba, M. Merino, B.-W. Qin and A. J. Rodríguez-Luis, “Study of a dynamical system with a strange attractor and invariant tori,” *Physics Letters A* 383 (2019), 1441–1449. DOI: `10.1016/j.physleta.2019.01.066`. Public article overview: https://doi.org/10.1016/j.physleta.2019.01.066.
