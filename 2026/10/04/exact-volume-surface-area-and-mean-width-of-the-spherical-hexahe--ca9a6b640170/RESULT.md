# Exact volume, surface area, and mean width of the spherical hexahedron
## Finding
Let
\[
K=\bigcap_{j=1}^{3}\left(B(e_j/\sqrt2,1)\cap B(-e_j/\sqrt2,1)\right)\subset\mathbb R^3
\]
be the intersection of the six unit balls centered at \(\pm e_1/\sqrt2\), \(\pm e_2/\sqrt2\), and \(\pm e_3/\sqrt2\). Set
\[
\alpha=\arccos(23/27).
\]
Then
\[
\operatorname{Vol}(K)=\frac{4\pi}{3}+\frac{2}{3\sqrt2}-\frac{49}{6}\alpha
=0.158029005045087\ldots,
\]
\[
\operatorname{Area}(\partial K)=4\pi-20\alpha
=1.540658645708557\ldots,
\]
and, with the mean-width normalization in Finch's paper,
\[
w(K)=2+\left(\frac{\sqrt3}{2}-\frac{10}{\pi}\right)\alpha
=0.722630772064860\ldots.
\]
The eight vertices are
\[
\left(\frac{\varepsilon_1}{3\sqrt2},\frac{\varepsilon_2}{3\sqrt2},\frac{\varepsilon_3}{3\sqrt2}\right),
\qquad \varepsilon_j\in\{-1,1\},
\]
so adjacent vertices are separated by \(\lambda=\sqrt2/3\). Thus
\[
\frac{\operatorname{Vol}(K)}{\lambda^3}=1.508535644735845\ldots,
\]
which agrees with the numerical value \(1.508\ldots\) reported with the original unanswered question.

## Assumptions and scope
All six balls have radius \(1\), and their centers are the six vertices of the regular octahedron \(\{\pm e_j/\sqrt2:1\le j\le3}\). Volume is ordinary Euclidean volume and surface area is the area of the six exposed spherical patches. Mean width is normalized exactly as in Finch: for a piecewise smooth convex body with unit-sphere face curvature, it is the smooth-face contribution \(\operatorname{Area}(\partial K)/(2\pi)\) plus the edge contribution \((4\pi)^{-1}\sum_e \theta_e\ell_e\), where \(\theta_e\) is the angle between the two outward face normals.

No assertion is made about the analogous spherical dodecahedron mentioned by Finch, nor about a general formula for arbitrary intersections of balls.

## Proof
For \(x=(x_1,x_2,x_3)\), imposing both balls with centers \(\pm e_j/\sqrt2\) gives
\[
\lVert x\rVert^2+\sqrt2\lvert x_j\rvert\le\frac12.
\]
Hence
\[
K=\left\{x:\lVert x\rVert^2+\sqrt2\lVert x\rVert_\infty\le\frac12}\right\}.
\]
At a vertex three coordinate constraints are active with equal absolute coordinates. Solving \(3t^2+\sqrt2 t=1/2\) gives \(t=1/(3\sqrt2)\), proving the vertex formula and \(\lambda=2t=\sqrt2/3\).

Consider the edge shared by the faces on the spheres centered at \(c_1=e_1/\sqrt2\) and \(c_2=e_2/\sqrt2\). Their intersection circle has center \(q=(c_1+c_2)/2\) and radius \(\rho=\sqrt3/2\). Its two relevant endpoints are \((-t,-t,\pm t)\). Relative to \(q\), the endpoint vectors have squared norm \(3/4\) and mutual dot product \(23/36\). Therefore the subtended angle is
\[
\alpha=\arccos\!\left(\frac{23}{27}\right),
\]
and each of the twelve edges has length \(\ell=\rho\alpha=(\sqrt3/2)\alpha\). The outward normals of two adjacent unit spheres have dot product \(1/2\), so their angle is \(\pi/3\).

Write \(\gamma=\arccos(1/3)\). The triple-angle identity gives
\[
\alpha=3\gamma-\pi.
\]
On one spherical face, each of its four boundary arcs lies on a small circle of angular radius \(\pi/3\), so its geodesic curvature with respect to the face interior is \(1/\sqrt3\). The two inward edge tangents at every face vertex have cosine \(-1/3\), hence the face interior angle is \(\beta=\pi-\gamma\). Gauss--Bonnet for the spherical quadrilateral therefore gives its area \(A_f\) from
\[
A_f+4\frac{\ell}{\sqrt3}+4(\pi-\beta)=2\pi,
\]
so
\[
A_f=\frac23(\pi-5\alpha).
\]
There are six congruent faces, proving
\[
\operatorname{Area}(\partial K)=6A_f=4\pi-20\alpha.
\]

For the volume, apply the divergence theorem:
\[
\operatorname{Vol}(K)=\frac13\int_{\partial K}x\cdot n\,dA.
\]
On the face centered at \(c_1=e_1/\sqrt2\), write \(x=c_1+s\), where \(\lVert s\rVert=1\) and \(n=s\). Thus its contribution is \(A_f+(1/\sqrt2)\int_F s_1\,dA\). To compute the vector-area term, orient one boundary edge positively and parameterize it by
\[
x(\theta)=q+\frac{\sqrt3}{2}\left(\cos\theta\,u+\sin\theta\,e_3\right),
\quad
u=\left(-\frac1{\sqrt2},-\frac1{\sqrt2},0\right),
\quad
-\frac\alpha2\le\theta\le\frac\alpha2.
\]
Since \(\sin(\alpha/2)=\sqrt{2/27}\), the first component of \(\int x\times dx\) along this edge is
\[
\frac16-\frac{3\alpha}{4\sqrt2}.
\]
Four congruent edges and the vector-area identity \(\int_F n\,dA=(1/2)\oint_{\partial F}x\times dx\) yield
\[
\int_F s_1\,dA=\frac13-\frac{3\alpha}{2\sqrt2}.
\]
Using sixfold symmetry in the divergence formula now gives
\[
\operatorname{Vol}(K)
=2\left[A_f+\frac1{\sqrt2}\left(\frac13-\frac{3\alpha}{2\sqrt2}\right)\right]
=\frac{4\pi}{3}+\frac{2}{3\sqrt2}-\frac{49}{6}\alpha.
\]

Finally, each spherical face has mean curvature \(1\), there are twelve equal edges, and every edge angle is \(\pi/3\). Therefore
\[
w(K)=\frac{\operatorname{Area}(\partial K)}{2\pi}
+\frac1{4\pi}\,12\left(\frac\pi3\right)\ell
=2+\left(\frac{\sqrt3}{2}-\frac{10}{\pi}\right)\alpha.
\]

## Verification
The accompanying verifier checks the rational edge-angle identity \(\cos\alpha=23/27\), the face-corner cosine \(-1/3\), the triple-angle relation, the Gauss--Bonnet balance, the vector-area contribution, and the three final closed forms. It also independently evaluates the volume by spherical midpoint quadrature using the radial function
\[
r(u)=\frac{\sqrt{1+\lVert u\rVert_\infty^2}-\lVert u\rVert_\infty}{\sqrt2},
\qquad u\in S^2,
\]
and compares the result with the exact formula.

The defining equations also provide a normalization check: \(\lambda=\sqrt2/3\) and the exact volume give \(\operatorname{Vol}(K)/\lambda^3=1.5085356447\ldots\), agreeing with Finch's numerical \(1.508\ldots\). Finch's displayed value \(2/\sqrt3\) for \(\lambda\) is incompatible with both the displayed sphere equations and that numerical ratio; the equations give \(\sqrt2/3\).

## Relationship to prior work
Finch's 2013 paper defines exactly these six unit spheres, calls their intersection a spherical hexahedron, states the common edge angle \(\pi/3\), and asks for exact expressions for volume, surface area, and mean width. The formulas above answer that question in closed form. Finch also cites general sphere-overlap literature, including Dodd--Theodorou's algorithmic treatment and Lustig's fused-sphere work, but nevertheless leaves this octahedrally centered intersection as an unanswered exact-evaluation problem.

A 2015 paper by Chkhartishvili and Narasimhan solves a different six-sphere volume problem motivated by a Stewart platform: their equal sphere centers are coplanar vertices of a regular hexagon. That geometry does not specialize to the octahedral-center configuration here. Dodd and Theodorou provide a general analytical algorithm for volumes and exposed areas of bodies formed from intersecting spheres and planes, but the accessible abstract does not state these three closed forms and does not address mean width.

## Limitations
The proof is specific to the highly symmetric six-ball configuration above. It does not classify general six-sphere intersections. The literature comparison cannot exclude an unindexed historical derivation or a differently phrased closed form. Lustig's 1985 paper is plausibly relevant because it treats fused-sphere systems associated with regular polyhedra, but its full text was not available through the bounded lawful-access attempts used here; only bibliographic descriptions and abstracts were inspected. This residual access risk is not used as evidence of novelty.

## References
1. Steven R. Finch, *Mutually Equidistant Spheres that Intersect*, arXiv:1301.5515v1, January 23, 2013. Primary MSC 53A05.
2. Lawrence R. Dodd and Doros N. Theodorou, *Analytical treatment of the volume and surface area of molecules formed by an arbitrary collection of unequal spheres intersected by planes*, Molecular Physics 72 (1991), 1313--1345, doi:10.1080/00268979100100941.
3. Levan Chkhartishvili and S. G. Narasimhan, *Volume of intersection of six spheres: A special case of practical interest*, Nano Studies 11 (2015), 111--126.
4. Rolf Lustig, *Surface and volume of three, four, six and twelve hard fused spheres*, Molecular Physics 55 (1985), 305--317.
