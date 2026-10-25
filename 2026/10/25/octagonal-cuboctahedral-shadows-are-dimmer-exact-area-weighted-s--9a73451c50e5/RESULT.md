# Octagonal cuboctahedral shadows are dimmer: exact area-weighted silhouette moments

## Finding
Let \(K=\operatorname{conv}\{(\pm1,\pm1,0),(\pm1,0,\pm1),(0,\pm1,\pm1)\}\subset\mathbb R^3\) be the regular cuboctahedron of edge length \(\sqrt2\). For a Haar-uniform unit direction \(U\in S^2\), denote by \(A(U)\) the Euclidean area of its orthogonal projection onto \(U^\perp\), and by \(N(U)\) the number of vertices of the projected polygon. Then \(N\in\{6,8\}\) almost surely, and
\[
\boxed{\mathbb E[A\,\mathbf1_{\{N=8\}}]=3,\qquad
       \mathbb E[A\,\mathbf1_{\{N=6\}}]=\sqrt3.}
\]
Write \(\alpha=\arcsin(1/3)\). The exact silhouette probabilities are
\[
p_8=\Pr(N=8)=\frac{6\alpha}{\pi},\qquad p_6=1-p_8.
\]
Consequently the conditional average areas are
\[
\boxed{\mathbb E[A\mid N=8]=\frac{\pi}{2\alpha},\qquad
\mathbb E[A\mid N=6]=\frac{\sqrt3}{1-6\alpha/\pi},}
\]
and satisfy the strict, counterintuitive ordering
\[
\boxed{\mathbb E[A\mid N=8]<\mathbb E[A\mid N=6].}
\]
Equivalently, the area and the number of silhouette vertices have the exact **negative** covariance
\[
\boxed{\operatorname{Cov}(A,N)=6-\frac{12(3+\sqrt3)}\pi\arcsin(1/3)<0.}
\]
The probability law itself is included to normalize the weighted moments; earlier random-section and shadow calculations cover the same arctangent/spherical-angle probability in related polyhedra. The new asserted content is the exact area-weighted split, its conditional mean contrast, and the negative mixed moment.

## Assumptions and scope
Every coordinate-sign combination appearing in the three displayed vertex families is included, giving twelve distinct vertices. Thus the cuboctahedron has six square faces of area \(2\) and eight equilateral triangular faces of area \(\sqrt3/2\). A viewing direction and its negative define the same unoriented plane. Exceptional directions where projected edges coincide or some face is parallel to the view form a union of great-circle arcs of spherical probability zero; all face-count assertions concern the complement. A uniform spatial rescaling by \(t>0\) multiplies all stated shadow areas and mixed area moments by \(t^2\), leaving the silhouette probabilities unchanged.

## Proof
**1. Piecewise area and silhouette complexity.** By coordinate permutations and sign changes assume \(U=(a,b,c)\) where \(a\ge b\ge c>0\) and \(a^2+b^2+c^2=1\). The outward normal vectors of the six square faces are \(\pm e_i\), and those of the eight triangular faces are \((\pm1,\pm1,\pm1)/\sqrt3\). Each edge joins one square face to one triangular face. An edge projects to a generic silhouette edge exactly when the adjacent face normal dot products with \(U\) have opposite signs. Enumerating these twenty-four adjacencies shows that there are eight silhouette edges when \(a>b+c\), and six when \(a<b+c\). A generic projected convex polygon has the same number of silhouette edges and vertices.

Cauchy's polyhedral projection formula, with each opposite face counted separately, gives
\[
A(U)=2(a+b+c)+\frac14\sum_{\sigma_i\in\{\pm1\}}
|\sigma_1a+\sigma_2b+\sigma_3c|.
\]
The signed sum is \(8a\) in the chamber \(a>b+c\), and \(4(a+b+c)\) in its complement. Therefore
\[
\boxed{A(U)=\begin{cases}
4a+2b+2c,&a>b+c\quad(N=8),\\
3(a+b+c),&a<b+c\quad(N=6).
\end{cases}}
\]
These identities also give a direct algebraic description of every generic orientation, not just its average.

**2. Spherical chamber area.** Let
\[
C=\{(x,y,z)\in S^2:x>y+z,\;y>0,\;z>0\}.
\]
Exactly twenty-four disjoint congruent copies of \(C\), apart from null boundaries, form the event \(N=8\). Its bounding great-circle arcs have vertices \(e_1\), \((1,1,0)/\sqrt2\), and \((1,0,1)/\sqrt2\). By spherical excess (or the three-vector solid-angle identity),
\[
\operatorname{area}(C)=2\arccos(1/\sqrt3)-\frac\pi2=\arcsin(1/3)=\alpha.
\]
As the sphere has area \(4\pi\), \(p_8=24\alpha/(4\pi)=6\alpha/\pi\).

**3. First spherical moments exactly.** For any fixed coordinate linear function \(f(u)\) on \(S^2\), the spherical Laplacian identity \(\Delta_{S^2}f=-2f\) and the divergence theorem give
\[
\int_C f\,d\omega=-\frac12\sum_{e\subset\partial C}\ell_e\,\partial_{\nu_e} f.
\]
The boundary arcs along \(y=0\), \(z=0\), and \(x=y+z\) have respective lengths \(\pi/4\), \(\pi/4\), and \(\pi/3\); their outward spherical unit conormals are \(-e_2\), \(-e_3\), and \((-1,1,1)/\sqrt3\), respectively. Because each arc lies in a great circle, these are constant conormals. Applying the formula to the three coordinates yields
\[
\int_C x\,d\omega=\frac\pi{6\sqrt3},\qquad
\int_C y\,d\omega=\int_C z\,d\omega
=\frac\pi8-\frac\pi{6\sqrt3}.
\]
Hence the exact weighted spherical integral over the octagonal chamber is
\[
\int_C A\,d\omega
=\int_C(4x+2y+2z)\,d\omega
=\frac\pi2.
\]
Normalizing by the full sphere and multiplying by the twenty-four congruent chambers proves
\[
\mathbb E[A\,\mathbf1_{\{N=8\}}]
=\frac{24}{4\pi}\cdot\frac\pi2=3.
\]

**4. Complement and strict sign.** The total surface area of the displayed cuboctahedron equals \(12+4\sqrt3\). Cauchy's mean projected-area theorem therefore yields
\[
\mathbb EA=\frac14(12+4\sqrt3)=3+\sqrt3.
\]
Subtracting the octagonal contribution gives \(\mathbb E[A\mathbf1_{\{N=6\}}]=\sqrt3\). Dividing by the positive event probabilities proves the conditional formulas.

Since \(N=6+2\mathbf1_{\{N=8\}}\), the covariance is exactly
\[
\operatorname{Cov}(A,N)=2\bigl(3-(3+\sqrt3)p_8\bigr).
\]
For strict negativity it suffices that \(p_8>3/(3+\sqrt3)\). Indeed \(\arcsin(1/3)>1/3\) and \(\pi<22/7\) give \(p_8>2/\pi>7/11>3/(3+\sqrt3)\), where the last inequality follows from \(7\sqrt3>12\). Therefore both claimed strict inequalities hold. \(\square\)

## Verification
The standalone script `verify.py` reconstructs all twelve three-dimensional vertices and, for 2,400 independent continuous viewing directions, directly projects the vertices and computes a planar convex hull. In every case its vertex count and area agree with the independent signed-normal formulas to absolute error below \(3\times10^{-12}\).

To independently check the nonstandard spherical-cone calculation, the script integrates in coordinates \(x=\cos t\), \(y=\sin t\cos\phi\), \(z=\sin t\sin\phi\), over \(0\le\phi\le\pi/2\) and \(0\le t\le\arctan(1/(\cos\phi+\sin\phi))\), using fifty-digit numerical quadrature. It confirms the exact cone area, all coordinate first moments, and the \(\pi/2\) weighted integral to error below \(10^{-44}\). A separate scrambled Sobol spherical sample of size \(2^{19}\) corroborates the unconditional and type-conditioned means.

Run `python verify.py` with `numpy`, `scipy`, and `mpmath` installed. The terminal line `ALL_CUBOCTAHEDRON_SHADOW_BRIGHTNESS_CHECKS_OK` means these finite checks passed. Neither a finite sample nor finite-precision integration is treated as the proof of a universal identity: the proof above is exact.

## Relationship to prior work
Cauchy's surface-area formula, exposited by Slepian, gives the unconditional mean \(3+\sqrt3\) but says nothing about conditional averages by silhouette type. Finch established unconditional projection-area moments and shadow-vertex probabilities for the cube, tetrahedron, and octahedron, none of which is the cuboctahedron. Lonke's section-count results for the cube yield an equivalent **unweighted** spherical-triangle probability at equal side lengths; the numerical coincidence with \(p_8\) is credited and is not treated as the principal contribution. A published calculation of conditional area moments for arbitrary tetrahedra likewise concerns a different polyhedron and different silhouette categories. None of those formulas implies a decomposition of the cuboctahedron's expected projected area into the exact two contributions \(3\) and \(\sqrt3\). The new part consists of the explicit cuboctahedral brightness-by-complexity law and its strict negative covariance.

## Limitations
This result concerns a single geometrically normalized Archimedean solid and Haar-uniform orthographic viewing directions. It does not establish a corresponding sign law for arbitrary polytopes, conditional second area moments, or the complete conditional distributions. Excluded nongeneric directions are measure-zero boundaries, not missing probabilistic cases. An older unindexed stereological table might contain an equivalent cuboctahedral weighted mean; historical priority is not established beyond the inspected sources.

## References
1. Z. Slepian, *The Average Projected Area Theorem — Generalization to Higher Dimensions*, arXiv:1109.0595v1 (3 September 2011), https://arxiv.org/abs/1109.0595. The relevant known input is the unconditional Cauchy mean in §6.
2. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1 (12 March 2012), https://arxiv.org/abs/1203.2464. The relevant comparisons are §2.1–2.3.
3. Y. Lonke, *On Random Sections of the Cube*, arXiv:math/9812123 (21 December 1998), https://arxiv.org/abs/math/9812123. Cited for the previously known equal-cube unweighted section probability.
4. J. C. Lagarias, Y. Luo, and A. Padrol, *Moser's Shadow Problem*, arXiv:1310.4345v1 (16 October 2013), https://arxiv.org/abs/1310.4345. Context on the distinction between silhouette complexity and projection area.
