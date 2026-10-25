# An interior logarithmic singularity and two sharp endpoint laws for random octahedron sections

## Finding
Let
\[
O=\{(x_1,x_2,x_3)\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le1\},
\]
let \(U\) be Haar-uniform on the Euclidean unit sphere, and let \(X\) be the Euclidean area of the central section \(O\cap U^\perp\). Then \(X\) is nonatomic, has support exactly
\[
\left[\frac{3\sqrt3}{4},\,2\right],
\]
and has a locally integrable density \(f_X\). The only interior critical value of its direction-to-area map is \(\sqrt2\); on the two sides of this value,
\[
\boxed{\quad f_X(s)=\frac{\sqrt6}{\pi}\log\frac1{|s-\sqrt2|}+O(1),\qquad s\to\sqrt2,\ s\ne\sqrt2.\quad}
\]
Both endpoints have different probabilistic orders. For \(\varepsilon\downarrow0\),
\[
\boxed{\quad \Pr\left(X<\frac{3\sqrt3}{4}+\varepsilon\right)
=\frac{64}{9\sqrt3}\,\varepsilon+o(\varepsilon),\quad}
\]
and
\[
\boxed{\quad \Pr(X>2-\varepsilon)
=\left(\frac1{2\pi}+\frac{\sqrt3}{9}\right)\varepsilon^2+o(\varepsilon^2).\quad}
\]
The logarithm comes from twelve nondegenerate saddle normals corresponding to square sections, while the lower and upper tails come respectively from eight regular-hexagon normals and six axial square-section normals. In particular, the logarithmic singularity is an intrinsic feature of the pushforward of spherical orientation measure, not of any random affine-offset model.

## Assumptions and scope
All areas use ordinary Euclidean area in the section plane. The octahedron has vertices \(\pm e_1,\pm e_2,\pm e_3\); its edge length is \(\sqrt2\). An unoriented Haar-uniform plane is represented by its uniformly distributed unit normal \(U\), with antipodal normals counted separately in spherical integration. Write \(a=|U_1|\), \(b=|U_2|\), and \(c=|U_3|\). For positive \(a,b,c\), the exact section area is
\[
\boxed{\quad
F(a,b,c)=\frac{2(ab+ac+bc)}{(a+b)(a+c)(b+c)}
\quad}\qquad(a^2+b^2+c^2=1).
\]
At normals with one zero coordinate it extends continuously; at coordinate-axis normals the limiting area equals \(2\). In homogeneous, unnormalized coordinates the numerator is multiplied by \(\sqrt{a^2+b^2+c^2}\). This distinction is essential to the stationary-point and local-Hessian calculations. The probability law is not that of the section diameter, section perimeter, octahedron chord length, or projected area.

## Proof
**1. Exact six-vertex area identity.** In the positive octant, a generic central plane intersects the six octahedron edges joining \(+e_i\) to \(-e_j\) for \(i\ne j\). Their intersection points are
\[
v_{ij}=\frac{u_je_i-u_ie_j}{u_i+u_j},\qquad i\ne j,
\]
where \(u=(a,b,c)\) is a unit normal. The cyclic vertex order is \(v_{21},v_{31},v_{32},v_{12},v_{13},v_{23}\). The oriented shoelace expression in the plane, \(\frac12\sum_k u\cdot(v_k\times v_{k+1})\), simplifies to
\[
\frac{2(ab+ac+bc)}{(a+b)(a+c)(b+c)}.
\]
Symmetry across the three coordinate planes replaces the coordinates by their absolute values. The formula and its limiting values hold at nongeneric orientations by continuity. This identity was also checked directly against six computed section vertices rather than using a preexisting random-section formula.

**2. All critical normals and support.** Work with the degree-zero extension
\[
\widetilde F(a,b,c)
=\frac{2\sqrt{a^2+b^2+c^2}(ab+ac+bc)}{(a+b)(a+c)(b+c)}.
\]
Its gradient is orthogonal to the radial vector. Consequently a stationary point on the unit sphere in the strictly positive octant is precisely a zero of its ambient gradient. Put \(Q=a^2+b^2+c^2\) and \(S=ab+ac+bc\). The difference of the logarithmic partial derivatives in the first two coordinates factors as
\[
\partial_a\log\widetilde F-\partial_b\log\widetilde F
=(a-b)\left[\frac1Q-\frac1S+\frac1{(a+c)(b+c)}\right],
\]
with analogous identities for the remaining pairs. If all three coordinates were distinct at a stationary point, all three bracketed quantities would vanish. Their last summands would then be equal, forcing equal coordinates, a contradiction. Hence at least two coordinates are equal. Along \((a,b,c)=(1,1,t)\),
\[
\widetilde F(1,1,t)=\frac{\sqrt{2+t^2}(1+2t)}{(1+t)^2},\qquad
\frac{d}{dt}\widetilde F(1,1,t)
=\frac{3t(t-1)}{(1+t)^3\sqrt{2+t^2}}.
\]
For \(t>0\) the only stationary choice is \(t=1\). Thus the eight body-diagonal normals are all the smooth interior stationary points, with value \(3\sqrt3/4\).

On a coordinate great circle (say \(c=0\)), the exact area is \(2/(a+b)\) for \(a,b>0\) and \(a^2+b^2=1\), with its sole relative stationary point at \(a=b=1/\sqrt2\), of value \(\sqrt2\). The six axis normals have value \(2\). Comparison of these finitely many values and compactness give the exact range and locate all potential density singularities. Since nonconstant analytic level sets have two-dimensional spherical measure zero within an octant, and the octant seams have spherical measure zero, \(X\) has no atoms. The coarea formula on the regular regions gives its density.

**3. Minimum: eight quadratic wells.** Near \((1,1,1)/\sqrt3\), consider the normalized direction proportional to \((1+t,1,1)\). Taylor expansion of the exact formula gives
\[
\widetilde F(1+t,1,1)=\frac{3\sqrt3}{4}
+\frac{\sqrt3}{16}t^2+O(t^3).
\]
The corresponding spherical angular distance is \(\frac{\sqrt2}{3}|t|+O(t^2)\). Threefold symmetry about the diagonal makes the tangential quadratic form isotropic, hence in orthonormal tangential coordinates \((x,y)\),
\[
F=\frac{3\sqrt3}{4}+\frac{9\sqrt3}{32}(x^2+y^2)
+O((x^2+y^2)^{3/2}).
\]
Each of the eight wells contributes spherical area \(\pi\varepsilon/(9\sqrt3/32)+o(\varepsilon)\). Division by total spherical area \(4\pi\) gives the coefficient \(8/[4(9\sqrt3/32)]=64/(9\sqrt3)\).

**4. Interior: twelve quadratic saddles.** Near \((1,1,0)/\sqrt2\), set
\[
u(x,y)=\bigl(\sqrt{1-y^2}\cos(\pi/4+x),\ 
\sqrt{1-y^2}\sin(\pi/4+x),\ y\bigr).
\]
These coordinates have exact spherical area element \(dx\,dy\). The section area is an even function of \(y\), obtained by replacing \(y\) with \(|y|\) in the homogeneous formula. The first \(|y|\) derivative vanishes at zero, and direct expansions give
\[
F(u(x,y))=\sqrt2+\frac{\sqrt2}{2}x^2
-\frac{3\sqrt2}{2}y^2+O((x^2+y^2)^{3/2}).
\]
Thus the quadratic coefficients are \(\alpha=\sqrt2/2\) and \(\beta=3\sqrt2/2\), with \(\alpha\beta=3/2\). The map is \(C^2\) across \(y=0\), piecewise analytic, and its quadratic saddle is nondegenerate. In local Morse coordinates, the pushforward of planar area by \(\alpha x^2-\beta y^2\) has density
\[
\frac{1}{\sqrt{\alpha\beta}}\log\frac1{|s|}+O(1).
\]
One obtains this coefficient directly by integrating \(\delta(s-\alpha x^2+\beta y^2)\) first in \(y\). The small coordinate change has Jacobian \(1+O(\sqrt{x^2+y^2})\), whose contribution to the density remains bounded; the piecewise-cubic remainder is likewise harmless. There are precisely twelve such signed permutation normals, so Haar normalization yields
\[
\frac{12}{4\pi\sqrt{3/2}}=\frac{\sqrt6}{\pi}.
\]
All other normals mapping close to \(\sqrt2\) are regular and give a bounded density contribution. This proves the two-sided singularity.

**5. Maximum: six nonsmooth axial peaks.** Near \((1,0,0)\), work in each coordinate-sign quadrant, with \(b,c\ge0\) small and normal proportional to \((1,b,c)\). Uniformly in angle,
\[
2-\widetilde F(1,b,c)
=2\frac{b^2+bc+c^2}{b+c}+O(b^2+c^2).
\]
In polar coordinates \(b=r\cos\phi\), \(c=r\sin\phi\), \(0\le\phi\le\pi/2\), the admissible radius for deficit smaller than \(\varepsilon\) is
\[
r<\frac\varepsilon2\frac{\cos\phi+\sin\phi}{1+\sin\phi\cos\phi}+O(\varepsilon^2).
\]
One quadrant therefore contributes spherical area \(\varepsilon^2 I/8+o(\varepsilon^2)\), where
\[
I=\int_0^{\pi/2}\frac{(\cos\phi+\sin\phi)^2}{(1+\sin\phi\cos\phi)^2}\,d\phi
=\int_0^\infty\frac{(1+t)^2}{(1+t+t^2)^2}\,dt
=\frac23+\frac{4\pi}{9\sqrt3}.
\]
There are six axis normals and four adjacent quadrants per axis, disjoint up to null sets. Dividing \(24(\varepsilon^2I/8)\) by \(4\pi\) gives \(3I/(4\pi)=1/(2\pi)+\sqrt3/9\), as claimed. The area-element correction near an axis is \(1+O(r^2)\) and does not affect this coefficient.

## Verification
Run `python3 verify.py` with Python 3; it requires no third-party libraries. It independently constructs all six polygon vertices for 250 positive-coordinate normals and compares their three-dimensional shoelace areas with the rational section formula. It checks the lower quadratic well, interior saddle Hessian, five directional axis asymptotics, and evaluates the angular integral by composite Simpson quadrature against its closed form. It additionally compares the two endpoint predictions with 480,000 directly generated Haar normals using a fixed seed. Each test is a finite diagnostic; the stated limit theorems follow from the analytical proof, not from the simulations. The package contains the complete verifier.

## Relationship to prior work
Ciccariello's arXiv:1401.7950 (initial posting January 30, 2014) computes the distribution of *chord lengths* of the regular octahedron under a different integral-geometric sampling law. A chord-length statistic integrates over affine line positions and does not determine the orientation-to-central-section-area distribution. The full accessible scientific article, including its definitions, central calculations and conclusion, was compared with the present statement.

Meyer and Pajor (1988) study volumes of sections of \(\ell_p\) balls and provide relevant general geometric background; a bibliographic record and abstract were available, but their full paper was not inspected. The public finding titled *Exact Haar diameter law for central sections of the regular octahedron* determines the distribution of a different functional, the section diameter. Indeed, that diameter depends only on the ratio of the smallest and largest absolute normal coordinates, whereas the area above varies as the intermediate coordinate varies with the two extremes fixed: the normals proportional to \((3,2,1)\) and \((3,3/2,1)\) have the same section diameter but areas \(11\sqrt{14}/30\) and \(7/5\), respectively. The public *Exact local Hessian phase diagram for two conjectural cross-polytope section maximizers* concerns restricted normal families in other dimensions, not the Haar pushforward distribution in dimension three. These comparisons establish nonimplication from the inspected results, not definitive priority over all possible literature.

## Limitations
The theorem is specific to three-dimensional central sections of the fixed regular octahedron with Haar-distributed normals. It does not give a closed elementary CDF for every interior threshold, a rate for the displayed \(o(\cdot)\) remainders, results for translated planes, or a uniform extension to all cross-polytopes. Priority may be affected by older, unindexed formulas for random octahedral sections; in particular, the full 1988 Meyer–Pajor paper was not available for an implication-by-implication inspection. Independent mathematical validation has not been performed.

## References
- S. Ciccariello, *The chord-length probability density of the regular octahedron*, arXiv:1401.7950v1, first posted 2014-01-30. https://arxiv.org/abs/1401.7950
- M. Meyer and A. Pajor, *Sections of the unit ball of \(\ell_p^n\)*, Journal of Functional Analysis 80 (1988), 109–123. DOI: 10.1016/0022-1236(88)90068-7.
- *Exact Haar diameter law for central sections of the regular octahedron*, public geometric-research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-diameter-law-for-central-sections-of-the-regular-octa--4948185eba2f.
- *Exact local Hessian phase diagram for two conjectural cross-polytope section maximizers*, public geometric-research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-local-hessian-phase-diagram-for-two-conjectural-cross-poly--77988d83412a.
