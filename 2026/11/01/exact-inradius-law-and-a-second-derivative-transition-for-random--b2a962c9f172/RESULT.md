# Exact inradius law and a second-derivative transition for random octahedron sections

## Finding
Let \(O=\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le1\}\), and choose a two-plane \(H=U^\perp\) through its center using Haar probability measure, where \(U\) is uniform on \(S^2\). Write \(R\) for the intrinsic Euclidean inradius of \(O\cap H\). Its distribution is continuous, has support exactly \([1/\sqrt3,1/\sqrt2]\), and has the following elementary closed form.

For \(0\le t\le1\), put
\[
\begin{aligned}
P_+(t)&=\frac6\pi\left[\frac\pi2-\frac{\pi t}{3\sqrt3}
 -2\arcsin\frac1{\sqrt{3-t^2}}
 +\frac{2t}{\sqrt3}\arctan\frac{t}{\sqrt{3(2-t^2)}}\right],\\
P_-(t)&=\begin{cases}
\displaystyle\frac2\pi\left(3\alpha(t)-\pi-\sqrt3\,t\,\theta(t)\right),&0\le t<1/\sqrt3,\\
0,&1/\sqrt3\le t\le1,
\end{cases}\\
\alpha(t)&=\arccos\frac{1+t^2}{3-t^2},\\
\theta(t)&=\arccos\left(\frac{a(t)^2+2a(t)t-t^2/3}{1-t^2/3}\right),\\
a(t)&=\sqrt{\frac{1-t^2}{2}}.
\end{aligned}
\]
Then for \(1/\sqrt3\le r\le1/\sqrt2\), with \(t(r)=\sqrt{3-r^{-2}}\),
\[
\boxed{\mathbb P\{R\le r\}=1-P_+(t(r))-P_-(t(r)).}
\]
The cumulative distribution is zero below the displayed support and one above it. There is precisely one interior change of analytic formula, at \(r_*=\sqrt{3/8}\). More sharply, the cumulative distribution is continuously differentiable but **not** twice differentiable at \(r_*\), and the one-sided second derivatives satisfy
\[
\boxed{F_R''(r_*^-)-F_R''(r_*^+)=-\frac{256\sqrt3}{\pi}.}
\]

## Assumptions and scope
All norms, radii, sections, and projections are Euclidean. The octahedron has vertices \(\pm e_1,\pm e_2,\pm e_3\); its edge length is \(\sqrt2\). The inradius is the radius of the largest disk *contained in the section*, not the inradius of the **orthogonal projection** of the octahedron. Haar measure on unoriented planes is induced by a uniform unit normal, identifying \(U\) and \(-U\). A central section is centrally symmetric, so an inball centered at the origin always realizes the inradius. All endpoint events of equalities have spherical measure zero.

## Proof
**1. Deterministic inradius.** Let \(C=[-1,1]^3=O^\circ\). Polarity inside \(H\) gives \((O\cap H)^{\circ,H}=P_H C\); hence its centered inradius is the reciprocal of the circumradius of \(P_H C\). The projected cube is the convex hull of its eight projected sign vertices. Thus
\[
R^{-2}=\max_{\varepsilon\in\{-1,1\}^3}\|P_H\varepsilon\|_2^2
=3-\min_{\varepsilon\in\{-1,1\}^3}(\varepsilon\cdot U)^2.
\]
If \(a\ge b\ge c\ge0\) are the three ordered absolute coordinates of \(U\), the smallest signed sum magnitude is \(|a-b-c|\), because the other possible magnitudes are \(a+b-c\), \(a-b+c\), and \(a+b+c\), all no smaller. Consequently,
\[
\boxed{R=(3-(a-b-c)^2)^{-1/2}.}
\]
The quantity \(q=a-b-c\) ranges over the full interval \([-1/\sqrt3,1]\): the minimum occurs at \(a=b=c=1/\sqrt3\) and the maximum at a coordinate axis. Indeed \(b+c-a\le (a+b+c)/3\le1/\sqrt3\) whenever \(a\ge b\ge c\), with equality at the diagonal (alternatively optimize on the positive spherical chamber). This establishes the support interval after squaring. For the threshold \(t=\sqrt{3-r^{-2}}\), the event \(R\le r\) is exactly \(|q|\le t\).

**2. Positive tail \(P_+\).** The event \(q>t\) is the disjoint union, apart from boundaries, of six equivalent spherical regions where one absolute coordinate exceeds the sum of the other two plus \(t\). Working with \(x,y,z\ge0\) and \(x>y+z+t\), write
\[
x=\cos\vartheta,\qquad y=\sin\vartheta\cos\phi,\qquad z=\sin\vartheta\sin\phi,
\quad0\le\phi\le\pi/2.
\]
Set \(b=\cos\phi+\sin\phi\). The permitted polar interval is \(0\le\vartheta<\vartheta_*(\phi)\), where
\[
\cos\vartheta_*=\frac{t+b\sqrt{1+b^2-t^2}}{1+b^2}.
\]
There are 24 congruent signed-and-permuted quadrants of this form; dividing their areas by \(4\pi\),
\[
P_+(t)=\frac6\pi\int_0^{\pi/2}\left[1-\frac{t+b\sqrt{1+b^2-t^2}}{1+b^2}\right]d\phi.
\]
The elementary integrals required here are
\[
\int_0^{\pi/2}\frac{d\phi}{1+b^2}=\frac\pi{3\sqrt3},\qquad
\int_0^{\pi/2}\frac{b\sqrt{1+b^2-t^2}}{1+b^2}\,d\phi
=2\arcsin\frac1{\sqrt{3-t^2}}-\frac{2t}{\sqrt3}\arctan\frac{t}{\sqrt{3(2-t^2)}}.
\]
For the second identity, split at \(\phi=\pi/4\), use \(z=|\cos\phi-\sin\phi|\), and integrate \(2\int_0^1\sqrt{3-t^2-z^2}/(3-z^2)\,dz\). Substitution proves the stated \(P_+\).

**3. Negative tail \(P_-\).** The event \(q<-t\) is nonempty precisely when \(t<1/\sqrt3\). In each of the eight absolute-coordinate octants it is the curvilinear spherical triangle cut out by
\[
(-1,1,1)\cdot u>t,\quad(1,-1,1)\cdot u>t,\quad(1,1,-1)\cdot u>t.
\]
Its vertices are the permutations of \((a(t),a(t),t)\). The three interior angles are \(\alpha(t)\): at any vertex the two inward normals projected into the tangent plane have mutual angle \(\pi-\alpha(t)\). The three boundary arcs lie on small circles of spherical (signed) geodesic curvature \(t/\sqrt{3-t^2}\) and each has length \(\sqrt{1-t^2/3}\,\theta(t)\), with the displayed \(\theta(t)\) supplied by the spherical circle cosine rule. Gauss–Bonnet on the unit sphere therefore gives the triangle area
\[
\operatorname{Area}(T_t)=3\alpha(t)-\pi-\sqrt3\,t\,\theta(t).
\]
Eight octants divided by spherical area \(4\pi\) give \(P_-(t)=2\operatorname{Area}(T_t)/\pi\). This proves the cumulative distribution, including both endpoints and absence of atoms: all threshold sets lie on finitely many spherical curves.

**4. The sharp differentiability transition.** Write \(t_c=1/\sqrt3\) and \(\delta=t_c-t\downarrow0\). The negative-tail spherical triangle collapses to \(u_0=(1,1,1)/\sqrt3\). Its three bounding small circles have tangent-plane normals of equal norm \(\sqrt{8/3}\), separated by \(120^\circ\). After rescaling by \(\delta^{-1}\) in the tangent plane, the triangle converges to an equilateral triangle of inradius \(\sqrt{3/8}\). Smoothness of the defining small circles gives the quantitative expansion
\[
\operatorname{Area}(T_t)=\frac{9\sqrt3}{8}(t_c-t)^2+O((t_c-t)^3).
\]
Thus
\[
P_-(t)=\frac{9\sqrt3}{4\pi}(t_c-t)_+^2+O((t_c-t)_+^3).
\]
Meanwhile \(P_+(t)\) is real analytic near \(t_c\); so is the map \(t(r)=\sqrt{3-r^{-2}}\), with \(t'(r_*)=16\sqrt2/3\). The expansion proves continuous first derivatives and a nonzero jump in the second derivative of \(F_R=1-P_+-P_-\). Its left-minus-right jump is \(-2\cdot(9\sqrt3/(4\pi))\cdot(16\sqrt2/3)^2=-256\sqrt3/\pi\), as claimed. \(\square\)

## Verification
Run `python3 verify.py` in a Python 3 standard-library environment. It independently constructs central section polygons by intersecting all twelve octahedron edges with deterministic sample planes and compares their intrinsic inradii with the polar formula; numerically integrates the spherical positive-tail area independently of the closed form; checks endpoints and range; and compares the complete law with 150,000 independently sampled uniform normals. It completed 533 diagnostics. These finite numerical checks support but do not replace the analytic proof. The proof of the non-differentiability threshold is geometric and asymptotic; no finite simulation is presented as its certificate.

## Relationship to prior work
Brazitikos and Pandis (2026) study extremal **volumes** of restricted cross-polytope and simplex sections and provide motivating section geometry; they do not derive an inradius distribution. The published exact inradius law for random *orthogonal projections of the regular octahedron* concerns a different dual operation: the polar is a **cube section**, whereas the polar of our **octahedron section** is a **cube projection**. The two statistics differ even at the body-diagonal normal. The published exact Haar diameter law for **central sections of the regular octahedron** is likewise different: its diameter depends only on the smallest-to-largest coordinate ratio of the plane normal, whereas the present inradius depends on all three coordinates. The older width law for the octahedron is a one-direction support-function statistic, not the inradius of a planar section.

## Limitations
The result is exact for Haar-uniform **central planar sections** of the three-dimensional regular octahedron at the specified unit-vertex normalization. No claim is made for random affine sections, non-Haar sampling, other polyhedra, or higher dimensions. Earlier specialized geometric-probability or stereological calculations under alternative terminology may contain an equivalent formula; absence from indexed searches is not a proof of historical priority. The exact curvature of the cumulative distribution at its two endpoint radii is not classified. No independent mathematical validation is asserted.

## References
1. S. Brazitikos and C. Pandis, *Restricted Hyperplane Sections of the Cross-Polytope and the Simplex*, arXiv:2606.07163v1, first posted 5 June 2026; full text https://arxiv.org/abs/2606.07163.
2. *Exact inradius law for random planar projections of the regular octahedron*, public mathematical result, 11 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-inradius-law-for-random-planar-projections-of-the-regular--5fbcddcea5e5 (full RESULT.md compared).
3. *Exact Haar diameter law for central sections of the regular octahedron*, public mathematical result, 11 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-haar-diameter-law-for-central-sections-of-the-regular-octa--4948185eba2f (full RESULT.md compared).
4. *Exact width distribution of the unit-edge regular octahedron*, public mathematical result, 11 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-width-distribution-of-the-unit-edge-regular-octahedron--953206d3d8c4 (full RESULT.md compared).
5. A. Hmadi and D.-M. Liakopoulos, *Negative moments of the support function and applications to isotropic convex bodies*, arXiv:2609.27757v1 (related random projection inradius bounds; source accessibility limited).
