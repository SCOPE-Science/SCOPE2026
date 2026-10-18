# The exact nearest-direction law of the regular icosahedron

## Finding
Let \(V\subset S^2\) be the twelve vertices of a regular icosahedron inscribed in the unit sphere. For Haar-uniform \(U\in S^2\), put
\[
\Theta=\min_{v\in V}\arccos\langle U,v\rangle.
\]
Set
\[
\rho=\tfrac12\arccos(1/\sqrt5),\qquad
R=\arccos\sqrt{(1+2/\sqrt5)/3},
\]
and, for \(\rho<t<R\),
\[
\alpha(t)=\arccos\!\left(\frac{\tan\rho}{\tan t}\right),\qquad
S(t)=2\left[\arccos\!\left(\frac{\sin\rho}{\sin t}\right)
-\cos t\,\alpha(t)\right].
\]
The complete cumulative distribution function is
\[
\boxed{\Pr(\Theta\le t)=
\begin{cases}
0,&t<0,\\
6(1-\cos t),&0\le t\le\rho,\\
6(1-\cos t)-\dfrac{15}{\pi}S(t),&\rho<t<R,\\
1,&t\ge R.
\end{cases}}
\]
In particular, its density is \(6\sin t\) for \(0<t<\rho\) and
\[
6\sin t\left[1-\frac5\pi\alpha(t)\right]
\]
for \(\rho<t<R\). The two endpoints have different sharp power laws: as \(\varepsilon\downarrow0\),
\[
\boxed{6(1-\cos(\rho+\varepsilon))-
\Pr(\Theta\le\rho+\varepsilon)
=\frac{20}{\pi}\sqrt{2\tan\rho}\,\varepsilon^{3/2}
+O(\varepsilon^{5/2})}
\]
and
\[
\boxed{\Pr(\Theta>R-\varepsilon)
=\frac{15\tan\rho}{\pi\sin R\sin(\pi/5)}\,
\varepsilon^2+O(\varepsilon^3).}
\]
There is also an exact quadratic-nearest-site chord loss. Writing
\(\ell=\arccos(\sqrt5/3)\) for one side of a spherical Voronoi pentagon,
\[
\boxed{\mathbb E\min_{v\in V}\|U-v\|^2
=2-\frac{15}{\pi}\,\ell\sin\rho
=0.16825138764926\ldots.}
\]
The packing threshold and covering radius are approximately \(31.7175^\circ\) and \(37.3774^\circ\), respectively. The probabilities are normalized by the surface area \(4\pi\), not by the area of a single cap.

## Assumptions and scope
The sphere is the Euclidean unit two-sphere with its normalized rotation-invariant area measure; the twelve vertices have the usual regular-icosahedral adjacency. The spherical distances are shorter-arc geodesic angles. The theorem describes this fixed twelve-point configuration, not an optimization over arbitrary twelve-point sets. Nearest-site ties have zero area. All angles in the formulas are in radians.

## Proof
**Voronoi geometry.** Adjacent unit icosahedral vertices have scalar product \(1/\sqrt5\), hence spherical separation \(2\rho\). The nearest-site spherical Voronoi decomposition consists of twelve congruent regular spherical pentagons. At a chosen site \(v\), the five bisecting great circles stand at geodesic distance \(\rho\) from \(v\); their outward azimuths are separated by \(2\pi/5\). Their intersections are the dual face normals. Each triangular icosahedral face has three unit vertices of mutual scalar product \(c=1/\sqrt5\), so its normalized sum has scalar product \(\sqrt{(1+2c)/3}\) with each vertex; consequently every pentagonal Voronoi corner lies at angular distance \(R\) from \(v\). The five corners in a cell are mutually separated in azimuth by \(2\pi/5\), giving spherical edge length
\[\ell=\arccos\bigl(\cos^2R+\sin^2R\cos(2\pi/5)\bigr)=\arccos(\sqrt5/3).\]

**Spherical-cap clipping.** Use polar coordinates \((s,\varphi)\) about one site, with a bisecting great-circle boundary centered on azimuth zero. Within the sector \(|\varphi|\le\pi/5\), the boundary radial distance \(b(\varphi)\) satisfies
\[
\tan b(\varphi)=\frac{\tan\rho}{\cos\varphi},\qquad
b(0)=\rho,\quad b(\pm\pi/5)=R.
\]
Thus the one-cell area inside a polar cap of radius \(t\) is exactly
\[
A(t)=5\int_{-\pi/5}^{\pi/5}
\bigl(1-\cos\min\{t,b(\varphi)\}\bigr)\,d\varphi.
\]
The cells partition the sphere, so the desired CDF is \(12A(t)/(4\pi)\). For \(t\le\rho\), the full cap is contained in the cell, yielding \(6(1-\cos t)\). For \(\rho<t<R\), only azimuths \(|\varphi|<\alpha(t)\) extend past an individual side, where \(\alpha(t)=\arccos(\tan\rho/\tan t)<\pi/5\). Because the five forbidden azimuth intervals are disjoint, the cap-minus-cell area is exactly five times the **single-side** segment
\[
S(t)=2\int_0^{\alpha(t)}\bigl(\cos b(\varphi)-\cos t\bigr)\,d\varphi.
\]
By differentiation, \(S'(t)=2\sin t\,\alpha(t)\) and \(S(\rho)=0\). Direct integration, or differentiation of the displayed elementary expression for \(S\), gives the claimed \(S(t)\). Therefore
\(A(t)=2\pi(1-\cos t)-5S(t)\), which yields the middle CDF branch. For \(t\ge R\) the whole cell has been reached, so the CDF is one. Differentiation gives the density and continuity at both thresholds.

**Sharp onset and terminal asymptotics.** From \(\tan\rho/\tan(\rho+\varepsilon)=1-\varepsilon/(\sin\rho\cos\rho)+O(\varepsilon^2)\),
\[
\alpha(\rho+\varepsilon)=
\sqrt{\frac{2}{\sin\rho\cos\rho}}\,\varepsilon^{1/2}
+O(\varepsilon^{3/2}).
\]
Integrating \(S'(t)=2\sin t\,\alpha(t)\) gives
\(S(\rho+\varepsilon)=\frac43\sqrt{2\tan\rho}\,\varepsilon^{3/2}+O(\varepsilon^{5/2})\), and multiplication by \(15/\pi\) proves the first assertion. At \(R\), \(\alpha(R)=\pi/5\); direct differentiation gives
\[
\alpha'(R)=\frac{\tan\rho}{\sin^2R\sin(\pi/5)},\qquad
F'(R-)=0,\qquad
F''(R-)=-\frac{30\tan\rho}{\pi\sin R\sin(\pi/5)}.
\]
The terminal Taylor expansion establishes the second assertion with its strictly positive constant.

**Quadratic chord loss.** The function \(g(u)=\langle u,v\rangle\) satisfies \(\Delta_{S^2}g=-2g\). On each of the five geodesic edges of the Voronoi cell of \(v\), its outward spherical normal derivative is the constant \(-\sin\rho\). The surface divergence theorem therefore gives
\[
\int_{\mathrm{cell}(v)}\langle u,v\rangle\,d\sigma(u)
=\tfrac12\,5\ell\sin\rho.
\]
Averaging the twelve congruent cells and dividing by \(4\pi\) yields
\(\mathbb E\max_{v\in V}\langle U,v\rangle=15\ell\sin\rho/(2\pi)\). Since \(\min_v\|U-v\|^2=2(1-\max_v\langle U,v\rangle)\), the stated expectation follows.

## Verification
The standalone standard-library program `check.py` checks twelve explicit icosahedral vertices, the polar-cell area, the complete CDF against independent radial quadrature at 21 radii, monotonicity, the two endpoint coefficients, the exact first dot-product moment by independent angular quadrature, and 100,000 direct uniform-sphere samples. Execute `python3 check.py`. Its expected success marker is `ICOSAHEDRAL_NEAREST_LAW_OK`. Finite computations corroborate the exact proof; they do not certify global priority or replace the analytical arguments.

## Relationship to prior work
Fowler, Tarnai and Gáspár (2002, §3(a)) identify the regular icosahedron as an established twelve-cap arrangement throughout the packing-to-covering range, and record the classical endpoint radii. No new packing/covering optimality is claimed here. Their coverage observable agrees with the CDF here but the inspected article does not give the analytic full-radius distribution, the explicit critical coefficients or the exact quadratic chord loss.

Mazonka (2012, §4.1, Eq. 41) derives the spherical-cap segment area used as one classical ingredient of the formula. The mathematical contribution assessed here is the **specific exact complete twelve-site law, the two endpoint expansions and the integral moment** from the pentagonal Voronoi decomposition, not the elementary segment formula itself. Earlier general spherical-covering tables record the endpoint, not the complete function. Relevant 2016 comparisons of point configurations discuss spherical Voronoi geometry and icosahedral nodes, not the present finite twelve-site distribution.

## Limitations
The result is specific to exactly twelve regular-icosahedral site directions with uniform spherical sampling. It neither claims an optimal **average** quadratic quantization loss among all twelve-site configurations nor establishes statistical estimation bounds. Historical priority for an equivalent closed expression under alternative terminology remains subject to additional literature inspection. The proof is purely mathematical; numerical checks are supplementary.

## References
1. P. W. Fowler, T. Tarnai, and Zs. Gáspár, “From circle packing to covering on a sphere with antipodal constraints,” *Proceedings of the Royal Society A* **458** (2002), 2275–2287, published online 24 July 2002, DOI: 10.1098/rspa.2002.0990. Full text: https://www.researchgate.net/publication/243685417_From_circle_packing_to_covering_on_a_sphere_with_antipodal_constraints.
2. O. Mazonka, “Solid Angle of Conical Surfaces, Polyhedral Cones, and Intersecting Spherical Caps,” arXiv:1205.1396 (4 May 2012), §4.1, https://arxiv.org/abs/1205.1396. Accessible full text: https://www.researchgate.net/publication/224907418_Solid_Angle_of_Conical_Surfaces_Polyhedral_Cones_and_IntersectingSpherical_Caps.
3. D. P. Hardin, T. Michaels, and E. B. Saff, “A Comparison of Popular Point Configurations on the Two-Sphere,” arXiv:1607.04590 (13 July 2016), particularly §1.2 and the icosahedral node constructions, https://arxiv.org/abs/1607.04590.
