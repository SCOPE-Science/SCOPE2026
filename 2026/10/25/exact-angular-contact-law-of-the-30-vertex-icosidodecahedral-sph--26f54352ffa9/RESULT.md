# Exact angular contact law of the 30-vertex icosidodecahedral spherical code

## Finding

Let \(I\) be a regular icosahedron inscribed in the unit sphere, and let \(V\subset S^2\) comprise the normalized midpoints of its thirty edges. These points are the vertices of the regular icosidodecahedron, viewed as a thirty-site spherical code. Choose \(U\) uniformly on \(S^2\) and measure the geodesic nearest-site distance
\[
R(U)=\min_{v\in V}\arccos(U\cdot v).
\]
The exact cumulative distribution function is elementary, including all threshold values. Write
\[
\varphi=\frac{1+\sqrt5}{2},\quad a=\varphi^{-2},\quad b=\varphi^{-1},\quad\rho=\frac{\pi}{10},\quad\psi=\arctan(a/b),\quad r_1=\arctan a,\quad r_2=\arctan b.
\]
For \(\rho<r<r_2\) define
\[
\begin{aligned}
\delta(r)&=\arccos\!\left(\frac{\tan\rho}{\tan r}\right),\\
\ell(r)&=\max\{0,\psi-\delta(r)\},\\
h(r)&=\min\{\pi/2,\psi+\delta(r)\},\\
H(\theta)&=\arcsin\!\left(\cos\rho\,\sin(\theta-\psi)\right).
\end{aligned}
\]
Then for every real \(r\), \(F(r)=\Pr(R(U)\le r)=30Q(r)/\pi\), with
\[
Q(r)=\begin{cases}
0, &r\le0,\\
\frac\pi2(1-\cos r),&0<r\le\rho,\\
\frac\pi2(1-\cos r)+\cos r(h-\ell)-H(h)+H(\ell),&\rho<r<r_2,\\
\frac\pi{30},&r\ge r_2.
\end{cases}
\]
Here \(h\) and \(\ell\) in the middle branch mean \(h(r)\) and \(\ell(r)\). The lower and upper support endpoints are \(0\) and \(r_2\). The active boundary interval first appears at \(\rho=\pi/10\), meets the first quadrant coordinate boundary at \(r_1\), and complete coverage occurs at \(r_2\). At these three radii,
\[
F(\rho)=15(1-\cos(\pi/10)),\qquad F(r_1)=\frac{30}{\pi}Q(r_1),\qquad F(r_2)=1.
\]
Two sharp endpoint effects hold as \(\varepsilon\downarrow0\):
\[
15(1-\cos(\rho+\varepsilon))-F(\rho+\varepsilon)
\sim\frac{40}{\pi}\sqrt{2\tan\rho}\,\varepsilon^{3/2},
\]
and
\[
1-F(r_2-\varepsilon)\sim\frac{15a\sqrt{1+b^2}}{\pi b}\,\varepsilon^2.
\]
The former quantifies the first failure of disjoint-cap coverage; the latter quantifies the disappearance of the last uncovered neighborhoods of the face-center directions.

## Assumptions and scope

The metric is great-circle angular distance on the **unit sphere**, not Euclidean chord distance. Orientations use normalized spherical surface area and the thirty sites are all equally weighted. A concrete choice of the underlying unit icosahedron is obtained by normalizing all twelve vectors of the forms \((0,\pm1,\pm\varphi)\), \((\pm1,\pm\varphi,0)\), and \((\pm\varphi,0,\pm1)\). The edge pairs are precisely pairs with inner product \(1/\sqrt5\). All statements are exact for this code; no asymptotic site-count limit is assumed.

## Proof

**1. Site geometry and spherical Voronoi cells.** Two icosahedral neighboring unit vectors \(u,v\) have dot product \(c=1/\sqrt5\). Their normalized edge midpoint is \(q=(u+v)/\sqrt{2+2c}\). The convex hull of these thirty points is the rectified icosahedron, with twenty equilateral triangular faces corresponding to old faces and twelve regular pentagonal faces corresponding to old vertices. Every site is incident with exactly two faces of each type. Under spherical Voronoi--convex-hull duality, the four face-normal directions incident with \(q\) are the vertices of its spherical nearest-site cell.

For a pentagonal face corresponding to \(u\), the normal is \(u\) and the distance from \(q\) to it satisfies \(\cos r_2=\sqrt{(1+c)/2}\). Therefore \(\tan r_2=\varphi^{-1}=b\). For a triangular face with original vertices \(u,v,w\), the unit face normal is \((u+v+w)/\sqrt{3+6c}\); its angle from \(q\) is \(r_1\) with \(\tan r_1=\varphi^{-2}=a\). The tangent directions toward the two pentagonal normals are opposite along \(u-v\); those toward the two triangular normals are opposite along the perpendicular direction. Thus gnomonic projection at \(q\), using these orthogonal tangent coordinates, turns the spherical Voronoi cell into the planar quadrilateral
\[
\{(x,y):|x|/a+|y|/b\le1\}.
\]
The basic quadrant \(T=\{x,y\ge0:x/a+y/b\le1\}\) occurs four times at each of thirty sites. Its angular inradius \(\rho\) is determined by \(\tan\rho=(a^{-2}+b^{-2})^{-1/2}=\tan(\pi/10)\). This also proves the two corner-radius values and the whole-sphere decomposition up to measure-zero cell boundaries.

**2. Exact area of a truncated cell.** Write a unit direction in the quadrant in gnomonic polar form \((x,y)=(s\cos\theta,s\sin\theta)\), with \(0\le\theta\le\pi/2\). Its spherical angular radius is \(t=\arctan s\), so the sphere's surface-area element is \(\sin t\,dt\,d\theta\). The boundary radius of the Voronoi quadrant is
\[
\tan\alpha(\theta)=\frac{1}{\cos\theta/a+\sin\theta/b}
=\frac{\tan\rho}{\cos(\theta-\psi)}.
\]
Consequently, for every \(r\ge0\), its area within angular radius \(r\) is
\[
Q(r)=\int_0^{\pi/2}\bigl[1-\cos\min\{r,\alpha(\theta)\}\bigr]\,d\theta.
\]
For \(r\le\rho\), every direction has \(\alpha(\theta)\ge r\), giving \(Q(r)=\frac\pi2(1-\cos r)\). For \(\rho<r<r_2\), precisely the interval \(\ell(r)<\theta<h(r)\) has \(\alpha(\theta)<r\). We have
\[
\cos\alpha(\theta)=\frac{\cos\rho\,\cos(\theta-\psi)}{\sqrt{1-\cos^2\rho\,\sin^2(\theta-\psi)}}=H'(\theta).
\]
Subtracting the baseline integrand and integrating on that interval yields the stated middle branch. The cuts \(\ell=0\) or \(h=\pi/2\) start at \(r_1\) and \(r_2\), respectively, because \(\tan r_1=a\) and \(\tan r_2=b\) are the two corner distances. At \(r=r_2\), all points in the quadrant have been included. By thirty-fold and fourfold symmetry, \(120 Q(r)/(4\pi)=30Q(r)/\pi=F(r)\). The total area identity \(Q(r_2)=\pi/30\) follows both from the partition and directly from the endpoint primitive.

**3. Cap-overlap onset.** For \(r=\rho+\varepsilon\), the active interval remains internal and is symmetric about \(\psi\), with \(\delta(r)=\sqrt{2\varepsilon/(\sin\rho\cos\rho)}+O(\varepsilon^{3/2})\). The baseline full-quadrant cap area would give \(15(1-\cos r)\) after normalization. The loss equals \((30/\pi)\int_{\psi-\delta}^{\psi+\delta}(\cos\alpha(\theta)-\cos r)\,d\theta\). Expanding \(\alpha(\psi+z)=\rho+\frac12\sin\rho\cos\rho\,z^2+O(z^4)\) and the positive difference \(\cos\alpha-\cos r\) uniformly on this shrinking interval, then integrating the quadratic profile, gives exactly \((40/\pi)\sqrt{2\tan\rho}\,\varepsilon^{3/2}+o(\varepsilon^{3/2})\).

**4. Completion exponent.** As \(r\uparrow r_2\), only vanishing triangles near the two farthest cell corners remain uncovered. In gnomonic coordinates near a corner \((0,b)\), set \(z=b-y\ge0\). The diamond constraint becomes \(0\le x\le(a/b)z\), and the angular disk inequality \(\arctan\sqrt{x^2+y^2}>r_2-\varepsilon\) becomes \(0\le z<(1+b^2)\varepsilon+O(\varepsilon^2)\) at leading order. The gnomonic spherical Jacobian is \((1+x^2+y^2)^{-3/2}=(1+b^2)^{-3/2}+O(\varepsilon)\). Integration gives uncovered area at one such corner \(a\sqrt{1+b^2}\,\varepsilon^2/(2b)+O(\varepsilon^3)\). There are thirty cells with two such distant corners each, but four quadrants per cell; equivalently exactly one distant corner per quadrant. The whole-sphere normalization \(30/\pi\) then gives \(15a\sqrt{1+b^2}/(\pi b)\,\varepsilon^2+O(\varepsilon^3)\). This proves both coefficients.

## Verification

Run the embedded `verify_icosidodecahedral_cover.py` using Python 3 with NumPy and SciPy. It builds the original twelve icosahedral vertices and all thirty normalized edge midpoints; reconstructs the rectified convex hull and its twenty triangular and twelve pentagonal faces; verifies every site's face-normal radii, tangent orthogonality, and the gnomonic inradius; independently integrates the spherical quadrant area; samples 420,000 Haar-uniform orientations; and checks the two asymptotic coefficients. Its output must end in `ALL_ICOSIDODECAHEDRAL_SPHERICAL_COVERAGE_CHECKS_OK`.

The numerical hull inspection and finite samples cross-check, but do not constitute the infinite theorem: Steps 1--4 above are the mathematical proof. The verifier needs the referenced Python packages installed; its random generator uses a fixed seed.

## Relationship to prior work

Na, Lee, and Cheong (2001) develop spherical Voronoi diagrams and their convex-hull duality. That framework is used explicitly, not claimed as new. The thirty edge-midpoint sites and the rectified icosahedral combinatorics are standard. Wang and Lee (2011) analyze an icosahedral--hexagonal spherical grid; that work concerns geometric properties of related icosahedral grids, but full-text comparison was unavailable. The exact thirty-site nearest-angle CDF, its two interior regime thresholds, and the \(3/2\) and quadratic contact exponents are the claims evaluated here. Formula equivalences from Voronoi area integration are not misrepresented as a new general algorithm. Published results on random widths or section-side counts of the icosahedron do not imply this law: those statistics use other sites and other functions of orientation.

## Limitations

The law applies only to equal nearest-angle sites at the thirty normalized edge midpoints of the regular icosahedron and Haar-uniform directions. It does not cover arbitrary spherical nets, perturbations, other radial metrics, or location-dependent sampling. The geometric identities are exact; historical priority is provisional, especially where full text of the Wang--Lee paper was inaccessible. Independent validation has not been performed.

## References

1. H.-S. Na, C.-N. Lee, and O. Cheong, *Voronoi Diagrams on the Sphere*, Utrecht University technical report CS-2001-47, dated 22 June 2001. https://ics-archive.science.uu.nl/research/techreps/repo/CS-2001/2001-47.pdf
2. N. Wang and J.-L. Lee, *Geometric Properties of the Icosahedral-Hexagonal Grid on the Two-Sphere*, SIAM Journal on Scientific Computing (2011), DOI:10.1137/090761355. Full text not inspected.
3. Standard rectification of the icosahedron into the icosidodecahedron and duality of convex-hull face normals with spherical nearest-site Voronoi cells; the explicit derivation is in the proof above.
